import sublime_plugin

class FileManagerCloseTabsRightCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()

        if window is None:
            return

        group_index, view_index = window.get_view_index(self.view)

        window.run_command('close_to_right_by_index', { 'group': group_index, 'index': view_index })

class FileManagerCloseTabsUnselectedCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()

        if window is None:
            return

        group_index, view_index = window.get_view_index(self.view)

        window.run_command('close_unselected', { 'group': group_index, 'index': view_index })

class FileManagerCloseTabsSelectedCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()

        if window is None:
            return

        group_index, view_index = window.get_view_index(self.view)

        window.run_command('close_selected', { 'group': group_index, 'index': view_index })

class FileManagerCloseTabsOtherCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()

        if window is None:
            return

        group_index, view_index = window.get_view_index(self.view)

        window.run_command('close_others_by_index', { 'group': group_index, 'index': view_index })
