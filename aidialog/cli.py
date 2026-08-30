"Command-line access to dialog and notebook navigation and structure."

import sys
from fastcore.script import call_parse
from .dlgskill import summary_dlg, find_msgs, view_dlg, view_msgs
from .ipynb import read_ipynb


def _die(msg): raise SystemExit(msg)


def _dialog(fname):
    if (res := read_ipynb(fname)) is None: _die(f"Could not read dialog: {fname}")
    return res


def _placement(before, after, required=False):
    if before and after: _die("Pass only one of --before and --after")
    if required and not (before or after): _die("Pass one of --before and --after")


def _ids(ids): return [o.strip() for o in ids.split(',') if o.strip()]


@call_parse
def summary_cli(
    fname:str, # Dialog or notebook path
    maxlen:int=180, # Maximum characters displayed per message
):
    "Show one preview row per message."
    print(summary_dlg(fname, maxlen=maxlen))


@call_parse(pos=['pattern'])
def find_cli(
    fname:str, # Dialog or notebook path
    pattern:str='', # Regex or plain text to find
    msg_type:str=None, # Limit matches to code, note, prompt, or raw messages
    errors:bool=False, # Match only code messages with errors?
    exported:bool=False, # Match only exported messages?
    ids:str='', # Comma-separated message IDs to select
    before:int=0, # Messages of context before each match
    after:int=0, # Messages of context after each match
    context:int=None, # Messages of context before and after each match
    limit:int=None, # Maximum matched messages
    case:bool=False, # Match case sensitively?
    plain:bool=False, # Treat pattern as plain text rather than regex?
    headers:bool=False, # Match only heading notes?
    section:str=None, # Return the section beginning at this heading
):
    "Find messages using dialog-aware filters and context."
    print(find_msgs(pattern, dlg=fname, msg_type=msg_type, only_err=errors, only_exp=exported, ids=ids,
        before=before, after=after, context=context, limit=limit, use_case=case, use_regex=not plain,
        headers_only=headers, header_section=section))


@call_parse(pos=['ids'])
def view_cli(
    fname:str, # Dialog or notebook path
    ids:str='', # Comma-separated message IDs; omit to view the whole dialog
    nums:bool=True, # Show line numbers for individual messages?
    lnhashs:bool=False, # Show hash-verified line addresses instead of line numbers?
    start_line:int=1, # First source line to show
    end_line:int=None, # Last source line to show
    out:bool=False, # Include prompt replies and code outputs?
    full_out:bool=False, # Do not truncate included outputs?
    errors:bool=False, # Show only code messages with errors?
):
    "View complete dialogs or selected messages."
    if (sel := _ids(ids)):
        if errors: _die("--errors applies only when viewing a whole dialog")
        res = view_msgs(*sel, dlg=fname, nums=nums, start_line=start_line, end_line=end_line,
            lnhashs=lnhashs, incl_out=out, trunc_out=not full_out)
    else:
        if lnhashs or not nums or start_line != 1 or end_line is not None: _die("Line options require message IDs")
        res = view_dlg(fname, incl_out=out, only_errors=errors, trunc_out=not full_out)
    print(res)


@call_parse
def add_cli(
    fname:str, # Dialog or notebook path
    source:str=None, # Message source; defaults to stdin
    msg_type:str='code', # Message type: code, note, prompt, or raw
    before:str=None, # Insert before this message ID
    after:str=None, # Insert after this message ID
    export:bool=False, # Mark the new message for nbdev export?
    dry_run:bool=False, # Preview without saving?
):
    "Add a message, reading multiline source from stdin by default."
    _placement(before, after)
    if source is None: source = sys.stdin.read()
    d = _dialog(fname)
    m = d.mk_message(source, before=before, after=after, msg_type=msg_type, export=export)
    if not dry_run: d.save()
    print(m.preview())


@call_parse
def del_cli(
    fname:str, # Dialog or notebook path
    ids:str, # Comma-separated message IDs to delete
    dry_run:bool=False, # Preview without saving?
):
    "Delete messages by stable ID."
    d = _dialog(fname)
    removed = d.remove_msgs([d.msg(i) for i in _ids(ids)])
    if not dry_run: d.save()
    print('\n'.join(str(m.preview()) for m in removed))


@call_parse
def move_cli(
    fname:str, # Dialog or notebook path
    ids:str, # Comma-separated message IDs to move
    before:str=None, # Move before this message ID
    after:str=None, # Move after this message ID
    dry_run:bool=False, # Preview without saving?
):
    "Move messages while retaining their relative order."
    _placement(before, after, required=True)
    d = _dialog(fname)
    d.move_msgs(_ids(ids), before=before, after=after)
    if not dry_run: d.save()
    print(d.summary())
