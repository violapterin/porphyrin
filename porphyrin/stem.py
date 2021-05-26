from pdb import set_trace

from .organ import Stem
from . import aid as AID

class Document(Stem):

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
      while (True):
         if (head >= len(self.source)):
            break
         head = self.move(0, head)
         bough, head = self.snip_bough(head)
         if bough:
            sinks.append(bough)

   def write(self):
      content = ''
      for bough in self.sinks:
         content += bough.write()
      result = AID.write_element(
         content = content,
         tag = self.TAG,
      )
      return result

   def expand(self, head_left):
      assert (len(self.definitions) == len(self.instructions))
      sink = self.source[head_left:]
      for count in range(len(self.definitions)):
         definition = self.definitions[count]
         instruction = self.instructions[count]
         sink = sink.replace(definition, instruction)
      self.source = sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Image(Stem):

   KIND = "image"
   TAG = "img"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''
      self.sink = None

   def parse(self):
      self.escape_hypertext()
      sinks.append(self.source)

   def write(self):
      result = AID.write_element(
         content = '',
         tag = self.TAG,
         attributes = ["class"],
         values = [self.KIND],
      )
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Break(Stem):

   KIND = "break"
   TAG = "div"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      dingbat = "&#10086;"
      repeat = 3
      self.sinks = dingbat * repeat

   def write(self):
      content = ''
      for sink in self.sinks:
         content += sink + ' '
      result = AID.write_element(
         content = content,
         tag = self.TAG,
         attributes = ["class"],
         values = [self.KIND],
      )
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Paragraphs(Stem):

   KIND = "paragraphs"
   TAG = "div"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (True):
         if (head >= len(self.source)):
            break
         head = self.move(0, head)
         twig, head = self.shatter_stem("newline", Paragraph, head)
         if twig:
            self.sinks.append(twig)

   def write(self):
      content = ' '
      for twig in self.sinks:
         content += twig.write() + ' '
      result = AID.write_element(
            content = content,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )
      return result

class Lines(Stem):

   KIND = "lines"
   TAG = "div"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (True):
         if (head >= len(self.source)):
            break
         head = self.move(0, head)
         twig, head = self.shatter_stem("newline", Line, head)
         if twig:
            self.sinks.append(twig)

   def write(self):
      content = ' '
      for twig in self.sinks:
         content += twig.write() + ' '
      result = AID.write_element(
            content = content,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )
      return result

class Rows(Stem):

   KIND = "rows"
   TAG_ALL = "table"
   TAG_PREFIX = "thead"
   TAG_BODY = "tbody"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (True):
         if (head >= len(self.source)):
            break
         head = self.move(0, head)
         twig, head = self.shatter_stem("newline", Row, head)
         if twig:
            sinks.append(twig)

   def write(self):
      content = ' '
      twig_prefix = self.sinks.pop(0)
      content += AID.write_element(
         content = twig_prefix.write(),
         tag = self.TAG_PREFIX,
         attributes = ["class"],
         values = [self.KIND],
      )
      for twig_body in self.sinks:
         content += AID.write_element(
            content = twig_body.write(),
            tag = self.TAG_BODY,
         )
         content += ' '
      result = AID.write_element(
         content = content,
         tag = self.TAG_ALL,
         attributes = ["class"],
         values = [self.KIND],
      )
      return result

class Newline(Stem):

   KIND = "newline"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sink = None

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Paragraph(Stem):

   KIND = "paragraph"
   TAG = "p"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (True):
         if (head >= len(self.source)):
            break
         head = self.move(0, head)
         frond, head = self.shatter_stem("space", Phrase, head)
         if frond:
            self.sinks.append(frond)

   def write(self):
      content = ' '
      for frond in self.sinks:
         content += frond.write() + ' '
      result = AID.write_element(
            content = content,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )
      return result

class Line(Stem):

   KIND = "line"
   TAG = "span"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (True):
         if (head >= len(self.source)):
            break
         head = self.move(0, head)
         frond, head = self.shatter_stem("space", Verse, head)
         if frond:
            self.sinks.append(frond)

   def write(self):
      content = ' '
      for frond in self.sinks:
         content += frond.write() + ' '
      result = AID.write_element(
            content = content,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )
      return result

class Row(Stem):

   KIND = "row"
   TAG = "tr"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (True):
         if (head >= len(self.source)):
            break
         head = self.move(0, head)
         frond, head = self.shatter_stem("space", Cell, head)
         if frond:
            self.sinks.append(frond)

   def write(self):
      content = ' '
      for frond in self.sinks:
         content += frond.write() + ' '
      result = AID.write_element(
            content = content,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )
      return result

class Space(Stem):

   KIND = "space"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sink = None

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Phrase(Stem):

   KIND = "phrase"
   TAG = "span"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (True):
         head = self.move(0, head)
         if (head >= len(self.source)):
            break
         leaf, head = self.snip_leaf(head)
         if leaf:
            self.sinks.append(leaf)

   def write(self):
      content = ' '
      for leaf in self.sinks:
         content += leaf.write() + ' '
      result = AID.write_element(
            content = content,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )
      return result

class Verse(Stem):

   KIND = "verse"
   TAG = "span"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (True):
         head = self.move(0, head)
         if (head >= len(self.source)):
            break
         leaf, head = self.snip_leaf(head)
         if leaf: self.sinks.append(leaf)

   def write(self):
      content = ' '
      for leaf in self.sinks:
         content += leaf.write() + ' '
      result = AID.write_element(
            content = content,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )
      return result

class Cell(Stem):

   KIND = "cell"
   TAG = "td"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      head = 0
      while (True):
         head = self.move(0, head)
         if (head >= len(self.source)):
            break
         leaf, head = self.snip_leaf(head)
         if leaf: self.sinks.append(leaf)

   def write(self):
      content = ' '
      for leaf in self.sinks:
         content += leaf.write() + ' '
      result = AID.write_element(
            content = content,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )
      return result

