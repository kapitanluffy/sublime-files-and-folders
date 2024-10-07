import sublime_plugin
from .utils import get_window_folders


class FileManagerCopyFolderLocationCommand(sublime_plugin.WindowCommand):
    def run(self):
        folders = get_window_folders(self.window)
        self.window.show_quick_panel(folders, lambda index: self.on_done(index, folders))

    def on_done(self, index, folders):
        if index < 0:
            return
        folder = folders[index]

        self.window.run_command('copy_path_sidebar', {'paths': [folder]})

