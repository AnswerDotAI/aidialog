# Release notes

<!-- do not remove -->

## 0.0.18

### New Features

- Make Dialog/Message.execute sync, track file mtime via new `safe_mtime` in read/`write_ipynb` ([#35](https://github.com/AnswerDotAI/aidialog/issues/35))


## 0.0.17

### New Features

- Replace nbrun `skip_noeval` with `ignore_eval`: eval cascade filtering now always on for bulk runs ([#34](https://github.com/AnswerDotAI/aidialog/issues/34))
- Simplify Message rich repr: use preview line instead of summary with details block ([#33](https://github.com/AnswerDotAI/aidialog/issues/33))


## 0.0.16

### New Features

- Move XML views, cell props, and dialog running into dialog.py; rename Dialog.run/Message.run to execute ([#32](https://github.com/AnswerDotAI/aidialog/issues/32))


## 0.0.15

### New Features

- Add Message.directive and Message.`has_directive` accessors for querying directives ([#31](https://github.com/AnswerDotAI/aidialog/issues/31))


## 0.0.14

### New Features

- Add `export_filter` and weave options to dlg2md for document exports; fix run/nbrun to only treat selection flags as selectors ([#30](https://github.com/AnswerDotAI/aidialog/issues/30))
- Add Dialog.run/Message.run to execute code messages on a CaptureShell with RunResult status report; bare %nbrun now runs all cells ([#29](https://github.com/AnswerDotAI/aidialog/issues/29))


## 0.0.13

### New Features

- nbrun: run cells via fastcore.nbio.`run_cell`, capture stderr, stop without re-raising on error ([#28](https://github.com/AnswerDotAI/aidialog/issues/28))


## 0.0.12

### New Features

- Add Message.`cell_type`/source and Dialog.cells properties so dialogs duck-type as notebooks; `to_cell` now uses them ([#27](https://github.com/AnswerDotAI/aidialog/issues/27))


## 0.0.11

### New Features

- Add reply2chat to convert a stored reply to chat messages, and a plain flag on dlg2hist/dlg2chat to skip the serving envelope ([#26](https://github.com/AnswerDotAI/aidialog/issues/26))


## 0.0.10

### New Features

- Replace dataclasses with BasicRepr/`store_attr` in `msg_parts`; move Completion, `mk_msg`, `mk_msgs` from fastllm ([#25](https://github.com/AnswerDotAI/aidialog/issues/25))
- clarify that dlg path expands ~ in docstrings ([#24](https://github.com/AnswerDotAI/aidialog/pull/24)), thanks to [@ncoop57](https://github.com/ncoop57)


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
