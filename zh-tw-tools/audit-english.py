"""掃描 herdr-app 所有面板，列出還沒翻的使用者可見英文。

用法: python -I audit-english.py
"""
import os
import re

HOME = os.path.join(os.path.expanduser("~"), ".config", "herdr-app")

LIT = re.compile(r"""(?P<q>['"`])(?P<s>(?:\\.|(?!\1)[^\\])*)\1""")
CJK = re.compile(r"[一-鿿]")

# 不算漏網的
SKIP_EXACT = {
    "Herdr", "Herdr 98", "Ctrl", "Alt", "Shift", "Super", "Fn", "Esc", "Enter", "Tab",
    "JetBrains Mono", "Berkeley Mono", "Geist", "Darwin", "Linux", "Windows", "macOS",
    "Recent", "Pane", "Space", "Layout", "Terminal", "Agent", "Window", "App",  # palette 的分組 key
    "graphite", "ink", "moss", "atom one dark", "paper",                        # 主題名
}
SKIP_PAT = re.compile(
    r"^(?:"
    r"[a-z0-9_.\-/]+"                              # 識別碼／指令／屬性
    r"|.*\.(?:js|json|svg|png|md|ts|exe|mp3)$"     # 檔名
    r"|(?:frame|mods|icons)/.*"                    # 資源路徑
    r"|[A-Z_]{2,}$"                                # 常數
    r"|[#.][A-Za-z0-9_\-]+$"                       # CSS
    r"|\d+(?:\.\d+)?(?:px|%|em)?$"
    r"|#\s*branch\..*"                             # git porcelain
    r"|(?:HEAD|git|sh|printf|uname|hc)\b.*"        # git/shell 指令
    r"|@@.*"                                       # diff 標頭
    r"|\s*$"
    r")"
)

def visible(s):
    if len(s) < 3 or len(s) > 240:
        return False
    if s in SKIP_EXACT or SKIP_PAT.match(s) or CJK.search(s):
        return False
    if not re.search(r"[A-Za-z]{3,}", s):
        return False
    # 詞組，或首字大寫的標籤
    return (" " in s.strip()) or s[:1].isupper()

found = {}
for kind in ("frame", "mods"):
    base = os.path.join(HOME, kind)
    if not os.path.isdir(base):
        continue
    for d in sorted(os.listdir(base)):
        if d == "win98":          # 懷舊主題彩蛋，預設看不到
            continue
        dpath = os.path.join(base, d)
        if not os.path.isdir(dpath):
            continue
        for root, _dirs, files in os.walk(dpath):
            for fn in sorted(files):
                if not fn.endswith(".js") or fn.endswith(".d.ts"):
                    continue
                path = os.path.join(root, fn)
                rel = os.path.relpath(path, HOME).replace("\\", "/")
                for i, line in enumerate(open(path, encoding="utf-8", newline="").read().splitlines(), 1):
                    st = line.strip()
                    if st.startswith("//") or st.startswith("*") or st.startswith("/*"):
                        continue
                    for m in LIT.finditer(line):
                        s = m.group("s")
                        if visible(s):
                            found.setdefault(rel, []).append((i, s))

n = sum(len(v) for v in found.values())
print("可能漏翻的字串: %d 處，分布在 %d 個檔案" % (n, len(found)))
print()
for rel in sorted(found):
    print("## %s" % rel)
    seen = set()
    for ln, s in found[rel]:
        if s in seen:
            continue
        seen.add(s)
        print("   %4d  %s" % (ln, s[:90]))
    print()
