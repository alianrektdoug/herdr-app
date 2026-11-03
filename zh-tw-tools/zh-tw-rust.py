"""把 herdr-app Rust 端畫在畫面上的英文翻成繁體中文。

用法:
    python -I zh-tw-rust.py --repo D:\\github\\herdr-app           # dry-run
    python -I zh-tw-rust.py --repo D:\\github\\herdr-app --apply

這些字串是 frame 自己畫的，JS 面板碰不到（src/window.rs:4248 的註解：
「the frame's, so no layout or mod can hide it」），只能改原始碼重新編譯。

只改字串字面值，格式佔位符（{}、{n}、{name}）原樣保留。
不碰 self.fail(...) 的錯誤訊息：那些主要給 CLI 與日誌看，翻了反而難查。
"""
import argparse
import os
import sys

ap = argparse.ArgumentParser()
ap.add_argument("--repo", required=True)
ap.add_argument("--apply", action="store_true")
a = ap.parse_args()

SRC = os.path.join(os.path.abspath(os.path.expanduser(a.repo)), "src")

T = {
    "window.rs": [
        # 空畫面
        ('format!("No space open. Make one{}.", key.unwrap_or_default())',
         'format!("目前沒有開啟的空間。可以新增一個{}。", key.unwrap_or_default())'),
        ('.child("no agents yet. start claude, codex or pi in a terminal")',
         '.child("尚無代理程式。在終端機裡啟動 claude、codex 或 pi")'),
        # 通知（JS 的 toast mod 也攔了一層；兩邊都中文不衝突，對不上就原樣顯示）
        ('"title": format!("{n} needs mods that aren\'t here")',
         '"title": format!("{n} 需要的面板不存在")'),
        ('"title": format!("Your edits are in {clone}")',
         '"title": format!("你的修改已保存在 {clone}")'),
        ('"body": "Herdr\'s own layouts and mods can\'t be changed: clone one to make it yours."',
         '"body": "Herdr 內建的版面與面板不能直接修改：複製一份再改成你要的。"'),
        ('"title":"Terminal failed to start"', '"title":"終端機啟動失敗"'),
        ('"title":format!("{name} failed")', '"title":format!("{name} 失敗")'),
        # 關閉空間的確認（JS 的 confirm mod 也攔了一層）
        ('self.confirm("Close space?"', 'self.confirm("要關閉這個空間嗎？"'),
        ('format!("{} \\u{2014} {} tabs, {} terminals"',
         'format!("{} \\u{2014} {} 個分頁、{} 個終端機"'),
        # 載入失敗
        ('format!("{} did not load:\\n\\n{}\\n\\nFix the files; Herdr retries on save."',
         'format!("{} 載入失敗：\\n\\n{}\\n\\n請修正檔案，存檔後 Herdr 會自動重試。"'),
        # 更新提示（frame 自己畫的那條）
        ('format!("Herdr {a} and herdr-core {c} are ready")',
         'format!("Herdr {a} 與 herdr-core {c} 已就緒")'),
        ('format!("Updated to {}", env!("CARGO_PKG_VERSION"))',
         'format!("已更新至 {}", env!("CARGO_PKG_VERSION"))'),
        ('format!("herdr-core update failed: {error} · Open Updates")',
         'format!("herdr-core 更新失敗：{error} · 開啟更新頁")'),
        ('.child("Restart")', '.child("重新啟動")'),
        ('if app_ready || success { "What changed" } else { "Open Updates" }',
         'if app_ready || success { "更新內容" } else { "開啟更新頁" }'),
    ],
    "window/floats.rs": [
        ('format!("{} did not load: {e}"', 'format!("{} 載入失敗：{e}"'),
    ],
}

ok = miss = 0
for rel, pairs in sorted(T.items()):
    path = os.path.join(SRC, rel.replace("/", os.sep))
    if not os.path.isfile(path):
        print("  %-22s 檔案不存在" % rel)
        continue
    s = open(path, encoding="utf-8", newline="").read()
    orig = s
    bad = []
    done = 0
    for old, new in pairs:
        if new in s:
            done += 1
            continue
        if s.count(old) == 0:
            bad.append(old)
            miss += 1
        else:
            s = s.replace(old, new)
            ok += 1
    note = ("  (%d 條本來就是中文)" % done) if done else ""
    print("  %-22s %2d/%-2d%s" % (rel, ok if len(T) == 1 else (len(pairs) - len(bad) - done) + done, len(pairs), note))
    for b in bad:
        print("      找不到: %s" % b[:92])
    if a.apply and s != orig:
        open(path, "w", encoding="utf-8", newline="").write(s)

print()
print("套用 %d 條，沒對上 %d 條" % (ok, miss))
print("已寫入" if a.apply else "(dry-run)")
if a.apply:
    print()
    print("提醒：這些改動需要重新編譯才生效，而且本機的 Smart App Control 擋掉")
    print("      cargo 的 build script，無法在這裡驗證編譯。")
