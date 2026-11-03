"""把 zh-tw-tables.py 的對照表套用到 herdr-app。

用法:
    python -I apply-zh-tw.py --repo  D:\\github\\herdr-app            # 套到原始碼
    python -I apply-zh-tw.py --home  ~/.config/herdr-app              # 套到安裝好的設定
    加 --apply 才會寫檔，否則只檢查每條原文找不找得到。

兩種目標的差別：
  --repo  改 defaults/mods/<name>/ 與 defaults/frame/<name>/，要重新編譯才生效，
          但 frame 的面板也能翻。換行用 LF（跟著 repo）。
  --home  改 mods/<name>/，熱重載立即生效，但 app 啟動時會把它們改名成
          <name>-edited 並寫回英文版（見 README）。換行用 CRLF（跟著安裝版）。
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util

spec = importlib.util.spec_from_file_location(
    "tables", os.path.join(os.path.dirname(os.path.abspath(__file__)), "zh-tw-tables.py"))
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)

ap = argparse.ArgumentParser()
g = ap.add_mutually_exclusive_group(required=True)
g.add_argument("--repo", help="herdr-app 原始碼目錄")
g.add_argument("--home", help="herdr-app 家目錄（~/.config/herdr-app）")
ap.add_argument("--apply", action="store_true")
ap.add_argument("--no-close-button", action="store_true", help="不要把 Esc 換成 X 鈕")
a = ap.parse_args()

if a.repo:
    root = os.path.abspath(os.path.expanduser(a.repo))
    mods_dir = os.path.join(root, "defaults", "mods")
    frame_dir = os.path.join(root, "defaults", "frame")
    newline = "\n"
    label = "repo"
else:
    root = os.path.abspath(os.path.expanduser(a.home))
    mods_dir = os.path.join(root, "mods")
    frame_dir = os.path.join(root, "frame")
    newline = "\r\n"
    label = "home"

print("目標: %s (%s)  換行: %s" % (root, label, "LF" if newline == "\n" else "CRLF"))
print()

def lf(text):
    """正規化換行，讓對照表的 \\n 能跟檔案裡的 \\r\\n 比對。"""
    return text.replace("\r\n", "\n")

def load(path):
    with open(path, encoding="utf-8", newline="") as f:
        return f.read()

def save(path, text):
    # 先統一成 \n 再依目標轉換，避免混用
    text = text.replace("\r\n", "\n")
    if newline == "\r\n":
        text = text.replace("\n", "\r\n")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

total_ok = total_miss = 0
missing = []

def run(base, table, kind):
    global total_ok, total_miss
    for rel, pairs in sorted(table.items()):
        path = os.path.join(base, rel.replace("/", os.sep))
        if not os.path.isfile(path):
            print("  %-34s 檔案不存在" % rel)
            continue
        s = load(path)
        orig = s
        ok = done = 0
        for old, new in pairs:
            # 已經套用過就跳過：有幾條的 new 含有 old（例如在原字串後面補一張對照表），
            # 重跑會造成重複定義，所以先認這個。比對前把換行正規化，否則
            # 表裡的 \n 對不上檔案裡的 \r\n。
            if lf(new) in lf(s):
                done += 1
                continue
            if s.count(old) == 0:
                missing.append("%s: %s" % (rel, old[:70]))
                total_miss += 1
            else:
                s = s.replace(old, new)
                ok += 1
                total_ok += 1
        note = ""
        if done:
            note += "  (%d 條本來就是中文)" % done
        if ok + done != len(pairs):
            note += "  (%d 條沒對上)" % (len(pairs) - ok - done)
        print("  %-34s %2d/%-2d%s" % (rel, ok + done, len(pairs), note))
        if a.apply and s != orig:
            save(path, s)

print("== 一般面板 ==")
run(mods_dir, T.MODS, "mods")
print()
print("== frame 面板 ==")
run(frame_dir, T.FRAME, "frame")
print()
print("== 面板標題 ==")
for rel, pairs in sorted(T.TITLES.items()):
    base = frame_dir if rel.startswith("frame/") else mods_dir
    r = rel[len("frame/"):] if rel.startswith("frame/") else rel
    path = os.path.join(base, r.replace("/", os.sep))
    if not os.path.isfile(path):
        print("  %-34s 檔案不存在" % rel)
        continue
    s = load(path)
    orig = s
    done = 0
    for old, new in pairs:
        if lf(new) in lf(s):
            done += 1
            continue
        if s.count(old) == 0:
            missing.append("%s: %s" % (rel, old[:70]))
            total_miss += 1
        else:
            s = s.replace(old, new)
            total_ok += 1
    print("  %-34s %s" % (rel, "本來就是中文" if done == len(pairs) else "OK"))
    if a.apply and s != orig:
        save(path, s)

if not a.no_close_button:
    print()
    print("== 對話框 X 關閉鈕 ==")
    jobs = [(mods_dir, rel, sv) for rel, sv in sorted(T.CLOSE_BUTTON.items())]
    jobs += [(frame_dir, rel, sv) for rel, sv in sorted(getattr(T, "FRAME_CLOSE_BUTTON", {}).items())]
    for base, rel, need_svg in jobs:
        path = os.path.join(base, rel.replace("/", os.sep))
        if not os.path.isfile(path):
            print("  %-34s 檔案不存在" % rel)
            continue
        s = load(path)
        orig = s
        if "ov-close" in s:
            print("  %-34s 已經有 X 鈕" % rel)
            continue
        n = s.count(T.ESC_OLD)
        if n != 1:
            print("  %-34s Esc 片段 %d 處（預期 1），跳過" % (rel, n))
            missing.append("%s: Esc 片段" % rel)
            total_miss += 1
            continue
        s = s.replace(T.ESC_OLD, T.ESC_NEW)
        note = ""
        if need_svg and T.IMPORT_OLD in s:
            s = s.replace(T.IMPORT_OLD, T.IMPORT_NEW, 1)
            note = " + svg import"
        total_ok += 1
        print("  %-34s OK%s" % (rel, note))
        if a.apply and s != orig:
            save(path, s)

print()
print("套用 %d 條，沒對上 %d 條" % (total_ok, total_miss))
for m in missing:
    print("  !! %s" % m)
print()
print("已寫入" if a.apply else "(dry-run，加 --apply 才寫檔)")
