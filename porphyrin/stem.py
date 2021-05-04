import organ as ORGAN
import leaflet as LEAFLET
import caution as CAUTION

class Document(ORGAN.Stem):

   kine = "document"

   def parse(self):
      head = 0
      while head <= self.source.size() - 1:
         organ, head = self.snip(head)
         sinks.append(organ)

   def write(self):
      result = ''
      for bough in self.sinks:
         result += bough.write()
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Section(ORGAN.Stem):

   kind = "section"

   def write(self):
      element = ''
      for twig in self.sinks:
         element += twig.write()
      return self.write_block_tag(element, self.kind)

class Stanza(ORGAN.Stem):

   kind = "stanza"

   def write(self):
      element = ''
      for twig in self.sinks:
         element += twig.write()
      return self.write_block_tag(element, self.kind)

class Table(ORGAN.Stem):

   kind = "table"

   def write(self):
      element = ''
      for twig in self.sinks:
         element += twig.write()
      return self.write_block_tag(element, self.kind)

class Image(ORGAN.Leaf):

   kind = "image"

   def write(self):
      pass

class Break(ORGAN.Leaf):

   kind = "break"

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Paragraph(ORGAN.Stem):

   def parse(self):
      pass

   def write(self):
      return self.write_tag("paragraph")


class Line(ORGAN.Stem):

   def parse(self):
      pass

   def write(self):
      return self.write_tag("line")

class Row(ORGAN.Stem):

   def parse(self):
      pass

   def write(self):
      return self.write_tag("row")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Sentence(ORGAN.Stem):

   def parse(self):
      while not self.source:
         self.element, self.mark = self.snip()
         label = get_label_from_mark(mark)
         fragment_left = self.find_fragment_left()
         fragment_right = self.find_fragment_right()
         data = {
             "place" : self.place,
             "fragment_left" : fragment_left,
             "mark" : mark,
             "fragment_right" : fragment_right
         }
         if (be_leaf_label(label)):
             error.outer_scope_leaf(**data)
         if (label == "serif-roman"):
            leaf = Serif_roman()
         elif (label == "serif-italic"):
            label = Serif_italic
         elif (label == "serif-bold"):
            label = Serif_bold
         elif (label == "sans-normal"):
            label = Sans_normal
         elif (label == "sans-bold"):
            label = Sans_bold
         # ...

class Verse(ORGAN.Stem):

   def parse(self):
      while not self.source:
         self.element, self.mark = self.snip()
         label = get_label_from_mark(mark)
         fragment_left = self.find_fragment_left()
         fragment_right = self.find_fragment_right()
         data = {
             "place" : self.place,
             "fragment_left" : fragment_left,
             "mark" : mark,
             "fragment_right" : fragment_right
         }
         if (be_leaf_label(label)):
             error.outer_scope_leaf(**data)
         if (label == "serif-roman"):
            leaf = Serif_roman()

class Cell(ORGAN.Stem):

   def parse(self):
      while not self.source:
         self.element, self.mark = self.snip()
         label = get_label_from_mark(mark)
         fragment_left = self.find_fragment_left()
         fragment_right = self.find_fragment_right()
         data = {
             "place" : self.place,
             "fragment_left" : fragment_left,
             "mark" : mark,
             "fragment_right" : fragment_right
         }
         if (be_leaf_label(label)):
             error.outer_scope_leaf(**data)
         if (label == "serif-roman"):
            leaf = Serif_roman()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Verbatim(ORGAN.Stem):

   def parse(self):
      pass

   def write(self):
      pass

class Alternative(ORGAN.Stem):

   def parse(self):
      pass

   def write(self):
      pass

class Traditional(ORGAN.Stem):

   def parse(self):
      pass

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


