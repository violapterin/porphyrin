import organ
import leaf
import leaflet
import error

class Document(tissue.Stem):

   def parse(self):
      head = 0
      while not head = self.source.size():
         organ, head = self.snip(head)
         sinks.append(organ)


   def write(self):
      result = ''
      for bough in self.sinks:
         bough.prune()
         result += bough.write()
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Section(tissue.Stem):

   kind = "Section"

   def write(self):
      return self.write_tag()

class Stanza(tissue.Stem):

   kind = "stanza"

   def write(self):
      return self.write_tag()

class Table(tissue.Stem):

   kind = "table"

   def write(self):
      return self.write_tag()

class Image(object):

   kind = "table"

class Break(object):

   kind = "table"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Twig(tree.Stem):

   def __init__(self, **data):
      self.source = data.pop("source", ''),
      self.place = data.pop("place", Place()),
      self.leftmost = data.pop("leftmost", '')
      self.rightmost = data.pop("rightmost", '')
      self.sinks = []

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

   def write(self):
      pass

   def write_tag(self, kind):
      result = ''
      result += "<div" + ' '
      result += "class=" + kind + ">"
      result += self.write_element()
      result += "<div" + "/>"
      return result

   def write_element(self):
      result = ''
      for leaf in sink:
         result += leaf.write()
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Paragraph(tissue.Stem):

   def parse(self):
      pass

   def write(self):
      return self.write_tag("paragraph"):


class Line(tissue.Stem):

   def parse(self):
      pass


class Row(tissue.Stem):

   def parse(self):
      pass


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Sentence(tissue.Stem):

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

class Verse(tissue.Stem):

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

class Cell(tissue.Stem):

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




