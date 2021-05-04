import organ as ORGAN
import stem as STEM
import caution as CAUTION

class Serif_roman(ORGAN.Leaflet):

   kind = "serif-roman"

   def parse(self):
      self.source = self.tune_text(self.source)

   def write(self):
      return self.write_inline_tag(self.content, self.kind)

class Serif_italic(ORGAN.Leaflet):

   kind = "serif-italic"

   def parse(self):
      self.source = self.tune_text(self.source)

   def write(self):
      return self.write_inline_tag(self.content, self.kind)

class Serif_bold(ORGAN.Leaflet):

   kind = "serif-bold"

   def parse(self):
      self.source = self.tune_text(self.source)

   def write(self):
      return self.write_inline_tag(self.content, self.kind)

class Sans_roman(ORGAN.Leaflet):

   kind = "sans-roman"

   def parse(self):
      self.source = self.tune_text(self.source)

   def write(self):
      return self.write_inline_tag(self.content, self.kind)

class Sans_bold(ORGAN.Leaflet):

   kind = "sans-bold"

   def parse(self):
      self.source = self.tune_text(self.source)

   def write(self):
      return self.write_inline_tag(self.content, self.kind)


