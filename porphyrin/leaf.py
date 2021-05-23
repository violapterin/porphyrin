import organ as ORGAN
import stem as STEM
import caution as CAUTION
import tissue as TISSUE
import aid as AID

class Serif_roman(ORGAN.Leaf):

   KIND = "serif-roman"
   TAG_PLAIN = "span"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''

   def write(self):
      content = self.tune_text()
      sink = self.write_text(content)
      return content

class Serif_italic(ORGAN.Leaf):

   KIND = "serif-italic"
   TAG_PLAIN = "em"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''

   def write(self):
      content = self.tune_text()
      sink = self.write_text(content)
      return content

class Serif_bold(ORGAN.Leaf):

   KIND = "serif-bold"
   TAG_PLAIN = 'b'

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''

   def write(self):
      content = self.tune_text()
      sink = self.write_text(content)
      return content

class Sans_roman(ORGAN.Leaf):

   KIND = "sans-roman"
   TAG_PLAIN = "span"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''

   def write(self):
      content = self.tune_text()
      sink = self.write_text(content)
      return content

class Sans_bold(ORGAN.Leaf):

   KIND = "sans-bold"
   TAG_PLAIN = 'b'

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''

   def write(self):
      content = self.tune_text()
      sink = self.write_text(content)
      return content

class Mono(ORGAN.Leaf):

   KIND = "mono"
   TAG = "pre"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''

   def write(self):
      content = self.tune_code()
      sink = self.write_text(content)
      return content

class Comment(ORGAN.Leaf):

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      token_left = "<!--"
      token_right = "-->"
      sink = self.tune_comment()
      sink = token_left + ' ' + sink + ' ' + token_right
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Math(ORGAN.Leaf):

   KIND = "math"

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      sink = ''
      head_left = 0
      head_right = 0
      while(head_right <= len(self.source)):
         tissue, head_right = self.snip_tissue_math(head_left)
         tissue.OUTSIDE = True
         sink += tissue.write()
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Pseudo(ORGAN.Leaf):

   KIND = "pseudo"

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      sink = ''
      head_left = 0
      head_right = 0
      while(head_right <= len(self.source)):
         tissue, head_right = self.snip_tissue_pseudo(head_left)
         sink += tissue.write()
      return sink

