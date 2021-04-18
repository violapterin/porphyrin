import tree
import leaf
import error
import main


class Bough(object):

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


class Paragraph(object):

   kind = "paragraph"

   def write(self):
      return self.write_tag():

class Line(object):

   kind = "line"

   def write(self):
      return self.write_tag():

class row(object):

   kind = "row"

   def write(self):
      return self.write_tag():

