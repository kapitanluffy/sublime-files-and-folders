from .utils import KIND_REMOVE
import sublime
import sublime_plugin

class FileManagerRemoveFolderCommand(sublime_plugin.WindowCommand):
    def is_enabled(self):
        return len(self.window.folders()) > 0

    def run(self):
        folders = self.window.folders()
        items = self.create_select_action_items(folders)
        self.window.show_quick_panel(items, lambda index: self.on_done(index, items))

    def on_done(self, index, folders):
        if index < 0:
            return
        folder = folders[index]

        if folder.kind[2] == KIND_REMOVE[2]:
            self.window.run_command("remove_folder", {"dirs": [folder.trigger[9:]]})

    def create_select_action_items(self, directories):
        items = []
        for directory in directories:
            items.append(self.create_select_item(directory))
        return items

    def create_select_item(self, value):
        return sublime.QuickPanelItem("{}".format(value), [], "", KIND_REMOVE)
