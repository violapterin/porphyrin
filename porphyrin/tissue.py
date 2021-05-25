import organ as ORGAN
import stem as STEM
import caution as CAUTION
import aid as AID

class Math_box(ORGAN.Leaf):

   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      sink = ''
      tissue = None
      head = 0
      count = 0
      while (head < len(self.source)):
         tissue, head = self.snip_tissue_math(head)
         sink = self.write_math_outside(tissue.write()) + ' '
         count += 1
      if (count == 1) and (tissue.LATERAL):
         self.LATERAL == False
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_bracket_round(ORGAN.Leaf):

   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      sink = ''
      content = ''
      head = 0
      mark_left = "\\left("
      mark_right = "\\right("
      while (head < len(self.source)):
         tissue, head = self.snip_tissue_math(head)
         content = tissue.write() + ' '
      sink = self.write_math_outside(content)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_bracket_square(ORGAN.Leaf):

   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      sink = ''
      content = ''
      head = 0
      mark_left = "\\left["
      mark_right = "\\right]"
      while (head < len(self.source)):
         tissue, head = self.snip_tissue_math(head)
         content = tissue.write() + ' '
      sink = self.write_math_outside(content)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_bracket_curly(ORGAN.Leaf):

   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      sink = ''
      content = ''
      head = 0
      mark_left = "\\left\\{"
      mark_right = "\\right\\}"
      while (head < len(self.source)):
         tissue, head = self.snip_tissue_math(head)
         content = tissue.write() + ' '
      sink = self.write_math_outside(content)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_bracket_angle(ORGAN.Leaf):

   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      sink = ''
      content = ''
      head = 0
      mark_left = "\\left\\langle"
      mark_right = "\\right\\rangle"
      while (head < len(self.source)):
         tissue, head = self.snip_tissue_math(head)
         content = tissue.write() + ' '
      sink = self.write_math_outside(content)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_bracket_line(ORGAN.Leaf):

   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      sink = ''
      content = ''
      head = 0
      mark_left = "\\left|"
      mark_right = "\\right|"
      while (head < len(self.source)):
         tissue, head = self.snip_tissue_math(head)
         content = tissue.write() + ' '
      sink = self.write_math_outside(content)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# #  &  &a  &A  &b  &B
