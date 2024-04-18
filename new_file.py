import sublime
import sublime_plugin

from os import path

class FileManagerInsertCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        content = kwargs.get('content', False)
        syntax = kwargs.get('syntax', False)

        if content != False:
            self.view.insert(edit, 0, content)


        if syntax != False:
            self.view.assign_syntax(syntax)


class FileManagerNewFileCommand(sublime_plugin.TextCommand):
	def run(self, edit, **kwargs):
		content = self.view.substr(sublime.Region(0, self.view.size()))
		syntax = self.view.syntax()

		directory = path.dirname(self.view.file_name())
		self.view.window().run_command('new_file_at', { 'dirs': [directory]})

		if kwargs.get('duplicate') is True:
			sublime.set_timeout_async(lambda: self.__duplicate(content, syntax), 100)

	def __duplicate(self, content, syntax):
		view = self.view.window().active_view()
		view.run_command('file_manager_insert', { "content": content, "syntax": syntax.path })

