class Block(main.Piece)

   def __init__(self, s__in, place):
      self.place = place
      self.s__in = s__in
      self.list_inline = []

   def run(self):
      while not self.s__in:
         self.process()

   def process(self):
      c = s__in[head]
      segment, self.s__in = self.cut(c, self.s__in)
      if (c == Boundary.serif_roman):
         self.push.Serif_roman(segment)
      elif (c == Boundary.link):
         self.list_inline.back.create_link(segment)

class Kind_block(object)
   PARAGRAPH = 0
   LINE = 1
   ROW = 2


class Group
   def __init__(self, s__in, head):
      self.head = head
      self.s__in = s__in
      self.list_inline = []

class Kind_group(Enum)
   Section = 0
   Stanza = 0
   Table = 0

