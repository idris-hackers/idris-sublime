## Sublime Text plugin for Idris language

- Syntax definition is developed based on the [SublimeHaskell](https://github.com/SublimeHaskell/SublimeHaskell) plugin using the [AAAPackageDev](https://github.com/SublimeText/AAAPackageDev) plugin for converting `YAML` to `tmLanguage`.
- `WIP` [Interactive editing](http://edwinb.wordpress.com/2013/10/28/interactive-idris-editing-with-vim/) functionality:
  + You have to start idris repl server manually.
  + It calls `idris --client` with commands like `:addclause!`, so just writing to your file. So no `--ideslave`.
  + There are some problems with this in idris itself: [idris-vim#11](https://github.com/idris-hackers/idris-vim/issues/11) for example.
  + Although the following commands are added to the Command Palette:
    - `Idris: Run REPL command...` (any command for the repl)
    - `Idris: Run editing command...` (this will be apended by the line number and the symbol name)
    - `Idris: Add clause` (`:addclause!` for current symbol)
    - `Idris: Case split` (`:casesplit!` for current symbol)
    - `Idris: Add missing clause` (`:addmissing!` for current symbol)
    - `Idris: Proof search` (`:proofsearch!` for current symbol)
    - `Idris: Make with pattern` (`:makewith!` for current symbol)

### TODO list

- Keybindings
- Launch repl server automatically
- Syntax definition for the literate source format
- Possibly some integration with [SublimeREPL](https://github.com/wuub/SublimeREPL) (idris support is [almost there](https://github.com/wuub/SublimeREPL/pull/354)) + [LoadFileTpRepl](https://github.com/laughedelic/LoadFileToRepl) (idris is already there)
- _Maybe_ some business with `idris --ideslave` if I will have time...
