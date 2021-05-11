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
         data = self.get_data_modified()
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      self.sinks[0] = sink

   def write(self):
      return self.sinks[0]

   def find_height():
      return 1

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
         data = self.get_data_modified()
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      self.sinks[0] = sink

   def write(self):
      return self.sinks[0]

   def find_height():
      return 1

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
      label = get_label_math(front)
      PLAIN = give_tips_math("PLAIN")
      sink = None

      if (label == "PLAIN"):
         if (back.islower() or back.isupper()):
            sink = back
         elif (back == PLAIN):
            sink = "."

      if (label == "BOLD"):
         if (back.islower() or back.isupper()):
            sink = back
         elif (back == PLAIN):
            sink = "\\#"

      if (label == "BLACK"):
         if (back.islower()):
            sink = write_brace("\\mathbb", back)
         elif (back.isupper()):
            sink = write_brace("\\fraktur", back)
         elif (back == PLAIN):
            sink = "\\&"

      if (label == "CURSIVE"):
         if (back.islower()):
            sink = write_brace("\\mathcal", back)
         elif (back.isupper()):
            sink = write_brace("\\mathscr", back)
         elif (back == PLAIN):
            sink = "@"

      if (label == "EXTENDED"):
         symbols = {
            'a': "\\alpha", 'b': "\\beta",
            # # ...
         }
         if (back.islower() or back.isupper()):
            sink = symbols[back]
         elif (back == PLAIN):
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

class Math_sign(ORGAN.Organ):

   def write(self):
      return self.sinks[0]

   def find_height():
      return 1

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

