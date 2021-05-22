import organ as ORGAN
import stem as STEM
import caution as CAUTION
import aid as AID

# #    .a  .A  .b  .B  .0  .1  ..
# # &  &a  &A  &b  &B          &.
# # *                  *0  *1  *.
class Math_symbol(ORGAN.Tissue):

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sink = ''

   def write(self):
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

      return self.sinks[0]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # boxes: pair, triplet, tuple

class Math_pair(ORGAN.Tissue):

   def __init__(self, **data):
      self.fill_basic(**data)
      self.tops = []
      self.bottoms = []

   def write(self):
      boxes = []
      cut = AID.get_tip_math("CUT_PAIR")
      source = self.source
      head_left = 0
      head_right = 0
      box = []
      while(head_right <= len(source)):
         tissue, head_right = self.snip_tissue_math(head_left)
         if (source[head_right] == cut):
            boxes.append(box)
            box = []
         else:
            box.append(tissue)

      assert(len(boxes) == 2)
      self.tops = boxes[0]
      self.bottoms = boxes[1]

      result = ''
      top = ''
      for top in self.tops:
         top += top.write()
         top += ' '
      bottom = ''
      for bottom in self.bottoms:
         bottom += top.write()
         bottom += ' '
      result = AID.write_command("\\frac", top, down)
      return result

class Math_triplet(ORGAN.Tissue):

   def __init__(self, **data):
      self.fill_basic(**data)
      self.tops = []
      self.mains = []
      self.bottoms = []

   def write(self):
      boxes = []
      cut = AID.get_tip_math("CUT_PAIR")
      source = self.source
      head_left = 0
      head_right = 0
      box = []
      while(head_right <= len(source)):
         tissue, head_right = self.snip_tissue_math(head_left)
         if (source[head_right] == cut):
            boxes.append(box)
            box = []
         else:
            box.append(tissue)

      assert(len(boxes) == 2)
      self.tops = boxes[0]
      self.mains = boxes[1]
      self.bottoms = boxes[2]

      result = ''
      top = ''
      for top in self.tops:
         top += top.write()
         top += ' '
      main = ''
      for main in self.mains:
         main += main.write()
         main += ' '
      bottom = ''
      for bottom in self.bottoms:
         bottom += top.write()
         bottom += ' '
      result += '{' + main + '}' + ' '
      result += '^{' + top + '}' + ' '
      result += '_{' + down + '}' + ' '
      return result

class Math_tuple(ORGAN.Tissue):

   def __init__(self, **data):
      self.fill_basic(**data)
      self.entries = []

   def write(self):
      boxes = []
      cut = AID.get_tip_math("CUT_PAIR")
      source = self.source
      head_left = 0
      head_right = 0
      box = []
      while(head_right <= len(source)):
         tissue, head_right = self.snip_tissue_math(head_left)
         if (source[head_right] == cut):
            boxes.append(box)
            box = []
         else:
            box.append(tissue)

      assert(len(boxes) == 2)
      self.boxes = boxes

      result = ''
      result += AID.write_command("\\begin", "matrix")
      for entry_self in self.entries:
         entry = ''
         for subentry_self in entry_self:
            entry += subentry_self.write()
            entry += ' '
         result += entry + '\\\\ '
      result += AID.write_command("\\end", "matrix")
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # texts: roman, sans, mono

class Math_roman(ORGAN.Tissue):

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sink = ''

   def write(self):
      self.source
      if not isalnum(self.source):
         data = self.give_data(0, len(source))
         caution = CAUTION.Allowing_only_alphabets(**data)
         caution.panic()
      self.sink = self.source

      result = ''
      command = '\\mathrm'
      result += write_command(command, self.sink)
      return result

class Math_sans(ORGAN.Tissue):

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sink = ''

   def write(self):
      self.source
      if not isalnum(self.source):
         data = self.give_data(0, len(source))
         caution = CAUTION.Allowing_only_alphabets(**data)
         caution.panic()
      self.sink = self.source

      result = ''
      command = '\\mathsf'
      result += write_command(command, self.sink)
      return result

class Math_mono(ORGAN.Tissue):

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sink = ''

   def write(self):
      self.source
      if not isalnum(self.source):
         data = self.give_data(0, len(source))
         caution = CAUTION.Allowing_only_alphabets(**data)
         caution.panic()
      self.sink = self.source

      result = ''
      command = '\\mathtt'
      result += write_command(command, self.sink)
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# #    .a  .A  .b  .B  .0  .1  ..
# # &  &a  &A  &b  &B          &.
# # *                  *0  *1  *.
class Pseudo_symbol(ORGAN.Tissue):

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
      self.sinks = sink

      return self.sinks

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Pseudo_bracket(ORGAN.Tissue):


   def __init__(self, **data):
      self.fill_basic(**data)
      self.level = 0

   def write(self):
      result = ''
      result += self.sink + ' '
      tag = "sub"
      result += write_element(
         content = self.level,
         tag = tag,
      )
      result = ' '
      return result

