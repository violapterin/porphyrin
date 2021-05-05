import organ as ORGAN
import leaf as LEAF
import caution as CAUTION


class Document(ORGAN.Organ):

   kine = "document"

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

class Section(ORGAN.Organ):

   attribute = "section"

   def parse(self):
      head = 0
      while head_left <= self.source.size() - 1:
         twig, head = self.shatter_twig(Line, head)
         sinks.append(twig)

   def write(self):
      element = ''
      for twig in self.sinks:
         element += twig.write()
      return self.write_block_tag(element, self.attribute)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Stanza(ORGAN.Organ):

   attribute = "stanza"

   def parse(self):
      head = 0
      while head_left <= self.source.size() - 1:
         twig, head = self.shatter_twig(Line, head)
         sinks.append(twig)

   def write(self):
      element = ''
      for twig in self.sinks:
         element += twig.write()
      return self.write_block_tag(element, self.attribute)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Table(ORGAN.Organ):

   attribute = "table"

   def parse(self):
      head = 0
      while head_left <= self.source.size() - 1:
         twig, head = self.shatter_twig(Row, head)
         sinks.append(twig)

   def write(self):
      element = ''
      for twig in self.sinks:
         element += twig.write()
      return self.write_block_tag(element, self.attribute)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Image(ORGAN.Leaf):

   attribute = "image"

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Break(ORGAN.Leaf):

   attribute = "break"

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Paragraph(ORGAN.Organ):

   attribute = "paragraph"

   def parse(self):
      head = 0
      while head_left <= self.source.size() - 1:
         twig, head = self.shatter_frond(Sentence, head)
         sinks.append(twig)

   def write(self):
      return self.write_tag("paragraph")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Line(ORGAN.Organ):

   attribute = "line"

   def parse(self):
      head = 0
      while head_left <= self.source.size() - 1:
         twig, head = self.shatter_frond(Verse, head)
         sinks.append(twig)

   def write(self):
      return self.write_tag("line")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Row(ORGAN.Organ):

   attribute = "row"

   def parse(self):
      head = 0
      while head_left <= self.source.size() - 1:
         twig, head = self.shatter_frond(Cell, head)
         sinks.append(twig)

   def write(self):
      return self.write_tag("row")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Sentence(ORGAN.Organ):

   attribute = "Sentence"

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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Verse(ORGAN.Organ):

   attribute = "verse"

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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Cell(ORGAN.Organ):

   attribute = "cell"

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

