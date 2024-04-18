import sublime
import sublime_plugin

from os import path

class FileManagerDeleteFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().run_command('delete_file', { 'files': [self.view.file_name()], 'prompt': True })

