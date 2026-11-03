"""herdr-app 繁體中文化：翻譯對照表（單一來源）。

這個模組只定義資料，不做事。套用請用 apply-zh-tw.py。

鍵是相對 defaults/ 的路徑（repo）或相對 mods/ 的路徑（使用者目錄），
兩邊的檔案內容相同，所以同一份表兩邊都能用。

刻意不翻的：
  Herdr                         產品名
  Ctrl / Alt / Shift / Esc      鍵盤上就印這樣
  "# branch.head " "# branch.ab "   git status --porcelain=v2 的解析標記
  graphite / ink / moss / paper 主題專有名稱
  ${name} Z、內部組合 key、svg 路徑、shell 指令、diff 標頭
"""

# ---------------------------------------------------------------- 一般 mod
MODS = {}

MODS["agents/main.js"] = [
    ('label: "Priority"', 'label: "優先順序"'),
    ('label: "Grouped by space"', 'label: "依空間分組"'),
    ('{ 4: "Needs you", 3: "Done", 2: "Working", 1: "Idle" }',
     '{ 4: "需要你", 3: "完成", 2: "工作中", 1: "閒置" }'),
    ('.child("Sort agents")', '.child("排序方式")'),
    ('isPinned ? "Unpin" : "Pin to the top"', 'isPinned ? "取消釘選" : "釘選到頂端"'),
    ('label: "Pinned"', 'label: "已釘選"'),
    ('.child("Agents")', '.child("代理程式")'),
    ('`Sort agents: ${sort.label}`', '`排序方式：${sort.label}`'),
    ('"No agent status yet. Agents show up here when they report their status. Older versions and agents inside tmux may not."',
     '"尚無代理程式狀態。代理程式回報狀態後就會出現在這裡；舊版本與在 tmux 內執行的可能不會回報。"'),
    ('.child("Needs you")', '.child("需要你")'),
    ('`${h}h` : `${Math.floor(h / 24)}d`', '`${h} 小時` : `${Math.floor(h / 24)} 天`'),
]

MODS["changes/main.js"] = [
    ('placeholder: "Commit message"', 'placeholder: "提交訊息"'),
    ('"Not a git repository"', '"不是 git 儲存庫"'),
    ('["Cannot preview this diff (too large or unreadable)"]', '["無法預覽此差異（太大或無法讀取）"]'),
    ('["Cannot preview this file (binary, too large, or unreadable)"]',
     '["無法預覽此檔案（二進位、太大或無法讀取）"]'),
    ('["Binary file · no text diff"]', '["二進位檔案 · 無文字差異"]'),
    ('"Binary file changed"', '"二進位檔案已變更"'),
    ('"No text diff available"', '"無可用的文字差異"'),
    ('"… (line truncated)"', '"…（此行已截斷）"'),
    ('`Cannot preview this diff (too large or unreadable): ${e}`', '`無法預覽此差異（太大或無法讀取）：${e}`'),
    ('`Commit failed: ${e}`', '`提交失敗：${e}`'),
    ('.child("Changes")', '.child("變更")'),
    ('`${this.files.length} files`', '`${this.files.length} 個檔案`'),
    ('"Loading changes…"', '"正在載入變更…"'),
    ('"No uncommitted changes"', '"沒有未提交的變更"'),
    ('"No folder"', '"沒有資料夾"'),
    ('"Showing the first 1,000 changed files"', '"僅顯示前 1,000 個變更檔案"'),
    ('"Select a file to view its changes"', '"選擇檔案以檢視其變更"'),
    ('this.busy ? "Committing…" : "Commit"', 'this.busy ? "正在提交…" : "提交"'),
]

MODS["confirm/main.js"] = [
    ('"Are you sure?"', '"確定嗎？"'),
    ('button("no", "Cancel"', 'button("no", "取消"'),
    ('button("yes", "Confirm"', 'button("yes", "確定"'),
]

MODS["files/main.js"] = [
    ('"Cannot list this folder"', '"無法列出此資料夾"'),
    ('"This file is no longer available"', '"此檔案已不存在"'),
    ('"Binary file · no text preview"', '"二進位檔案 · 無文字預覽"'),
    ('"\\n… (file truncated)"', '"\\n…（檔案已截斷）"'),
    ('"Cannot preview this file (binary, too large, or unreadable)"',
     '"無法預覽此檔案（二進位、太大或無法讀取）"'),
    ('.child("Files")', '.child("檔案")'),
    # 複數是檔案樹、單數是單一檔案內容。譯文要不同，否則套用第一條後，
    # 第二條會被「已經是中文」的檢查誤判成跳過。
    ('"Loading files…"', '"正在載入檔案清單…"'),
    ('"No files"', '"沒有檔案"'),
    ('"File list limited to 500 entries per folder and 5,000 total"',
     '"檔案清單上限為每個資料夾 500 筆、總計 5,000 筆"'),
    ('"Loading file…"', '"正在載入檔案…"'),
    ('"No folder"', '"沒有資料夾"'),
]

MODS["help/main.js"] = [
    ('placeholder: "Type to filter…"', 'placeholder: "輸入以篩選…"'),
    ('.child("Keybinds")', '.child("快捷鍵")'),
]

