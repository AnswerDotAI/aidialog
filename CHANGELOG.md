# Release notes

<!-- do not remove -->

## 0.0.9

### New Features

- nbrun: only display output of cells named by id, add `show` flag to force display ([#23](https://github.com/AnswerDotAI/aidialog/issues/23))
- chat2dlg: deterministic message ids from meta uid or turn position, allow transcripts starting mid-conversation; move summary to dialog ([#22](https://github.com/AnswerDotAI/aidialog/issues/22))


## 0.0.8

### New Features

- Part subclasses replace Part/ToolCall, id-indexed find results with context marks, and new `update_msg` transaction ([#21](https://github.com/AnswerDotAI/aidialog/issues/21))
- Export `mk_content`, `mk_result_fence`, `split_fence_msgs` and `trunc_str` publicly; add `extract_fence_call`, Part.formatted, and showthink/pending-tool rendering in hist2fmt ([#20](https://github.com/AnswerDotAI/aidialog/issues/20))
- Add `is_nameerr` helper to hist for detecting NameError results from `eval_exprs` ([#19](https://github.com/AnswerDotAI/aidialog/issues/19))


## 0.0.7

### New Features

- Move prompt envelope, sigil refs, variables, and #ai static media into aidialog core; bump context image budget to 768px ([#17](https://github.com/AnswerDotAI/aidialog/issues/17))
- Resize images for LLM context and pick one image per output, via shared `output_parts`/`merge_media` helpers ([#13](https://github.com/AnswerDotAI/aidialog/issues/13))
- Move `join_out`/`output_from_msg` to fastcore.nbio, add `render_md` output-to-markdown renderer, and add %nbrun line magic ([#12](https://github.com/AnswerDotAI/aidialog/issues/12))
- Support nbdev meta directives: `export=` in `add_msg`/`mk_message`, `[export]` in previews, and directive attrs in XML views ([#11](https://github.com/AnswerDotAI/aidialog/issues/11))
- `url_mime`: use server Content-Type as fallback before byte sniffing ([#10](https://github.com/AnswerDotAI/aidialog/issues/10))


## 0.0.6

### New Features

- Add SVG mime type and ensure `url_mime` falls back to default when sniffing fails ([#9](https://github.com/AnswerDotAI/aidialog/issues/9))


## 0.0.5

### New Features

- Add hist module with dialog↔chat history conversions, migrated from llmsurgery ([#7](https://github.com/AnswerDotAI/aidialog/issues/7))

### Bugs Squashed

- Add ToolResponse, moved from fastllm ([#8](https://github.com/AnswerDotAI/aidialog/pull/8)), thanks to [@curtis-allan](https://github.com/curtis-allan)


## 0.0.4

### New Features

- Show a prompt reply on its own preview line, with size hints for truncated content ([#6](https://github.com/AnswerDotAI/aidialog/issues/6))
- Split export state into a read-only merged `exported` and a host-owned `meta_exported` switch ([#5](https://github.com/AnswerDotAI/aidialog/pull/5)), thanks to [@jph00](https://github.com/jph00)


## 0.0.3

### New Features

- Add the `msg_parts` message model and `msg2md`/`dlg2md` Markdown rendering ([#4](https://github.com/AnswerDotAI/aidialog/pull/4)), thanks to [@jph00](https://github.com/jph00)
- Add folded-display rendering for tool calls and token usage blocks ([#3](https://github.com/AnswerDotAI/aidialog/issues/3))


## 0.0.2

### New Features

- Move .hist and .compact back to llmsurgery, consolidating other functions into .dialog and replacing nbformat with fastcore.nbio ([#2](https://github.com/AnswerDotAI/aidialog/issues/2))


## 0.0.1

### New Features

- Migrate from llmsurgery ([#1](https://github.com/AnswerDotAI/aidialog/issues/1))
