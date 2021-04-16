import branch
import leaf
import error
import main


class Twig(object):

   def __init__(self, **arguments):
      self.source = arguments.pop("source", ''),
      self.place = arguments.pop("place", Place()),



   def write_content(self):
      result = ''
      for leaf in self.pile:
         result += leaf.write()



