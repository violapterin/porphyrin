import os

import organ as ORGAN
import stem as STEM
import leaf as LEAF
import tissue as TISSUE
import caution as CAUTION

def make(folder_in, folder_out):
   extension = ".ppr"
   things_in = os.scandir(folder_in)
   for thing_in in things_in:
      name_in = thing.name
      path_in = os.path.join(folder_in, name_in)
      if not thing_in.is_file():
         print("Warning: ", name_in, " is not a file.")
         continue
      if not path_in.endswith(extension):
         print(
            "Warning: file ", name_in,
            " does not end in \"", extension, "\".",
         )
         continue
      path_out = os.path.join(folder_out, path_in)
      if os.path.isfile(path_out):
         time_in = thing.stat().st_ctime
         time_out = os.path.getmtime(path_out)
         if time_in < time_out:
            continue
      convert(path_in, path_out) 

def convert(path_in, path_out):
   handle_in = open(path_in, mode = 'r')
   source = handle_in.read()
   handle_in.close()
   document = STEM.Document({"source": source})
   document.parse()
   sink = document.write()
   handle_out = open(path_out, mode = 'w')
   handle_out.write(sink)
   handle_out.close()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def get_mark_right(mark_left):
   assert(len([glyph for glyph in mark_left]) == 1)
   label = get_label_math(mark_left[0])
   considered = {"DEFINITION_LEFT", "COMMENT_LEFT"}
   if (label not in considered):
      return mark_left

   mark_right = mark_left
   if (label = "DEFINITION_LEFT"):
      tip_left = get_tip("DEFINITION_LEFT")
      tip_right = get_tip("DEFINITION_RIGHT")
   if (label = "COMMENT_LEFT"):
      tip_left = get_tip("COMMENT_LEFT")
      tip_right = get_tip("COMMENT_RIGHT")
   table = mark_right.maketrans(tip_left, tip_right)
   mark_right = mark_right.translate(table)
   return mark_right

def write_element(**data):
   assert(content in data)
   assert(tag in data)
   enter = ''
   if ('\n' in data[content]): enter = '\n'

   result = '<' + data[tag] + ' '
   if (attributes in data):
      attributes = data[attributes]
      values = data[values]
      assert(len(values) == len(attributes))
      size = len(attributes)
      for index in range(size)
         result += ' ' + data[attributes][index]
         result += "=\"" + data[values][index] + '\"'
   result += "> "
   result += enter + data[content] + ' ' + enter
   result += "</" + data[tag] + '>'
   return result


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def get_label(tip):
   labels = {
      '@': "SERIF_NORMAL",
      '%': "SERIF_ITALIC",
      '#': "SERIF_BOLD",
      '$': "SANS_NORMAL",
      '&': "SANS_BOLD",
      '+': "CODE",
      '*': "PSEUDO",
      '^': "MATH",
      '\\': "LINK",
      #
      '=': "PARAGRAPHS",
      '/': "LINES",
      '\"': "ROWS",
      '|': "IMAGE",
      '`': "IDENITFIER",
      '<': "COMMENT_LEFT",
      '>': "COMMENT_RIGHT",
      '{': "DEFINITION_LEFT",
      '}': "DEFINITION_RIGHT",
      #
      '~': "BREAK",
      '_': "SPACE",
      '\'': "NEWLINE",
   }
   label = labels.get(tip)
   return label

def be_bough_start(label):
   labels = {
      "PARAGRAPHS",
      "LINES",
      "ROWS",
      "IMAGE",
      "BREAK",
   }
   return (label in labels)

def be_leaf_start(label):
   labels = {
      "SERIF_NORMAL",
      "SERIF_ITALIC",
      "SERIF_BOLD",
      "SANS_NORMAL",
      "SANS_BOLD",
      "CODE",
      "PSEUDO",
      "MATH",
      "LINK",
      "COMMENT_LEFT",
      "DEFINITION_LEFT",
      "IDENITFIER",
   }
   return (label in labels)

def be_macro_start(label):
   labels = {
      "IDENITFIER",
      "DEFINITION_LEFT",
   }
   return (label in labels)

def be_hollow(label):
   labels = {
      "BREAK",
      "SPACE",
      "NEWLINE",
   }
   return (label in labels)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def write_brace(command, *options):
   result = ''
   result += command + ' '
   for option in options:
      result += '{' + option + '}' + ' '
   return result

def get_label_math(tip):
   labels = {
      '.': "PLAIN"
      '#': "BOLD"
      '&': "BLACK"
      '@': "CURSIVE"
      '$': "GREEK"
      #
      '%': "ABSTRACTION"
      '+': "ARITHMETICS"
      '^': "OPERATION"
      '*': "SHAPE"
      '-': "LINE"
      '\\': "ARROW_LEFT"
      '|': "ARROW_MIDDLE"
      '/': "ARROW_RIGHT"
      '=': "EQUIVALENCE"
      '<': "ORDER_LEFT"
      '>': "ORDER_RIGHT"
      #
      '(': "START_PAIR"
      ':': "CUT_PAIR"
      ')': "STOP_PAIR"
      '[': "START_TRIPLET"
      '': "CUT_TRIPLET"
      ']': "STOP_TRIPLET"
      '{': "START_TUPLE"
      '}': "STOP_TUPLE"
      ';': "CUT_TUPLE"
      '\': "SANS" 
      '\"': "ROMAN"
      '!': "ACCENT_ONE"
      '?': "ACCENT_TWO"
   }
   label = labels.get(tip)
   return label

