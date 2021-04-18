import main
import tree
import bough
import error

class Leaf(main.Piece):

   def __init__(self, **arguments):
      self.source = arguments.pop("source", ''),
      self.place = arguments.pop("place", Place()),
      self.fragment_global_left = ''
      self.fragment_global_right = ''
      self.pile = []
      self.head = 0

   def write_tag(self, content, kind):
      result = ''
      result += "<span" + ' '
      result += "class=" + kind + ">"
      for leaf in self.pile:
         result += leaf.write()
      result += "<class" + "/>"
      return result

   def remove_character(source, group):
      for symbol in group:
         source = source.translate(source.maketrans(symbol: ''))
      return source

   def erase_character(source, group):
      for symbol in group:
         source = source.translate(source.maketrans(symbol: ' '))
      return source

   def adjust_space(source):
      spaces = {'\n', '\t'}
      result = erase_character(source, spaces)
      result = ' '.join(result.split())
      return result

   def ignore_mark_text(source):
      marks_ignored = {'<', '>', '@', '#', '$', '%', '&'}
      result = erase_character(source, marks_ignored)
      return result

   def tune_text(source):
      result = ignore_mark_text(source)
      result = adjust_space(result)
      return result

   def tune_code(source):
      result = adjust_space(source)
      return result

   def write(self):
      pass

class Serif_roman(main.Piece):

   kind = "serif-roman"

   def __init__(self, **arguments):
      self.source = arguments.pop("source", ''),
      self.place = arguments.pop("place", Place())
      self.fragment_left_global = arguments.pop("fragment_left", '')
      self.fragment_right_global = arguments.pop("fragment_right", '')
      self.pile = []
      self.head = 0

   def write(self):
      sink = self.source
      sink = self.tune_text(sink)
      return self.write_inner(sink, self.kind):

class Serif_italic(main.Piece):

   kind = "serif-italic"

   def __init__(self, **arguments):
      self.source = arguments.pop("source", ''),
      self.place = arguments.pop("place", Place())
      self.fragment_left_global = arguments.pop("fragment_left", '')
      self.fragment_right_global = arguments.pop("fragment_right", '')
      self.pile = []
      self.head = 0

   def write(self):
      sink = self.source
      sink = self.tune_text(sink)
      return self.write_inner(sink, self.kind):


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def get_leaf_label(mark):
   labels = get_leaf_labels()
   if mark not in labels:
      return 0
   return labels[mark]

def get_leaf_mark(label):
   marks = get_leaf_marks()
   if label not in marks:
      return 0
   return marks[label]

def give_leaf_labels():
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
   return labels

def give_leaf_marks():
   labels = get_labels_from_mark()
   marks = {label: token for token, label in my_map.items()}
   return marks


