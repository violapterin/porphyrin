import twig
import leaf
import main
import error

class Branch(object):

   tag = "BRANCH"

   def __init__(self, **arguments):
      self.source = arguments.pop("source", ''),
      self.place = Place()
      self.pile = []
      self.fragment_global_left = ''
      self.fragment_global_right = ''
      self.head = 0


def get_leaf_mark_from_tag(tag):
   marks = get_leaf_marks()
   if tag not in marks:
      return 0
   return marks[tag]

def get_leaf_tag_from_mark(mark):
   tags = get_leaf_tags()
   if mark not in tags:
      return 0
   return tags[mark]

def get_leaf_tags():
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
      '^': "TRADITIONAL",
      '*': "ALTERNATIVE",
      '+': "VERBATIM",
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


