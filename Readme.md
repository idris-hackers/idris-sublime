## Sublime Text plugin for Idris language

- Syntax definition is developed based on the [SublimeHaskell](https://github.com/SublimeHaskell/SublimeHaskell) plugin using the [AAAPackageDev](https://github.com/SublimeText/AAAPackageDev) plugin for converting `YAML` to `tmLanguage`.
- `WIP` [Interactive editing](http://edwinb.wordpress.com/2013/10/28/interactive-idris-editing-with-vim/) functionality:
  + You have to start idris REPL server manually.
  + It calls `idris --client` with commands like `:addclause!`, just writing to your file (it doesn't use `--ideslave`).
  + There are some problems with this in idris itself: [idris-vim#11](https://github.com/idris-hackers/idris-vim/issues/11) for example.
  + The following commands are added to the Command Palette:
    - `Idris: Run REPL command...` (any command for the REPL)
    - `Idris: Run editing command...` (this will be apended by the line number and the symbol name)
    - `Idris: Add clause` (`:addclause!` for current symbol)
    - `Idris: Case split` (`:casesplit!` for current symbol)
    - `Idris: Add missing clause` (`:addmissing!` for current symbol)
    - `Idris: Proof search` (`:proofsearch!` for current symbol)
    - `Idris: Make with pattern` (`:makewith!` for current symbol)

## Installation (with Sublime Package Control)

1. Add this repository to Sublime Package Control. To do this, open up the command pallete with `Ctrl/Cmd + P`, start typing "repository" and choose the option "Package Control: Add Repository" when it comes up. Then paste the url (https://github.com/idris-hackers/idris-sublime) into the field at the bottom and press enter.

2. Install the package. To do this, open the command pallete again, select "Package Control: Install Package", and choose `idris-sublime`.

3. Re-open any `.idr` source files, and they will now be recognized as Idris source files.

### TODO list

Things that would be nice to have:

- Optional keybindings
- Launch REPL server automatically
- Syntax definition for the literate source format
- Possibly some integration with [SublimeREPL](https://github.com/wuub/SublimeREPL) (idris support is [almost there](https://github.com/wuub/SublimeREPL/pull/354)) + [LoadFileTpRepl](https://github.com/laughedelic/LoadFileToRepl) (idris is already there)
- Proper interaction with the `idris --ideslave` mode
