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

class Alternative(ORGAN.Organ):

   def parse(self):
      pass

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Code_kana(ORGAN.Organ):

   def parse(self):
      table_symbol = {}
      table_symbol['~'] = {
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
      first = source[0]
      second = source[1]
      sink = table_symbol.get(first).get(second)
      if (sink == None):
         data = self.get_changed_data()
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      self.sinks[0] = sink

   def write(self):
      return self.sinks[0]

class Code_kanji(ORGAN.Organ):

   def parse(self):
      table_symbol = {}
      table_symbol['!'] = {
         'A': '零', 'B': '壹', 'C': '貳', 'D': '參', 'E': '肆',
      }
      table_symbol['?'] = {
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
      first = source[0]
      second = source[1]
      sink = table_symbol.get(first).get(second)
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

class Traditional(ORGAN.Organ):

   BOLD = 1
   BLACK = 2
   CURSIVE = 3
   EXTENDED = 4
   ABSTRACTION = 11
   EQUIVALENCE = 21
   ARITHMETICS = 22
   OPERATION = 23
   SHAPE = 24
   LINE = 25
   ARROW_LEFT = 31
   ARROW_RIGHT = 32
   ORDER_LEFT = 33
   ORDER_RIGHT = 34
   DIACRITICS = 40
   PAIR = 41
   TRIPLET = 42
   TUPLE = 43
   ROMAN = 50
   SANS = 51
   MONO = 51

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

class Code_letter(ORGAN.Organ):

   def parse(self):
      assert(len(self.source) == 2)
      first = self.source[0]
      second = self.source[1]
      sink = None
      command = None

      if (first == self.PLAIN):
         if (second.islower() or second.isupper()):
            sink = second
         elif (second == self.PLAIN):
            sink = self.PLAIN

      if (first == self.BOLD):
         if (second.islower() or second.isupper()):
            sink = second
         elif (second == self.PLAIN):
            sink = "\\#"

      if (first == self.BLACK):
         if (second.islower):
            sink = write_brace("\\mathbb", second)
         elif (second.isupper):
            sink = write_brace("\\fraktur", second)
         elif (second == self.PLAIN):
            sink = "\\&"

      if (first == self.CURSIVE):
         if (second.islower):
            sink = write_brace("\\mathcal", second)
         elif (second.isupper):
            sink = write_brace("\\mathscr", second)
         elif (second == self.PLAIN):
            sink = "@"

      if (first == self.EXTENDED):
         table_symbol = {
            'a': "\\alpha", 'b': "\\beta",
            # # ...
         }
         if (second.islower() or second.isupper()):
            sink = table_symbol[second]
         elif (second == self.PLAIN):
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

class Code_sign(ORGAN.Organ):


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Code_pair(ORGAN.Organ):

class Code_triplet(ORGAN.Organ):

class Code_tuple(ORGAN.Organ):

class Code_box(ORGAN.Organ):

# # # # # # # # # # # # # # # #

class Code_diacritics(ORGAN.Organ):

class Code_roman(ORGAN.Organ):

class Code_sans(ORGAN.Organ):

class Code_mono(ORGAN.Organ):

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
   table_escape = {
      '<': "&lt;",
      '>': "&gt;",
      '&': "&amp;",
      '\"': "&quote;",
      '\'': "&apos;",
   }
   sink = replace_token(sink, table_escape)
   return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def write_brace(command, *options):
   result = ''
   result += command + ' '
   for option in options:
      result += '{' + option + '}' + ' '
   return result

def give_table_label_traditional():
   table = {
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

def give_table_tip_traditional():
  labels = give_group_label()
  tips = {label: tip for tip, label in labels.items()}
  return tips

def be_letter_traditional():
   group = set([
      "PLAIN", "BOLD", "EXTENDED",
      "BLACK", "CURSIVE",
   ])
   return (label in group)

def be_sign_traditional(label):
   group = set([
      "ABSTRACTION", "ARITHMETICS", "OPERATION", "SHAPE",
      "LINE", "ARROW_LEFT", "ARROW_RIGHT",
      "EQUIVALENCE", "ORDER_LEFT", "ORDER_RIGHT",
   ])
   return (label in group)

def be_symbol_traditional():

