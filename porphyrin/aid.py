import os

def get_mark_right(mark_left):
   label = get_label(mark_left[0])
   considered = {"DEFINITION_LEFT", "COMMENT_LEFT"}
   if (label not in considered):
      return mark_left

   mark_right = mark_left
   if (label == "DEFINITION_LEFT"):
      tip_left = get_tip("DEFINITION_LEFT")
      tip_right = get_tip("DEFINITION_RIGHT")
   if (label == "COMMENT_LEFT"):
      tip_left = get_tip("COMMENT_LEFT")
      tip_right = get_tip("COMMENT_RIGHT")
   mark_right = mark_right.replace(tip_left, tip_right)
   return mark_right

def write_element(**data):
   assert("content" in data)
   assert("tag" in data)
   enter = ''
   if ('\n' in data["content"]): enter = '\n'

   sink = '<' + data["tag"] + ' '
   if ("attributes" in data):
      attributes = data["attributes"]
      values = data["values"]
      assert(len(values) == len(attributes))
      size = len(attributes)
      for index in range(size):
         sink += ' '
         sink += data["attributes"][index]
         sink += "=\"" + data["values"][index] + "\" "
   sink += "> "
   sink += enter + data["content"] + ' ' + enter
   sink += "</" + data["tag"] + '>'
   return sink


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def give_labels():
   labels = {
      '@': "SERIF_NORMAL",
      '%': "SERIF_ITALIC",
      '#': "SERIF_BOLD",
      '$': "SANS_NORMAL",
      '&': "SANS_BOLD",
      '+': "mono",
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
   return labels

def give_tips(tip):
   labels = give_labels()
   tips = {label: tip for tip, label in labels}
   return tips

def get_label(tip):
   labels = give_labels()
   label = labels.get(tip)
   return label

def get_tip(label):
   tips = give_tips()
   tip = tips.get(label)
   return label

def be_start_bough(label):
   labels = {
      "PARAGRAPHS",
      "LINES",
      "ROWS",
      "IMAGE",
      "BREAK",
   }
   return (label in labels)

def be_start_leaf(label):
   labels = {
      "SERIF_NORMAL",
      "SERIF_ITALIC",
      "SERIF_BOLD",
      "SANS_NORMAL",
      "SANS_BOLD",
      "MONO",
      "PSEUDO",
      "MATH",
      "LINK",
      "COMMENT_LEFT",
      "DEFINITION_LEFT",
      "IDENITFIER",
   }
   return (label in labels)

def be_start_macro(label):
   labels = {
      "IDENITFIER",
      "DEFINITION_LEFT",
   }
   return (label in labels)

def be_hollow_leaf(label):
   labels = {
      "SPACE",
      "NEWLINE",
   }
   return (label in labels)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def tune_text(source):
   glyphs_space = set([' ', '\t', '\n'])
   glyphs_mark = set([])
   glyphs_mark.add(get_tip("SERIF_NORMAL"))
   glyphs_mark.add(get_tip("SERIF_ITALIC"))
   glyphs_mark.add(get_tip("SERIF_BOLD"))
   glyphs_mark.add(get_tip("SANS_NORMAL"))
   glyphs_mark.add(get_tip("SANS_BOLD"))
   glyphs_mark.add(get_tip("COMMENT_LEFT"))
   glyphs_mark.add(get_tip("COMMENT_RIGHT"))

   sink = remove_token(glyphs_mark, source)
   sink = erase_token(glyphs_space, sink)
   return sink

def tune_code(source):
   glyphs_space = set([' ', '\t', '\n'])
   sink = erase_token(glyphs_space, source)
   return sink

def tune_comment(source):
   escapes = {
      '----': '-',
      '---': '-',
      '--': '-',
   }
   sink = replace_token(escapes, source)
   return sink

def tune_hypertext(source):
   escapes = {
      '<': "&lt;",
      '>': "&gt;",
      '&': "&amp;",
      '\"': "&quote;",
      '\'': "&apos;",
   }
   sink = replace_token(escapes, source)
   return sink

def remove_token(tokens, source):
   sink = source
   for token in tokens:
      sink = sink.replace(token, '')
   return sink

def erase_token(tokens, source):
   sink = source
   for token in tokens:
      sink = sink.replace(token, ' ')
   ' '.join(sink.split())
   return sink

def replace_token(tokens_out, source):
   sink = source
   for token_in in tokens_out:
      sink = sink.replace(token_in, tokens_out[token_in])
   return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def write_latex(command, *items):
   sink = ''
   sink += command + ' '
   for item in items:
      sink += '{' + item + '}' + ' '
   return sink

def give_alphabets_upper():
   alphabets = (
      'A', 'B', 'C',
      'D', 'E', 
      'F', 'G', 'H', 
      'I', 'J', 'K', 
      'L', 'M', 'N', 
      'O', 'P', 'Q', 
      'R', 'S', 'T',
      'U', 'V', 'W',
      'X', 'Y', 'Z',
   )
   return alphabets

def give_alphabets_lower():
   alphabets = give_alphabets_upper().lower()
   return alphabets

def give_digits():
   digits = (
      '0', '1', '2', '3', '4',
      '5', '6', '7', '8', '9',
   )
   return digits

def get_table_sign(targets):
   digits = give_digits()
   table = dict(zip(digits, targets))
   return table

def get_table_upper(targets):
   table = dict(zip(give_alphabets_upper(), targets))
   return table

def get_table_lower(targets):
   table = dict(zip(give_alphabets_lower(), targets))
   return table

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def give_labels_math():
   labels = {
      '.': "PLAIN",
      '#': "BOLD",
      '&': "BLACK",
      '@': "CURSIVE",
      '$': "GREEK",
      '!': "ACCENT_ONE",
      '?': "ACCENT_TWO",
      #
      '%': "ABSTRACTION",
      '/': "LINE",
      '+': "OPERATION_ONE",
      '-': "OPERATION_TWO",
      '*': "OPERATION_THREE",
      '=': "EQUIVALENCE_ONE",
      '~': "EQUIVALENCE_TWO",
      '^': "ARROW_MIDDLE",
      '\\': "ARROW_LEFT",
      '|': "ARROW_RIGHT",
      '<': "ORDER_LEFT",
      '>': "ORDER_RIGHT",
      #
      '(': "START_PAIR",
      ',': "CUT_PAIR",
      ')': "STOP_PAIR",
      '[': "START_TRIPLET",
      ':': "CUT_TRIPLET",
      ']': "STOP_TRIPLET",
      '{': "START_TUPLE",
      '}': "STOP_TUPLE",
      ';': "CUT_TUPLE",
      '\'': "SERIF" ,
      '\"': "SANS",
      '`': "MONO",
      '_': "CHECK",
   }
   return labels

def give_tips_math(tip):
   labels = give_labels_math()
   tips = {label: tip for tip, label in labels}
   return tips

def get_label_math(tip):
   labels = give_labels_math()
   label = labels.get(tip)
   return label

def get_tip_math(label):
   tips = give_tips_math()
   tip = tips.get(label)
   return label

def be_start_letter_math(label):
   labels = {
      "ESCAPE",
      "BOLD",
      "BLACK",
      "CURSIVE",
      "GREEK",
   }
   return (label in labels)

def be_start_sign_math(label):
   labels = {
      "ESCAPE",
      "ABSTRACTION",
      "ARITHMETICS",
      "OPERATION",
      "SHAPE",
      "LINE",
      "ARROW",
      "EQUIVALENCE",
      "ORDER_LEFT",
      "ORDER_RIGHT",
   }
   return (label in labels)

def be_start_box_math(label):
   labels = {
      "START_PAIR",
      "START_TRIPLET",
      "START_TUPLE",
      "START_SERIF",
      "START_SANS",
      "START_MONO",
   }
   return (label in labels)

def be_start_bracket_math(label):
   labels = {
      "START_PAIR",
      "START_TRIPLET",
      "START_TUPLE",
      "ARROW_LEFT",
      "ORDER_LEFT",
   }
   return (label in labels)


def be_start_accent_math(label):
   labels = {
      "ACCENT_ONE",
      "ACCENT_TWO",
   }
   return (label in labels)

def be_start_symbol_math(label):
   being = (be_start_letter_math(label) or be_start_sign_math(label))
   return being

def be_start_math(label):
   being = (be_start_symbol_math(label) or be_start_box_math(label))
   return being

def get_tip_right_math(tip_left):
   assert(len(tip_left) == 1)
   tip_right = ''
   label = get_label_math(tip_left)
   if (label == "START_ROUND"):
      tip_right = get_tip_math("STOP_ROUND")
   if (label == "START_SQUARE"):
      tip_right = get_tip_math("STOP_SQUARE")
   if (label == "START_CURLY"):
      tip_right = get_tip_math("STOP_CURLY")
   if (label == "ARROW_LEFT"):
      tip_right = get_tip_math("ARROW_RIGHT")
   if (label == "ORDER_LEFT"):
      tip_right = get_tip_math("ORDER_RIGHT")
   if (label in {"SERIF", "SANS", "MONO", "CHECK"}):
      tip_right = tip_left
   return tip_right

def get_tip_middle_math(tip_left):
   assert(len(tip_left) == 1)
   tip_middle = ''
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

def give_labels_pseudo():
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
      "STOP_ROUND": ')',
      "CUT_ROUND": '/',
      "START_SQUARE": '[',
      "CUT_SQUARE": '\\',
      "STOP_SQUARE": ']',
      "START_CURLY": '{',
      "CUT_CURLY": '|',
      "STOP_CURLY": '}',
      "START_COMMENT": '<',
      "STOP_COMMENT": '>',
      "SERIF": '\"',
      "SERIF": '\'',
      "SERIF": '`',
      "SANS": '_',
   }
   return labels

