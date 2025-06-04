import sublime_plugin

class FileManagerCloseUnmodifiedCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()

        if window is None:
            return

        group_index, view_index = window.get_view_index(self.view)

        window.run_command('close_unmodified', { 'group': group_index, 'index': view_index })

class FileManagerCloseUnmodifiedRightCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()

        if window is None:
            return

        group_index, view_index = window.get_view_index(self.view)

        window.run_command('close_unmodified_to_right_by_index', { 'group': group_index, 'index': view_index })

