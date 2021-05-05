import organ as ORGAN
import stem as STEM
import caution as CAUTION

class Serif_roman(object):

   kind = "serif-roman"

   def parse(self):
      self.source = self.tune_text(self.source)
      self.sinks = source.split(' ')

   def write(self):
      result = ''
      for sink in self.sinks:
         result += self.write_inline_tag(sink, self.kind)
         result += ' '
      return result

class Serif_italic(object):

   kind = "serif-italic"

   def parse(self):
      self.source = self.tune_text(self.source)
      self.sinks = source.split(' ')

   def write(self):
      TAG = "em"
      result = ''
      for sink in self.sinks:
         result += self.write_inline_tag(sink, self.kind)
         result += ' '
      result = self.write_tag(result, TAG)
      return result

class Serif_bold(object):

   kind = "serif-bold"

   def parse(self):
      self.source = self.tune_text(self.source)
      self.sinks = source.split(' ')

   def write(self):
      TAG = 'b'
      result = ''
      for sink in self.sinks:
         result += self.write_inline_tag(sink, self.kind)
         result += ' '
      result = self.write_tag(result, TAG)
      return result

class Sans_roman(object):

   kind = "sans-roman"

   def parse(self):
      self.source = self.tune_text(self.source)
      self.sinks = source.split(' ')

   def write(self):
      result = ''
      for sink in self.sinks:
         result += self.write_inline_tag(sink, self.kind)
         result += ' '
      return result

class Sans_bold(object):

   kind = "sans-bold"

   def parse(self):
      self.source = self.tune_text(self.source)
      self.sinks = source.split(' ')

   def write(self):
      TAG = 'b'
      result = ''
      for sink in self.sinks:
         result += self.write_inline_tag(sink, self.kind)
         result += ' '
      result = self.write_tag(result, TAG)
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Verbatim(object):

   def parse(self):
      pass

   def write(self):
      pass

class Alternative(object):

   def parse(self):
      pass

   def write(self):
      pass

class Traditional(object):

   def parse(self):
      pass

   def write(self):
      pass

