import organ as ORGAN
import stem as STEM
import leaf as LEAF
import tissue as TISSUE
import aid as AID

class Caution(ORGAN.Organ):

   def __init__(self, **data):
      self.fill_basic(**data)
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
   message_right = "is not a leaf; here only a leaf is allowed."

class Allowing_only_bough(Caution):

   message_left = "Token"
   message_right = "is not a bough; here only a bough is allowed."

class Not_agreeing_column(Caution):

   message_left = "Columns in the row"
   message_right = "does not agree others rows in number."

class Not_matching_bracket(Caution):

   message_left = "Bracket"
   message_right = "is not matched in the leaf."

class Not_being_balanced_bracket(Caution):

   message_left = "Bracket"
   message_right = "is not balanced in the leaf."

class Not_being_valid_symbol(Caution):

   message_left = "Token"
   message_right = "is not a valid symbol".

class Conflicting_delimiter_tissue(Caution):

   message_left = "Tissue"
   message_right = "contain conflicting delimiters".

class Macro_not_gathered(Caution):

   message_left = "Macro"
   message_right = "is not gathered in the very beginning".

class Disallowing_link(Caution):

   message_left = "Link"
   message_right = "is disallowed in this position."

class Allowing_only_symbol(Caution):

   message_left = "Token"
   message_right = "is not a symbol; here only a symbol is allowed."



