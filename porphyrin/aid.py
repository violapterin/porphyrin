import os
from pdb import set_trace

def convert(path_in, path_out):
   from .stem import Document
   handle_in = open(path_in, mode = 'r')
   source = handle_in.read()
   handle_in.close()
   document = Document(source = source)
   sink = document.write()
   handle_out = open(path_out, mode = 'w')
   handle_out.write(sink)
   handle_out.close()

def make_all(folder_in, folder_out):
   make("ALL", folder_in, folder_out)

def make_new(folder_in, folder_out):
   make("NEW", folder_in, folder_out)

def make(flag, folder_in, folder_out):
   extension_in = ".ppr"
   extension_out = ".txt"
   things_in = os.scandir(folder_in)
   for thing_in in things_in:
      name_in = thing_in.name
      path_in = os.path.join(folder_in, name_in)
      if not thing_in.is_file():
         print(f"Warning: {name_in} is not a file.")
         continue
      if not path_in.endswith(extension_in):
         print(
            f"Warning: file {name_in}",
            f"does not end in \"{extension_in}\".",
         )
         continue
      name_out = name_in.replace(extension_in, extension_out)
      name_out = name_in.replace("in", "out")
      path_out = os.path.join(folder_out, name_out)
      if not (flag == "ALL"):
         if os.path.isfile(path_out):
            time_in = thing_in.stat().st_ctime
            time_out = os.path.getmtime(path_out)
            if time_in < time_out:
               continue
      print(f"Trying to convert {path_in} to {path_out}:")
      convert(path_in, path_out) 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def get_mark_right(mark_left):
   assert (len(list(set(mark_left))) == 1)
   tip_left = mark_left[0]
   label_left = get_label(mark_left[0])
   if not be_start_asymmetry(label_left):
      mark_right = mark_left
      return mark_left

   mark_right = mark_left
   if (label_left == "DEFINITION_LEFT"):
      tip_right = get_tip("DEFINITION_RIGHT")
   elif (label_left == "COMMENT_LEFT"):
      tip_right = get_tip("COMMENT_RIGHT")
   mark_right = mark_left.replace(tip_left, tip_right)
   return mark_right

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def write_element(cut = '\n', **data):
   assert ("content" in data)
   assert ("tag" in data)
   sink = ''
   sinks_left = ['<' + data["tag"]]
   if ("attributes" in data):
      attributes = data["attributes"]
      values = data["values"]
      assert (len(values) == len(attributes))
      for index in range(len(attributes)):
         sinks_left.append(
            attributes[index] +
            "=\"" + values[index] + '\"'
         )
   sinks_left[-1] += '>'
   sink_left = unite(sinks_left)
   sink_middle = cut + data["content"] + cut
   sink_right = "</" + data["tag"] + '>'
   sink += sink_left
   if (sink_middle.strip(" \n\t")):
      sink += sink_middle
   sink += sink_right
   return sink

def unite(sources, cut = ' '):
   for index in range(len(sources)):
      sources[index] = (sources[index]).strip()
   sink = cut.join(sources)
   return sink
   

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def be_bough(kind):
   kinds = {
      "paragraphs",
      "lines",
      "rows",
   }
   return (kind in kinds)

def be_stem(kind):
   kinds = {
      "paragraph",
      "line",
      "row",
   }
   return (kind in kinds)

def be_frond(kind):
   kinds = {
      "phrase",
      "verse",
      "cell",
   }
   return (kind in kinds)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def give_labels():
   labels = {
      '=': "PARAGRAPHS",
      '/': "LINES",
      '\"': "ROWS",
      '|': "IMAGE",
      '`': "IDENITFIER",
      '~': "BREAK",
      '<': "COMMENT_LEFT",
      '>': "COMMENT_RIGHT",
      '{': "DEFINITION_LEFT",
      '}': "DEFINITION_RIGHT",
      #
      '@': "SERIF_ROMAN",
      '%': "SERIF_ITALIC",
      '#': "SERIF_BOLD",
      '$': "SANS_ROMAN",
      '&': "SANS_BOLD",
      '+': "mono",
      '*': "PSEUDO",
      '^': "MATH",
      '\\': "LINK",
      '_': "SPACE",
      '\'': "NEWLINE",
   }
   return labels

def give_tips():
   labels = give_labels()
   tips = {label: tip for tip, label in labels.items()}
   return tips

def get_label(tip):
   labels = give_labels()
   label = labels.get(tip)
   return label

def get_tip(label):
   tips = give_tips()
   tip = tips.get(label)
   return tip

def be_start_bough(label):
   labels = {
      "PARAGRAPHS",
      "LINES",
      "ROWS",
      "IMAGE",
      "BREAK",
      "COMMENT_LEFT",
   }
   return (label in labels)

