"""翻譯 herdr-app 的更新說明快取（~/.config/herdr-app/update-notes-cache.md）。

用法:
    python -I zh-tw-changelog.py           # dry-run
    python -I zh-tw-changelog.py --apply

這份內容不是介面文字，是 app 從 releases.herdr.dev 下載的 changelog.md
（src/update.rs 的 curl_text(".../changelog.md")）。每次更新都會下載新的英文版，
所以這個腳本的對照表只對當下的版本有效，下次更新後要補新的條目。

格式不能動的地方（src/update_notes.rs 的 parse_for_os）：
  "## [版本] - 日期"        版本標頭，split_once("] - ")
  "<!-- spotlight xxx -->"  平台標記
  "### Fixed"               精確比對決定 fixed 旗標，翻了所有項目都會變成「新增」
  "- **標題** 內文"          ** 之間是 headline，其餘是 detail
  "![](url)"                圖片
"""
import os
import re
import sys

CACHE = os.path.join(os.path.expanduser("~"), ".config", "herdr-app", "update-notes-cache.md")
APPLY = "--apply" in sys.argv

# 整行對照（去掉開頭的 "- " 之後比對）。保留 (#123, thanks @someone) 尾巴。
T = {
    # --- 0.1.12 New ---
    "**On macOS, your agents now run fully apart from the app.** Close Herdr, quit it, update it: your agents keep running. Agents already running pick this up the next time they start.":
        "**在 macOS 上，代理程式現在完全獨立於 app 之外執行。** 關閉 Herdr、結束它、更新它，代理程式都會繼續執行。已在執行的代理程式會在下次啟動時套用這項改變。",
    "On macOS, the system may ask once if **herdr-core** can access a folder like Documents. That's Herdr; click Allow.":
        "在 macOS 上，系統可能會問一次 **herdr-core** 是否能存取「文件」之類的資料夾。那就是 Herdr，請按允許。",
    "On macOS, Settings > Keyboard chooses what Option does: Alt, typing characters like á and €, or left or right Option as Alt.":
        "在 macOS 上，設定 > 鍵盤可以決定 Option 鍵的行為：當 Alt、輸入 á 與 € 之類的字元，或只讓左／右 Option 當 Alt。",
    "A machine that was rebuilt or replaced shows \"rebuilt · Connect\" in the sidebar: one click connects to the new one.":
        "被重建或更換過的機器會在側邊欄顯示「rebuilt · 連線」，點一下就能連到新的那台。",
    "Seen and pinned agents are shared between Herdr windows and the phone app.":
        "已讀與釘選的代理程式會在 Herdr 視窗與手機 app 之間同步。",
    "Mods can take the keyboard, so moving focus can land on them.":
        "面板可以接收鍵盤輸入，所以移動焦點時會停在它們上面。",
    "PiG agents have their own icon.": "PiG 代理程式有自己的圖示。",
    "Add machine takes a port, like `can@server:2222`.":
        "新增機器可以指定連接埠，例如 `can@server:2222`。",
    # --- 0.1.12 Fixed ---
    "On Linux, color emoji show in color instead of blank (Fedora's emoji font).":
        "在 Linux 上，彩色表情符號會正常顯示顏色而不是空白（Fedora 的表情符號字型）。",
    "Emoji like ✍️ and ❤️ take two cells and draw in color.":
        "✍️ 與 ❤️ 這類表情符號會佔兩格並以彩色繪製。",
    "On macOS, programs in Herdr terminals can ask for the microphone, camera and to control other apps.":
        "在 macOS 上，Herdr 終端機裡的程式可以請求麥克風、相機權限，以及控制其他 app。",
    "Agents on another machine find the commands their shell setup puts on PATH.":
        "其他機器上的代理程式找得到該機 shell 設定加進 PATH 的指令。",
    "New spaces open on the machine you're looking at.": "新空間會開在你正在看的那台機器上。",
    "Horizontal scrolling reaches programs like vim and less.": "水平捲動可以傳給 vim、less 這類程式。",
    "Clicks work in Textual apps.": "在 Textual 應用程式裡點擊可以正常運作。",
    "btop's braille graphs draw without gaps.": "btop 的點字圖表繪製時不再有空隙。",
    "Nerd Font icons use your terminal font.": "Nerd Font 圖示會使用你設定的終端機字型。",
    "Rounded corners and dashed lines in boxes draw like Ghostty.":
        "方框的圓角與虛線繪製方式與 Ghostty 一致。",
    "Herdr uses less CPU with many busy agents.": "同時有多個忙碌的代理程式時，Herdr 使用的 CPU 較少。",
    "A big project no longer makes the folder watcher burn a CPU core.":
        "大型專案不會再讓資料夾監看吃掉一整顆 CPU 核心。",
    "Mod pictures and icons update when their file is saved.": "面板的圖片與圖示會在檔案存檔時更新。",
    "Moving focus back into a split returns to the pane you came from.":
        "把焦點移回分割區時，會回到你原本所在的窗格。",
    "Unnamed tabs show what their agent is doing in the agents list.":
        "未命名的分頁會在代理程式清單顯示它的代理程式正在做什麼。",
    "A new tab with no space open starts a space.": "在沒有開啟空間時新增分頁，會自動建立一個空間。",
    "Files marks the files inside a new folder, and opens folder symlinks.":
        "檔案面板會標記新資料夾內的檔案，也能開啟資料夾符號連結。",
    "Lists in mods follow the zoom.": "面板裡的清單會跟著縮放比例調整。",
    "The + menu shows your agents right away.": "＋ 選單會立即顯示你的代理程式。",
    "Grok shows its own icon.": "Grok 會顯示自己的圖示。",
    "A malformed command can't close the tab you're on.": "格式錯誤的指令不會關掉你目前所在的分頁。",
    "On Linux, Ctrl+Insert and Shift+Insert copy and paste in new installs; add them to your keys.json to get them on an existing one.":
        "在 Linux 上，全新安裝的 Ctrl+Insert 與 Shift+Insert 可以複製貼上；既有安裝請自行加進 keys.json。",
    "In full screen on macOS, the sidebar header lines up.": "在 macOS 全螢幕下，側邊欄標題會對齊。",
    "On Windows, file names in Korean, Chinese and other languages show and open in Files.":
        "在 Windows 上，韓文、中文與其他語言的檔名可以在檔案面板正常顯示與開啟。",
}

