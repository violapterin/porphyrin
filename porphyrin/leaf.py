import organ as ORGAN
import stem as STEM
import caution as CAUTION
import aid as AID

class Serif_roman(Leaf):

   KIND = "serif-roman"
   TAG = "span"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []
      self.address = ''

   def parse(self):
      AID.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.snip_tissue_text(head)
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

class Serif_italic(Leaf):

   KIND = "serif-italic"
   TAG = "em"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []
      self.address = ''

   def parse(self):
      AID.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.snip_tissue_text(head)
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
      result = AID.write_element(result, TAG)
      return result

class Serif_bold(Leaf):

   KIND = "serif-bold"
   TAG = 'b'

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []
      self.address = ''

   def parse(self):
      AID.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.snip_tissue_text(head)
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
      result = AID.write_element(result, TAG)
      return result

class Sans_roman(Leaf):

   KIND = "sans-roman"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []
      self.address = ''

   def parse(self):
      AID.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.snip_tissue_text(head)
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

class Sans_bold(Leaf):

   KIND = "sans-bold"
   TAG = 'b'

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []
      self.address = ''

   def parse(self):
      AID.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.snip_tissue_text(head)
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
      result = AID.write_element(result, self.TAG)
      return result

class Mono(Leaf):

   KIND = "sans-bold"
   TAG = "pre"

   def parse(self):
      AID.tune_text()
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.snip_tissue_text(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if (self.address is not None):
         tag = 'a'
      for sink in self.sinks:
         result += write_element(
            content = sink,
            tag = tag,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      result = AID.write_element(result, self.TAG)
      return result

class Comment(Leaf):

   def parse(self):
      head = 0
      while head <= len(self.source) - 1:
         text, head = self.snip_tissue_text(head)
         text = escape_comment(text)
         sinks.append(text)

   def write(self):
      token_left = "<!--"
      token_right = "-->"
      result = ''
      if (self.address is not None):
         tag = 'a'
      for sink in self.sinks:
         result += sink + ' '
      result = token_left + result + token_right
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Pseudo(Leaf):

   KIND = "serif-roman"
   TAG = "span"

   def parse(self):
      pass

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Pseudo_letter(Leaf):

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
      tip = source[0]
      tail = source[1]
      sink = symbols.get(tip).get(tail)
      if (sink == None):
         data = self.get_data_modified()
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      self.sinks[0] = sink

   def write(self):
      return self.sinks[0]

   def find_height():
      return 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Pseudo_sign(Leaf):

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
      tip = source[0]
      tail = source[1]
      sink = symbols.get(tip).get(tail)
      if (sink == None):
         data = self.get_data_modified()
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      self.sinks[0] = sink

   def write(self):
      return self.sinks[0]

   def find_height():
      return 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Pseudo_bracket(Leaf):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Math(Leaf):

   def parse(self):
      pass

   def write(self):
      pass

   def snip_tissue(self, head_left):
      tissue = None
      while head <= len(self.source) - 1:
         text, head = self.snip_tissue_text(head)
         sinks.append(text)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# #     a   A   b    B   0   1   .
# # .  .a  .A  .b   .B  .0  .1  ..
# # &  &a  &A  &b   &B          &.
# # *                   *0  *1  *.

class Math_letter(Leaf):

   def parse(self):
      assert(len(self.source) == 2)
      tip = self.source[0]
      tail = self.source[1]
      label = get_label_math(tip)
      PLAIN = give_tips_math("PLAIN")
      sink = None

      if (label == "PLAIN"):
         if (tail.islower() or tail.isupper()):
            sink = tail
         elif (tail == PLAIN):
            sink = "."

      if (label == "BOLD"):
         if (tail.islower() or tail.isupper()):
            sink = tail
         elif (tail == PLAIN):
            sink = "\\#"

      if (label == "BLACK"):
         if (tail.islower()):
            sink = write_brace("\\mathbb", tail)
         elif (tail.isupper()):
            sink = write_brace("\\fraktur", tail)
         elif (tail == PLAIN):
            sink = "\\&"

      if (label == "CURSIVE"):
         if (tail.islower()):
            sink = write_brace("\\mathcal", tail)
         elif (tail.isupper()):
            sink = write_brace("\\mathscr", tail)
         elif (tail == PLAIN):
            sink = "@"

      if (label == "GREEK"):
         symbols = {
            'a': "\\alpha", 'b': "\\beta",
            # # ...
         }
         if (tail.islower() or tail.isupper()):
            sink = symbols[tail]
         elif (tail == PLAIN):
            sink = "\\$"

      if (sink == None):
         data = self.get_data_modified()
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      else:
         self.sinks.append(sink)

   def write(self):
      return self.sinks[0]

   def find_height():
      return 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Math_sign(Leaf):

   def write(self):
      return self.sinks[0]

   def find_height():
      return 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Math_bracket(Leaf):

   def write(self):
      return self.sinks[0]

   def find_height():
      return 1


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_pair(Leaf):

class Math_triplet(Leaf):

class Math_tuple(Leaf):

class Math_box(Leaf):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_diacritics(Leaf):

class Math_roman(Leaf):

class Math_sans(Leaf):

class Math_mono(Leaf):