def be_symbol_math(label):
   labels = {
      "PLAIN",
      "BOLD",
      "BLACK",
      "CURSIVE",
      "GREEK",
      "ABSTRACTION",
      "ARITHMETICS",
      "OPERATION",
      "SHAPE",
      "LINE",
      "ARROW_LEFT",
      "ARROW_MIDDLE",
      "ARROW_RIGHT",
      "EQUIVALENCE",
      "ORDER_LEFT",
      "ORDER_RIGHT",
   }
   return (label in labels)

def be_box_left_math(label):
   labels = {
      "START_PAIR",
      "CUT_PAIR",
      "STOP_PAIR",
      "START_TRIPLET",
      "CUT_TRIPLET",
      "STOP_TRIPLET",
      "START_TUPLE",
      "STOP_TUPLE",
      "CUT_TUPLE",
      "SANS" ,
      "ROMAN",
   }
   return (label in labels)

def get_tip_right_math(tip_left):
   assert(len(tip_left) == 1)
   tip_right = None
   label = get_label_math(tip_left)
   if (label == "START_ROUND"):
      tip_right = get_tip_math("STOP_ROUND")
   if (label == "START_SQUARE"):
      tip_right = get_tip_math("STOP_SQUARE")
   if (label == "START_CURLY"):
      tip_right = get_tip_math("STOP_CURLY")
   if (label == "START_ANGLE"):
      tip_right = get_tip_math("STOP_ANGLE")
   if (label in {"SANS", "ROMAN", "MONO"}):
      tip_right = tip_left
   return tip_right

def get_tip_middle_math(tip_left):
   assert(len(tip_left) == 1)
   tip_middle = None
   label = get_label_math(tip_left)
   if (label == "START_ROUND"):
      tip_middle = get_tip_math("MIDDLE_ROUND")
   if (label == "START_SQUARE"):
      tip_middle = get_tip_math("MIDDLE_SQUARE")
   if (label == "START_CURLY"):
      tip_middle = get_tip_math("MIDDLE_CURLY")
   if (label == "START_ANGLE"):
      tip_middle = get_tip_math("MIDDLE_ANGLE")
   return tip_middle

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def get_label_pseudo(tip):
   labels = {
      "PLAIN": '.',
      "BOLD": ',',
      "ROMAN": '\"',
      "ROMAN_BLACK": ';',
      "SANS": '\'',
      "SANS_BLACK": ':',
      "GREEK": '-',
      "GREEK_BOLD": '=',
      "KANJI_FIRST": '!',
      "KANJI_SECOND": '?',
      #
      "KANA_ZEROTH": '_',
      "KANA_FIRST": '~',
      "KANA_SECOND": '@',
      "KANA_THIRD": '#',
      "KANA_FOURTH": '$',
      "KANA_FIFTH": '%',
      "KANA_SIXTH": '^',
      "KANA_SEVENTH": '&',
      "KANA_EIGHTH": '*',
      "KANA_NINTH": '+',
      #
      "START_ROUND": '(',
      "START_SQUARE": '[',
      "START_CURLY": '{',
      "START_ANGLE": '<',
      "STOP_ROUND": ')',
      "STOP_SQUARE": ']',
      "STOP_CURLY": '}',
      "STOP_ANGLE": '>',
      "CUT_RIGHT": '/',
      "CUT_MIDDLE": '|',
      "CUT_LEFT": '\\',
   }
   labels = get_labels()
   label = labels.get(tip)
   return label

def be_letter_pseudo(label):
   labels = give_labels_letter_pseudo()
   return (label in labels)

def be_sign_pseudo(label):
   labels = give_labels_sign_pseudo()
   return (label in labels)

def be_bracket_pseudo(label):
   labels = give_labels_bracket_pseudo()
   return (label in labels)

def get_tip_right_pseudo(tip_left):
   assert(len(tip_left) == 1)
   label = get_label_pseudo(tip_left)
   if (label == "START_ROUND"):
      tip_right = get_tip_pseudo("STOP_ROUND")
   if (label == "START_SQUARE"):
      tip_right = get_tip_pseudo("STOP_SQUARE")
   if (label == "START_CURLY"):
      tip_right = get_tip_pseudo("STOP_CURLY")
   if (label == "START_ANGLE"):
      tip_right = get_tip_pseudo("STOP_ANGLE")
   if (label == "QUOTE_SINGLE"):
      tip_right = tip_left
   if (label == "QUOTE_DOUBLE"):
      tip_right = tip_left
   return tip_right

