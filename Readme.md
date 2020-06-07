## Sublime Text plugin for Idris2 language

- Syntax definition is developed based on the [SublimeHaskell](https://github.com/SublimeHaskell/SublimeHaskell) plugin using the [AAAPackageDev](https://github.com/SublimeText/AAAPackageDev) plugin for converting `YAML` to `tmLanguage`.
- [Interactive editing] Based on idris2-vim https://github.com/edwinb/idris2-vim/blob/master/doc/idris2-vim.txt#L41 functionality:
  + It calls `idris2 --find-ipkg` with commands like `:cs!`, just writing to your file.
  + The following commands are added to the Command Palette:
    - <kbd>⌘</kbd> <kbd>\`</kbd> or <kbd>⌃</kbd> <kbd>⌘</kbd> <kbd>T</kbd> `Idris: Show type` (`:t` for current symbol)
    - <kbd>⌃</kbd> <kbd>⌘</kbd> <kbd>R</kbd> `Idris: Reload`
    - <kbd>⌃</kbd> <kbd>⌘</kbd> <kbd>C</kbd> `Idris: Case split` (`:cs!` for current symbol)
    - <kbd>⌃</kbd> <kbd>⌘</kbd> <kbd>V</kbd> `Idris: Add clause` (`:ac!` for current symbol)
    - <kbd>⌃</kbd> <kbd>⌘</kbd> <kbd>J</kbd> `Idris: Add clause (pattern-matching proof)` (`:apc!` for current symbol)
    - <kbd>⌃</kbd> <kbd>⌘</kbd> <kbd>M</kbd> `Idris: Add missing clauses` (`:am!` for current symbol)
    - <kbd>⌃</kbd> <kbd>⌘</kbd> <kbd>Y</kbd> `Idris: Refine item` (`:ref!` for current symbol)
    - <kbd>⌃</kbd> <kbd>⌘</kbd> <kbd>S</kbd> `Idris: Proof search` (`:ps!` for current symbol)
    - <kbd>⌃</kbd> <kbd>⌘</kbd> <kbd>O</kbd> `Idris: Proof search with hints` (`:ps!` for current symbol)
    - <kbd>⌃</kbd> <kbd>⌘</kbd> <kbd>A</kbd> `Idris: Generate definition` (`:gd!` for current symbol)
    - <kbd>⌃</kbd> <kbd>⌘</kbd> <kbd>L</kbd> `Idris: Make lemma` (`:ml!` for current symbol)
    - <kbd>⌃</kbd> <kbd>⌘</kbd> <kbd>E</kbd> `Idris: Evaluate expression` (any command for the REPL)
    - <kbd>⌃</kbd> <kbd>⌘</kbd> <kbd>W</kbd> `Idris: Make with pattern` (`:ml!` for current symbol)
    - <kbd>⌃</kbd> <kbd>⌘</kbd> <kbd>N</kbd> `Idris: Make case` (`:mc!` for current symbol)
    - <kbd>⌃</kbd> <kbd>⌘</kbd> <kbd>H</kbd> `Idris: Documentation` (`:doc!` for current symbol)

## Installation (with Sublime Package Control)

1. Add this repository to Sublime Package Control. To do this, open up the command pallete with `Ctrl/Cmd + P`, start typing "repository" and choose the option "Package Control: Add Repository" when it comes up. Then paste the url (https://github.com/idris-hackers/idris-sublime) into the field at the bottom and press enter.

2. Install the package. To do this, open the command pallete again, select "Package Control: Install Package", and choose `idris-sublime`.

3. Re-open any `.idr` source files, and they will now be recognized as Idris source files.

### TODO list

Things that would be nice to have:

- Syntax definition for the literate source format
- Possibly some integration with [SublimeREPL](https://github.com/wuub/SublimeREPL) (idris support is [almost there](https://github.com/wuub/SublimeREPL/pull/354)) + [LoadFileTpRepl](https://github.com/laughedelic/LoadFileToRepl) (idris is already there)
