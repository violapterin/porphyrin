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
      self.address = ''
      self.sink = ''

   def write(self):
      result = ''
      content = ''
      self.sink = self.tune_text()
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      result += write_element(
         content = self.source,
         tag = tag.
         attributes = ["class"],
         values = [self.KIND],
      )
      return result

class Serif_italic(ORGAN.Leaf):

   KIND = "serif-italic"
   TAG = "em"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''
      self.sink = ''

   def write(self):
      result = ''
      content = ''
      self.sink = self.tune_text()
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      result += write_element(
         content = self.source,
         tag = tag.
         attributes = ["class"],
         values = [self.KIND],
      )
      return result

class Serif_bold(ORGAN.Leaf):

   KIND = "serif-bold"
   TAG = 'b'

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''
      self.sink = ''

   def write(self):
      result = ''
      content = ''
      self.sink = self.tune_text()
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      result += write_element(
         content = self.source,
         tag = tag.
         attributes = ["class"],
         values = [self.KIND],
      )
      return result

class Sans_roman(ORGAN.Leaf):

   KIND = "sans-roman"
   TAG = 'span'

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''
      self.sink = ''

   def write(self):
      result = ''
      content = ''
      self.sink = self.tune_text()
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      result += write_element(
         content = self.source,
         tag = tag.
         attributes = ["class"],
         values = [self.KIND],
      )
      return result

class Sans_bold(ORGAN.Leaf):

   KIND = "sans-bold"
   TAG = 'b'

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''
      self.sink = ''

   def write(self):
      result = ''
      content = ''
      self.sink = self.tune_text()
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      result += write_element(
         content = self.source,
         tag = tag.
         attributes = ["class"],
         values = [self.KIND],
      )
      return result

class Comment(ORGAN.Leaf):

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sink = ''

   def write(self):
      token_left = "<!--"
      token_right = "-->"
      self.sink = self.tune_comment()
      result = token_left + ' ' + self.source + ' ' + token_right
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Code(ORGAN.Leaf):

   KIND = "code"
   TAG = "pre"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sink = ''

   def write(self):
      result = ''
      content = ''
      self.sink = self.tune_code()
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      result += write_element(
         content = self.sink,
         tag = tag.
         attributes = ["class"],
         values = [self.KIND],
      )
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Math(ORGAN.Leaf):

   KIND = "math"
   TAG = "span"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sink = None

   def write(self):
      content = ' '
      self.sink = TISSUE.Box(**self.get_data)
      for subbox in self.sink
         content += '$' + subbox.write() + '$'
         result = write_element(
            content = content
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
         )
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Pseudo(ORGAN.Leaf):

   KIND = "pseudo"
   TAG = "span"

   def __init__(self, **data):
      self.fill_basic(**data)

   def parse(self):

   def write(self):
      content = ' '
      box = TISSUE.Box(**self.get_data)
      for box in self.sink.sinks
         content += '$' + box.write() + '$'
         result = write_element(
            content = content,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
         )
      return result