MODS["machine-add/main.js"] = [
    ('"it didn\'t answer"', '"它沒有回應"'),
    ('"it didn\'t work"', '"沒有成功"'),
    ('`${mac.name} is a Mac: allow its folders once`', '`${mac.name} 是 Mac：需要先允許存取它的資料夾`'),
    ('`Open the setting on ${mac.name}`', '`在 ${mac.name} 上開啟該設定`'),
    ('"It\'s open on the Mac\'s screen."', '"已在那台 Mac 的畫面上開啟。"'),
    ('"Couldn\'t open a terminal for it. Run `hc machine add "',
     '"無法為它開啟終端機。請在終端機中執行 `hc machine add "'),
    ('"` in one."', '"`。"'),
    ('`Adding ${props().target}: answer it here`', '`正在新增 ${props().target}：請在這裡回答`'),
    ('.child("Added")', '.child("已新增")'),
    ('.child("Connecting")', '.child("正在連線")'),
    ('.child("Waiting in its terminal")', '.child("正在它的終端機中等待")'),
    ('.child("Add a machine")', '.child("新增機器")'),
    ('.child("A VPS, a Mac mini, a box at home: Herdr reaches it over ssh, and agents there keep running while your laptop sleeps.")',
     '.child("VPS、Mac mini、家裡的主機：Herdr 透過 ssh 連上它，上面的代理程式在你的筆電睡眠時仍會繼續執行。")'),
    ('hosts.length ? "From your ssh config" : "Your ssh config lists no hosts"',
     'hosts.length ? "來自你的 ssh 設定" : "你的 ssh 設定中沒有主機"'),
    ('.child("Reading ~/.ssh/config…")', '.child("正在讀取 ~/.ssh/config…")'),
    ('.child("Or type how ssh reaches it")', '.child("或直接輸入 ssh 連線方式")'),
    ('.child("Add");', '.child("新增");'),
    ('.child("Add"),', '.child("新增"),'),
]

MODS["menu/main.js"] = [
    ('["Split right", "pane.split"', '["向右分割", "pane.split"'),
    ('["Split down", "pane.split"', '["向下分割", "pane.split"'),
    ('["Zoom", "pane.zoom"', '["縮放", "pane.zoom"'),
    ('["Use Herdr right-click menu", "terminal.right_click"', '["使用 Herdr 右鍵選單", "terminal.right_click"'),
    ('["Send right-clicks to pane", "terminal.right_click"', '["將右鍵傳給窗格內的程式", "terminal.right_click"'),
    ('[`Send back to ${parent.name || parent.address}`, "terminal.park"',
     '[`送回 ${parent.name || parent.address}`, "terminal.park"'),
    ('["Close pane", "pane.close"', '["關閉窗格", "pane.close"'),
    ('["Rename", "tab.rename"', '["重新命名", "tab.rename"'),
    ('["New tab", "tab.new"', '["新增分頁", "tab.new"'),
    ('["Close", "tab.close"', '["關閉", "tab.close"'),
    ('["Rename", "space.rename"', '["重新命名", "space.rename"'),
    ('["New worktree", "worktree"', '["新增工作樹", "worktree"'),
    ('["Open worktree", "worktree"', '["開啟工作樹", "worktree"'),
    ('["Remove worktree", "worktree"', '["移除工作樹", "worktree"'),
    ('["Close", "space.close"', '["關閉", "space.close"'),
    ('["New space", "space.new", {}]', '["新增空間", "space.new", {}]'),
    ('["Keybinds", "app.help"', '["快捷鍵", "app.help"'),
    ('["Theme: graphite"', '["主題：graphite"'),
    ('["Theme: ink"', '["主題：ink"'),
    ('["Theme: moss"', '["主題：moss"'),
    ('["Theme: atom one dark"', '["主題：atom one dark"'),
]

MODS["new-menu/main.js"] = [
    ('"Terminal", () => run("tab.new"', '"終端機", () => run("tab.new"'),
    ('.child("Start an agent")', '.child("啟動代理程式")'),
    (': "not installed"', ': "未安裝"'),
    ('this.failed ? "Could not load agents" : "Checking installed agents…"',
     'this.failed ? "無法載入代理程式" : "正在檢查已安裝的代理程式…"'),
    ('"New worktree…", () =>', '"新增工作樹…", () =>'),
    ('"Open worktree\\u2026", () =>', '"開啟工作樹\\u2026", () =>'),
    ('"New space", () => run("space.new")', '"新增空間", () => run("space.new")'),
]

MODS["pane/main.js"] = [
    ('.child("Needs you")', '.child("需要你")'),
]

MODS["peek/main.js"] = [
    ('{ working: "working", blocked: "needs you", done: "finished", idle: "idle" }',
     '{ working: "工作中", blocked: "需要你", done: "已完成", idle: "閒置" }'),
    ('`from ${parent.name || parent.address}`', '`來自 ${parent.name || parent.address}`'),
    ('home ? "↗ go to" : "↗ keep"', 'home ? "↗ 前往" : "↗ 保留"'),
]

MODS["picker/main.js"] = [
    ('placeholder: "Go to a tab, space or agent…"', 'placeholder: "前往分頁、空間或代理程式…"'),
    ('`earlier: ${r.count} quiet space${r.count > 1 ? "s" : ""} ${this.showEarlier ? "▴" : "▾"}`',
     '`較早：${r.count} 個閒置空間 ${this.showEarlier ? "▴" : "▾"}`'),
    ('r.kind === "new" ? "new tab" : r.machine ? `new space on ${r.machine}` : "new space"',
     'r.kind === "new" ? "新增分頁" : r.machine ? `在 ${r.machine} 上新增空間` : "新增空間"'),
    ('.child("needs you")', '.child("需要你")'),
    ('.child("finished")', '.child("已完成")'),
    ('.child("Go to…")', '.child("前往…")'),
]

