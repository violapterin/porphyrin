import tree
import bough
import leaf
import main

class Caution(forest.Piece)

   COLOR_STRESS = "\033[93m"
   COLOR_NORMAL = "\033[0m"

   def __init__(self, **data_in):
      place = data.pop(place, Place())
      fragment_left = data.pop(fragment_left, '')
      token_error = data.pop(token_error, '')
      fragment_right = data.pop(fragment_right, '')
      message_left = data.pop(message_left, '')
      message_right = data.pop(message_right, '')

   def warn(self):
      self.emit()

   def panic(self):
      self.cease()
      self.emit()

   def emit(self):
      print("At ", place.emit(), ":\n")
      print("      ", fragment_left, ' ',
            COLOR_STRESS, token_error,
            COLOR_NORMAL, fragment_right, '\n')
      print(message_left,
            COLOR_STRESS, token_error,
            COLOR_NORMAL, message_right)

   def cease(self):
      raise SystemExit()

class Not_recognized_mark_tree(Caution):
   message_left = "Token",
   message_right = "is not a tree opening mark."

class not_recognized_mark_tree(Caution):
   message_left = "Token",
   message_right = "is not a tree opening mark."

class warn_not_matched_mark_tree(Caution):
   message_left = "Tree opening mark",
   message_right = "is not matched."

class warn_not_recognized_mark_leaf(Caution):
   message_left = "Token",
   message_right = "is not an leaf opening mark."

class warn_not_matched_mark_leaf(Caution):
   message_left = "Leaf opening mark",
   message_right = "is not matched."

class warn_outer_scope_leaf(Caution):
   message_left = "Leaf",
   message_right = "cannot occur in the outer scope."

class warn_inner_scope_tree(Caution):
   message_left = "Tree",
   message_right = "cannot occur in the outer scope."

# def table_column_not_match




