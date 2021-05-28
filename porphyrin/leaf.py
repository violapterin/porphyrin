from pdb import set_trace

from .organ import Leaf
from . import aid as AID

class Serif_roman(Leaf):

   KIND = "serif-roman"
   TAG_PLAIN = "span"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''

   def write(self):
      content = AID.tune_text(self.source)
      sink = self.write_text(content)
      return sink

class Serif_italic(Leaf):

   KIND = "serif-italic"
   TAG_PLAIN = "em"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''

   def write(self):
      content = AID.tune_text(self.source)
      sink = self.write_text(content)
      return sink

class Serif_bold(Leaf):

   KIND = "serif-bold"
   TAG_PLAIN = 'b'

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''

   def write(self):
      content = AID.tune_text(self.source)
      sink = self.write_text(content)
      return sink

class Sans_roman(Leaf):

   KIND = "sans-roman"
   TAG_PLAIN = "span"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''

   def write(self):
      content = AID.tune_text(self.source)
      sink = self.write_text(content)
      return sink

class Sans_bold(Leaf):

   KIND = "sans-bold"
   TAG_PLAIN = 'b'

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''

   def write(self):
      content = AID.tune_text(self.source)
      sink = self.write_text(content)
      return sink

class Mono(Leaf):

   KIND = "mono"
   TAG = "pre"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.address = ''

   def write(self):
      content = AID.tune_code(self.source)
      sink = self.write_text(content)
      return sink

class Comment(Leaf):

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      token_left = "<!--"
      token_right = "-->"
      sinks = [
         token_left,
         AID.tune_comment(self.source),
         token_right,
      ]
      sink = AID.unite(sinks)
      return sink

class Newline(Leaf):

   KIND = "newline"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sink = None

