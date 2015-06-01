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


### TODO list

Things that would be nice to have:

- Optional keybindings
- Launch REPL server automatically
- Syntax definition for the literate source format
- Possibly some integration with [SublimeREPL](https://github.com/wuub/SublimeREPL) (idris support is [almost there](https://github.com/wuub/SublimeREPL/pull/354)) + [LoadFileTpRepl](https://github.com/laughedelic/LoadFileToRepl) (idris is already there)
- Proper interaction with the `idris --ideslave` mode
