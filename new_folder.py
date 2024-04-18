import sublime
import sublime_plugin

from os import path

class FileManagerNewFolderCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		directory = path.dirname(self.view.file_name())
		self.view.window().run_command('new_folder', { 'dirs': [directory]})

