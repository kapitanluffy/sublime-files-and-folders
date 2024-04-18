import sublime
import sublime_plugin

from os import path

class FileManagerAddFolderCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("prompt_add_folder")