MODS["prompt/main.js"] = [
    ('label("Name")', 'label("名稱")'),
    ('button("pm-save", "Save"', 'button("pm-save", "儲存"'),
    ('button("pm-cancel", "Cancel"', 'button("pm-cancel", "取消"'),
]

MODS["spaces/main.js"] = [
    ('collapsed ? "…" : "Loading…"', 'collapsed ? "…" : "正在載入…"'),
    ('m ?? "This computer"', 'm ?? "這台電腦"'),
    ('el.child("New space there")', 'el.child("在這裡新增空間")'),
    ('el.child("Spaces")', 'el.child("空間")'),
    # 0.1.12 新增：機器重建後的重新連線
    ('"Couldn\'t connect."', '"無法連線。"'),
    ('"This machine was rebuilt or replaced. Click to connect to the new one."',
     '"這台機器已重建或更換。點一下連到新的那台。"'),
    ('repair?.busy ? "Connecting…" : "Connect"', 'repair?.busy ? "正在連線…" : "連線"'),
]

MODS["tabs/main.js"] = [
    ('program?.name ?? "Terminal"', 'program?.name ?? "終端機"'),
    ('panelButton("files", "Files"', 'panelButton("files", "檔案"'),
    ('panelButton("changes", "Changes"', 'panelButton("changes", "變更"'),
]

MODS["workspace-chrome/main.js"] = [
    ('row("machine", "plus", "Add machine"', 'row("machine", "plus", "新增機器"'),
    ('row("settings", "settings", "Settings"', 'row("settings", "settings", "設定"'),
]

MODS["workspace-status/main.js"] = [
    ('`${key}  commands` : "commands"', '`${key}  指令` : "指令"'),
    ('`${list.length} agents`', '`${list.length} 個代理程式`'),
    ('`· ${needs} needs you`', '`· ${needs} 個需要你`'),
    ('space?.machine ?? "This computer"', 'space?.machine ?? "這台電腦"'),
]

MODS["worktree/main.js"] = [
    ('placeholder: this.opening ? "filter worktrees" : "branch name"',
     'placeholder: this.opening ? "篩選工作樹" : "分支名稱"'),
    ('"Could not find the remote home folder."', '"找不到遠端的家目錄。"'),
    ('"Type a branch name."', '"請輸入分支名稱。"'),
    ('"git worktree add failed."', '"git worktree add 失敗。"'),
    ('"git status failed."', '"git status 失敗。"'),
    ('"git rev-parse failed."', '"git rev-parse 失敗。"'),
    ('`Couldn\'t check submodule ${m.name}.`', '`無法檢查子模組 ${m.name}。`'),
    ('"It changed since this opened. Enter again removes it anyway."',
     '"開啟後它已變更。再按一次 Enter 仍會移除。"'),
    ('"git worktree remove failed."', '"git worktree remove 失敗。"'),
    ('.child("main checkout")', '.child("主要簽出")'),
    ('`${all.length} checkouts`', '`${all.length} 個簽出`'),
    ('`${rows.length}/${all.length} checkouts`', '`${rows.length}/${all.length} 個簽出`'),
    ('"No matching worktrees."', '"沒有符合的工作樹。"'),
    ('"\\u2191\\u2193 choose \\u00b7 \\u21b5 open \\u00b7 esc close"',
     '"\\u2191\\u2193 選擇 \\u00b7 \\u21b5 開啟 \\u00b7 esc 關閉"'),
    ('"This is the repository\'s main checkout, not a worktree."', '"這是儲存庫的主要簽出，不是工作樹。"'),
    ('"It has uncommitted changes: they will be lost."', '"它有未提交的變更：這些變更將會遺失。"'),
    ('`Submodule ${this.unpushed.join(", ")} has commits that aren\'t pushed anywhere: they will be lost.`',
     '`子模組 ${this.unpushed.join(", ")} 有尚未推送到任何地方的提交：這些提交將會遺失。`'),
    ('`Remove worktree ${s?.name ?? ""}?`', '`移除工作樹 ${s?.name ?? ""}？`'),
    ('this.busy ? "working…" : blocked ? "esc close" : remove ? "↵ remove · esc cancel" : "↵ create · esc cancel"',
     'this.busy ? "處理中…" : blocked ? "esc 關閉" : remove ? "↵ 移除 · esc 取消" : "↵ 建立 · esc 取消"'),
    ('`${Math.max(1, Math.round(d / 60))}m`', '`${Math.max(1, Math.round(d / 60))} 分`'),
    ('`${Math.round(d / 3600)}h`', '`${Math.round(d / 3600)} 小時`'),
    ('`${Math.round(d / 86400)}d`', '`${Math.round(d / 86400)} 天`'),
    ('`${Math.round(d / 86400 / 30)}mo`', '`${Math.round(d / 86400 / 30)} 個月`'),
    ('`Open worktree${r ? ` of ${r.name}` : ""}`', '`開啟工作樹${r ? `：${r.name}` : ""}`'),
    ('`New worktree${r ? ` of ${r.name}` : ""}`', '`新增工作樹${r ? `：${r.name}` : ""}`'),
    ('tilde(this.folder, this.userHome ?? "") : "This folder"} is not in a git repository.`',
     'tilde(this.folder, this.userHome ?? "") : "這個資料夾"} 不在 git 儲存庫中。`'),
    ('tilde(this.folder, this.userHome) : "This folder"} is not in a git repository.`',
     'tilde(this.folder, this.userHome) : "這個資料夾"} 不在 git 儲存庫中。`'),
    ('`Closes the space and deletes ${tilde(r.top, this.userHome)}. The branch stays.`',
     '`關閉該空間並刪除 ${tilde(r.top, this.userHome)}。分支會保留。`'),
    ('`A new space on a checkout in ${tilde(ROOT(this.userHome), this.userHome)}/${r.name}/. A branch that exists is checked out; a new one starts from here.`',
     '`在 ${tilde(ROOT(this.userHome), this.userHome)}/${r.name}/ 的簽出上建立新空間。已存在的分支會被簽出；新分支則從目前位置開始。`'),
]

