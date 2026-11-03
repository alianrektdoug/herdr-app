// How notifications look. Anything can post one with notify({ title, body,
// level, icon, action }); replace this mod to restyle them all. Click to
// run its action (e.g. go to the agent) and dismiss it.

import { View, div, image } from "gpui-kit";
import { v_flex, h_flex } from "gpui-base";
import { props, closeOverlay, run, theme } from "herdr";

// Rust 送來的通知文字（src/window.rs）。[比對, 轉換] 依序試，第一個命中的為準。
const ZH_NOTE = [
  [/^Your edits are in (.+)$/, (m) => `你的修改已保存在 ${m[1]}`],
  [/^Herdr's own layouts and mods can't be changed: clone one to make it yours\.$/,
    () => "Herdr 內建的版面與面板不能直接修改：複製一份再改成你要的。"],
  [/^Terminal failed to start$/, () => "終端機啟動失敗"],
  [/^(.+) needs mods that aren't here$/, (m) => `${m[1]} 需要的面板不存在`],
  [/^Showing Herdr instead\. Missing: (.+?)\. (.*)$/,
    (m) => `改為顯示 Herdr 版面。缺少：${m[1]}。${m[2]}`],
  [/^(.+) failed$/, (m) => `${m[1]} 失敗`],
];
const zhNote = (s) => {
  const text = String(s ?? "");
  for (const [re, to] of ZH_NOTE) {
    const m = text.match(re);
    if (m) return to(m);
  }
  return text;
};

const DOT = { error: "blocked", warning: "working", success: "done", info: "accent" };

export default class Toast extends View {
  render(cx) {
    const t = theme();
    const p = props() ?? {};
    return h_flex()
      .id("toast")
      .size_full()
      .px(18)
      .gap(12)
      .items_center()
      .bg(t.popover)
      .cursor_pointer()
      .hover((s) => s.bg(t.hover))
      .on_click(() => {
        if (p.action?.name) run(p.action.name, p.action.args ?? {});
        closeOverlay(p.overlay);
      })
      .child(p.icon ? image(p.icon).w(18).h(18).flex_none() : div().size(8).rounded(4).flex_none().bg(t[DOT[p.level] ?? "accent"]))
      .child(
        v_flex()
          .flex_1()
          .overflow_hidden()
          .child(div().truncate().font_semibold().text_size(13).text_color(t.foreground).child(zhNote(p.title)))
          .when(Boolean(p.body), (el) => el.child(div().truncate().text_size(12).text_color(t.muted).child(zhNote(p.body)))),
      );
  }
}
