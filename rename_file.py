import sublime
import sublime_plugin

class FileManagerRenameFileCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        self.view.window().run_command('rename_file')


