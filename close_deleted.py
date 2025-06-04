import sublime_plugin

from os import path

class FileManagerCloseDeletedCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()

        if window is None:
            return

        group_index, _ = window.get_view_index(self.view)

        window.run_command('close_deleted_files', { 'group': group_index })
