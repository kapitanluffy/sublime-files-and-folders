from .utils import KIND_NEW, KIND_OPEN, get_subdirectories, get_window_folders, has_subdirectories, remove_dupe
import sublime
import sublime_plugin
from os import path, makedirs
import os

class FileManagerNewFolderCommand(sublime_plugin.WindowCommand):
    def is_enabled(self):
        return len(self.window.folders()) > 0

    def run(self):
        folders = get_window_folders(self.window)
        view = self.window.active_view()
        file = view.file_name() if view is not None else None

        if view is not None and file is not None and os.path.exists(file):
            directory = os.path.dirname(file)
            parent_directory = os.path.dirname(directory)
            subdirectories = get_subdirectories(directory)
            folders = [directory, parent_directory] + subdirectories + folders

        folders = remove_dupe(folders)
        items = self.create_select_action_items(folders) + self.create_open_action_items(folders)
        self.window.show_quick_panel(items, lambda index: self.on_done(index, items))

    def on_done(self, index, folders):
        if index < 0:
            return
        folder = folders[index]

        if folder.kind[2] == KIND_NEW[2]:
            init_text = path.join(folder.trigger[7:], '')
            self.window.show_input_panel('Folder Name:', init_text, lambda v: self.on_input_done(init_text, v), None, None)

        if folder.kind[2] == KIND_OPEN[2]:
            parent_directory = os.path.dirname(folder.trigger[7:])
            subdirectories = [parent_directory] + get_subdirectories(folder.trigger[7:])
            items = self.create_select_action_items(subdirectories) + self.create_open_action_items(subdirectories)
            self.window.show_quick_panel(items, lambda index: self.on_done(index, items))

    def on_input_done(self, basedir, value):
        folder = value.replace(basedir, "")
        makedirs(path.join(basedir, folder), 0o775)

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
        return sublime.QuickPanelItem(" [new] {}".format(value), [], "", KIND_NEW)

    def create_open_item(self, value):
        return sublime.QuickPanelItem("[open] {}".format(value), [], "", KIND_OPEN)
