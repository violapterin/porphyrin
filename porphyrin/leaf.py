import main
import branch
import twig
import error

class Leaf(object):


   def __init__(self, **arguments):
      self.source = arguments.pop("source", ''),
      self.place = arguments.pop("place", Place()),


def get_leaf_mark(tag):
   marks = get_leaf_marks()
   if tag not in marks:
      return 0
   return marks[tag]

def get_leaf_tag(mark):
   tags = get_leaf_tags()
   if mark not in tags:
      return 0
   return tags[mark]

def give_leaf_tags():
   tags = {
      '=': "PARAGRAPH",
      '/': "LINE",
      '\"': "ROW",
      '|': "IMAGE",
      '@': "SERIF_NORMAL",
      '%': "SERIF_ITALIC",
      '#': "SERIF_BOLD",
      '$': "SANS_NORMAL",
      '&': "SANS_BOLD",
      '^': "PALEOZOIC",
      '*': "MESOZOIC",
      '+': "CENOZOIC",
      '`': "MONOSPACE",
      '_': "TAB",
      '\'': "PAUSE",
      '~': "BREAK",
      '\\': "LINK",
      '<': "COMMENT_LEFT",
      '>': "COMMENT_RIGHT",
   }
   return tags

def give_leaf_marks():
   tags = get_tags_from_mark()
   marks = {tag: token for token, tag in my_map.items()}
   return marks
