import sublime_plugin

from os import path, makedirs

class FileManagerNewFolderCommand(sublime_plugin.WindowCommand):
    def run(self):
        directory = None
        folders = self.window.folders()
        view = self.window.active_view()

        if view is None and len(folders):
            directory = folders[0]

        if view is not None:
            viewFilePath = view.file_name()
            if viewFilePath is not None:
                directory = path.dirname(viewFilePath)

        if directory is None:
            return

        init_text = path.join(directory, '')
        self.window.show_input_panel('Folder Name:', init_text, lambda v: self.on_done(directory, v), None, None)

    def on_done(self, basedir, value):
        folder = value.replace(basedir, "")
        makedirs(path.join(basedir, folder), 0o775)
