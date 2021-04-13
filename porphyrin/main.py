import text
import code
import block
import error

class Porphyrin(Piece)

   def __init__(self, **kwargs):
      self.many_block = []
      super(Porphyrin, self).__init__(source, place)

   def write(self):
      sink = ''
      for block in self.many_block:
         sink += block.write()
      sink = shatter_word(sink)
      sink = combine_table(sink)

   def shatter_word(self, sink):
      pass

   def combine_table(self, sink):
      pass

class Piece(object)

   self.set_cut_word = {' ', '\t', '\n', '\r'}

   self.set_cut_line = {'\n', '\r'}

   self.token = {
      "paragraph" : '=',
      "line" : '/',
      "row" : '\"',
      "image" : '|',
      "serif_normal" : '@',
      "serif_italic" : '%',
      "serif_bold" : '#',
      "sans_normal" : '$',
      "sans_bold" : '&',
      "paleozoic" : '^',
      "mesozoic" : '*',
      "cenozoic" : '`',
      "tab" : '_',
      "pause" : '~',
      "break" : '+',
      "link" : '\\',
      "comment_left" : '<',
      "comment_right" : '>',
   }

   def __init__(self, **kwargs):
      self.source = kwargs.pop("source", '')
      self.place = kwargs.pop("place", Place())

   def snip(self, opening, closing):

   def probe_opening(self):


   def find_closing(self, opening):



class Place

   def __init__(self, line, character):
      self.line = line
      self.character = character

   def write()
      result = "line " + self.line
      result += ", character " + self.character + ":\n"
      return result




