import tissue
import tree
import leaf
import leaflet

class Caution(forest.Piece)

   def __init__(self, **data_in):
      token = data.pop(token, '')
      fragment_left = data.pop(fragment_left, '')
      fragment_right = data.pop(fragment_right, '')
      self.count_line = data.pop("count_line", 0)
      self.count_character = data.pop("count_character", 0)
      message_left = ''
      message_right = ''

   def warn(self):
      self.emit()

   def panic(self):
      self.emit()
      self.cease()

   def emit(self):
      color_stress = "\033[93m"
      color_normal = "\033[0m"
      print("At ", place.emit(), ":\n")
      print("      ", fragment_left, ' ',
            color_stress, token_error,
            color_normal, fragment_right, '\n')
      print(message_left,
            color_stress, token_error,
            color_normal, message_right)

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




