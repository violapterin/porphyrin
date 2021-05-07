import organ as ORGAN
import leaf as LEAF
import caution as CAUTION


class Document(ORGAN.Organ):

   KIND = "document"
   TAG = "body"

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
   TAG = "img"

   def parse(self):
      sinks.append(self.escape_hypertext(self.source))

   def write(self):
      return write_tag_image(self.sinks[0], self.KIND)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Break(ORGAN.Leaf):

   KIND = "break"
   TAG = "div"
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
   TAG = "div"

   def parse(self):
      head = 0
      while head <= self.give_head_max():
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
   TAG = "div"

   def parse(self):
      head = 0
      while head <= self.give_head_max():
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
   TAG_ALL = "table"
   TAG_PREFIX = "thead"
   TAG_BODY = "tbody"

   def parse(self):
      head = 0
      while head <= self.give_head_max():
         twig, head = self.shatter_twig(Row, head)
         sinks.append(twig)

   def write(self):
      element = ' '
      twig_prefix = self.sinks.pop(0)
      element += write_tag(
         element = twig_prefix.write(),
         tag = self.TAG_PREFIX,
         attributes = ["class"],
         values = [self.KIND],
      )
      for twig_body in self.sinks:
         element += write_tag(
            element = twig_body.write(),
            tag = self.TAG_BODY,
         )
         element += ' '
      return write_tag(
         element = sink,
         tag = self.TAG_ALL,
         attributes = ["class"],
         values = [self.KIND],
      )

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Paragraph(ORGAN.Organ):

   KIND = "paragraph"
   TAG = "p"

   def parse(self):
      head = 0
      while head <= self.give_head_max():
         twig, head = self.shatter_frond(Sentence, head)
         sinks.append(twig)

   def write(self):
      return self.write_tag("paragraph")

class Line(ORGAN.Organ):

   KIND = "line"
   TAG = "span"

   def parse(self):
      head = 0
      while head <= self.give_head_max():
         twig, head = self.shatter_frond(Verse, head)
         sinks.append(twig)

   def write(self):
      return self.write_tag("line")

class Row(ORGAN.Organ):

   KIND = "row"
   TAG = "tr"

   def parse(self):
      head = 0
      while head <= self.give_head_max():
         twig, head = self.shatter_frond(Cell, head)
         sinks.append(twig)

   def write(self):
      return self.write_tag("row")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Sentence(ORGAN.Organ):

   KIND = "sentence"
   TAG = "span"

   def parse(self):
      head = 0
      while head <= self.give_head_max():
         leaf, head = self.snip_leaf(head)
         sinks.append(leaf)

   def write(self):
      result = ''
      for leaf in self.sinks:
         result += leaf.write()
      return result

class Verse(ORGAN.Organ):

   KIND = "verse"
   TAG = "span"

   def parse(self):
      head = 0
      while head <= self.give_head_max():
         leaf, head = self.snip_leaf(head)
         sinks.append(leaf)

   def write(self):
      result = ''
      for leaf in self.sinks:
         result += leaf.write()
      return result

class Cell(ORGAN.Organ):

   KIND = "cell"
   TAG = "td"

   def parse(self):
      head = 0
      while head <= self.give_head_max():
         leaf, head = self.snip_leaf(head)
         sinks.append(leaf)

   def write(self):
      result = ''
      for leaf in self.sinks:
         result += leaf.write()
      return result

