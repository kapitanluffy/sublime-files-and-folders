from .utils import KIND_OPEN, KIND_RENAME, get_subdirectories, get_window_folders, has_subdirectories, remove_dupe
import sublime
import sublime_plugin
import os

class FileManagerRenameFolderCommand(sublime_plugin.WindowCommand):
    def is_enabled(self):
        return len(self.window.folders()) > 0

    def run(self):
        folders = get_window_folders(self.window)
        view = self.window.active_view()
        file = view.file_name() if view is not None else None

        if view is not None and file is not None and os.path.exists(file):
            directory = os.path.dirname(file)
            subdirectories = get_subdirectories(directory)
            folders = [directory] + subdirectories + folders

        folders = remove_dupe(folders)
        items = self.create_select_action_items(folders) + self.create_open_action_items(folders)
        self.window.show_quick_panel(items, lambda index: self.on_done(index, items))

    def on_done(self, index, folders):
        if index < 0:
            return
        folder = folders[index]

        if folder.kind[2] == KIND_RENAME[2]:
            self.window.run_command('rename_path', {'paths': [folder.trigger[9:]]})

        if folder.kind[2] == KIND_OPEN[2]:
            subdirectories = get_subdirectories(folder.trigger[9:])
            items = self.create_select_action_items(subdirectories) + self.create_open_action_items(subdirectories)
            self.window.show_quick_panel(items, lambda index: self.on_done(index, items))

    def create_select_action_items(self, directories):
        items = []
        for directory in directories:
            items.append(self.create_select_item(directory))
        return items

    def create_open_action_items(self, directories):
        items = []
        for directory in directories:
            if has_subdirectories(directory):
                items.append(self.create_open_item(directory))
        return items

    def create_select_item(self, value):
        return sublime.QuickPanelItem("[rename] {}".format(value), [], "", KIND_RENAME)

    def create_open_item(self, value):
        return sublime.QuickPanelItem("  [open] {}".format(value), [], "", KIND_OPEN)
