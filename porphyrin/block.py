import main
import text
import code
import error


class Block(main.Piece)
   PARAGRAPH = 0
   LINE = 1
   ROW = 2
   IMAGE = 3
   BREAK = 3

   def process(self, prefix, suffix):
      while not self.source:
         left = source[0]
         segment, self.source = self.snip(head, self.source)
         if (head == Boundary.serif_roman):
            self.push.Serif_roman(segment)
         elif (head == Boundary.link):
            self.stack.back.create_link(segment)