def give_tips_pseudo(tip):
   labels = give_labels_pseudo()
   tips = {label: tip for tip, label in labels}
   return tips

def get_label_pseudo(tip):
   labels = give_labels_pseudo()
   label = labels.get(tip)
   return label

def get_tip_pseudo(label):
   tips = give_tips_pseudo()
   tip = tips.get(label)
   return label

def be_start_letter_pseudo(label):
   labels = {
      "PLAIN",
      "BOLD",
      "SERIF",
      "SERIF_BLACK",
      "SANS",
      "SANS_BLACK",
      "GREEK",
      "GREEK_BOLD",
      "KANJI_FIRST",
      "KANJI_SECOND",
   }
   return (label in labels)

def be_start_sign_pseudo(label):
   labels = {
      "KANA_ZEROTH",
      "KANA_FIRST",
      "KANA_SECOND",
      "KANA_THIRD",
      "KANA_FOURTH",
      "KANA_FIFTH",
      "KANA_SIXTH",
      "KANA_SEVENTH",
      "KANA_EIGHTH",
      "KANA_NINTH",
   }
   return (label in labels)

def be_start_bracket_pseudo(label):
   labels = {
      "START_ROUND",
      "START_SQUARE",
      "START_CURLY",
      "START_COMMENT",
      "SERIF",
      "SANS",
      "MONO",
      "CHECK",
   }
   return (label in labels)

def be_start_symbol_pseudo(label):
   being = (be_start_letter_pseudo(label) or be_start_sign_pseudo(label))
   return being

def be_start_pseudo(label):
   being = (be_start_symbol_pseudo(label) or be_start_box_pseudo(label))
   return being

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

