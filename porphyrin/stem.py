import organ as ORGAN
import leaf as LEAF
import caution as CAUTION


class Document(ORGAN.Organ):

   KIND = "document"
   TAG = "body"

   def parse(self):
      head = 0
      while head <= len(self.source) - 1:
         bough, head = self.snip_bough(head)
         sinks.append(bough)

   def write(self):
      content = ''
      for bough in self.sinks:
         content += bough.write()
      result = write_element(
            content = sinks[0],
            tag = self.TAG,
      )
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Image(ORGAN.Organ):

   KIND = "image"
   TAG = "img"

   def parse(self):
      self.escape_hypertext()
      sinks.append(self.source)

   def write(self):
      result = write_element(
            content = sinks[0],
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Break(ORGAN.Organ):

   KIND = "break"
   TAG = "div"
   DINGBAT = "&#10086;"
   REPEAT = 3

   def parse(self):
      content = ''
      for index in range(Break.REPEAT):
         element += Break.DINGBAT
      sinks.append(element)

   def write(self):
      content = ''
      for sink in self.sinks:
         content += write_element(
            content = sink,
            tag = "span",
         )
         content += ' '
      result = write_element(
            content = content,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Paragraphs(ORGAN.Organ):

   KIND = "paragraphs"
   TAG = "div"

   def parse(self):
      head = 0
      while head <= len(self.source) - 1:
         twig, head = self.shatter(Line, "newline", head)
         sinks.append(twig)

   def write(self):
      content = ' '
      for twig in self.sinks:
         content += twig.write()
         content += ' '
      result = write_element(
            content = content,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )
      return result

class Lines(ORGAN.Organ):

   KIND = "lines"
   TAG = "div"

   def parse(self):
      head = 0
      while head <= len(self.source) - 1:
         twig, head = self.shatter(Line, "newline", head)
         sinks.append(twig)

   def write(self):
      content = ' '
      for twig in self.sinks:
         content += twig.write()
         content += ' '
      return result += write_element(
            content = content,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )

class Rows(ORGAN.Organ):

   KIND = "rows"
   TAG_ALL = "table"
   TAG_PREFIX = "thead"
   TAG_BODY = "tbody"

   def parse(self):
      head = 0
      while head <= len(self.source) - 1:
         twig, head = self.shatter(Row, "newline", head)
         sinks.append(twig)

   def write(self):
      content = ' '
      twig_prefix = self.sinks.pop(0)
      content += write_element(
         content = twig_prefix.write(),
         tag = self.TAG_PREFIX,
         attributes = ["class"],
         values = [self.KIND],
      )
      for twig_body in self.sinks:
         element += write_element(
            content = twig_body.write(),
            tag = self.TAG_BODY,
         )
         element += ' '
      return write_element(
         content = sink,
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
      while head <= len(self.source) - 1:
         twig, head = self.shatter(Sentence, "space", head)
         sinks.append(twig)

   def write(self):
      return self.write_element("paragraph")

class Line(ORGAN.Organ):

   KIND = "line"
   TAG = "span"

   def parse(self):
      head = 0
      while head <= len(self.source) - 1:
         twig, head = self.shatter(Verse, "space", head)
         sinks.append(twig)

   def write(self):
      return self.write_element("line")

class Row(ORGAN.Organ):

   KIND = "row"
   TAG = "tr"

   def parse(self):
      head = 0
      while head <= len(self.source) - 1:
         twig, head = self.shatter(Cell, "space", head)
         sinks.append(twig)

   def write(self):
      return self.write_element("row")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Sentence(ORGAN.Organ):

   KIND = "sentence"
   TAG = "span"

   def parse(self):
      head = 0
      while head <= len(self.source) - 1:
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
      while head <= len(self.source) - 1:
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
      while head <= len(self.source) - 1:
         leaf, head = self.snip_leaf(head)
         sinks.append(leaf)

   def write(self):
      result = ''
      for leaf in self.sinks:
         result += leaf.write()
      return result

