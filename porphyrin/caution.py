import organ as ORGAN
import stem as STEM
import leaf as LEAF

class Caution(ORGAN.Organ):

   def __init__(self, **data):
      self.token = data.pop(token, '')
      self.fragment_left = data.pop("fragment_left", '')
      self.fragment_right = data.pop("fragment_right", '')
      self.count_line = data.pop("count_line", 0)
      self.count_character = data.pop("count_character", 0)
      message_left = ''
      message_right = ''

   def panic(self):
      self.warn()
      self.cease()

   def warn(self):
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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Not_recognizing_mark_bough(Caution):

   message_left = "Token",
   message_right = "is not a bough opening mark."

class Not_recognizing_mark_leaf(Caution):

   message_left = "Token",
   message_right = "is not a leaf opening mark."

class Not_matching_mark_bough(Caution):

   message_left = "Bough opening mark"
   message_right = "is not matched."

class Not_recognizing_mark_leaf(Caution):

   message_left = "Leaf opening mark"
   message_right = "is not matched."

class Occurring_outer_scope_leaf(Caution):

   message_left = "Leaf"
   message_right = "cannot occur in the outer scope."

class Occurring_inner_scope_bough(Caution):

   message_left = "Bough"
   message_right = "cannot occur in the inner scope."

# def table_column_not_match




