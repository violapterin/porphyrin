import organ as ORGAN
import stem as STEM
import leaf as LEAF
import aid as AID

class Caution(object):

   def __init__(self, **data):
      self.source = data.pop("source", '')
      self.leftmost = data.pop("leftmost", '')
      self.rightmost = data.pop("rightmost", '')
      self.count_line = data.pop("count_line", 0)
      self.count_glyph = data.pop("count_glyph", 0)
      message_left = ''
      message_right = ''

   def panic(self):
      self.warn()
      raise SystemExit()

   def warn(self):
      color_stress = "\033[93m"
      color_normal = "\033[0m"
      print("At ", place.emit(), ":\n")
      print(
         "      ", leftmost, ' ',
         color_stress, token_error,
         color_normal, rightmost, '\n'
      )
      print(
         message_left,
         color_stress, token_error,
         color_normal, message_right
      )

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Not_valid_mark_bough(Caution):

   message_left = "Token",
   message_right = "does not begin a bough."

class Not_valid_mark_leaf(Caution):

   message_left = "Token",
   message_right = "does not begin a leaf."

class Not_matching_mark_bough(Caution):

   message_left = "Bough opening mark"
   message_right = "is not matched."

class Not_matching_mark_leaf(Caution):

   message_left = "Leaf opening mark"
   message_right = "is not matched."

class Allowing_only_leaf(Caution):

   message_left = "Token"
   message_right = "is not a leaf; only a leaf is allowed."

class Allowing_only_bough(Caution):

   message_left = "Token"
   message_right = "is not a bough; only a bough is allowed."

class Not_agreeing_table_column(Caution):

   message_left = "Rows column"
   message_right = "does not agree the others in number."

class Not_matching_bracket(Caution):

   message_left = "Bracket"
   message_right = "is not matched in the leaf."

class Not_being_balanced_bracket(Caution):

   message_left = "Bracket"
   message_right = "is not balanced in the leaf."

class Not_being_valid_symbol(Caution):

   message_left = "Token"
   message_right = "is not a valid symbol".

class Conflicting_delimiter_tuple(Caution):

   message_left = "Tuple"
   message_right = "contain conflicting delimiters".

class Not_gathering_macro_front(Caution):

   message_left = "Macro"
   message_right = "is not gathered in front of the document".


