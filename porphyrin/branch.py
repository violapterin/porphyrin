import twig
import leaf
import main
import error

class Branch(object):

   label = "BRANCH"

   def __init__(self, **arguments):
      self.source = arguments.pop("source", ''),
      self.place = arguments.pop("place", Place()),
      self.pile = []
      self.fragment_global_left = ''
      self.fragment_global_right = ''
      self.head = 0

   def write_block(self, content, kind)
      result = ''
      result += "<div" + ' '
      result += "class=" + kind + ">"
      for twig in pile:
         result += twig.write()
      result += "<class" + "/>"


   def print(self):
      pass

class Paragraph(object):

class Line(object):

class Table(object):

class Image(object):

class Break(object):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def get_leaf_mark_from_label(label):
   marks = get_leaf_marks()
   if label not in marks:
      return 0
   return marks[label]

def get_leaf_label_from_mark(mark):
   labels = get_leaf_labels()
   if mark not in labels:
      return 0
   return labels[mark]

def get_leaf_labels():
   labels = {
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
   return labels

def give_leaf_marks():
   labels = get_labels_from_mark()
   marks = {label: token for token, label in my_map.items()}
   return marks


