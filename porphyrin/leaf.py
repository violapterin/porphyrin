import main
import branch
import twig
import error

class Leaf(object):

   def __init__(self, **arguments):
      self.source = arguments.pop("source", ''),
      self.place = Place()
      self.pile = []
      self.fragment_left_global = ''
      self.fragment_right_global = ''
      self.head = 0


   def write_inline(self, content, kind)
      result = ''
      result += "<span" + ' '
      result += "class=" + kind + ">"
      result += content
      result += "<span" + "/>"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

   def remove_character(source, group):
      for symbol in group:
         source = source.translate(source.maketrans(symbol: ''))
      return source

   def erase_character(source, group):
      for symbol in group:
         source = source.translate(source.maketrans(symbol: ' '))
      return source

   def adjust_space(source):
      result = source
      spaces = {'\n', '\t'}
      result = erase_character(result)
      result = ' '.join(result.split())
      return result

   def ignore_mark_text():
      result = source
      marks_text = {'<', '>', '@', '#', '$', '%', '&'}
      result = erase_character(marks_text)
      return result

   def prune_text(source):
      result = source
      result = adjust_space(result)
      result = ignore_mark_text(result)
      return result

   def prune_code(source):
      result = source
      result = adjust_space(result)
      return result


   def write(self):
      pass

class Serif_roman(main.Piece):

   label = "SERIF_ROMAN"

   def __init__(self, **arguments):
      self.source = arguments.pop("source", ''),
      self.place = arguments.pop("place", Place()),

   def write(self):
      sink = self.source
      sink = self.prune_text(sink)
      return sink


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def get_leaf_mark(label):
   marks = get_leaf_marks()
   if label not in marks:
      return 0
   return marks[label]

def get_leaf_label(mark):
   labels = get_leaf_labels()
   if mark not in labels:
      return 0
   return labels[mark]

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
