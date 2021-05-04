import organ as ORGAN
import leaflet as LEAFLET
import caution as CAUTION


class Stem(Organ):

   def __init__(self, **data):
      super().__init__(**data)
      self.sinks = []

   def __copy__(self, organ):
      self.__init__(organ.give_data())
      self.sinks.append(organ)

   def parse(self):
      pass

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Document(Stem):

   kine = "document"

   def parse(self):
      head = 0
      while head <= self.source.size() - 1:
         organ, head = self.snip_bough(head)
         sinks.append(organ)

   def write(self):
      result = ''
      for bough in self.sinks:
         result += bough.write()
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Section(Stem):

   kind = "section"

   def parse(self):
      head = 0
      BE_NEWLINE = False
      while head <= self.source.size() - 1:
         organ, head = self.snip_twig(head)
         if (organ.kind == "newline")
            BE_NEWLINE = True
         if (organ.kind == "space")
            sinks[-1].
         sinks.append(organ)


   def write(self):
      element = ''
      for twig in self.sinks:
         element += twig.write()
      return self.write_block_tag(element, self.kind)

class Stanza(Stem):

   kind = "stanza"

   def write(self):
      element = ''
      for twig in self.sinks:
         element += twig.write()
      return self.write_block_tag(element, self.kind)

class Table(Stem):

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

class Paragraph(Stem):

   kind = "paragraph"

   def parse(self):
      pass

   def write(self):
      return self.write_tag("paragraph")

class Line(Stem):

   kind = "line"

   def parse(self):
      pass

   def write(self):
      return self.write_tag("line")

class Row(Stem):

   kind = "row"

   def parse(self):
      pass

   def write(self):
      return self.write_tag("row")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Sentence(Stem):

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

class Verse(Stem):

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

class Cell(Stem):

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

class Verbatim(Stem):

   def parse(self):
      pass

   def write(self):
      pass

class Alternative(Stem):

   def parse(self):
      pass

   def write(self):
      pass

class Traditional(Stem):

   def parse(self):
      pass

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