# ---------------------------------------------------------------- frame 面板
FRAME = {}

FRAME["settings/main.js"] = [
    ('{ id: "look", title: "Look"', '{ id: "look", title: "外觀"'),
    ('{ id: "machines", title: "Machines"', '{ id: "machines", title: "機器"'),
    ('{ id: "alerts", title: "Alerts"', '{ id: "alerts", title: "提醒"'),
    ('{ id: "updates", title: "Updates"', '{ id: "updates", title: "更新"'),
    ('{ id: "privacy", title: "Privacy"', '{ id: "privacy", title: "隱私"'),
    ('.child("Settings")', '.child("設定")'),
    ('"st-feedback", "Send feedback"', '"st-feedback", "傳送意見回饋"'),
    ('terminals: "Terminals"', 'terminals: "終端機"'),
    ('[null, "System"]', '[null, "系統"]'),
    ('["light", "Light"]', '["light", "淺色"]'),
    ('["dark", "Dark"]', '["dark", "深色"]'),
    ('.text_color(t.muted).child("Dark"))', '.text_color(t.muted).child("深色"))'),
    ('.text_color(t.muted).child("Light"))', '.text_color(t.muted).child("淺色"))'),
    ('placeholder: "Type to search fonts"', 'placeholder: "輸入以搜尋字型"'),
    ('`Default (${def})`', '`預設（${def}）`'),
    ('"This layout sets its own; yours shows in the others."', '"此版面自行指定；你的設定會套用在其他版面。"'),
    ('this.heading(t, "Layout")', 'this.heading(t, "版面")'),
    ('this.heading(t, "Theme")', 'this.heading(t, "主題")'),
    ('this.row(t, "Appearance", "Light or dark, or as your system is now."',
     'this.row(t, "外觀模式", "淺色或深色，或跟隨目前的系統設定。"'),
    ('"For the layout you\'re in: each layout keeps its own light and dark theme."',
     '"僅套用於目前的版面：每個版面各自保有淺色與深色主題。"'),
    ('this.heading(t, "Size and fonts")', 'this.heading(t, "大小與字型")'),
    ('      "Zoom",', '      "縮放",'),
    ('"Everything: terminals, panels, text."', '"包含終端機、面板與文字。"'),
    ('"st-zoom-reset", "Reset"', '"st-zoom-reset", "重設"'),
    ('"font", "font_size", "Terminal font"', '"font", "font_size", "終端機字型"'),
    ('"ui_font", null, "Interface font"', '"ui_font", null, "介面字型"'),
    ('"Couldn\'t read machines."', '"無法讀取機器清單。"'),
    ('"It didn\'t work."', '"沒有成功。"'),
    ('`Updated ${machine}${payload?.version ? ` to hc ${payload.version}` : ""}; its terminals kept running.`',
     '`已更新 ${machine}${payload?.version ? `至 hc ${payload.version}` : ""}；它的終端機仍在執行。`'),
    ('`Renamed ${machine} to ${name.trim()}.`', '`已將 ${machine} 重新命名為 ${name.trim()}。`'),
    ('`Removed ${machine}; its terminals keep running there.`',
     '`已移除 ${machine}；它上面的終端機仍會繼續執行。`'),
    ('"Updating…"', '"正在更新…"'),
    ('"Renaming…"', '"正在重新命名…"'),
    ('"Removing…"', '"正在移除…"'),
    ('[["rename", "Rename"], ["rm", "Remove"]]', '[["rename", "重新命名"], ["rm", "移除"]]'),
    ('"Copying this computer\'s herdr-core. Its terminals keep running."',
     '"正在複製這台電腦的 herdr-core。它的終端機仍會繼續執行。"'),
    ('`st-m-cancel-${m.name}`, "Cancel"', '`st-m-cancel-${m.name}`, "取消"'),
    ('`Remove ${m.name}? Its terminals keep running there.`',
     '`要移除 ${m.name} 嗎？它上面的終端機仍會繼續執行。`'),
    ('"Remove machine"', '"移除機器"'),
    ('"New name (addresses using the old name stop working)"', '"新名稱（使用舊名稱的位址將失效）"'),
    ('`st-m-save-${m.name}`, "Save"', '`st-m-save-${m.name}`, "儲存"'),
    ('"Your computers, reached over ssh. Their terminals keep running when you disconnect."',
     '"你的電腦，透過 ssh 連線。中斷連線後它們的終端機仍會繼續執行。"'),
    ('this.row(t, "This computer"', 'this.row(t, "這台電腦"'),
    ('"Reading machines…"', '"正在讀取機器…"'),
    ('"No other machines yet."', '"尚未新增其他機器。"'),
    ('"st-m-add", "Add a machine"', '"st-m-add", "新增機器"'),
    ('"Herdr\'s sound"', '"Herdr 預設音效"'),
    ('this.heading(t, "Sounds")', 'this.heading(t, "音效")'),
    ('      "Play sounds",', '      "播放音效",'),
    ('"When an agent needs you, and when one finishes while you\'re not looking. A note shows in the corner either way."',
     '"當代理程式需要你，或在你沒注意時完成工作。兩種情況角落都會有提示。"'),
    ('this.row(t, "An agent needs you"', 'this.row(t, "代理程式需要你"'),
    ('"st-play-blocked", "Play"', '"st-play-blocked", "試聽"'),
    ('this.row(t, "An agent finished"', 'this.row(t, "代理程式已完成"'),
    ('"st-play-done", "Play"', '"st-play-done", "試聽"'),
    ('"Want your own sounds? Ask your agent to set sounds.done and sounds.blocked in settings.json to an MP3."',
     '"想用自己的音效？請代理程式在 settings.json 把 sounds.done 與 sounds.blocked 設成 MP3 檔。"'),
    ('` Checked at ${at(u.checked)}.`', '` 檢查時間 ${at(u.checked)}。`'),
    ('"Checking\\u2026"', '"正在檢查\\u2026"'),
    ('`Up to date.${checked}`', '`已是最新版本。${checked}`'),
    ('"No successful check. Check your connection and try again."', '"檢查未成功。請確認網路連線後再試。"'),
    ('"\\u2713 Up to date"', '"\\u2713 已是最新"'),
    ('t, id, "Check now"', 't, id, "立即檢查"'),
    ('"A build from source: it updates with git, not here."', '"由原始碼建置的版本：請用 git 更新，不在這裡。"'),
    ('`${u.app.ready} is ready. Restart to switch now; it also switches when you quit.`',
     '`${u.app.ready} 已就緒。重新啟動即可切換；下次結束程式時也會切換。`'),
    ('"Restart to update"', '"重新啟動以更新"'),
    ('`Managed by ${c.managed}: update it there.`', '`由 ${c.managed} 管理：請在那邊更新。`'),
    ('"Updating\\u2026 your terminals keep running."', '"正在更新\\u2026 你的終端機仍會繼續執行。"'),
    ('`The update failed: ${c.error}`', '`更新失敗：${c.error}`'),
    ('"st-core-retry", "Try again"', '"st-core-retry", "再試一次"'),
    ('`${c.ready} is ready. Your terminals keep running through it.`',
     '`${c.ready} 已就緒。更新過程中你的終端機會繼續執行。`'),
    ('"st-core-update", "Update herdr-core"', '"st-core-update", "更新 herdr-core"'),
    ('"Not checked: a build from source looks for no updates."', '"未檢查：由原始碼建置的版本不會尋找更新。"'),
    ('"st-whats-new", "What\'s new"', '"st-whats-new", "更新內容"'),
    ('"Herdr looks for both every hour and tells you in the corner. herdr-core runs your terminals, so they keep running through its updates."',
     '"Herdr 每小時檢查一次並在角落提示。你的終端機由 herdr-core 執行，所以更新時不會中斷。"'),
    ('`Off for now: ${s.off_because} is set where Herdr started.`',
     '`目前已關閉：啟動 Herdr 的環境設了 ${s.off_because}。`'),
    ('this.heading(t, "Usage data")', 'this.heading(t, "使用資料")'),
    ('      "Share anonymous usage data",', '      "分享匿名使用資料",'),
    ('"Once a day: which agents and features you use, how many spaces and tabs, your system and Herdr\'s version. Never what\'s in your terminals, never names of files, folders or projects."',
     '"每天一次：你用了哪些代理程式與功能、有幾個空間與分頁、你的系統與 Herdr 版本。絕不包含終端機內容，也不包含檔案、資料夾或專案名稱。"'),
    ('      "What we send",', '      "會傳送的內容",'),
    ('"This build never sends: it\'s built from source. You can still see what a release would send."',
     '"此版本不會傳送：它由原始碼建置。你仍可以看正式版會傳什麼。"'),
    ('"Exactly what leaves your computer, word for word."', '"離開你電腦的內容，逐字如實呈現。"'),
    ('this.showData ? "Hide" : "Show"', 'this.showData ? "隱藏" : "顯示"'),
    ('"Nothing is collected or sent while it\'s off."', '"關閉期間不會收集也不會傳送任何資料。"'),
    ('`Waiting to send: ${r.day}`', '`等待傳送：${r.day}`'),
    ('"Sent as is, soon."', '"將原樣傳送。"'),
    ('"st-td", "Today so far"', '"st-td", "今日目前"'),
    ('"A draft: it changes until the day ends (UTC), then goes out once."',
     '"草稿：會持續變動至當日（UTC）結束，然後傳送一次。"'),
    ('`Last sent: ${s.last_sent.report.day}`', '`上次傳送：${s.last_sent.report.day}`'),
    ('`Sent ${at(s.last_sent.at)}.`', '`傳送於 ${at(s.last_sent.at)}。`'),
    # 0.1.12 新增的鍵盤分頁（只在 macOS 顯示）
    ('{ id: "keyboard", title: "Keyboard", icon: "keyboard" }',
     '{ id: "keyboard", title: "鍵盤", icon: "keyboard" }'),
    ('["auto", "Automatic (Alt on US keyboards)"]', '["auto", "自動（美式鍵盤上視為 Alt）"]'),
    ('["off", "Types characters"]', '["off", "輸入字元"]'),
    ('["left", "Left Option is Alt"]', '["left", "左 Option 當 Alt"]'),
    ('["right", "Right Option is Alt"]', '["right", "右 Option 當 Alt"]'),
    ('this.heading(t, "Option key")', 'this.heading(t, "Option 鍵")'),
    ('"Use Option for terminal shortcuts or to type accents and special characters."',
     '"用 Option 執行終端機快捷鍵，或輸入重音與特殊字元。"'),
    # 機器頁的區塊標題與狀態
    ('this.heading(t, "Machines")', 'this.heading(t, "機器")'),
    ('`st-m-update-${m.name}`, "Update"', '`st-m-update-${m.name}`, "更新"'),
    ('`Connected · ${version ? `hc ${version}` : "hc version unknown"}`',
     '`已連線 · ${version ? `hc ${version}` : "hc 版本未知"}`'),
    # 其他機器的狀態列。state 由後端給，只有這三個值（src/*.rs）。
    # 用行內的對照表，不另外宣告全域，免得重跑時重複定義。
    ('const state = String(m.state ?? "unknown").replace(/[_-]/g, " ");',
     'const state = ({ connected: "已連線", unreachable: "無法連線", unknown: "狀態未知" })[m.state]\n'
     '      ?? String(m.state ?? "unknown").replace(/[_-]/g, " ");'),
    ('`${m.target ?? ""} · ${state} · ${m.version ? `hc ${m.version}` : "hc version unknown"}`',
     '`${m.target ?? ""} · ${state} · ${m.version ? `hc ${m.version}` : "hc 版本未知"}`'),
]

