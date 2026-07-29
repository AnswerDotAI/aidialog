# Release notes

<!-- do not remove -->

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
