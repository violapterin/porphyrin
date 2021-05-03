import organ
import stem
import leaflet
import caution

class Serif_roman(organ.Leaflet):

   kind = "serif-roman"

   def parse(self):
      self.source = self.tune_text(self.source)

   def write(self):
      return self.write_inline_tag(self.content, self.kind)

class Serif_italic(organ.Leaflet):

   kind = "serif-italic"

   def parse(self):
      self.source = self.tune_text(self.source)

   def write(self):
      return self.write_inline_tag(self.content, self.kind)

class Serif_bold(organ.Leaflet):

   kind = "serif-bold"

   def parse(self):
      self.source = self.tune_text(self.source)

   def write(self):
      return self.write_inline_tag(self.content, self.kind)

class Sans_roman(organ.Leaflet):

   kind = "sans-roman"

   def parse(self):
      self.source = self.tune_text(self.source)

   def write(self):
      return self.write_inline_tag(self.content, self.kind)

class Sans_bold(organ.Leaflet):

   kind = "sans-bold"

   def parse(self):
      self.source = self.tune_text(self.source)

   def write(self):
      return self.write_inline_tag(self.content, self.kind)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Verbatim(organ.Stem):

   def parse(self):
      pass

   def write(self):
      pass

class Alternative(organ.Stem):

   def parse(self):
      pass

   def write(self):
      pass

class Traditional(organ.Stem):

   def parse(self):
      pass

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

