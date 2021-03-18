class Error(Exception):
   self.message = ''
   def __init__(self, s__line_remain, place_start):
      self.s__line_remain = s__line_remain
      self.place_start = place_start

   def print():
       print("At")
       place_start.print()
       print('\n')
       print("    ")
       print(self.message)


class ErrorParenthesesMatching(Error):
   self.message = "Parentheses do not match."

