import bough
import leaf
import main
import error

class Twig(object):

   def __init__(self, **arguments):
      self.source = arguments.pop("source", ''),
      self.place = arguments.pop("place", Place()),
      self.fragment_global_left = ''
      self.fragment_global_right = ''
      self.pile = []
      self.head = 0

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

class Sentence(object):

   kind = "sentence"

   def write(self):
      return self.write_tag():

class Verse(object):

   kind = "verse"

   def write(self):
      return self.write_tag():

class Cell(object):

   kind = "cell"

   def write(self):
      return self.write_tag():


