import organ as ORGAN
import stem as STEM
import caution as CAUTION
import aid as AID

class Math_box(ORGAN.Leaf):

   KIND = "math"
   TAG = "span"
   OUTSIDE = False

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      content = ''
      head_left = 0
      head_right = 0
      while (head_right < len(self.source)):
         tissue, head_right = self.snip_tissue_math(head_left)
         content += tissue.write()
      sink = write_math_outside(self, content)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# #    .a  .A  .b  .B  .0  .1  ..
# # &  &a  &A  &b  &B          &.
# # *                  *0  *1  *.
class Math_plain(ORGAN.Leaf):

   KIND = "math"
   TAG = "span"
   OUTSIDE = False

   def __init__(self, **data):
      self.fill_basic(**data)
      self.accent = ''

   def write(self):
      tip = self.source[0]
      label = get_label_math(tip)
      symbols = {
         "ABSTRACTION": "\\wp",
         "ARITHMETICS": '+',
         "OPERATION": "\\uparrow",
         "SHAPE": "\\cdot",
         "LINE": '-',
         "ARROW_LEFT": "\\leftarrow",
         "ARROW_MIDDLE": "\\downarrow",
         "ARROW_RIGHT": "\\rightarrow",
         "EQUIVALENCE": '=',
         "ORDER_LEFT": '<',
         "ORDER_RIGHT": '>',
      }
      symbol = symbols.get(label)

      if (symbol == None):
         data = self.get_data()
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      sink = write_math_outside(self, symbol)
      return sink

class Math_letter(ORGAN.Leaf):

   KIND = "math"
   TAG = "span"
   OUTSIDE = False

   def __init__(self, **data):
      self.fill_basic(**data)
      self.accent = ''

   def write(self):
      content = ''
      if (len(self.source) >= 4):
         tip_one = self.source[2]
         tip_two = self.source[3]
         label_one = get_label_math(tip_one)
         label_two = get_label_math(tip_two)
         if (label_one == "ACCENT_ONE"):
            if (label_two == "ACCENT_ONE"):
               self.accent = "\\bar"
            elif (label_two == "ACCENT_TWO"):
               self.accent = "\\hat"
         elif (label_one == "ACCENT_TWO"):
            if (label_two == "ACCENT_ONE"):
               self.accent = "\\breve"
            elif (label_two == "ACCENT_TWO"):
               self.accent = "\\tilde"

      tip = self.source[0]
      tail = self.source[1]
      plain = get_tip_math("PLAIN")

      if (label == "PLAIN"):
         if (tail.islower() or tail.isupper()):
            letter = tail
         elif (tail == plain):
            letter = "."

      if (label == "BOLD"):
         if (tail.islower() or tail.isupper()):
            letter = tail
         elif (tail == plain):
            letter = "\\aleph"

      if (label == "BLACK"):
         if (tail.islower()):
            letter = write_math_command("\\mathbb", tail)
         elif (tail.isupper()):
            letter = write_math_command("\\fraktur", tail)
         elif (tail == plain):
            letter = "\\forall"

      if (label == "CURSIVE"):
         if (tail.islower()):
            letter = write_math_command("\\mathcal", tail)
         elif (tail.isupper()):
            letter = write_math_command("\\mathscr", tail)
         elif (tail == plain):
            letter = "\\rightsquigarrow"

      if (label == "GREEK"):
         letters_greek = {
            'a': "\\alpha", 'b': "\\beta",
            # # ...
         }
         if (tail.islower() or tail.isupper()):
            letter = symbols[tail]
         elif (tail == PLAIN):
            letter = "\\exists"

      if (letter == None):
         data = self.get_data()
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      sink = write_math_outside(self, letter)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_sign(ORGAN.Leaf):

   KIND = "math"
   TAG = "span"
   OUTSIDE = False

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      assert(len(self.source) == 2)
      tip = self.source[0]
      tail = self.source[1]
      label = get_label_math(tip)
      keys = (
         '0', '1', '2', '3', '4',
         '5', '6', '7', '8', '9', '.',
      )
      signs = ()

      elif (label == "ABSTRACTION"):
         signs = ()
      elif (label == "ARITHMETICS"):
         signs = ()
      elif (label == "OPERATION"):
         signs = ()
      elif (label == "SHAPE"):
         signs = ()
      elif (label == "LINE"):
         signs = ()
      elif (label == "ARROW_LEFT"):
         signs = ()
      elif (label == "ARROW_MIDDLE"):
         signs = ()
      elif (label == "ARROW_RIGHT"):
         signs = ()
      elif (label == "EQUIVALENCE"):
         signs = ()
      elif (label == "ORDER_LEFT"):
         signs = ()
      elif (label == "ORDER_RIGHT"):
         signs = ()
      sign = signs[keys.index(key)]

      if (sign == None):
         data = self.get_data()
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      sink = write_math_outside(self, sign)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # boxes: pair, triplet, tuple

class Math_pair(ORGAN.Leaf):

   KIND = "math"
   TAG = "span"
   OUTSIDE = False

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      cut = AID.get_tip_math("CUT_PAIR")
      head_left = 0
      head_right = 0
      boxes = []
      while (head_right < len(self.source)):
         _, head_right = self.snip_tissue_math(head_left)
         if (self.source[head_right] == cut):
            box = Math_box(self.source[head_left: head_right])
            boxes.append(box)
            head_left = head_right
      assert(len(boxes) == 2)
      top, bottom = *boxes

      sink_top = top.write()
      sink_bottom = bottom.write()
      command = "\\frac"
      sink = AID.write_command(command, sink_top, sink_bottom)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_triplet(ORGAN.Leaf):

   KIND = "math"
   TAG = "span"
   OUTSIDE = False
   
   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      cut = AID.get_tip_math("CUT_TRIPLET")
      head_left = 0
      head_right = 0
      boxes = []
      while (head_right < len(self.source)):
         _, head_right = self.snip_tissue_math(head_left)
         if (self.source[head_right] == cut):
            box = Math_box(self.source[head_left: head_right])
            boxes.append(box)
            head_left = head_right
      assert(len(boxes) == 3)
      main, top, bottom = *boxes

      sink = ''
      sink += AID.write_math_command('', main.write()) + ' '
      sink += AID.write_math_command('^', top.write()) + ' '
      sink += AID.write_math_command('_', bottom.write()) + ' '
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_tuple(ORGAN.Leaf):

   KIND = "math"
   TAG = "span"
   OUTSIDE = False

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      cut = AID.get_tip_math("CUT_TUPLE")
      head_left = 0
      head_right = 0
      boxes = []
      while (head_right < len(self.source)):
         _, head_right = self.snip_tissue_math(head_left)
         if (self.source[head_right] == cut):
            box = Math_box(self.source[head_left: head_right])
            boxes.append(box)
            head_left = head_right
      assert(len(boxes) == 2)
      self.boxes = boxes

      newline = "\\\\"
      sink = ''
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

   KIND = "math"
   TAG = "span"

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

   KIND = "pseudo-sign"
   TAG = "span"

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

   KIND = "pseudo-sign"
   TAG = "span"

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

      assert(len(self.source) == 2)
      tip = self.source[0]
      tail = self.source[1]
      sink = symbols.get(tip).get(tail)
      if (sink == None):
         data = self.get_data_modified()
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()

      result = write_element(
            content = sink,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )
      return result



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
