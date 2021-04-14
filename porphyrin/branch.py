import twig
import leaf
import main
import error

class Branch(object):

   def __init__(self, **kwargs):
      self.kind = kwargs.pop("kind", 0)
      super(Text, self).__init__(source, place)


def create(mark, content):

   return leaf

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


