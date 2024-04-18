import sublime
import sublime_plugin

from os import path

class FileManagerMoveFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.message_dialog('oooh, you really need this huh?')

