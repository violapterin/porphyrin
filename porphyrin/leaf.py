import organ as ORGAN
import stem as STEM
import caution as CAUTION
import tissue as TISSUE
import aid as AID

class Serif_roman(ORGAN.Leaf):

   KIND = "serif-roman"
   TAG = "span"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []
      self.address = ''

   def parse(self):
      AID.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.snip_tissue_text(head)
         sinks.append(text)

   def write(self):
      result = ''
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_element(
            content = sink,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      return result

class Serif_italic(ORGAN.Leaf):

   KIND = "serif-italic"
   TAG = "em"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []
      self.address = ''

   def parse(self):
      AID.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.snip_tissue_text(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_element(
            content = sink,
            tag = tag,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      result = AID.write_element(result, TAG)
      return result

class Serif_bold(ORGAN.Leaf):

   KIND = "serif-bold"
   TAG = 'b'

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []
      self.address = ''

   def parse(self):
      AID.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.snip_tissue_text(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_element(
            content = sink,
            tag = tag,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      result = AID.write_element(result, TAG)
      return result

class Sans_roman(ORGAN.Leaf):

   KIND = "sans-roman"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []
      self.address = ''

   def parse(self):
      AID.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.snip_tissue_text(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_element(
            content = sink,
            tag = tag,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      return result

class Sans_bold(ORGAN.Leaf):

   KIND = "sans-bold"
   TAG = 'b'

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []
      self.address = ''

   def parse(self):
      AID.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.snip_tissue_text(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_element(
            content = sink,
            tag = tag,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      result = AID.write_element(result, self.TAG)
      return result

class Comment(ORGAN.Leaf):

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sink = ''

   def parse(self):
      self.sink = tune_code(self.source)

   def write(self):
      token_left = "<!--"
      token_right = "-->"
      result = token_left + ' ' + self.sink + ' ' + token_right
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Code(ORGAN.Leaf):

   KIND = "sans-bold"
   TAG = "pre"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      AID.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.snip_tissue_text(head)
         sinks.append(text)

   def write(self):
      content = ''
      tag = self.TAG
      if (self.address is not None):
         tag = 'a'
      for sink in self.sinks:
         content += write_element(
            content = sink,
            tag = tag,
            attributes = ["class"],
            values = [self.KIND],
         )
         content += ' '
      result = AID.write_element(content, self.TAG)
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Math(ORGAN.Leaf):

   KIND = "math"
   TAG = "math"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sink = None

   def parse(self):
      data_organ = {
         "source" : self.source,
         "leftmost" : self.leftmost,
         "rightmost" : self.rightmost,
         "count_line" : self.count_line,
         "count_glyph" : self.count_glyph,
      }
      self.sink = TISSUE.Box(**data_organ)

   def write(self):
      content = ' '
      tag = self.TAG
      for box in self.sink.sinks
         content += '$' + box.write() + '$'
         content += ' '
      result = write_element(
        content = content
        tag = tag,
        attributes = ["class"],
        values = [self.KIND],
      )
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Pseudo(ORGAN.Leaf):

   KIND = "serif-roman"
   TAG = "span"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def parse(self):
      pass

   def write(self):
      pass

