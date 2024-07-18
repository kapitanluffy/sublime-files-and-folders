import sublime
import os

def has_subdirectories(directory):
    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)):
            return True
    return False

def get_subdirectories(directory):
    subdirectories = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path) is False:
            continue
        subdirectories.append(item_path)
    return subdirectories

def remove_dupe(items):
    seen = {}
    return [seen.setdefault(x, x) for x in items if x not in seen]


KIND_OPEN = (sublime.KindId.COLOR_BLUISH, "O", "Open")
KIND_RENAME = (sublime.KindId.COLOR_GREENISH, "R", "Rename")
KIND_DELETE = (sublime.KindId.COLOR_REDISH, "D", "Delete")
