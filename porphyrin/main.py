class Porphyrin(Piece)

class Error

class Piece(object)
   self.set_separation_word = {' ', '\t', '\n', '\r'}
   self.set_separation_line = {'\n', '\r'}

   def __init__(self, string_in, place):
      self.place = place
      self.string_in = string_in
      self.list_inline = []

   def cut(self, string_in, token_left, token_right):
      many_segment_left = s.split(token_left, 3)[1] 
      if not many_segment_left[2]:
         raise error token_left "does not occur"
      many_segment = s.split(token_left, 2)[1] 
      if not many_segment_right[2]:
         raise error token_right "does not occur"
      segment = many_segment[0]
      remain = many_segment[2]
      return segment, remain

# inline
class Boundary(object)
   # block
   self.paragraph = '~',
   self.separation = '/',
   self.image = '\\',
   self.table_outer = '\',
   self.table_inner = '\'',
   # inline
   self.space_wide = '_',
   self.serif_normal = '@',
   self.serif_italic = '%',
   self.serif_bold = '#',
   self.sans_normal = '$',
   self.sans_bold = '&',
   self.Rdt_simple = '+',
   self.Rdt_old = '*',
   self.Rdt_new = '^',
   self.comment_left = '<',
   self.comment_right = '>',
   self.link = '|',

# block

# block kind
kind_paragraph = 0
kind_separation = 0
kind_image = 0
kind_table = 0

def _init_(self, string_in):
   self.string_in = string_in
   self.line = []
   self.string_out = ""
   self.be_success = True
   self.slice_block = ""
   self.message = "Conversion succeeded!"
   self.head_left = 0
   self.head_right = 0
   self.site_left = Site()
   self.site_right = Site()
   self.list_block = []

def fetch_head_left(self, index):
   return line[line_head_left][place_head_left]

def fetch_head_right(self, index):
   return line[line_head_right][place_head_right]


   def run(self):
      while self.string_in:
         self.process_block()

   def print(self):
      for group in self.list
         r += group.print()
      return r

class Place
   def __init__(self, line, character):
      self.line = line
      self.character = character

   def output()
      return "line" + self.line + "character" + self.character




