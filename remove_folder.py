import sublime_plugin


class FileManagerRemoveFolderCommand(sublime_plugin.WindowCommand):
    def run(self):
        folders = self.window.folders()
        self.window.show_quick_panel(folders, lambda index: self.on_done(index, folders))

    def on_done(self, index, folders):
        if index < 0:
            return
        folder = folders[index]

        self.window.run_command("remove_folder", {"dirs": [folder]})