# #  *                  *0  *1
# #     .a  .A  .b  .B  .0  .1  ..  .&  .*
class Math_plain(ORGAN.Leaf):

   KIND = "math"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      assert(len(self.source) == 2)
      content = ''
      sign = ''
      tip = self.source[0]
      tail = self.source[1]
      label_tip = AID.get_label_math(tip)
      label_tail = AID.get_label_math(tail)

      if (tail.islower() or tail.isupper()):
         sign = tail
      elif (tail.isdigit()):
         sign = tail
      else:
         table_symbol = {
            "PLAIN": '.',
            "BOLD": "\\aleph",
            "BLACK": "\\forall",
            "CURSIVE": "\\leftthreetimes",
            "GREEK": "\\exists",
            #
            "ABSTRACTION": "\\wp",
            "LINE": '/',
            "OPERATION_ONE": '+',
            "OPERATION_TWO": '-',
            "OPERATION_THREE": "\\cdot",
            "ARROW_MIDDLE": "\\uparrow",
            "EQUIVALENCE_ONE": '=',
            "EQUIVALENCE_TWO": "\\sim",
            "SERIF": "\\prime",
            "SANS": "\\prime\\prime",
            "MONO": "\\prime\\prime\\prime",
            "CUT_PAIR": ',',
            "CUT_TRIPLET": ':',
            "CUT_TUPLE": ';',
            "PLAIN": '.',
            "CHECK": "\\quad",
            "ACCENT_ONE": '!',
            "ACCENT_TWO": '?',
         }
         sign = table_symbol.get(label_tail)
         labels_not_lateral = {
            "EQUIVALENCE_ONE", "EQUIVALENCE_TWO",
         }
         if (label_tail in labels_not_lateral):
            self.LATERAL = False

      if not sign:
         data = self.get_data()
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      sink = write_math_outside(self, sign)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_letter(ORGAN.Leaf):

   KIND = "math"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)
      self.accent = ''

   def write(self):
      content = ''
      letter = ''
      tip = self.source[0]
      tail = self.source[1]
      label_tip = AID.get_label_math(tip)
      label_tail = AID.get_label_math(tail)

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

      elif (label == "BOLD"):
         if (tail.islower() or tail.isupper()):
            letter = tail
      elif (label == "BLACK"):
         if (tail.islower()):
            letter = AID.write_latex("\\mathbb", tail)
         elif (tail.isupper()):
            letter = AID.write_latex("\\fraktur", tail)
      elif (label == "CURSIVE"):
         if (tail.islower()):
            letter = AID.write_latex("\\mathcal", tail)
         elif (tail.isupper()):
            letter = AID.write_latex("\\mathscr", tail)
      elif (label == "GREEK"):
         uppers = (
            "\\@", "\\infty", "\\Xi",
            "\\Delta", "\\&",
            "\\Phi", "\\Gamma", "\\hslash",
            "\\bot", "\\top", "\\S",
            "\\Lambda", "\\mho", "\\nabla",
            "\\%", "\\Pi", "\\Theta",
            "\\surd", "\\Sigma", "\\eth",
            "\\Upsilon", "\\$", "\\Omega",
            "\\#", "\\Psi", "\\partial",
         )
         lowers = (
            "\\alpha", "\\beta", "\\xi",
            "\\delta", "\\varepsilon
            "\\varphi", "\\gamma", "\\eta",
            "\\iota", "\\imath","\\kappa",
            "\\lambda", "\\mu", "\\nu",
            "\\varnothing", "\\pi", "\\vartheta",
            "\\rho", "\\sigma", "\\tau",
            "\\upsilon", "\\digamma", "\\omega",
            "\\chi", "\\psi", "\\zeta",
         )
         table_upper = get_table_upper(uppers)
         table_lower = get_table_lower(lowers)
         if (tail.isupper()):
            letter = table_upper.get(tail)
         elif (tail.islower()):
            letter = table_lower.get(tail)

      if not letter:
         data = self.get_data()
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      if self.accent:
         content = AID.write_latex(self.accent, letter)
      else:
         content = letter
      sink = write_math_outside(self, content)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_sign(ORGAN.Leaf):

   KIND = "math"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      assert(len(self.source) == 2)
      content = ''
      sign = ''
      tip = self.source[0]
      tail = self.source[1]
      label_tip = AID.get_label_math(tip)
      label_tail = AID.get_label_math(tail)

      if (label == "ABSTRACTION"):
         signs = (
            "\\sum", "\\prod", "\\int", "\\oint",
            "\\bigoplus", "\\bigodot", "\\bigotimes",
            "\\bigcup", "\\bigcap", "\\bigsqcup",
         )
      elif (label == "OPERATION_ONE"):
         signs = (
            "\\pm", "\\oplus", "\\cup",
            "\\sqcup", "\\vee", "\\curlyvee",
            "\\spadesuit", "\\heartsuit",
            "\\diamondsuit", "\\clubsuit", 
         )
      elif (label == "OPERATION_TWO"):
         signs = (
            "\\mp", "\\ominus", "\\cap",
            "\\sqcap", "\\wedge", "\\curlywedge",
            "\\neg", "\\angle",
            "\\square", "\\blacksquare",
         )
      elif (label == "OPERATION_THREE"):
         signs = (
            "\\times", "\\odot", "\\otimes",
            "\\bullet", "\\circ", "\\star",
            "\\ltimes", "\\rtimes", "\\div", "\\oslash", 
         )
      elif (label == "LINE"):
         signs = (
            "\\mid", "\\nmid", "\\backslash",
            "\\parallel", "\\nparallel", "\\between",
            "\\dotsc", "\\dotsb", "\\vdots", "\\ddots",
         )
      elif (label == "ARROW_LEFT"):
         self.LATERAL = False
         signs = (
            "\\leftarrow", "\\Leftarrow",
            "\\nwarrow", "\\swarrow",
            "\\leftarrowtail", "\\twoheadleftarrow", 
            "\\hookleftarrow", "\\curvearrowleft",
            "\\triangleleft", "\\blacktriangleleft", 
         )
      elif (label == "ARROW_RIGHT"):
         self.LATERAL = False
         signs = (
            "\\rightarrow", "\\Rightarrow",
            "\\nearrow", "\\searrow",
            "\\rightarrowtail", "\\twoheadrightarrow", 
            "\\hookrightarrow", "\\curvearrowright",
            "\\triangleright", "\\blacktriangleright", 
         )
      elif (label == "ARROW_MIDDLE"):
         self.LATERAL = False
         signs = (
            "\\downarrow", "\\Uparrow", "\\Downarrow",
            "\\updownarrow", "\\Updownarrow",
            "\\blacktriangle", "\\blacktriangledown",
            "\\dagger", "\\ddagger", "\\wr",
         )
      elif (label == "EQUIVALENCE_ONE"):
         self.LATERAL = False
         signs = (
            "\\neq", "\\equiv", "\\not\\equiv", "\\doteq",
            "\\leftrightarrow", "\\not\\leftrightarrow",
            "\\Leftrightarrow", "\\not\\Leftrightarrow",
            "\\leftrightsquigarrow", "\\not\\leftrightsquigarrow",
         )
      elif (label == "EQUIVALENCE_TWO"):
         self.LATERAL = False
         signs = (
            "\\approx", "\\simeq", "\\approxeq", "\\cong",
            "\\propto", "\\asymp", "\\gtreqless", "\\lesseqgtr"
            "\\leftrightarrows", "\\rightleftarrows",
         )
      elif (label == "ORDER_LEFT"):
         self.LATERAL = False
         signs = (
            "\\leq", "<", "\\ll", "\\lesssim",
            "\\subseteq", "\\subsetneq", "\\in",
            "\\preceq", "\\precneqq", "\\dashv",
         )
      elif (label == "ORDER_RIGHT"):
         self.LATERAL = False
         signs = (
            "\\geq", ">", "\\gtrsim", "\\gg",
            "\\supseteq", "\\supsetneq", "\\notin",
            "\\succeq", "\\succneqq", "\\vdash",
         )

      if signs:
         table_sign = get_table_for_sign(signs)
      if tail.isdigit():
         sign = table_sign.get(tail)
      if not sign:
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
   LATERAL = True

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
   LATERAL = True
   
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
      box_top, box_main, box_bottom = *boxes
      top = top.write()
      main = main.write()
      bottom = bottom.write()

      sink = ''
      if (self.LATERAL):
         sink += AID.write_latex('', main) + ' '
         sink += AID.write_latex('^', top) + ' '
         sink += AID.write_latex('_', bottom) + ' '
      else:
         underset = AID.write_latex("\\underset", bottom, main)
         sink += AID.write_latex("\\overset", top, underset)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_tuple(ORGAN.Leaf):

   KIND = "math"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

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
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      command = "\\mathrm"
      sink = AID.write_math_word(command, self.source)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_sans(ORGAN.Leaf):

   KIND = "math"
   TAG = "span"
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      command = "\\mathsf"
      sink = AID.write_math_word(command, self.source)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_mono(ORGAN.Leaf):

   KIND = "math"
   TAG = "span"
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      command = "\\mathtt"
      sink = AID.write_math_word(command, self.source)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# #  &  &a  &A  &b  &B
# #  *                  *0  *1
# #     .a  .A  .b  .B  .0  .1  ..  &.  *.
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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

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
      if not sink:
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
      result += ' '
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Pseudo_square(ORGAN.Leaf):

class Pseudo_curly(ORGAN.Leaf):

class Pseudo_serif(ORGAN.Leaf):

class Pseudo_sans(ORGAN.Leaf):

class Pseudo_mono(ORGAN.Leaf):

class Pseudo_tiny(ORGAN.Leaf):
