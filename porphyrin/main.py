#! /usr/bin/env python3

import os

import organ as ORGAN
import stem as STEM
import leaf as LEAF
import caution as CAUTION

def make(folder_in, folder_out):
   EXTENSION = ".ppr"
   things_in = os.scandir(folder_in)
   for thing_in in things_in:
      name_in = thing.name
      path_in = os.path.join(folder_in, name_in)
      if not thing_in.is_file():
         print("Warning: ", name_in, " is not a file.")
         continue
      if not path_in.endswith(EXTENSION):
         print("Warning: file ", name_in, " does not end in \"", EXTENSION, "\".")
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
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def get_mark_right(self, mark_left):
   assert(len([glyph for glyph in mark_left]) == 1)
   tip = mark_left[0]
   mark_right = mark_left
   comment_left = get_tip("COMMENT_LEFT")
   comment_right = get_tip("COMMENT_RIGHT")
   if (tip == comment_left):
      mark_right = mark_left.translate(
         mark_left.maketrans(comment_left, comment_right)
      )
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
  labels = give_labels()
  label = labels.get(tip)
  return label

def get_tip(label):
  tips = give_labels()
  tip = tips.get(label)
  return tip

def give_labels(self):
   labels = {
      '@': "SERIF_NORMAL",
      '%': "SERIF_ITALIC",
      '#': "SERIF_BOLD",
      '$': "SANS_NORMAL",
      '&': "SANS_BOLD",
      '+': "MONOSPACE",
      '*': "MATH_NEW",
      '^': "MATH_OLD",
      '=': "SECTION",
      '/': "STANZA",
      '\"': "TABLE",
      '|': "IMAGE",
      '_': "SPACE",
      '\'': "NEWLINE",
      '~': "BREAK",
      '\\': "LINK",
      '<': "COMMENT_LEFT",
      '>': "COMMENT_RIGHT",
   }
   return labels

def give_tips():
   labels = give_labels()
   tips = {label: tip for tip, label in labels.items()}
   return tips

def be_bough(label):
   labels = set([
      "SECTION", "STANZA", "TABLE",
      "IMAGE", "BREAK",
   ])
   return (label in labels)

def be_leaf(label):
   labels = set([
      "SERIF_NORMAL", "SERIF_ITALIC", "SERIF_BOLD",
      "SANS_NORMAL", "SANS_BOLD",
      "MATH", "PSEUDO", "CODE",
      "LINK",
   ])
   return (label in labels)






# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
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

def give_labels_math():
   labels = {
      "PLAIN": '.',
      "BOLD": '#',
      "BLACK": '&',
      "CURSIVE": '@',
      "EXTENDED": '$',
      "ABSTRACTION": '%',
      "ARITHMETICS": '+',
      "OPERATION": '^',
      "SHAPE": '*',
      "LINE": '-',
      "ARROW_LEFT": '{',
      "ARROW_RIGHT": '}',
      "EQUIVALENCE": '=',
      "ORDER_LEFT": '<',
      "ORDER_RIGHT": '>',
   }
   return labels

def give_tips_math():
  labels = give_labels_math()
  tips = {label: tip for tip, label in labels.items()}
  return tips

def be_letter_math(label):
   labels = set([
      "PLAIN", "BOLD", "EXTENDED",
      "BLACK", "CURSIVE",
   ])
   return (label in labels)

def be_sign_math(label):
   labels = set([
      "ABSTRACTION", "ARITHMETICS", "OPERATION", "SHAPE",
      "LINE", "ARROW_LEFT", "ARROW_RIGHT",
      "EQUIVALENCE", "ORDER_LEFT", "ORDER_RIGHT",
   ])
   return (label in labels)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def get_label_pseudo(tip):
  labels = get_labels()
  label = labels.get(tip)
  return label

def get_tip_pseudo(label):
  tips = get_tips()
  tip = tips.get(label)
  return tip

def give_labels_pseudo():
   labels = {
      "PLAIN": '.',
      "BOLD": ',',
      "ROMAN": ';',
      "SANS": ':',
      "EXTENDED": '-',
      "EXTENDED_BOLD": '=',
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
      "KANJI_FIRST": '!',
      "KANJI_SECOND": '?',
      "START_FIRST": '(',
      "START_SECOND": '[',
      "START_THIRD": '{',
      "START_FOURTH": '<',
      "STOP_FIRST": ')',
      "STOP_SECOND": ']',
      "STOP_THIRD": '}',
      "STOP_FOURTH": '>',
      "CUT_FIRST": '/',
      "CUT_SECOND": '|',
      "CUT_THIRD": '\\',
   }
   return labels

def give_tips_pseudo():
  labels = give_labels_pseudo()
  tips = {label: tip for tip, label in labels.items()}
  return tips

def be_letter_pseudo(label):
   labels = set([
      "PLAIN", "BOLD",
      "GREEK", "CYRILLIC",
      "BLACK", "CURSIVE",
   ])
   return (label in labels)

def be_kana_pseudo(label):
   labels = set([
      "KANA_FIRST", "KANA_SECOND", "KANA_THIRD",
      "KANA_FOURTH", "KANA_FIFTH", "KANA_SIXTH",
      "KANA_SEVENTH", "KANA_EIGHTH", "KANA_NINTH",
   ])
   return (label in labels)

def be_kanji_pseudo(label):
   labels = set([
      "KANJI_FIRST", "KANJI_SECOND",
   ])
   return (label in labels)

def be_bracket_pseudo(label):
   labels = set([
      "START_FIRST",
      "START_SECOND",
      "START_THIRD",
      "START_FOURTH",
      "STOP_FIRST",
      "STOP_SECOND",
      "STOP_THIRD",
      "STOP_FOURTH",
      "CUT_FIRST",
      "CUT_SECOND",
      "CUT_THIRD",
   ])
   return (label in labels)



