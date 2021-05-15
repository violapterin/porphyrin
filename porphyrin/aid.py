import os

import organ as ORGAN
import stem as STEM
import leaf as LEAF
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

def tune_text(source):
   sink = source
   glyphs_mark = set([
      '{', '}', '<', '>',
      '@', '#', '$', '%', '&',
   ])
   glyphs_space = set([' ', '\t', '\n'])
   sink = remove_token(glyphs_mark, sink)
   sink = erase_token(glyphs_space, sink)
   return sink

def tune_code(source):
   sink = source
   glyphs_space = set([' ', '\t', '\n'])
   sink = erase_token(sink, glyphs_space)
   return sink

def remove_token(group, source):
   sink = source
   for glyph in group:
      sink = sink.translate(source.maketrans(glyph, ''))
   return source

def erase_token(group, source):
   sink = source
   for glyph in group:
      sink = sink.translate(source.maketrans(glyph, ' '))
   ' '.join(sink.split())
   return sink

def replace_token(table, source):
   sink = source
   for glyph in group:
      sink = sink.translate(source.maketrans(glyph, table[glyph]))
   return sink

def escape_hypertext(source):
   sink = source
   escapes = {
      '<': "&lt;",
      '>': "&gt;",
      '&': "&amp;",
      '\"': "&quote;",
      '\'': "&apos;",
   }
   sink = replace_token(sink, escapes)
   return sink

def escape_comment(source):
   sink = source
   escapes = {
      '----': '-',
      '---': '-',
      '--': '-',
   }
   sink = replace_token(sink, escapes)
   return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def get_label(tip):
  labels = give_labels()
  label = labels.get(tip)
  return label

def get_tip(label):
  tips = give_labels()
  tip = tips.get(label)
  return tip

def give_labels_leaf():
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
      '`': "IDENITFIER",
      '<': "COMMENT_LEFT",
   }
   return labels

def give_labels_bough():
   labels = {
      '=': "PARAGRAPHS",
      '/': "LINES",
      '\"': "ROWS",
      '|': "IMAGE",
      '~': "BREAK",
      '<': "COMMENT_LEFT",
      '{': "INSTRUCTION_LEFT",
   }
   return labels

def give_labels_other():
   labels = {
      '_': "SPACE",
      '\'': "NEWLINE",
      '}': "DEFINITION_RIGHT",
      '>': "COMMENT_RIGHT",
   }
   return labels

def give_labels():
   labels = {
      **give_labels_bough(),
      **give_labels_leaf(),
      **give_labels_other(),
   }
   return labels

def give_tips():
   labels = give_labels()
   tips = {label: tip for tip, label in labels.items()}
   return tips

def give_tips_leaf():
   labels = give_labels_leaf()
   tips = {label: tip for tip, label in labels.items()}
   return tips

def give_tips_bough():
   labels = give_labels_bough()
   tips = {label: tip for tip, label in labels.items()}
   return tips

def give_tips_other():
   labels = give_labels_other()
   tips = {label: tip for tip, label in labels.items()}
   return tips

def be_bough(label):
   labels = give_labels_bough()
   return (label in labels)

def be_leaf(label):
   labels = give_labels_leaf()
   return (label in labels)

def be_other(label):
   labels = give_labels_other()
   return (label in labels)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def write_brace(command, *options):
   result = ''
   result += command + ' '
   for option in options:
      result += '{' + option + '}' + ' '
   return result

def get_label_math(tip):
  labels = get_labels()
  label = labels.get(tip)
  return label

def get_tip_math(label):
  tips = get_tips()
  tip = tips.get(label)
  return tip

def give_labels_letter_math():
   labels = {
      "PLAIN": '.',
      "BOLD": '#',
      "BLACK": '&',
      "CURSIVE": '@',
      "GREEK": '$',
   }
   return labels

def give_labels_sign_math():
   labels = {
      "PLAIN": '.',
      "ABSTRACTION": '%',
      "ARITHMETICS": '+',
      "OPERATION": '^',
      "SHAPE": '*',
      "LINE": '-',
      "ARROW_LEFT": '\\',
      "ARROW_MIDDLE": '|',
      "ARROW_RIGHT": '/',
      "EQUIVALENCE": '=',
      "ORDER_LEFT": '<',
      "ORDER_RIGHT": '>',
   }
   return labels

def give_labels_bracket_math():
   labels = {
      "START_PAIR": '(',
      "CUT_PAIR": ',',
      "STOP_PAIR": ')',
      "START_TRIPLET": '[',
      "CUT_TRIPLET": ':',
      "STOP_TRIPLET": ']',
      "START_TUPLE": '{',
      "STOP_TUPLE": '}',
      "CUT_TUPLE": ';',
   }
   return labels

def give_labels_math():
   labels = {
      **give_labels_letter_math(),
      **give_labels_sign_math(),
      **give_labels_bracket_math(),
   }
   return labels

def give_tips_math():
   labels = give_labels_math()
   tips = {label: tip for tip, label in labels.items()}
   return tips

def give_tips_letter_math():
   labels = give_labels_letter_math()
   tips = {label: tip for tip, label in labels.items()}
   return tips

def give_tips_sign_math():
   labels = give_labels_sign_math()
   tips = {label: tip for tip, label in labels.items()}
   return tips

def give_tips_bracket_math():
   labels = give_labels_bracket_math()
   tips = {label: tip for tip, label in labels.items()}
   return tips

def be_symbol_math(label):
   labels = give_labels_symbol_math()
   return (label in labels)

def be_box_math(label):
   labels = give_labels_bracket_math()
   return (label in labels)

def get_tip_right_math(tip_left):
   assert(len(tip_left) == 1)
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
   label = get_label_math(tip_left)
   if (label == "START_ROUND"):
      tip_right = get_tip_math("MIDDLE_ROUND")
   if (label == "START_SQUARE"):
      tip_right = get_tip_math("MIDDLE_SQUARE")
   if (label == "START_CURLY"):
      tip_right = get_tip_math("MIDDLE_CURLY")
   if (label == "START_ANGLE"):
      tip_right = get_tip_math("MIDDLE_ANGLE")
   if (label in {"SANS", "ROMAN", "MONO"}):
      tip_right = None
   return tip_right

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def get_label_pseudo(tip):
  labels = get_labels()
  label = labels.get(tip)
  return label

def get_tip_pseudo(label):
  tips = get_tips()
  tip = tips.get(label)
  return tip

def give_labels_letter_pseudo():
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
   }
   return labels

def give_labels_sign_pseudo():
   labels = {
      "PLAIN": '.',
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
   }
   return labels

def give_labels_bracket_pseudo():
   labels = {
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
   return labels

def give_labels_pseudo():
   labels = {
      **give_labels_letter_pseudo(),
      **give_labels_sign_pseudo(),
      **give_labels_bracket_pseudo(),
   }
   return labels

def give_tips_letter_pseudo():
   labels = give_labels_letter_pseudo()
   tips = {label: tip for tip, label in labels.items()}
   return tips

def give_tips_sign_pseudo():
   labels = give_labels_sign_pseudo()
   tips = {label: tip for tip, label in labels.items()}
   return tips

def give_tips_bracket_pseudo():
   labels = give_labels_bracket_pseudo()
   tips = {label: tip for tip, label in labels.items()}
   return tips

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

