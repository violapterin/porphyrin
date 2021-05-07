import organ as ORGAN
import stem as STEM
import caution as CAUTION

class Serif_roman(ORGAN.Organ):

   KIND = "serif-roman"
   TAG = "span"

   def parse(self):
      self.tune_text()
      head = 0
      while head <= self.source.len() - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      for sink in self.sinks:
         result += write_tag(
            element = sink,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      return result

class Serif_italic(ORGAN.Organ):

   KIND = "serif-italic"
   TAG = "em"

   def parse(self):
      self.tune_text()
      head = 0
      while head <= self.source.len() - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      for sink in self.sinks:
         result += write_tag(
            element = sink,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      result = self.write_tag(result, TAG)
      return result

class Serif_bold(ORGAN.Organ):

   KIND = "serif-bold"
   TAG = 'b'

   def parse(self):
      self.tune_text()
      head = 0
      while head <= self.source.len() - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      for sink in self.sinks:
         result += self.write_tag_inline(sink, self.KIND)
         result += ' '
      result = self.write_tag(result, TAG)
      return result

class Sans_roman(ORGAN.Organ):

   KIND = "sans-roman"

   def parse(self):
      self.tune_text()
      head = 0
      while head <= self.source.len() - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      for sink in self.sinks:
         result += self.write_tag_inline(sink, self.KIND)
         result += ' '
      return result

class Sans_bold(ORGAN.Organ):

   KIND = "sans-bold"
   TAG = 'b'

   def parse(self):
      self.tune_text()
      head = 0
      while head <= self.source.len() - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      for sink in self.sinks:
         result += self.write_tag_inline(sink, self.KIND)
         result += ' '
      result = self.write_tag(result, self.TAG)
      return result

class Monospace(ORGAN.Organ):

   KIND = "sans-bold"
   TAG = "pre"

   def parse(self):
      self.tune_text()
      head = 0
      while head <= self.source.len() - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      for sink in self.sinks:
         result += self.write_tag_inline(sink, self.KIND)
         result += ' '
      result = self.write_tag(result, self.TAG)
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Alternative(ORGAN.Organ):

   def parse(self):
      pass

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Traditional(ORGAN.Organ):

   BOLD = 1
   BLACK = 2
   CURSIVE = 3
   EXTENDED = 4
   ABSTRACTION = 11
   EQUIVALENCE = 21
   ARITHMETICS = 22
   OPERATION = 23
   SHAPE = 24
   LINE = 25
   ARROW_LEFT = 31
   ARROW_RIGHT = 32
   ORDER_LEFT = 33
   ORDER_RIGHT = 34

   def parse(self):
      pass

   def write(self):
      pass

   # # # # # # # # # # # # # # # #

   class Letter(object):

      def __init__(self, number):
         self.number = number

   class Sign(object):

      def __init__(self, number):
         self.number = number

   # # # # # # # # # # # # # # # #

   class Script(object):

      def __init__(self, symbol, up, down):
         self.symbol = symbol
         self.up = up
         self.down = down

   class Fraction(object):

      def __init__(self, symbol, up, down):
         self.symbol = symbol
         self.up = up
         self.down = down

   class Array(object):

      def __init__(self, **entries):
         pass

   # # # # # # # # # # # # # # # #

   class Diacritics(object):

      def __init__(self, symbol, number):
         self.symbol = symbol
         self.number = number

   class Roman(object):

      def __init__(self, text):
         self.text = text

   class Sans(object):

      def __init__(self, text):
         self.text = text