FRAME["settings/release-notes.js"] = [
    ('const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];',
     'const months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"];'),
    ('`${months[Number(month) - 1]} ${Number(day)}`', '`${months[Number(month) - 1]}${Number(day)}日`'),
    ('.child("Also fixed")', '.child("其他修正")'),
]

FRAME["palette/main.js"] = [
    # GROUPS 同時是分組 key（NAMED 第 3 欄、rows() 的比對）與顯示文字，
    # 不能直接翻。保留 key，另加一張顯示用的表，在輸出處查。
    ('const GROUPS = ["Recent", "Tab", "Pane", "Space", "Layout", "Terminal", "Agent", "Window", "App"];',
     'const GROUPS = ["Recent", "Tab", "Pane", "Space", "Layout", "Terminal", "Agent", "Window", "App"];\n'
     '// 分組的顯示名：GROUPS 的值是 key，不能動，這裡只管畫出來的字。\n'
     'const GROUP_LABEL = { Recent: "最近", Tab: "分頁", Pane: "窗格", Space: "空間", Layout: "版面",\n'
     '  Terminal: "終端機", Agent: "代理程式", Window: "視窗", App: "應用程式" };\n'
     'const DIR_LABEL = { left: "左", right: "右", up: "上", down: "下" };'),
    ('.child(r.head));', '.child(GROUP_LABEL[r.head] ?? r.head));'),
    ('.child(r.e.group)))', '.child(GROUP_LABEL[r.e.group] ?? r.e.group)))'),
    # 指令名稱
    ('"Tab", "New tab"', '"Tab", "新增分頁"'),
    ('"Tab", "Go to space or tab…"', '"Tab", "前往空間或分頁…"'),
    ('"Tab", "Rename tab"', '"Tab", "重新命名分頁"'),
    ('"Tab", "Close tab"', '"Tab", "關閉分頁"'),
    ('"Tab", "Next tab"', '"Tab", "下一個分頁"'),
    ('"Tab", "Previous tab"', '"Tab", "上一個分頁"'),
    ('"Pane", "Split right"', '"Pane", "向右分割"'),
    ('"Pane", "Split down"', '"Pane", "向下分割"'),
    ('"Pane", "Close pane"', '"Pane", "關閉窗格"'),
    ('"Pane", "Zoom pane"', '"Pane", "縮放窗格"'),
    ('`Focus pane ${d}`', '`聚焦${DIR_LABEL[d]}側窗格`'),
    ('`Swap pane ${d}`', '`與${DIR_LABEL[d]}側窗格互換`'),
    ('"Space", "New space"', '"Space", "新增空間"'),
    ('"Space", "Rename space"', '"Space", "重新命名空間"'),
    ('"Space", "Close space"', '"Space", "關閉空間"'),
    ('"Space", "Next space"', '"Space", "下一個空間"'),
    ('"Space", "Previous space"', '"Space", "上一個空間"'),
    ('"Layout", "Next layout"', '"Layout", "下一個版面"'),
    ('"Layout", "Reset layout"', '"Layout", "重設版面"'),
    ('"Layout", "Duplicate layout"', '"Layout", "複製版面"'),
    ('"Layout", "Duplicate mod"', '"Layout", "複製面板"'),
    ('"Terminal", "New terminal"', '"Terminal", "新增終端機"'),
    ('"Terminal", "Copy"', '"Terminal", "複製"'),
    ('"Terminal", "Paste"', '"Terminal", "貼上"'),
    ('"Agent", "Next agent"', '"Agent", "下一個代理程式"'),
    ('"Agent", "Previous agent"', '"Agent", "上一個代理程式"'),
    ('"Window", "Minimize window"', '"Window", "最小化視窗"'),
    ('"Window", "Maximize window"', '"Window", "最大化視窗"'),
    ('"Window", "Close window"', '"Window", "關閉視窗"'),
    ('"App", "Settings"', '"App", "設定"'),
    ('"App", "Keys"', '"App", "快捷鍵"'),
    ('"App", "Welcome"', '"App", "歡迎畫面"'),
    ('"App", "What\'s new"', '"App", "更新內容"'),
    ('"App", "Reset to the default screen"', '"App", "重設為預設畫面"'),
    ('"App", "Zoom in"', '"App", "放大"'),
    ('"App", "Zoom out"', '"App", "縮小"'),
    ('"App", "Reset zoom"', '"App", "重設縮放"'),
    ('"App", "Quit Herdr"', '"App", "結束 Herdr"'),
    ('`Theme: ${n.replace(/-/g, " ")}`', '`主題：${n.replace(/-/g, " ")}`'),
    ('terminals: "Terminals", win98: "Herdr 98"', 'terminals: "終端機", win98: "Herdr 98"'),
    ('`Layout: ${t}`', '`版面：${t}`'),
    ('placeholder: "Type a command…"', 'placeholder: "輸入指令…"'),
    ('title: "Duplicate mod", hint: "Mod to copy; creates <name>-copy"',
     'title: "複製面板", hint: "要複製的面板；會建立 <name>-copy"'),
    ('`Nothing matches "${this.query}". Places are in the picker.`',
     '`找不到符合「${this.query}」的項目。空間與分頁請用前往選擇器。`'),
]

