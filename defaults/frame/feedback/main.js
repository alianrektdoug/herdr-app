import { View, div, image } from "gpui-kit";
import { v_flex, h_flex, InputState, Input, TextareaState, Textarea } from "gpui-base";
import { theme, props, closeOverlay, feedbackPreview, feedbackPasteImage, feedbackPickImages, feedbackAttachImages, feedbackClearImages, sendFeedback } from "herdr";

const MAX_SHOTS = 3;

export default class Feedback extends View {
  init(_props, cx) {
    this.message = TextareaState.new({ value: props()?.message ?? "", placeholder: "發生了什麼事？你原本預期如何？", rows: 4 });
    this.email = InputState.new({ placeholder: "電子郵件（選填）" });
    this.message.on("change", (_e, cx) => { this.error = null; cx.notify(); });
    this.email.on("change", (_e, cx) => { this.error = null; cx.notify(); });
    // A paste with no text: a screenshot, if the clipboard holds one.
    this.message.on("paste_other", (_e, cx) => {
      if (this.shots.length >= MAX_SHOTS) this.error = "最多 3 張截圖。";
      else this.add([feedbackPasteImage()].filter(Boolean));
      cx.notify();
    });
    feedbackClearImages();
    this.shots = [];
    this.sending = false;
    this.sent = false;
    this.error = null;
    this.handle = cx.focus_handle();
    this.message.focus();
  }

  close() { closeOverlay(props()?.overlay); }

  /** Takes `{ path }`s up to the limit; the first `{ error }` is shown. */
  add(results) {
    this.error = null;
    for (const r of results) {
      if (r.error) this.error = r.error;
      else if (this.shots.length >= MAX_SHOTS) this.error = "最多 3 張截圖。";
      else this.shots.push(r.path);
    }
  }

  pick(cx) {
    cx.spawn(async (cx) => {
      try { this.add(await feedbackPickImages()); }
      catch (e) { this.error = String(e.message ?? e); }
      cx.notify();
    });
  }

  shots_row(t) {
    const thumb = (path, i) => div().id(`shot-${i}`).relative().h(72).rounded(6).overflow_hidden().border_1().border_color(t.border)
      .child(image(path).h(72))
      .child(div().id(`shot-x-${i}`).absolute().top(4).right(4).size(20).rounded(10).bg(t.raised).text_color(t.foreground)
        .flex().items_center().justify_center().text_size(12).cursor_pointer()
        .on_click((_e, cx) => { this.shots.splice(i, 1); this.error = null; cx.notify(); }).child("×"));
    return h_flex().w_full().gap(8).items_center()
      .children(this.shots.map(thumb))
      .when(this.shots.length < MAX_SHOTS, (el) => el.child(this.button(t, "feedback-add", "加入截圖", (_e, cx) => this.pick(cx))));
  }

  button(t, id, label, action, primary = false, disabled = false) {
    return div().id(id).px(14).py(7).rounded(7).border_1().border_color(t.border)
      .bg(primary && !disabled ? t.accent : t.raised)
      .text_color(primary && !disabled ? t.accent_foreground : t.muted)
      .cursor_pointer().on_click((e, cx) => { if (!disabled) action(e, cx); }).child(label);
  }

  send(body, cx) {
    if (this.sending || this.sent) return;
    this.sending = true;
    this.error = null;
    cx.notify();
    cx.spawn(async (cx) => {
      try { this.error = await sendFeedback(body, this.shots); this.sent = !this.error; }
      catch (e) { this.error = String(e.message ?? e); }
      this.sending = false;
      cx.notify();
    });
  }

  render(cx) {
    const t = theme();
    const preview = feedbackPreview(this.message.value(), this.email.value(), this.shots.length);
    const body = preview.body;
    const disabled = !preview.available || this.sending || !this.message.value().trim();
    const label = (text) => div().text_size(13).text_color(t.muted).child(text);
    const field = (el) => el.w_full().p(10).rounded(7).border_1().border_color(t.border).bg(t.background).text_color(t.foreground).text_size(14);
    return v_flex().id("feedback").track_focus(this.handle).w_full().min_h(0).h(650).bg(t.popover)
      .on_drop((e, cx) => {
        if (this.sending || this.sent) return;
        if (this.shots.length >= MAX_SHOTS) this.error = "最多 3 張截圖。";
        else this.add(feedbackAttachImages(e.paths.slice(0, MAX_SHOTS - this.shots.length)));
        cx.notify();
      })
      .on_key_down((e, cx) => { if (e.key === "escape") { this.close(); cx.stop_propagation(); } })
      // The title drags the window; everything below keeps its presses (selecting text).
      .child(div().flex_none().px(24).py(18).cursor_grab().text_size(19).font_semibold().text_color(t.foreground).child("傳送意見回饋"))
      .when(!preview.available, (el) => el.child(div().flex_none().px(24).pb(12).text_size(13).text_color(t.accent).child("此版本由原始碼建置，不會傳送意見回饋。請改用正式發行版。")))
      .child(v_flex().id("feedback-body").on_mouse_down("left", (_e, cx) => cx.stop_propagation()).flex_1().flex_shrink(1).min_h(0).overflow_y_scrollbar().px(24).gap(10)
        .when(props()?.from === "agent", (el) => el.child(div().p(10).rounded(7).bg(t.raised).text_color(t.accent).text_size(14).child("由代理程式草擬：送出前請先看過")))
        .when(this.sent, (el) => el.child(div().py(20).text_size(16).text_color(t.foreground).child("已送出。感謝你協助我們改進 Herdr。")))
        .when(!this.sent, (el) => el
          .child(label("你的訊息（上限 4000 字）。可貼上或拖放截圖，最多 3 張。"))
          .child(field(Textarea.new(this.message)).h(130))
          .child(this.shots_row(t))
          .child(label("電子郵件：只有想收到回覆才需要填"))
          .child(field(Input.new(this.email)).h(40))
          .child(label("會傳送的內容：就是下面這份 JSON，加上上方的截圖。不含日誌或安裝 ID。"))
          .child(v_flex().w_full().p(10).rounded(7).border_1().border_color(t.border).bg(t.background)
            .children(JSON.stringify(body, null, 2).split("\n").map((line) => div().text_size(11).line_height("15px").text_color(t.dim).child(line))))))
      .when(Boolean(this.error), (el) => el.child(div().flex_none().px(24).pt(10).text_size(13).text_color(t.accent).child(this.error)))
      .child(h_flex().flex_none().px(24).py(16).gap(10).justify_end().on_mouse_down("left", (_e, cx) => cx.stop_propagation())
        .child(this.button(t, "feedback-cancel", this.sent ? "完成" : "取消", () => this.close()))
        .when(!this.sent, (el) => el.child(this.button(t, "feedback-send", this.sending ? "正在傳送…" : "傳送", (_e, cx) => this.send(body, cx), true, disabled))));
  }
}
