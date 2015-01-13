import sublime, sublime_plugin
import subprocess
import os, os.path, re, sys

def strip_ansi_codes(s):
    return re.sub(r'\x1b\[([0-9,A-Z]{1,2}(;[0-9]{1,2})?(;[0-9]{3})?)?[m|K]?', '', s)

class RunIdrisCommandCommand(sublime_plugin.TextCommand):

    def run(self, edit, cmd=None, editing=True):
        v = self.view
        cursor = v.sel()[0].begin()
        (r,c) = v.rowcol(cursor) 
        line = r + 1
        name = v.substr(v.word(cursor))
        # filename = v.file_name()

        def idris_cmd(cmd, l, n):
            args = [str(l), n] if editing else []
            return (["idris", "--client", " ".join([cmd] + args)])

        def run_cmd(cmd):
            env = os.environ
            env["PATH"] += ":" + env["HOME"] + "/bin"
            idris_p = subprocess.Popen(
                    idris_cmd(cmd, str(line), name),
                    env=env,
                    stdout=subprocess.PIPE
                ) 
            exit_code = idris_p.wait()
            if exit_code != 0:
                if exit_code == 127: 
                    sublime.error_message("idris is not found in Sublime's PATH: " + env["PATH"])
                return None
            else:
                output = strip_ansi_codes(idris_p.communicate()[0].decode("utf-8"))
                print(output)
                if output:
                    out_panel = v.window().create_output_panel("idris_panel")
                    out_panel.run_command("append", {"characters": output})
                    out_panel.set_syntax_file("Packages/sublime-idris/Idris.tmLanguage")
                    v.window().run_command("show_panel", {"panel": "output.idris_panel"})

        if cmd: run_cmd(cmd)
        else: v.window().show_input_panel("Command: ", "", run_cmd, None, None)
