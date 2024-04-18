import sublime
import sublime_plugin

class FileManagerCloseFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().run_command('close_file')
