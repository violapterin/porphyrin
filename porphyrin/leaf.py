import organ as ORGAN
import stem as STEM
import caution as CAUTION

class Serif_roman(ORGAN.Organ):

   KIND = "serif-roman"
   TAG = "span"

   def parse(self):
      self.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_element(
            content = sink,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      return result

class Serif_italic(ORGAN.Organ):

   KIND = "serif-italic"
   TAG = "em"

   def parse(self):
      self.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_element(
            content = sink,
            tag = tag,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      result = self.write_element(result, TAG)
      return result

class Serif_bold(ORGAN.Organ):

   KIND = "serif-bold"
   TAG = 'b'

   def parse(self):
      self.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_element(
            content = sink,
            tag = tag,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      result = self.write_element(result, TAG)
      return result

class Sans_roman(ORGAN.Organ):

   KIND = "sans-roman"

   def parse(self):
      self.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_element(
            content = sink,
            tag = tag,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      return result

class Sans_bold(ORGAN.Organ):

   KIND = "sans-bold"
   TAG = 'b'

   def parse(self):
      self.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_element(
            content = sink,
            tag = tag,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      result = self.write_element(result, self.TAG)
      return result

class Mono(ORGAN.Organ):

   KIND = "sans-bold"
   TAG = "pre"

   def parse(self):
      self.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_element(
            content = sink,
            tag = tag,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      result = self.write_element(result, self.TAG)
      return result

class Comment(ORGAN.Organ):

   KIND = "sans-bold"
   TOKEN_LEFT = "<!--"
   TOKEN_RIGHT = "-->"

   def parse(self):
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.split_word(head)
         sinks.append(text)


   def write(self):
      result = ''
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += sink + ' '
      result = self.TOKEN_LEFT + result + self.TOKEN_RIGHT
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Pseudo(ORGAN.Organ):

   def parse(self):
      pass

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Pseudo_kana(ORGAN.Organ):

   def parse(self):
      symbols = {}
      symbols['~'] = {
         '0': 'い', '1': 'ろ', '2': 'は', '3': 'に', '4': 'ほ',
         '5': 'へ', '6': 'と', '7': 'ち', '8': 'り', '9': 'ぬ',
      }
      # # い ろ は に ほ へ と ち り ぬ 
      # # る を わ か よ た れ そ つ ね
      # # な ら む う ゐ の お く や ま
      # # け ふ こ え て あ さ き ゆ め
      # # み し ゑ ひ も
      # # ... ...

      assert(len(source) == 2)
      front = source[0]
      back = source[1]
      sink = symbols.get(front).get(back)
      if (sink == None):
         data = self.get_changed_data()
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      self.sinks[0] = sink

   def write(self):
      return self.sinks[0]

class Pseudo_kanji(ORGAN.Organ):

   def parse(self):
      symbols = {}
      symbols['!'] = {
         'A': '零', 'B': '壹', 'C': '貳', 'D': '參', 'E': '肆',
      }
      symbols['?'] = {
         # # ... ...
      }

      # # ... ...
      # # 零壹貳參肆伍陸柒捌玖
      # # 甲乙丙丁戊己庚辛壬癸
      # # 子丑寅卯辰巳午未申酉戌亥
      # # 乾兌離震巽坎艮坤
      # # 鼠牛虎兔龍蛇馬羊猴雞狗豬
      # # 
      # # 幫滂並明非敷奉微
      # # 端透定泥知澈澄娘
      # # 精清從心邪照穿床審禪
      # # 見溪群疑影曉匣喻來日
      # # 通江止遇蟹臻山效
      # # 果假宕梗曾流深咸


      assert(len(source) == 2)
      front = source[0]
      back = source[1]
      sink = symbols.get(front).get(back)
      if (sink == None):
         data = self.get_changed_data()
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      self.sinks[0] = sink

   def write(self):
      return self.sinks[0]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Math(ORGAN.Organ):

   def parse(self):
      pass

   def write(self):
      pass

   # # # # # # # # # # # # # # # #

   def snip_tissue(self, head_left):
      tissue = None
      while head <= len(self.source) - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def give_group_label_tissue():
      return {
         '[': self.
      }

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# #     a  A  b  B  0  1  .
# # .  .a .A .b .B .0 .1 ..
# # &  &a &A &b &B       &.
# # *              *0 *1 *.

class Math_letter(ORGAN.Organ):

   def parse(self):
      assert(len(self.source) == 2)
      front = self.source[0]
      back = self.source[1]
      sink = None
      command = None

      if (front == self.PLAIN):
         if (back.islower() or back.isupper()):
            sink = back
         elif (back == self.PLAIN):
            sink = self.PLAIN

      if (front == self.BOLD):
         if (back.islower() or back.isupper()):
            sink = back
         elif (back == self.PLAIN):
            sink = "\\#"

      if (front == self.BLACK):
         if (back.islower):
            sink = write_brace("\\mathbb", back)
         elif (back.isupper):
            sink = write_brace("\\fraktur", back)
         elif (back == self.PLAIN):
            sink = "\\&"

      if (front == self.CURSIVE):
         if (back.islower):
            sink = write_brace("\\mathcal", back)
         elif (back.isupper):
            sink = write_brace("\\mathscr", back)
         elif (back == self.PLAIN):
            sink = "@"

      if (front == self.EXTENDED):
         symbols = {
            'a': "\\alpha", 'b': "\\beta",
            # # ...
         }
         if (back.islower() or back.isupper()):
            sink = symbols[back]
         elif (back == self.PLAIN):
            sink = "\\$"

      if (sink == None):
         data = self.get_changed_data()
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      else:
         self.sinks.append(sink)

   def write(self):
      return self.sinks[0]

   def find_height():
      return 1

class Math_sign(ORGAN.Organ):


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_pair(ORGAN.Organ):

class Math_triplet(ORGAN.Organ):

class Math_tuple(ORGAN.Organ):

class Math_box(ORGAN.Organ):

# # # # # # # # # # # # # # # #

class Math_diacritics(ORGAN.Organ):

class Math_roman(ORGAN.Organ):

class Math_sans(ORGAN.Organ):

class Math_mono(ORGAN.Organ):

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
      "BLACK": ':',
      "CURSIVE": ';',
      "GREEK": '-',
      "CYRILLIC": '=',
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

