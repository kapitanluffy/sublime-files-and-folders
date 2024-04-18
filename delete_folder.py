import sublime
import sublime_plugin
import os


class FileManagerDeleteFolderCommand(sublime_plugin.WindowCommand):
    def run(self):
        folders = self.window.folders()
        self.window.show_quick_panel(folders, lambda index: self.on_root_pick(index, folders))

    def on_root_pick(self, index, folders):
        if index < 0:
            return
        folder = folders[index]

        subdirectories = self.list_subdirectories(folder)
        self.window.show_quick_panel(subdirectories, lambda index: self.on_done(index, subdirectories))

    def on_done(self, index, folders):
        if index < 0:
            return
        folder = folders[index]

        self.view.window().run_command('delete_folder', {'dirs': [folder], 'prompt': True})

    # expensive as fck
    def list_subdirectories(self, directory):
        subdirectories = []
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                subdirectories.append(item_path)
                subdirectories.extend(self.list_subdirectories(item_path))
        return subdirectories
