# Herdr changelog

## [0.1.12] - 2026-11-02
<!-- spotlight macos -->

### New
- **在 macOS 上，代理程式現在完全獨立於 app 之外執行。** 關閉 Herdr、結束它、更新它，代理程式都會繼續執行。已在執行的代理程式會在下次啟動時套用這項改變。
- 在 macOS 上，系統可能會問一次 **herdr-core** 是否能存取「文件」之類的資料夾。那就是 Herdr，請按允許。
- 在 macOS 上，設定 > 鍵盤可以決定 Option 鍵的行為：當 Alt、輸入 á 與 € 之類的字元，或只讓左／右 Option 當 Alt。
- 被重建或更換過的機器會在側邊欄顯示「rebuilt · 連線」，點一下就能連到新的那台。
- 已讀與釘選的代理程式會在 Herdr 視窗與手機 app 之間同步。
- 面板可以接收鍵盤輸入，所以移動焦點時會停在它們上面。 (#283, thanks @Osc100)
- PiG 代理程式有自己的圖示。 (#299, thanks @balcsida)
- 新增機器可以指定連接埠，例如 `can@server:2222`。

### Fixed
- 在 Linux 上，彩色表情符號會正常顯示顏色而不是空白（Fedora 的表情符號字型）。
- ✍️ 與 ❤️ 這類表情符號會佔兩格並以彩色繪製。 (#287, thanks @occultsound)
- 在 macOS 上，Herdr 終端機裡的程式可以請求麥克風、相機權限，以及控制其他 app。 (#137, thanks @shivanandasai-altir; #252)
- 其他機器上的代理程式找得到該機 shell 設定加進 PATH 的指令。 (#262, thanks @tajchert)
- 新空間會開在你正在看的那台機器上。
- 水平捲動可以傳給 vim、less 這類程式。
- 在 Textual 應用程式裡點擊可以正常運作。
- btop 的點字圖表繪製時不再有空隙。
- Nerd Font 圖示會使用你設定的終端機字型。
- 方框的圓角與虛線繪製方式與 Ghostty 一致。 (#255, thanks @occultsound)
- 同時有多個忙碌的代理程式時，Herdr 使用的 CPU 較少。
- 大型專案不會再讓資料夾監看吃掉一整顆 CPU 核心。 (#263, #257)
- 面板的圖片與圖示會在檔案存檔時更新。
- 把焦點移回分割區時，會回到你原本所在的窗格。 (#304, thanks @sundarshahi)
- 未命名的分頁會在代理程式清單顯示它的代理程式正在做什麼。 (#281, thanks @sundarshahi)
- 在沒有開啟空間時新增分頁，會自動建立一個空間。 (#303, thanks @sundarshahi)
- 檔案面板會標記新資料夾內的檔案，也能開啟資料夾符號連結。 (#309, thanks @Nagell; #301, thanks @azaeldrm)
- 面板裡的清單會跟著縮放比例調整。 (#296, thanks @Calonca)
- ＋ 選單會立即顯示你的代理程式。 (#251, thanks @shellscape)
- Grok 會顯示自己的圖示。 (#293, thanks @Zynoo71)
- 格式錯誤的指令不會關掉你目前所在的分頁。 (#297, thanks @chanyang721)
- 在 Linux 上，全新安裝的 Ctrl+Insert 與 Shift+Insert 可以複製貼上；既有安裝請自行加進 keys.json。 (#258, thanks @dr-moreira)
- 在 macOS 全螢幕下，側邊欄標題會對齊。 (#261, thanks @runkids)
- 在 Windows 上，韓文、中文與其他語言的檔名可以在檔案面板正常顯示與開啟。 (#236, thanks @loonslo)
- On Windows, Esc then Ctrl+C reach the program as two keys. (#162, thanks @JJLiebig)
- In Git Bash on Windows, the installer points to the PowerShell one. (#238, thanks @sundarshahi)

## [0.1.11] - 2026-10-31

### Fixed
- The window no longer freezes or spikes the CPU for seconds at a time while mods run.
- Programs get the new colors right away when you change the theme or switch light and dark. (#122, thanks @geoqiao)
- On macOS, Vietnamese input methods like OpenKey, DauKey and Gõ Nhanh type in terminals. (#230, thanks @emizuki)
- Links a program breaks across lines open with Cmd+click. (thanks @pdeveltere)
- Editing the theme you're using repaints the window. (thanks @shawnyeager)
- Mod tooltips show in embedded windows. (thanks @ruilopesm)
- Opening the palette or a popup again closes it instead of stacking another. (#151, thanks @ruttybob)
- The status bar shows your real palette key. (#150, thanks @ruttybob)
- The Go-to popup keeps the selected row in view. (#152, thanks @ruttybob)
- No empty strip under the agents list in a wide sidebar. (thanks @kaofelix)
- A failed update check no longer says "Up to date". (#186, thanks @weichieh0204)

## [0.1.10] - 2026-10-30

### Fixed
- Images that Claude Code, yazi and other programs draw with kitty placeholders show up instead of rows of boxes. (#110)
- Images are the right size and sharp on Retina and other HiDPI screens. (#70, thanks @wpdmitry)
- Hover effects work in Claude Code and other programs that track the mouse.
- A drag that starts in another pane no longer reaches nvim or tmux, and a drag inside one keeps working when you let go outside it.
- Dragging a selection past the top or bottom of a terminal scrolls it.
- Closing a tab or space no longer brings its terminals back as unnamed tabs for a moment. (#108)
- The + menu starts agents with 1 to 9 while it's open, and shows your own shortcuts. (#102, #133, thanks @notHuman9504)
- Add a machine lists every host in your SSH config and shows the install prompt on top. (#95)
- Your own alert sounds play, and sound changes apply without a restart.
- A layout block that shows the focused agent stays in your layout when that agent ends.
- The Files panel keeps your open folders and preview when you switch spaces. (#86, thanks @ruilopesm)
- Dragging a space in the sidebar shows where it will land. (#114, thanks @takahashi-seiryu)
- Long agent titles cut off before the pin and the time. (#127, thanks @rashim2104)
- The + above Spaces lines up with the sidebar button. (#121, thanks @weskor)
- On macOS, a slow mouse wheel scrolls terminals. (#80, thanks @juanibiapina)
- On macOS, Cmd+V pastes copied files and screenshots into agents. (#105, thanks @WesleyBLDC)
- On macOS, Cmd+Shift+[ and ] switch tabs, and other Shift+punctuation shortcuts work.
- On macOS, Option types [ ] { } on ABC-QWERTZ and ABC-AZERTY.
- On macOS, Vietnamese Telex and other input methods compose. (#93)
- On macOS, keys typed with Fn held, like Fn+Esc for a backtick, reach terminals.
- On macOS, agents started from the + menu load your login setup, like Homebrew's PATH.
- On Windows, Ctrl+V pastes text, like Windows Terminal.
- On Windows, the Files panel opens folders with spaces or parentheses in their path. (#130)
- On Windows, the window buttons line up and stay crisp at every display scale.
- On Linux, Chinese typed through fcitx or ibus on X11 comes out right. (#97)
- On Linux, accent keys no longer type a stray character first. (#87, thanks @ruilopesm)
- On Linux, right-clicking a tab no longer opens the window manager's menu too. (#79, thanks @dev-gvs)
- `terminal.open` with a command starts in the folder you give it.
- `herdr-app check` no longer crashes on mods with scrolling lists or layout animations.

## [0.1.9] - 2026-10-30

### Fixed
- On macOS, updates keep Herdr's Apple signature again, so macOS stops forgetting the permissions you gave Herdr.
- Herdr no longer uses CPU in the background when the Changes or Files panel is open in a git repo.
- Mods use less CPU while they wait for work.

## [0.1.8] - 2026-10-30

### New
- **Option works as Alt on macOS.** Claude Code's Option shortcuts work, automatically on US keyboards. Change it with `option_as_alt` in settings.json.
- **Programs can copy to your clipboard,** also from other machines. Pi's or Claude Code's own mouse selection lands on your clipboard.
- **Your own commands in the + menu.** Entries in programs.json show up, shell functions included.

### Fixed
- Accent keys work on macOS and with ibus on Linux, and Caps Lock types capitals on macOS.
- @, [ and friends type on Slovenian, German and other Mac layouts in every program.
- Terminal colors show exactly as programs set them, so powerline prompts look right.
- Double-click selects a word, triple-click a line.
- Agents start from the + menu under fish, and one that fails at launch says why.
- On macOS, the window buttons stay clear of a narrow sidebar and the tabs.
- You can type a commit message in the Changes panel.
- Spaces named with emoji or accents work everywhere.
- The font list in Settings scrolls on its own.
- A downloaded update installs at the next start, even after a crash.

## [0.1.7] - 2026-10-29

### Fixed
- Herdr no longer freezes when a terminal shows an older Nerd Font icon it has no picture for, like some powerlevel10k battery icons. It draws them as text instead.

## [0.1.6] - 2026-10-29

### New
- **Coming from herdr?** The welcome says what carries over and gives you one line for your agent to bring your keybinds and settings across. Open it again with Show the welcome again in the command palette.
- **Updates at a glance.** Settings → Updates shows the app and the core on one row each, with What's new a click away.
- **herdr-core updates with Herdr.** After Herdr updates, its core moves to the latest version too. Your terminals keep running.
- **Screenshots in feedback.** Drop images straight onto the feedback form.

### Fixed
- Paste and copy in a peek go to the terminal you're peeking at, not the agent behind it.
- Scroll back through thousands of lines instead of a few hundred.
- Mod data, like topics and colors, can't get lost if Herdr closes in the middle of saving.
- Commands with an argument they don't know say so instead of acting on the current terminal.
- On Windows, file links at the end of a sentence open the right file.

## [0.1.5] - 2026-10-27
<!-- spotlight -->

### New
- **Drag panes where you want them.** Hover the top of a pane and grab the dots. Drop it on another pane to swap them, or near an edge to put it beside. A highlight shows where it lands.
  ![Dragging a pane beside another](https://media.herdr.dev/0.1.5/pane-drag.webp)
- **Ctrl-click a terminal to peek at it.** When an agent mentions another terminal, like t2, Ctrl-click (Cmd on macOS) its address to see it over your tab. Go to jumps there.
  ![Peeking at a terminal an agent mentioned](https://media.herdr.dev/0.1.5/peek.webp)
- **Agents can see the window.** `herdr-app shot` saves a picture of Herdr as it looks right now, so an agent building a mod can check its work. `herdr-app --skill` and `hc --skill` teach an agent the rest.
- **What changed, after every update.** Release notes like these, in Settings → Updates, including versions you skipped.

### Fixed
- nvim and other full-screen programs redraw right after you resize their pane.
- On Windows, AltGr and accent keys type the right characters, and Shift+Enter adds a new line in Claude Code.
- On Windows, new terminals start in PowerShell 7 when you have it, and Herdr follows their folder.
- On macOS, Herdr keeps the permissions you gave it across updates.
- Short menus open next to the pointer instead of near the top of the window.
- Removing a worktree asks once, then removes it.
- Mods can fetch from the web, know their size, and clean up when they close.

## [0.1.4] - 2026-10-23
<!-- spotlight -->

### New
- **See the agents that need you first.** Pick Priority beside the Agents title: agents waiting on you, then the ones that just finished, then the ones still working. Grouped by space is still there.
- **Pin the ones you're watching.** Hover an agent and click the pin. Pinned agents stay on top in both views until they end.
- **Fold what you don't need.** Click a space or section header to fold it; the header still shows how many agents are inside.

### Fixed
- Temporary agent sandboxes stay out of your spaces and machine lists.
- The agents list keeps its place when you scroll.
- An agent you're in moves to its new section right away.
- A pane closes when its terminal finishes instead of showing “has finished”.
- On macOS, the red close button hides Herdr instead of leaving it without a window.
- Mods reload cleanly when you save them, and tell you when a save didn't load.