def be_start_leaf(label):
   labels = {
      "SERIF_ROMAN",
      "SERIF_ITALIC",
      "SERIF_BOLD",
      "SANS_ROMAN",
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

def be_start_asymmetry(label):
   labels = {
      "DEFINITION_LEFT",
      "COMMENT_LEFT",
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
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def tune_text(source):
   glyphs_space = set([' ', '\t', '\n'])
   glyphs_mark = set([])
   glyphs_mark.add(get_tip("SERIF_ROMAN"))
   glyphs_mark.add(get_tip("SERIF_ITALIC"))
   glyphs_mark.add(get_tip("SERIF_BOLD"))
   glyphs_mark.add(get_tip("SANS_ROMAN"))
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
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def get_tip_right_math(tip_left):
   assert (len(tip_left) == 1)
   tip_right = ''
   label_left = get_label_math(tip_left)
   if not be_start_asymmetry(label_left):
      tip_right = tip_left
      return tip_right
   if (label_left == "START_PAIR"):
      tip_right = get_tip_math("STOP_PAIR")
   elif (label_left == "START_TRIPLET"):
      tip_right = get_tip_math("STOP_TRIPLET")
   elif (label_left == "START_TUPLE"):
      tip_right = get_tip_math("STOP_TUPLE")
   elif (label_left == "ARROW_LEFT"):
      tip_right = get_tip_math("ARROW_RIGHT")
   elif (label_left == "ORDER_LEFT"):
      tip_right = get_tip_math("ORDER_RIGHT")
   return tip_right

def get_tip_middle_math(tip_left):
   assert (len(tip_left) == 1)
   tip_middle = ''
   label_left = get_label_math(tip_left)
   if (label_left == "START_PAIR"):
      tip_middle = get_tip_math("CUT_PAIR")
   if (label_left == "START_TRIPLET"):
      tip_middle = get_tip_math("CUT_TRIPLET")
   if (label_left == "START_TUPLE"):
      tip_middle = get_tip_math("CUT_TUPLE")
   return tip_middle

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def write_latex(command, *items):
   sink = ''
   sinks = []
   sinks.append(command)
   for item in items:
      sinks.append('{' + item + '}')
   sink = unite(sinks)
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

def give_tips_math():
   labels = give_labels_math()
   tips = {label: tip for tip, label in labels.items()}
   return tips

def get_label_math(tip):
   labels = give_labels_math()
   label = labels.get(tip)
   return label

def get_tip_math(label):
   tips = give_tips_math()
   tip = tips.get(label)
   return tip

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
      "SERIF",
      "SANS",
      "MONO",
      "CHECK",
   }
   return (label in labels)

def be_start_asymmetry_math(label):
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

def be_not_lateral_math(label):
   labels = {
      "BOLD",
      "BLACK",
      "CURSIVE",
      "GREEK",
      "EQUIVALENCE_ONE",
      "EQUIVALENCE_TWO",
   }
   return (label in labels)

def be_start_symbol_math(label):
   being = (
      (label == "PLAIN")
      or be_start_letter_math(label)
      or be_start_sign_math(label)
   )
   return being

def be_start_math(label):
   being = (
      be_start_symbol_math(label)
      or be_start_box_math(label)
   )
   return being

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def get_tip_right_pseudo(tip_left):
   assert (len(tip_left) == 1)
   label_left = get_label_pseudo(tip_left)
   tip_right = ''
   if not be_start_asymmetry(label_left):
      tip_right = tip_left
      return tip_right
   if (label_left == "START_ROUND"):
      tip_right = get_tip_pseudo("STOP_ROUND")
   elif (label_left == "START_SQUARE"):
      tip_right = get_tip_pseudo("STOP_SQUARE")
   elif (label_left == "START_CURLY"):
      tip_right = get_tip_pseudo("STOP_CURLY")
   elif (label_left == "START_ANGLE"):
      tip_right = get_tip_pseudo("STOP_ANGLE")
   elif (label_left == "QUOTE_SINGLE"):
      tip_right = tip_left
   elif (label_left == "QUOTE_DOUBLE"):
      tip_right = tip_left
   return tip_right

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
      "START_REMARK": '<',
      "STOP_REMARK": '>',
      "SERIF": '\"',
      "SANS": '\'',
      "MONO": '`',
      "CHECK": '_',
   }
   return labels

def give_tips_pseudo():
   labels = give_labels_pseudo()
   tips = {label: tip for tip, label in labels.items()}
   return tips

def get_label_pseudo(tip):
   labels = give_labels_pseudo()
   label = labels.get(tip)
   return label

def get_tip_pseudo(label):
   tips = give_tips_pseudo()
   tip = tips.get(label)
   return tip

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
   being = (
      be_start_letter_pseudo(label)
      or be_start_sign_pseudo(label)
   )
   return being

def be_start_pseudo(label):
   being = (
      be_start_symbol_pseudo(label)
      or be_start_box_pseudo(label)
   )
   return being
