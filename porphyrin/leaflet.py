import organ as ORGAN
import stem as STEM
import caution as CAUTION

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Leaflet(Organ):

   def __init__(self, **data):
      super().__init__(**data)
      self.sink = ''

   def parse(self):
      pass

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Serif_roman(Leaflet):

   kind = "serif-roman"

   def parse(self):
      self.source = self.tune_text(self.source)

   def write(self):
      return self.write_inline_tag(self.content, self.kind)

class Serif_italic(Leaflet):

   kind = "serif-italic"

   def parse(self):
      self.source = self.tune_text(self.source)

   def write(self):
      return self.write_inline_tag(self.content, self.kind)

class Serif_bold(Leaflet):

   kind = "serif-bold"

   def parse(self):
      self.source = self.tune_text(self.source)

   def write(self):
      return self.write_inline_tag(self.content, self.kind)

class Sans_roman(Leaflet):

   kind = "sans-roman"

   def parse(self):
      self.source = self.tune_text(self.source)

   def write(self):
      return self.write_inline_tag(self.content, self.kind)

class Sans_bold(Leaflet):

   kind = "sans-bold"

   def parse(self):
      self.source = self.tune_text(self.source)

   def write(self):
      return self.write_inline_tag(self.content, self.kind)

