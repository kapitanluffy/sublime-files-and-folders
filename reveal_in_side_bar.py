import sublime_plugin


class FileManagerRevealInSideBarCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        self.view.window().run_command('reveal_in_side_bar')
