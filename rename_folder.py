import sublime
import sublime_plugin

from os import path

class FileManagerRenameFolderCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        directory = path.dirname(self.view.file_name())
        self.view.window().run_command('rename_path', { 'paths': [directory] })


