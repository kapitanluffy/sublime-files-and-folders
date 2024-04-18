import sublime
import sublime_plugin

class FileManagerCopyFileLocationCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().run_command('copy_path_sidebar', { 'paths': [self.view.file_name()] })
