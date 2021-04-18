import tree
import leaf
import error
import main


class Tree(object):

   def __init__(self, **arguments):
      self.source = arguments.pop("source", ''),
      self.place = arguments.pop("place", Place()),

   def write(self):
      pass

   def write_tag(self):
      result = ''
      result += "<div" + ' '
      result += "class=" + self.kind + ">"
      result += self.write_content()
      result += "<class" + "/>"
      return result

   def write_content(self):
      result = ''
      for leaf in pile:
         result += leaf.write()
      return result

class Section(object):

   kind = "Section"

   def write(self):
      return self.write_tag():

class Stanza(object):

   kind = "stanza"

   def write(self):
      return self.write_tag():

class Table(object):

   kind = "table"

   def write(self):
      return self.write_tag():

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Image(object):

   kind = "table"

class Break(object):

   kind = "table"

