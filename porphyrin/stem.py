import organ as ORGAN
import leaf as LEAF
import tissue as TISSUE
import caution as CAUTION
import aid as AID


class Document(ORGAN.Stem):

   KIND = "document"
   TAG = "body"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []
      self.address = ''
      self.definitions = []
      self.instructions = []
      self.expanded = False

   def parse(self):
      head = 0
      while (head < len(self.source)):
         bough, head = self.snip_bough(head)
         if (bough is not None):
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

class Image(ORGAN.Stem):

   KIND = "image"
   TAG = "img"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''

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

class Break(ORGAN.Stem):

   KIND = "break"
   TAG = "div"

   def __init__(self, **data):
      self.fill_basic(**data)

   def parse(self):
      dingbat = "&#10086;"
      repeat = 3
      self.sinks = dingbat * repeat

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

class Paragraphs(ORGAN.Stem):

   KIND = "paragraphs"
   TAG = "div"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (head < len(self.source)):
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

class Lines(ORGAN.Stem):

   KIND = "lines"
   TAG = "div"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (head < len(self.source)):
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

class Rows(ORGAN.Stem):

   KIND = "rows"
   TAG_ALL = "table"
   TAG_PREFIX = "thead"
   TAG_BODY = "tbody"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (head < len(self.source)):
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

class Paragraph(ORGAN.Stem):

   KIND = "paragraph"
   TAG = "p"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (head < len(self.source)):
         frond, head = self.shatter(Phrase, "space", head)
         sinks.append(frond)

   def write(self):
      return self.write_element("paragraph")

class Line(ORGAN.Stem):

   KIND = "line"
   TAG = "span"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (head < len(self.source)):
         frond, head = self.shatter(Verse, "space", head)
         sinks.append(frond)

   def write(self):
      return self.write_element("line")

class Row(ORGAN.Stem):

   KIND = "row"
   TAG = "tr"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (head < len(self.source)):
         frond, head = self.shatter(Cell, "space", head)
         sinks.append(frond)

   def write(self):
      return self.write_element("row")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Phrase(ORGAN.Stem):

   KIND = "phrase"
   TAG = "span"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (head < len(self.source)):
         leaf, head = self.snip_leaf(head)
         if (leaf): sinks.append(leaf)

   def write(self):
      result = ''
      for leaf in self.sinks:
         result += leaf.write()
      return result

class Verse(ORGAN.Stem):

   KIND = "verse"
   TAG = "span"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (head < len(self.source)):
         leaf, head = self.snip_leaf(head)
         if (leaf): sinks.append(leaf)

   def write(self):
      result = ''
      for leaf in self.sinks:
         result += leaf.write()
      return result

class Cell(ORGAN.Stem):

   KIND = "cell"
   TAG = "td"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (head < len(self.source)):
         leaf, head = self.snip_leaf(head)
         if (leaf): sinks.append(leaf)

   def write(self):
      result = ''
      for leaf in self.sinks:
         result += leaf.write()
      return result