FRAME["whatsnew/main.js"] = [
    ('.child("What\'s new in Herdr")', '.child("Herdr 更新內容")'),
    ('.child("Something off or missing? Settings › Send feedback.")',
     '.child("有問題或少了什麼？設定 › 傳送意見回饋。")'),
    ('.child("Got it")', '.child("知道了")'),
]

FRAME["whatsnew/release-notes.js"] = [
    ('const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];',
     'const months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"];'),
    ('`${months[Number(month) - 1]} ${Number(day)}`', '`${months[Number(month) - 1]}${Number(day)}日`'),
    ('.child("Also fixed")', '.child("其他修正")'),
]

FRAME["welcome/main.js"] = [
    ('[null, "System"]', '[null, "系統"]'),
    ('["light", "Light"]', '["light", "淺色"]'),
    ('["dark", "Dark"]', '["dark", "深色"]'),
    ('title: "Files", about: "The folder you\'re in as a tree. Open a file to read it, highlighted."',
     'title: "檔案", about: "目前資料夾的樹狀檢視。點開檔案即可閱讀，附語法高亮。"'),
    ('title: "Changes", about: "What your agents changed: every file with its diff, and a commit box."',
     'title: "變更", about: "代理程式改了什麼：每個檔案與其差異，還有提交欄。"'),
    ('copied ? "Copied" : "Copy"', 'copied ? "已複製" : "複製"'),
    ('.child("Coming from herdr?")', '.child("從 herdr 過來的嗎？")'),
    ('"This is a new app on a new core. Your herdr workspaces stay where they are; nothing moves over."',
     '"這是建在新核心上的新程式。你原本 herdr 的工作區留在原處，不會搬過來。"'),
    ('"Same idea as before: spaces, tabs and terminals."', '"概念跟以前一樣：空間、分頁與終端機。"'),
    ('"Want your keybinds and settings carried over? Give your agent this line:"',
     '"想把快捷鍵與設定帶過來？把這行交給你的代理程式："'),
    ('"Herdr runs your terminals in the background"', '"Herdr 讓你的終端機在背景持續執行"'),
    ('"Agents tell you when they need you"', '"代理程式需要你時會通知"'),
    ('"A ring while one works, \\u201cNeeds you\\u201d when it asks something, a sound when it finishes."',
     '"工作中會有轉圈動畫，要問你事情時顯示「需要你」，完成時發出音效。"'),
    ('"Agents can start helpers"', '"代理程式可以啟動協作程式"'),
    ('"They show up under the agent that started them. Click one to watch it."',
     '"它們會列在啟動它的代理程式底下。點一下就能看它在做什麼。"'),
    ('"Your other machines, in the same window"', '"你的其他電腦，在同一個視窗裡"'),
    ('"A server or a Mac mini runs its own herdr-core, so its agents keep going even while this laptop sleeps."',
     '"伺服器或 Mac mini 跑它自己的 herdr-core，所以這台筆電睡眠時，上面的代理程式仍會繼續執行。"'),
    ('.child("Appearance"))', '.child("外觀"))'),
    ('.child("Size"))', '.child("大小"))'),
    ('"Add your other machines"', '"加入你的其他電腦"'),
    ('"Pick a host from your ssh config. Herdr connects, installs herdr-core there if it\'s missing, and lists that machine in the sidebar with its own spaces."',
     '"從你的 ssh 設定挑一台主機。Herdr 會連上去，必要時幫它裝 herdr-core，然後在側邊欄列出那台電腦與它的空間。"'),
    ('"monitor", "This computer"', '"monitor", "這台電腦"'),
    ('.child("Add a machine"),', '.child("新增機器"),'),
    ('"Not now? Add machine is at the bottom of the sidebar too."', '"現在不要？側邊欄底部也有「新增機器」。"'),
    ('"Choose your panels"', '"選擇你的面板"'),
    ('"Herdr comes with a couple of panels. Turn one on and it appears beside your terminals. Drag this window aside to see it. Later, the buttons in the tab bar open and close them."',
     '"Herdr 內建幾個面板。開啟後它會出現在終端機旁邊；把這個視窗拖開就看得到。之後用分頁列上的按鈕開關它們。"'),
    ('"Ask your agent for a board of your agents, your pull requests, a cost meter, or the sidebar on the right. Not sure what\'s possible? Ask it that too."',
     '"你可以請代理程式做一個代理程式看板、PR 清單、花費計量，或把側邊欄移到右邊。不確定能做什麼？也問它。"'),
    ('.child("One key opens everything")', '.child("一個按鍵開啟一切")'),
    ('"It opens the command palette, with every action by name and its key. It works the same in every layout."',
     '"它會開啟命令面板，列出每個動作的名稱與快捷鍵。在每種版面下都一樣好用。"'),
    ('"Make it yours"', '"打造成你的樣子"'),
    ('"Every part of this window is a layout or a mod: plain files your agent can change or add to. Give it this line to start:"',
     '"這個視窗的每個部分都是版面或面板：都是代理程式可以修改或新增的純文字檔。把這行交給它開始："'),
    ('"Then ask for anything: \\u201cmove the sidebar to the right\\u201d, \\u201ca panel with my pull requests\\u201d."',
     '"然後想要什麼就說：「把側邊欄移到右邊」、「做一個顯示我的 PR 的面板」。"'),
    ('.child("Your terminals, outside this window too")', '.child("你的終端機，在這個視窗之外也能用")'),
    ('.child("More examples in Settings")', '.child("設定裡有更多範例")'),
    ('"Settings \\u203a Look has more layouts to try or start from, Herdr 98 among them. Your agent can copy any of them and change anything."',
     '"設定 › 外觀還有更多版面可以試用或當起點，包含 Herdr 98。代理程式可以複製任何一個再隨意修改。"'),
    ('"Something off or missing? Settings \\u203a Send feedback. We read every one."',
     '"有問題或少了什麼？設定 › 傳送意見回饋。我們每一則都會看。"'),
    ('.child("Welcome to Herdr")', '.child("歡迎使用 Herdr")'),
    ('.child("Drag to move")', '.child("拖曳即可移動")'),
    ('"w-back", "Back"', '"w-back", "上一步"'),
    ('this.page === 2 && !this.machines.length ? "Not now" : "Next"',
     'this.page === 2 && !this.machines.length ? "現在不要" : "下一步"'),
    ('spaces().length ? "Done" : "Open a space"', 'spaces().length ? "完成" : "開啟一個空間"'),
]

