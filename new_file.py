import sublime
import sublime_plugin
from os import path, makedirs
from .utils import get_window_folders

def get_target_dir(filename, basedirectory):
    target_dir: str = path.dirname(filename)
    is_path_abs = path.isabs(filename)

    if is_path_abs is True:
        return target_dir

    return path.abspath(path.join(basedirectory, target_dir))

def get_view_name(view: sublime.View):
    return view.name() or path.basename(view.file_name() or "untitled")

class FileManagerInsertCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        content = kwargs.get('content', False)
        syntax = kwargs.get('syntax', False)
        if content is not False:
            self.view.insert(edit, 0, content)
        if syntax is not False:
            self.view.assign_syntax(syntax)

class FileManagerNewFileCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        view = self.window.active_view()
        if view is None:
            return

        is_dupe = kwargs.get('duplicate', False)
        NEW_FILE_NAME = view.file_name() or ""

        folders = get_window_folders(self.window)
        directory = path.dirname(NEW_FILE_NAME) if NEW_FILE_NAME else path.expanduser('~')
        # for now, fallback to the first directory
        if directory is None and len(folders) > 0:
            directory = folders[0]

        initial_text = path.join(directory or "", NEW_FILE_NAME)

        self.window.show_input_panel(
            caption="New File:",
            initial_text=initial_text,
            on_done=lambda v: self.on_done(v, is_dupe, view, directory),
            on_change=None,
            on_cancel=None,
        )

    def on_done(self, filename: str, is_dupe, view, basedirectory):
        filename = filename.strip() or get_view_name(view)
        new_view = self.window.new_file()

        if is_dupe is True:
            content = view.substr(sublime.Region(0, view.size()))
            syntax: sublime.Syntax = view.syntax()
            new_view.assign_syntax(syntax)
            new_view.run_command("file_manager_insert", {"content": content})

        filename = path.join(get_target_dir(filename, basedirectory), path.basename(filename))
        directory = path.dirname(filename)

        if path.exists(directory) is False:
            makedirs(directory)

        # if the provided filename is a directory
        # set the default_dir of the new file
        if path.isdir(filename) is True:
            new_view.settings().set('default_dir', filename)

        if path.isdir(filename) is False:
            new_view.retarget(filename)
