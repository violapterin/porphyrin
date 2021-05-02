import organ
import stem
import leaflet
import error



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Serif_roman(organ.Leaflet):

   def __init__(self, **data):
      self.source = data.pop("source", '')
      self.place = data.pop("place", Place())
      self.leftmost = data.pop("fragment_left", '')
      self.rightmost = data.pop("fragment_right", '')
      self.content = ''
      self.head = 0

   def parse(self):
      content = self.source
      self.content = self.tune_text(content)

   def write(self):
      return self.write_tag(self.content, "serif-roman")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Serif_italic(organ.Leaflet):

   def __init__(self, **data):
      self.source = data.pop("source", ''),
      self.place = data.pop("place", Place())
      self.leftmost = data.pop("fragment_left", '')
      self.rightmost = data.pop("fragment_right", '')
      self.content = ''
      self.head = 0

   def parse(self):
      content = self.source
      self.content = self.tune_text(content)

   def write(self):
      return self.write_tag(self.content, "serif-italic")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Serif_bold(organ.Leaflet):

   def __init__(self, **data):
      self.source = data.pop("source", ''),
      self.place = data.pop("place", Place())
      self.leftmost = data.pop("fragment_left", '')
      self.rightmost = data.pop("fragment_right", '')
      self.content = ''
      self.head = 0

   def parse(self):
      content = self.source
      self.content = self.tune_text(content)

   def write(self):
      return self.write_tag(self.content, "serif-bold")