FRAME["feedback/main.js"] = [
    ('placeholder: "What happened? What did you expect?"', 'placeholder: "發生了什麼事？你原本預期如何？"'),
    ('placeholder: "Email (optional)"', 'placeholder: "電子郵件（選填）"'),
    ('"Up to 3 screenshots."', '"最多 3 張截圖。"'),
    ('"feedback-add", "Add screenshot"', '"feedback-add", "加入截圖"'),
    ('.child("Send feedback")', '.child("傳送意見回饋")'),
    ('"This build was made from source and doesn\'t send feedback. Use a release build."',
     '"此版本由原始碼建置，不會傳送意見回饋。請改用正式發行版。"'),
    ('"Drafted by an agent: read it before sending"', '"由代理程式草擬：送出前請先看過"'),
    ('"Sent. Thanks for helping us improve Herdr."', '"已送出。感謝你協助我們改進 Herdr。"'),
    ('label("Your message (up to 4000 characters). Paste or drop screenshots, up to 3.")',
     'label("你的訊息（上限 4000 字）。可貼上或拖放截圖，最多 3 張。")'),
    ('label("Email: only if you want a reply")', 'label("電子郵件：只有想收到回覆才需要填")'),
    ('label("What we send: exactly this JSON, plus the screenshots above. No logs or install ID.")',
     'label("會傳送的內容：就是下面這份 JSON，加上上方的截圖。不含日誌或安裝 ID。")'),
    ('this.sent ? "Done" : "Cancel"', 'this.sent ? "完成" : "取消"'),
    ('this.sending ? "Sending…" : "Send"', 'this.sending ? "正在傳送…" : "傳送"'),
]

