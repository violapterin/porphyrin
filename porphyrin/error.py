import main
import text
import code
import block


class Error(Exception):

   self.message_left = ''
   self.message_right = ''

   def __init__(self, place, source_left, source_token, source_right):
      self.place = place
      self.left = left
      self.token = token
      self.right = self.right

   def output():
       print("At ", place.write(), ":\n")
       print("    ", self.source_left, self.token, self.source_right)
       print("    ", self.message_left, self.token, self.message_right)

class Error_wrong_boundary_block(Error):
   self.message_first = "Token"
   self.message_second = "is not a block boundary."

class Error_match_boundary_block(Error):
   self.message_first = "Block boundary"
   self.message_second = "is not matched."

class Error_wrong_boundary_inline(Error):
   self.message_first = "Token"
   self.message_second = "is not a inline boundary."

class Error_match_boundary_inline(Error):
   self.message_first = "Inline boundary"
   self.message_second = "is not matched."

