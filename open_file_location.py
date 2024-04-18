import sublime
import sublime_plugin

from os import path

class FileManagerOpenFileLocationCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		directory = path.dirname(self.view.file_name())
		file = path.basename(self.view.file_name())
		self.view.window().run_command('open_dir', { 'dir': directory, 'file': file })