# mod.json 的面板標題
TITLES = {
    "frame/settings/mod.json": [('"title": "Settings"', '"title": "設定"')],
    "frame/palette/mod.json": [('"title": "Command palette"', '"title": "命令面板"')],
    "frame/welcome/mod.json": [('"title": "Welcome"', '"title": "歡迎畫面"')],
    "frame/whatsnew/mod.json": [('"title": "What\'s new"', '"title": "更新內容"')],
    "frame/feedback/mod.json": [('"title": "Send feedback"', '"title": "傳送意見回饋"')],
}

# ---------------------------------------------------------------- X 關閉鈕
# 對話框右上角的 "Esc" 文字改成可點的 X（鍵盤 Esc 照舊能用）
ESC_OLD = 'div().text_size(11).text_color(t.dim).child("Esc")'
ESC_NEW = (
    'div().id("ov-close").size(22).flex_none().flex().items_center().justify_center()'
    '.rounded(5).cursor_pointer().text_color(t.dim)'
    '.hover((s) => s.bg(t.hover).text_color(t.foreground))'
    '.on_click((_e, cx) => { cx.stop_propagation(); closeOverlay(props().overlay); })'
    '.child(svg("mods/pane/close.svg").size(13))'
)
# 這些檔案要加 X 鈕；True 代表還要補 svg import
CLOSE_BUTTON = {
    "machine-add/main.js": False,
    "picker/main.js": False,
    "confirm/main.js": True,
    "prompt/main.js": True,
    "help/main.js": True,
}
# frame 底下的同樣處理（palette 已有 svg 與 closeOverlay）
FRAME_CLOSE_BUTTON = {
    "palette/main.js": False,
}
IMPORT_OLD = 'import { View, div } from "gpui-kit";'
IMPORT_NEW = 'import { View, div, svg } from "gpui-kit";'
