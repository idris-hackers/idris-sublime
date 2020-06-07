import sublime, sublime_plugin
import subprocess
import os, os.path, re, sys
from os.path import join, split
import zipfile

def strip_ansi_codes(s):
    return re.sub(r'\x1b\[([0-9,A-Z]{1,2}(;[0-9]{1,2})?(;[0-9]{3})?)?[m|K]?', '', s)

cursorBeforeCommand = None

class AlwaysCenterCommand(sublime_plugin.EventListener):
    def on_modified(self, view):
        global cursorBeforeCommand
        if cursorBeforeCommand != None:
            view.show_at_center(cursorBeforeCommand)
            cursorBeforeCommand = None

class RunIdrisCommandCommand(sublime_plugin.TextCommand):

    def run(self, edit, cmd=None, evalExpr=False, inputExpr=None):
        v = self.view
        cursor = v.sel()[0].begin()
        (row, column) = v.rowcol(cursor)
        name = v.substr(v.word(cursor))

        def idris_cmd(cmd, row, column, n, additionalInput):
            global cursorBeforeCommand
            cursorBeforeCommand = cursor

            if cmd == ':cs!':
                args = [row, column, n]
            elif cmd in [':t', ':doc']:
                args = [n]
            elif cmd in [':ac!', ':apc!', ':am!', ':mw!', ':mc!', ':ml!', ':gd!']:
                args = [row, n]
            elif cmd == ':ref!':
                args = [row, n, additionalInput]
            elif cmd == ':ps!':
                args = [row, n, additionalInput] if additionalInput != None else [row, n]
            else:
                args = []

            return ["idris2", "--find-ipkg", v.file_name(), "--client", " ".join([cmd] + args)]

        def run_cmd(cmd, additionalInput=None):
            env = os.environ
            env["PATH"] += ":" + env["HOME"] + "/bin"
            idris_p = subprocess.Popen(
                    idris_cmd(cmd, str(row + 1), str(column), name, additionalInput),
                    env=env,
                    cwd=os.path.dirname(v.file_name()),
                    stdout=subprocess.PIPE
                ) 
            exit_code = idris_p.wait()
            if exit_code != 0:
                if exit_code == 127: 
                    sublime.error_message("idris is not found in Sublime's PATH: " + env["PATH"])
                return None
            else:
                isReloaded = cmd == ""
                if isReloaded:
                    output = "Successfully reloaded: " + v.file_name()
                else:
                    output = strip_ansi_codes(idris_p.communicate()[0].decode("utf-8"))

                if output:
                    out_panel = v.window().create_output_panel("idris_panel")
                    out_panel.run_command("append", {"characters": output})

                    packageName = 'idris-sublime'
                    tmFilename = 'Idris.tmLanguage'
                    packagesPath = sublime.packages_path()
                    tmLangFile = join(packagesPath, packageName, tmFilename)
                    tmFileRelative = join(split(packagesPath)[1], packageName, tmFilename)
                    if os.path.isfile(tmLangFile):
                        out_panel.set_syntax_file(tmFileRelative)
                    else:
                        installedPackageFile = join(sublime.installed_packages_path(), packageName + '.sublime-package')
                        if os.path.isfile(installedPackageFile):
                            with zipfile.ZipFile(installedPackageFile, 'r') as zipRef:
                                zipRef.extract(tmFilename, split(tmLangFile)[0])
                            out_panel.set_syntax_file(tmFileRelative)

                    v.window().run_command("show_panel", {"panel": "output.idris_panel"})

        if evalExpr:
            v.window().show_input_panel("Expression: ", "", run_cmd, None, None)
        elif inputExpr != None:
            v.window().show_input_panel(inputExpr + ": ", "", lambda s: run_cmd(cmd, s), None, None)
        else:
            run_cmd(cmd)
