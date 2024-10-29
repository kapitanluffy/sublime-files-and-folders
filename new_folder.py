from .utils import KIND_NEW, KIND_OPEN, get_subdirectories, get_window_folders, has_subdirectories, remove_dupe
import sublime
import sublime_plugin
from os import path, makedirs
import os

def get_folder_label(folder, base_folders):
    for base_folder in base_folders:
        if os.path.commonpath([base_folder, folder]) != base_folder:
            continue
        label = os.path.basename(base_folder)
        return folder.replace(base_folder, f"{os.sep}{label}")
    return folder

# rework folder commands to show only relevant path not the full path
class FileManagerNewFolderCommand(sublime_plugin.WindowCommand):
    BASE_FOLDERS = []

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
            folders = [parent_directory] + subdirectories + folders

        # bug shows current directory twice in new
        # bug shows current directory in open
        folders = remove_dupe(folders)
        self.BASE_FOLDERS = get_window_folders(self.window)

        items = self.create_select_action_items([directory] + folders) + self.create_open_action_items(folders)
        self.window.show_quick_panel(items, lambda index: self.on_done(index, items))

    def on_done(self, index, items):
        if index < 0:
            return
        item = items[index]
        folder_path = item.kind[3]  # item.trigger[7:]

        if item.kind[2] == KIND_NEW[2]:
            init_text = path.join(folder_path, '')
            self.window.show_input_panel('Folder Name:', init_text, lambda v: self.on_input_done(init_text, v), None, None)

        if item.kind[2] == KIND_OPEN[2]:
            parent_directory = os.path.dirname(folder_path)
            subdirectories = [parent_directory] + get_subdirectories(folder_path)
            items = self.create_select_action_items([folder_path] + subdirectories) + self.create_open_action_items(subdirectories)
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
        label = get_folder_label(value, self.BASE_FOLDERS)
        return sublime.QuickPanelItem(" [new] {}".format(label), [], "", KIND_NEW + (value,))

    def create_open_item(self, value):
        label = get_folder_label(value, self.BASE_FOLDERS)
        return sublime.QuickPanelItem("[open] {}".format(label), [], "", KIND_OPEN + (value,))