class Space(Leaf):

   KIND = "space"

   def __init__(self, **data):
      self.fill_basic(**data)
      self.sink = None

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Math(Leaf):

   KIND = "math"
   TAG = "span"

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      content = ''
      head_left = 0
      head_right = 0
      interval = range(len(self.source))
      for head in interval:
         tissue, head_right = self.snip_tissue_math(head_left)
         tissue.OUTSIDE = True
         content += tissue.write()
      sink = AID.write_element(
            content = content,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Pseudo(Leaf):

   KIND = "pseudo"
   TAG = "span"

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      content = ''
      head_left = 0
      head_right = 0
      interval = range(len(self.source))
      for head in interval:
         tissue, head_right = self.snip_tissue_pseudo(head_left)
         content += tissue.write()
      sink = AID.write_element(
            content = content,
            tag = self.TAG,
            attributes = ["class"],
            values = [self.KIND],
      )
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_box(Leaf):

   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      tissue = None
      sinks = []
      count = 0
      head = self.move_right(0)
      interval = range(len(self.source))
      for head in interval:
         tissue, head = self.snip_tissue_math(head)
         sink.append(self.write_math_outside(tissue.write()))
         count += 1
      if (count == 1) and not tissue.LATERAL:
         self.LATERAL == False
      sink = AID.unite(sinks)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_bracket_round(Leaf):

   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      mark_left = "\\left("
      mark_right = "\\right)"
      sink = self.write_math_bracket(mark_left, mark_right)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_bracket_square(Leaf):

   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      mark_left = "\\left["
      mark_right = "\\right]"
      sink = self.write_math_bracket(mark_left, mark_right)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_bracket_curly(Leaf):

   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      mark_left = "\\left\\{"
      mark_right = "\\right\\}"
      sink = self.write_math_bracket(mark_left, mark_right)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_bracket_angle(Leaf):

   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      mark_left = "\\left\\langle"
      mark_right = "\\right\\rangle"
      sink = self.write_math_bracket(mark_left, mark_right)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_bracket_line(Leaf):

   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      mark_left = "\\left|"
      mark_right = "\\right|"
      sink = self.write_math_bracket(mark_left, mark_right)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# #  &  &a  &A  &b  &B
# #  *                  *0  *1
# #     .a  .A  .b  .B  .0  .1  ..  .&  .*
class Math_plain(Leaf):

   KIND = "math"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      assert (len(self.source) == 2)
      content = ''
      sign = ''
      tip = self.source[0]
      tail = self.source[1]
      label_tip = AID.get_label_math(tip)
      label_tail = AID.get_label_math(tail)

      if (tail.isalnum()):
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
            "EQUIVALENCE_ONE": '=',
            "EQUIVALENCE_TWO": "\\sim",
            "ARROW_MIDDLE": "\\uparrow",
            "ARROW_LEFT": "\\leftarrow",
            "ARROW_RIGHT": "\\rightarrow",
            #
            "SERIF": "\\prime",
            "SANS": "\\prime\\prime",
            "MONO": "\\prime\\prime\\prime",
            "CUT_PAIR": ',',
            "CUT_TRIPLET": ':',
            "CUT_TUPLE": ';',
            "CHECK": "\\quad",
            "ACCENT_ONE": '!',
            "ACCENT_TWO": '?',
         }
         sign = table_symbol.get(label_tail)

      if not sign:
         data = self.give_data(0, len(self.source))
         from .caution import Not_being_valid_symbol as creator
         creator(**data).panic()
      sink = self.write_math_outside(sign)
      if AID.be_not_lateral_math(label_tail):
         self.LATERAL = False
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_letter(Leaf):

   KIND = "math"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)
      self.accent = ''

   def write(self):
      print("writing: ", self.source)
      letter_accent = ''
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
            "\\delta", "\\varepsilon",
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
         data = self.give_data(0, len(self.source))
         from .caution import Not_being_valid_symbol as creator
         creator(**data).panic()
      if self.accent:
         letter_accent = AID.write_latex(self.accent, letter)
      else:
         letter_accent = letter
      sink = self.write_math_outside(letter_accent)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_sign(Leaf):

   KIND = "math"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      assert (len(self.source) == 2)
      content = ''
      sign = ''
      signs = ()
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
            "\\Leftarrow", "\\Lleftarrow",
            "\\nwarrow", "\\swarrow",
            "\\leftarrowtail", "\\twoheadleftarrow", 
            "\\hookleftarrow", "\\curvearrowleft",
            "\\triangleleft", "\\blacktriangleleft", 
         )
      elif (label == "ARROW_RIGHT"):
         self.LATERAL = False
         signs = (
            "\\Rightarrow", "\\Rrightarrow",
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
         table_sign = get_table_sign(signs)
      if tail.isdigit():
         sign = table_sign.get(tail)
      if not sign:
         data = self.give_data(0, len(self.source))
         from .caution import Not_being_valid_symbol as creator
         creator(**data).panic()
      sink = self.write_math_outside(sign)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # boxes: pair, triplet, tuple

class Math_pair(Leaf):

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
      interval = range(len(self.source))
      for head in interval:
         _, head_right = self.snip_tissue_math(head_left)
         if (self.source[head_right] == cut):
            box = Math_box(self.source[head_left: head_right])
            boxes.append(box)
            head_left = head_right
      assert (len(boxes) == 2)
      top, bottom = boxes

      sink_top = top.write()
      sink_bottom = bottom.write()
      command = "\\frac"
      sink = AID.write_command(command, sink_top, sink_bottom)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_triplet(Leaf):

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
      interval = range(len(self.source))
      for head in interval:
         _, head_right = self.snip_tissue_math(head_left)
         if (self.source[head_right] == cut):
            box = Math_box(self.source[head_left: head_right])
            boxes.append(box)
            head_left = head_right
      assert (len(boxes) == 3)
      box_top, box_main, box_bottom = boxes
      top = top.write()
      main = main.write()
      bottom = bottom.write()

      sink = ''
      contents = []
      if (main.LATERAL):
         contents.append(AID.write_latex('', main))
         contents.append(AID.write_latex('^', top))
         contents.append(AID.write_latex('_', bottom))
      else:
         underset = AID.write_latex("\\underset", bottom, main)
         contents.append(AID.write_latex("\\overset", top, underset))
      sink = AID.unite(contents)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_tuple(Leaf):

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
      interval = range(len(self.source))
      for head in interval:
         _, head_right = self.snip_tissue_math(head_left)
         if (self.source[head_right] == cut):
            box = Math_box(self.source[head_left: head_right])
            boxes.append(box)
            head_left = head_right

      sink = ''
      sink += AID.write_command("\\begin", "matrix") + '\n'
      for box in boxes:
         sink += box.write() + "\\\\\n"
      sink += AID.write_command("\\end", "matrix") + '\n'
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # texts: serif, sans, mono

class Math_serif(Leaf):

   KIND = "math"
   TAG = "span"
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      command = "\\mathrm"
      if not isalnum(self.source):
         data = self.give_data()
         from .caution import Allowing_only_alphabets as creator
         creator(**data).panic()
      sink = AID.write_latex(command, self.source)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_sans(Leaf):

   KIND = "math"
   TAG = "span"
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      command = "\\mathsf"
      if not isalnum(self.source):
         data = self.give_data()
         from .caution import Allowing_only_alphabets as creator
         creator(**data).panic()
      sink = AID.write_latex(command, self.source)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_mono(Leaf):

   KIND = "math"
   TAG = "span"
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      command = "\\mathtt"
      if not isalnum(self.source):
         data = self.give_data()
         from .caution import Allowing_only_alphabets as creator
         creator(**data).panic()
      sink = AID.write_latex(command, self.source)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# #  &  &a  &A  &b  &B
# #  *                  *0  *1
# #     .a  .A  .b  .B  .0  .1  ..  &.  *.
class Pseudo_letter(Leaf):

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

class Pseudo_sign(Leaf):

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

      assert (len(self.source) == 2)
      tip = self.source[0]
      tail = self.source[1]
      sink = symbols.get(tip).get(tail)
      if not sink:
         data = self.give_data()
         from .caution import Not_being_valid_symbol as creator
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