# 這幾行是格式，碰不得
KEEP = re.compile(r"^(#|<!--|###\s|!\[|$)")
# 尾巴的貢獻者資訊：(#283, thanks @Osc100) 或 (#137, thanks @a; #252)
TAIL = re.compile(r"\s*(\((?:#\d+|thanks)[^)]*\))\s*$")

if not os.path.isfile(CACHE):
    print("找不到快取：%s" % CACHE)
    print("（app 還沒下載過 changelog，或路徑不同）")
    raise SystemExit(1)

text = open(CACHE, encoding="utf-8", newline="").read()
lines = text.split("\n")
out = []
hit = miss = skip = 0
unknown = []

for line in lines:
    raw = line.rstrip("\r")
    stripped = raw.strip()
    if not stripped.startswith("- "):
        out.append(raw)
        continue
    body = stripped[2:]
    m = TAIL.search(body)
    tail = ""
    if m:
        tail = " " + m.group(1)
        body = body[:m.start()]
    if re.search(r"[一-鿿]", body):
        skip += 1
        out.append(raw)
        continue
    if body in T:
        hit += 1
        indent = raw[:len(raw) - len(raw.lstrip())]
        out.append("%s- %s%s" % (indent, T[body], tail))
    else:
        miss += 1
        unknown.append(body[:92])
        out.append(raw)

print("翻譯 %d 條，已是中文 %d 條，沒有對照 %d 條" % (hit, skip, miss))
if unknown:
    # 終端機可能是 cp950，印不出某些字元；寫成檔案比較保險
    report = os.path.join(os.path.dirname(os.path.abspath(__file__)), "changelog-untranslated.txt")
    with open(report, "w", encoding="utf-8") as f:
        f.write("沒有對照的條目（多半是舊版本的說明，或上游新加的）\n\n")
        for u in unknown:
            f.write("- %s\n" % u)
    print("沒有對照的 %d 條已列在 %s" % (len(unknown), report))

if APPLY and hit:
    open(CACHE, "w", encoding="utf-8", newline="").write("\n".join(out))
    print()
    print("已寫入 %s" % CACHE)
    print("重開 Herdr 後「更新內容」就會是中文。")
elif not APPLY:
    print()
    print("(dry-run，加 --apply 寫檔)")
