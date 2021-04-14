import branch
import twig
import leaf
import main


class Error(Exception):

   def __init__(self, **arguments):
      self.place = arguments.pop("place", Place())
      self.remain_left = arguments.pop("remain_left", '')
      self.token = arguments.pop("token", '')
      self.remain_right = arguments.pop("remain_right", '')
      self.message_left = ''
      self.message_right = ''

   def output():
       print("At ", place.write(), ":\n")
       print("    ", self.remain_left, self.token, self.remain_right)
       print("    ", self.message_left, self.token, self.message_right)

class Error_wrong_boundary_twig(Error):

   message_first = "Token"
   message_second = "is not a twig boundary."

   def __init__(self, **arguments):
      Error.__init__(**arguments)

class Error_match_boundary_twig(Error):

   message_first = "Twig boundary"
   message_second = "is not matched."

   def __init__(self, **arguments):
      Error.__init__(self, **arguments)

class Error_wrong_boundary_leaf(Error):

   message_first = "Token"
   message_second = "is not a leaf boundary."

   def __init__(self, **arguments):
      Error.__init__(self, **arguments)

class Error_match_boundary_leaf(Error):

   message_first = "Leaf boundary"
   message_second = "is not matched."

   def __init__(self, **arguments):
      Error.__init__(self, **arguments)


