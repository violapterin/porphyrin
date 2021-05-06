import organ as ORGAN
import leaf as LEAF
import caution as CAUTION


class Document(ORGAN.Organ):

   KIND = "document"

   def parse(self):
      head = 0
      while head <= self.source.size() - 1:
         bough, head = self.snip_bough(head)
         sinks.append(bough)

   def write(self):
      result = ''
      for bough in self.sinks:
         result += bough.write()
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Image(ORGAN.Leaf):

   KIND = "image"

   def parse(self):
      sinks.append(self.escape_hypertext(self.source))

   def write(self):
      return write_tag_image(self.sinks[0], self.KIND)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Break(ORGAN.Leaf):

   KIND = "break"
   DINGBAT = "&#10086;"
   REPEAT = 3

   def parse(self):
      element = ''
      for index in range(Break.REPEAT):
         element += Break.DINGBAT
      sinks.append(element)

   def write(self):
      return write_tag_block(self.sink[0], self.KIND)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Section(ORGAN.Organ):

   KIND = "section"

   def parse(self):
      head = 0
      while head_left <= self.source.size() - 1:
         twig, head = self.shatter_twig(Line, head)
         sinks.append(twig)

   def write(self):
      element = ' '
      for twig in self.sinks:
         element += twig.write()
         element += ' '
      return self.write_tag_block(element, self.attribute)

class Stanza(ORGAN.Organ):

   KIND = "stanza"

   def parse(self):
      head = 0
      while head_left <= self.source.size() - 1:
         twig, head = self.shatter_twig(Line, head)
         sinks.append(twig)

   def write(self):
      element = ' '
      for twig in self.sinks:
         element += twig.write()
         element += ' '
      return self.write_tag_block(element, self.attribute)

class Table(ORGAN.Organ):

   KIND = "table"

   def parse(self):
      head = 0
      while head_left <= self.source.size() - 1:
         twig, head = self.shatter_twig(Row, head)
         sinks.append(twig)

   def write(self):
      element = ' '
      for twig in self.sinks:
         element += twig.write()
         element += ' '
      return self.write_tag_block(element, self.attribute)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Paragraph(ORGAN.Organ):

   KIND = "paragraph"

   def parse(self):
      head = 0
      while head_left <= self.source.size() - 1:
         twig, head = self.shatter_frond(Sentence, head)
         sinks.append(twig)

   def write(self):
      return self.write_tag("paragraph")

class Line(ORGAN.Organ):

   KIND = "line"

   def parse(self):
      head = 0
      while head_left <= self.source.size() - 1:
         twig, head = self.shatter_frond(Verse, head)
         sinks.append(twig)

   def write(self):
      return self.write_tag("line")

class Row(ORGAN.Organ):

   KIND = "row"

   def parse(self):
      head = 0
      while head_left <= self.source.size() - 1:
         twig, head = self.shatter_frond(Cell, head)
         sinks.append(twig)

   def write(self):
      return self.write_tag("row")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Sentence(ORGAN.Organ):

   KIND = "Sentence"

   def parse(self):
      head = 0
      while head <= self.source.size() - 1:
         leaf, head = self.snip_leaf(head)
         sinks.append(leaf)

   def write(self):
      result = ''
      for leaf in self.sinks:
         result += leaf.write()
      return result

class Verse(ORGAN.Organ):

   KIND = "verse"

   def parse(self):
      head = 0
      while head <= self.source.size() - 1:
         leaf, head = self.snip_leaf(head)
         sinks.append(leaf)

   def write(self):
      result = ''
      for leaf in self.sinks:
         result += leaf.write()
      return result

class Cell(ORGAN.Organ):

   KIND = "cell"

   def parse(self):
      head = 0
      while head <= self.source.size() - 1:
         leaf, head = self.snip_leaf(head)
         sinks.append(leaf)

   def write(self):
      result = ''
      for leaf in self.sinks:
         result += leaf.write()
      return result

