from pdb import set_trace

from .organ import Leaf
from . import aid as AID

# #  &  &a  &A  &b  &B
# #  *                  *0  *1
# #     .a  .A  .b  .B  .0  .1  ..  &.  *.
class Pseudo_letter(Leaf):

   KIND = "pseudo-sign"

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Pseudo_sign(Leaf):

   KIND = "pseudo-sign"

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
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

      assert (len(self.source) == 2)
      tip = self.source[0]
      tail = self.source[1]
      sink = symbols.get(tip).get(tail)
      if not sink:
         data = self.give_data()
         from .caution import Token_invalid_as_symbol as creator
         creator(**data).panic()

      result = write_element(
            cut = '',
            content = sink,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Pseudo_round(Leaf):

   KIND = "pseudo-round"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.level = 0

   def write(self):
      sink += '('
      sink += write_element(
         cut = '',
         content = self.level,
         tag = "sub",
      )

      sink += ')'
      sink += write_element(
         cut = '',
         content = self.level,
         tag = "sub",
      )
      result += ' '
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Pseudo_square(Leaf):
   pass

class Pseudo_curly(Leaf):
   pass

class Pseudo_serif(Leaf):
   pass

class Pseudo_sans(Leaf):
   pass

class Pseudo_mono(Leaf):
   pass

class Pseudo_tiny(Leaf):
   pass
