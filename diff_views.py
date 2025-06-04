import sublime_plugin

class FileManagerDiffViewsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()

        if window is None:
            return

        group_index, view_index = window.get_view_index(self.view)

        window.run_command('diff_views', { 'group': group_index, 'index': view_index })
