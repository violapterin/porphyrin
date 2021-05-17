import organ as ORGAN
import stem as STEM
import caution as CAUTION
import aid as AID

class Pseudo_symbol(ORGAN.Tissue):

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sink = ''

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

class Pseudo_bracket(ORGAN.Tissue):


   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# #     a   A   b   B   0   1  ..
# # &  &a  &A  &b  &B          .&
# # *                  *0  *1  .*

class Math_symbol(ORGAN.Tissue):

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sink = ''

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

class Math_bracket(ORGAN.Tissue):

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sinks = []

   def write(self):
      return self.sinks[0]

   def find_height():
      return 1


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # boxes: pair, triplet, tuple

class Math_pair(ORGAN.Tissue):

class Math_triplet(ORGAN.Tissue):

class Math_tuple(ORGAN.Tissue):

class Math_queue(ORGAN.Tissue):

class Math_roman(ORGAN.Tissue):

class Math_sans(ORGAN.Tissue):

class Math_mono(ORGAN.Tissue):

class Math_accent(ORGAN.Tissue):

