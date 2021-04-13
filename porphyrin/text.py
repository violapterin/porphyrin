import main
import code
import block
import error

class Text(Piece)

   self.SERIF_ROMAN = 0
   self.SERIF_ITALIC = 1
   self.SERIF_BOLD = 2
   self.SANS_ROMAN = 3
   self.SANS_BOLD = 4
   self.MONOSPACE = 5
   self.SPACE = 6

   def __init__(self, **kwargs):
      self.kind = kwargs.pop("kind", 0)
      super(Text, self).__init__(source, place)


