from enum import Enum

class Text(Piece)
   def __init__(self, string_in, head):
      self.head = head
      self.string_in = string_in
      self.list_inline = []


class Kind_text(object)
   SERIF_ROMAN = 0
   SERIF_ITALIC = 1
   SERIF_BOLD = 2
   SANS_ROMAN = 3
   SANS_BOLD = 4


