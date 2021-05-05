import organ as ORGAN
import stem as STEM
import caution as CAUTION

class Serif_roman(ORGAN.Organ):

   attribute = "serif-roman"

   def parse(self):
      self.source = self.tune_text(self.source)
      self.sinks = source.split(' ')

   def write(self):
      result = ''
      for sink in self.sinks:
         result += self.write_inline_tag(sink, self.attribute)
         result += ' '
      return result

class Serif_italic(ORGAN.Organ):

   attribute = "serif-italic"

   def parse(self):
      self.source = self.tune_text(self.source)
      self.sinks = source.split(' ')

   def write(self):
      TAG = "em"
      result = ''
      for sink in self.sinks:
         result += self.write_inline_tag(sink, self.attribute)
         result += ' '
      result = self.write_tag(result, TAG)
      return result

class Serif_bold(ORGAN.Organ):

   attribute = "serif-bold"

   def parse(self):
      self.source = self.tune_text(self.source)
      self.sinks = source.split(' ')

   def write(self):
      TAG = 'b'
      result = ''
      for sink in self.sinks:
         result += self.write_inline_tag(sink, self.attribute)
         result += ' '
      result = self.write_tag(result, TAG)
      return result

class Sans_roman(ORGAN.Organ):

   attribute = "sans-roman"

   def parse(self):
      self.source = self.tune_text(self.source)
      self.sinks = source.split(' ')

   def write(self):
      result = ''
      for sink in self.sinks:
         result += self.write_inline_tag(sink, self.attribute)
         result += ' '
      return result

class Sans_bold(ORGAN.Organ):

   attribute = "sans-bold"

   def parse(self):
      self.source = self.tune_text(self.source)
      self.sinks = source.split(' ')

   def write(self):
      TAG = 'b'
      result = ''
      for sink in self.sinks:
         result += self.write_inline_tag(sink, self.attribute)
         result += ' '
      result = self.write_tag(result, TAG)
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Verbatim(ORGAN.Organ):

   def parse(self):
      pass

   def write(self):
      pass

class Alternative(ORGAN.Organ):

   def parse(self):
      pass

   def write(self):
      pass

class Traditional(ORGAN.Organ):

   def parse(self):
      pass

   def write(self):
      pass

