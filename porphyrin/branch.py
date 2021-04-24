import tree
import leaf
import error
import main

class Tree(Tissue):

   def __init__(self, **data):
      self.source = data.pop("source", '')
      self.place = Place()
      self.sink = []
      self.leftmost = ''
      self.rightmost = ''
      self.head = 0

   def parse(self):
      while not self.source:
         content, mark = self.snip()
         kind = get_kind_tree(mark)
         fragment_left = self.find_fragment_left()
         fragment_right = self.find_fragment_right()
         if (kind == 0):
         error.outer_scope_leaf(
                   place = self.place,
                   fragment_left = fragment_left,
                   mark = mark,
                   fragment_right = fragment_right)

         self.push(leaf)

   def write(self):
      result = ''
      for tree in self.treees:
         result += tree.write()
      return result


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Bough(tree.Flesh):

   def __init__(self, **data):
      self.source = data.pop("source", ''),
      self.place = data.pop("place", Place()),
      self.leftmost = data.pop("leftmost", '')
      self.rightmost = data.pop("rightmost", '')
      self.sinks = []

   def write(self):
      pass

   def write_tag(self):
      result = ''
      result += "<div" + ' '
      result += "class=" + self.kind + ">"
      result += self.write_element()
      result += "<class" + "/>"
      return result

   def write_element(self):
      result = ''
      for leaf in sink:
         result += leaf.write()
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Section(Bough):

   kind = "Section"

   def write(self):
      return self.write_tag():

class Stanza(Bough):

   kind = "stanza"

   def write(self):
      return self.write_tag():

class Table(Bough):

   kind = "table"

   def write(self):
      return self.write_tag():

class Image(object):

   kind = "table"

class Break(object):

   kind = "table"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Twig(tree.Flesh):

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

class Paragraph(Bough):


   def write(self):
      return self.write_tag("paragraph"):


class Line(object):

   def write(self):
      return self.write_tag("line"):


class Row(object):

   def write(self):
      return self.write_tag("row"):


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Frond(tree.Flesh):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Sentence(object):

   def write(self):
      return self.write_tag("sentence")

class Verse(object):

   def write(self):
      return self.write_tag("verse")

class Cell(object):

   kind = "cell"

   def write(self):
      return self.write_tag("cell")




