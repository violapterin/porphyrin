from .organ import Caution

class Token_cannot_begin_bough(Caution):

   message_left = "Token",
   message_right = "cannot begin a bough."

class Token_cannot_begin_leaf(Caution):

   message_left = "Token",
   message_right = "cannot begin a leaf."

class Mark_mismatched_in_bough(Caution):

   message_left = "Bough opening mark"
   message_right = "is mismatched."

class Mark_mismatched_in_leaf(Caution):

   message_left = "Leaf opening mark"
   message_right = "is mismatched."

class Allowing_only_leaf(Caution):

   message_left = "Token"
   message_right = "is not a leaf; here only a leaf is allowed."

class Allowing_only_bough(Caution):

   message_left = "Token"
   message_right = "is not a bough; here only a bough is allowed."

class Column_not_agreeing(Caution):

   message_left = "Columns in the row"
   message_right = "does not agree others array in number."
class Too_many_column(Caution):

   message_left = "Row"
   message_right = "has too many columns."

class Bracket_mismatched(Caution):

   message_left = "Bracket"
   message_right = "is not matched in the leaf."

class Bracket_not_balanced(Caution):

   message_left = "Bracket"
   message_right = "is not balanced in the leaf."

class Token_invalid_as_symbol(Caution):

   message_left = "Token"
   message_right = "is invalid as a symbol."

class Conflicting_delimiter(Caution):

   message_left = "Tissue"
   message_right = "contain conflicting delimiters."

class Macro_not_gathered(Caution):

   message_left = "Macro"
   message_right = "is not gathered in the very beginning."

class Disallowing_link(Caution):

   message_left = "Link"
   message_right = "is disallowed in the very beginning."

class Invalid_link_for_image(Caution):

   message_left = "Token"
   message_right = "is not a valid link for the image."

class Allowing_only_symbol(Caution):

   message_left = "Token"
   message_right = "is not a symbol; only a symbol is allowed."

class Allowing_only_alphabet(Caution):

   message_left = "Token"
   message_right = "is not an alphabet; only an alphabet is allowed."

class Wrong_number_boxes(Caution):

   message_left = "Token"
   message_right = "contains too many or too few boxes."


