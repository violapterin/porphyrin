import organ as ORGAN
import stem as STEM
import caution as CAUTION
import aid as AID

class Math_box(ORGAN.Leaf):

   TAG = "span"

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      sink = None
      source = self.source
      head_left = 0
      head_right = 0
      while(head_right <= len(source)):
         tissue, head_right = self.snip_tissue_math(head_left)

      self.boxes = boxes

      sink = ''
      box = TISSUE.Math_box(**self.get_data)
      content = "\\( " + box.write() + " \\)"
      sink = write_element(
         content = content,
         tag = self.TAG,
         attributes = ["class"],
         values = [self.KIND],
      )
      return sink



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# #    .a  .A  .b  .B  .0  .1  ..
# # &  &a  &A  &b  &B          &.
# # *                  *0  *1  *.
class Math_letter(ORGAN.Leaf):

   def __init__(self, **data):
      self.fill_basic(**data)

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

class Math_sign(ORGAN.Leaf):

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      assert(len(self.source) == 2)
      tip = self.source[0]
      tail = self.source[1]
      label = get_label_math(tip)
      sink = None

      if (label == "SHAPE"):
         if (tail.islower() or tail.isupper()):
            sink = tail
         elif (tail == PLAIN):
            sink = "."


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

class Math_pair(ORGAN.Leaf):

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      sink = None
      cut = AID.get_tip_math("CUT_PAIR")
      source = self.source
      head_left = 0
      head_right = 0
      boxes = []
      while(head_right <= len(source)):
         _, head_right = self.snip_tissue_math(head_left)
         if (source[head_right] == cut):
            box = Math_box(source[head_left: head_right])
            boxes.append(box)
            head_left = head_right
      assert(len(boxes) == 2)
      top, bottom = *boxes

      sink_top = top.write()
      sink_bottom = bottom.write()
      comman = "\\frac"
      sink = AID.write_command(command, sink_top, sink_bottom)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_triplet(ORGAN.Leaf):

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      sink = None
      cut = AID.get_tip_math("CUT_TRIPLET")
      source = self.source
      head_left = 0
      head_right = 0
      boxes = []
      while(head_right <= len(source)):
         _, head_right = self.snip_tissue_math(head_left)
         if (source[head_right] == cut):
            box = Math_box(source[head_left: head_right])
            boxes.append(box)
            head_left = head_right
      assert(len(boxes) == 3)
      main, top, bottom = *boxes

      sink_main = main.write()
      sink_top = top.write()
      sink_bottom = bottom.write()
      sink += '{' + sink_main + '}' + ' '
      sink += '^{' + sink_top + '}' + ' '
      sink += '_{' + sink_bottom + '}' + ' '
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_tuple(ORGAN.Leaf):

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      sink = None
      cut = AID.get_tip_math("CUT_TUPLE")
      source = self.source
      head_left = 0
      head_right = 0
      boxes = []
      while(head_right <= len(source)):
         _, head_right = self.snip_tissue_math(head_left)
         if (source[head_right] == cut):
            box = Math_box(source[head_left: head_right])
            boxes.append(box)
            head_left = head_right
      assert(len(boxes) == 2)
      self.boxes = boxes

      newline = "\\\\"
      sink += AID.write_command("\\begin", "matrix")
      for box in boxes:
         sink += box.write() + newline + ' '
      sink += AID.write_command("\\end", "matrix")
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # texts: serif, sans, mono

class Math_serif(ORGAN.Leaf):

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      command = "\\mathrm"
      sink = AID.write_math_word(command, self.source)
      return sink

class Math_sans(ORGAN.Leaf):

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      command = "\\mathsf"
      sink = AID.write_math_word(command, self.source)
      return sink

class Math_mono(ORGAN.Leaf):

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      command = "\\mathtt"
      sink = AID.write_math_word(command, self.source)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# #    .a  .A  .b  .B  .0  .1  ..
# # &  &a  &A  &b  &B          &.
# # *                  *0  *1  *.
class Pseudo_letter(ORGAN.Leaf):

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

class Pseudo_sign(ORGAN.Leaf):

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

class Pseudo_round(ORGAN.Leaf):


   def __init__(self, **data):
      self.fill_basic(**data)
      self.level = 0

   def write(self):
      sink += '('
      sink += write_element(
         content = self.level,
         tag = "sub",
      )
      sink += ')'
      sink += write_element(
         content = self.level,
         tag = "sub",
      )
      result = ' '
      return result

class Pseudo_square(ORGAN.Leaf):

class Pseudo_curly(ORGAN.Leaf):

class Pseudo_serif(ORGAN.Leaf):

class Pseudo_sans(ORGAN.Leaf):

class Pseudo_mono(ORGAN.Leaf):

class Pseudo_tiny(ORGAN.Leaf):
