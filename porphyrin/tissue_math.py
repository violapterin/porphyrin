from pdb import set_trace

from .organ import Leaf
from . import aid as AID

# #  &  &a  &A  &b  &B
# #  *                  *0  *1
# #     .a  .A  .b  .B  .0  .1  ..  .&  .*
class Math_letter(Leaf):

   KIND = "math-letter"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)
      self.accent = ''

   def write(self):
      assert (len(self.source) == 2 or len(self.source) == 4)
      letter_accent = ''
      letter = ''
      tip = self.source[0]
      tail = self.source[1]
      label_tip = AID.get_label_math(tip)
      label_tail = AID.get_label_math(tail)

      if (len(self.source) >= 4):
         accent = self.source[2:4]
         self.accent = AID.get_accent(accent)

      if (label_tip == "BOLD"):
         if (tail.islower() or tail.isupper()):
            letter = AID.write_latex("\\mathbf", tail)
      elif (label_tip == "BLACK"):
         if (tail.islower()):
            letter = AID.write_latex("\\mathbb", tail.upper())
         elif (tail.isupper()):
            letter = AID.write_latex("\\mathfrak", tail.upper())
      elif (label_tip == "CURSIVE"):
         if (tail.islower()):
            letter = AID.write_latex("\\mathcal", tail.upper())
         elif (tail.isupper()):
            letter = AID.write_latex("\\mathscr", tail.upper())
      elif (label_tip == "GREEK"):
         uppers = (
            "\\@", "\\infty", "\\Xi",
            "\\Delta", "\\&amp;",
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
         table_upper = AID.get_table_upper(uppers)
         table_lower = AID.get_table_lower(lowers)
         if (tail.isupper()):
            letter = table_upper.get(tail)
         elif (tail.islower()):
            letter = table_lower.get(tail)

      if not letter:
         data = self.give_data(0, len(self.source))
         from .caution import Token_invalid_as_symbol as creator
         creator(**data).panic()
      if self.accent:
         letter_accent = AID.write_latex(self.accent, letter)
      else:
         letter_accent = letter
      sink = self.write_math_outside(letter_accent)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_sign(Leaf):

   KIND = "math-sign"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)
      self.accent = ''

   def write(self):
      assert (len(self.source) == 2 or len(self.source) == 4)
      content = ''
      sign = ''
      many_sign = ()
      tip = self.source[0]
      tail = self.source[1]
      label_tip = AID.get_label_math(tip)
      label_tail = AID.get_label_math(tail)

      if (len(self.source) >= 4):
         accent = self.source[2:4]
         self.accent = AID.get_accent(accent)

      if (label_tip == "LINE"):
         many_sign = (
            "\\mid", "\\nmid", "\\backslash",
            "\\parallel", "\\nparallel", "\\between",
            "\\dotsc", "\\dotsb", "\\vdots", "\\ddots",
         )
         many_sign = AID.surround_tuple_with_affix("\\,", many_sign)
      elif (label_tip == "OPERATION_ONE"):
         many_sign = (
            "\\pm", "\\oplus", "\\cup",
            "\\sqcup", "\\vee", "\\curlyvee",
            "\\spadesuit", "\\heartsuit",
            "\\diamondsuit", "\\clubsuit", 
         )
         many_sign = AID.surround_tuple_with_affix("\\,", many_sign)
      elif (label_tip == "OPERATION_TWO"):
         many_sign = (
            "\\mp", "\\ominus", "\\cap",
            "\\sqcap", "\\wedge", "\\curlywedge",
            "\\neg", "\\angle",
            "\\square", "\\blacksquare",
         )
         many_sign = AID.surround_tuple_with_affix("\\,", many_sign)
      elif (label_tip == "OPERATION_THREE"):
         many_sign = (
            "\\times", "\\odot", "\\otimes",
            "\\bullet", "\\circ", "\\star",
            "\\ltimes", "\\rtimes", "\\div", "\\oslash", 
         )
         many_sign = AID.surround_tuple_with_affix("\\,", many_sign)

      elif (label_tip == "ARROW_MIDDLE"):
         self.LATERAL = False
         many_sign = (
            "\\downarrow", "\\Uparrow", "\\Downarrow",
            "\\updownarrow", "\\Updownarrow",
            "\\blacktriangle", "\\blacktriangledown",
            "\\dagger", "\\ddagger", "\\wr",
         )
         many_sign = AID.surround_tuple_with_affix("\\:", many_sign)
      elif (label_tip == "ARROW_LEFT"):
         self.LATERAL = False
         many_sign = (
            "\\Leftarrow", "\\Lleftarrow",
            "\\nwarrow", "\\swarrow",
            "\\leftarrowtail", "\\twoheadleftarrow", 
            "\\hookleftarrow", "\\curvearrowleft",
            "\\triangleleft", "\\blacktriangleleft", 
         )
         many_sign = AID.surround_tuple_with_affix("\\:", many_sign)
      elif (label_tip == "ARROW_RIGHT"):
         self.LATERAL = False
         many_sign = (
            "\\Rightarrow", "\\Rrightarrow",
            "\\nearrow", "\\searrow",
            "\\rightarrowtail", "\\twoheadrightarrow", 
            "\\hookrightarrow", "\\curvearrowright",
            "\\triangleright", "\\blacktriangleright", 
         )
         many_sign = AID.surround_tuple_with_affix("\\:", many_sign)
      elif (label_tip == "EQUIVALENCE_ONE"):
         self.LATERAL = False
         many_sign = (
            "\\neq", "\\equiv", "\\not\\equiv", "\\doteq",
            "\\leftrightarrow", "\\not\\leftrightarrow",
            "\\Leftrightarrow", "\\not\\Leftrightarrow",
            "\\leftrightsquigarrow", "\\not\\leftrightsquigarrow",
         )
         many_sign = AID.surround_tuple_with_affix("\\;", many_sign)
      elif (label_tip == "EQUIVALENCE_TWO"):
         self.LATERAL = False
         many_sign = (
            "\\approx", "\\simeq", "\\approxeq", "\\cong",
            "\\propto", "\\asymp", "\\gtreqless", "\\lesseqgtr"
            "\\leftrightararray", "\\rightleftararray",
         )
         many_sign = AID.surround_tuple_with_affix("\\;", many_sign)

      elif (label_tip == "ORDER_LEFT"):
         self.LATERAL = False
         many_sign = (
            "\\leq", "&lt;", "\\ll", "\\lesssim",
            "\\subseteq", "\\subsetneq", "\\in",
            "\\preceq", "\\precneqq", "\\dashv",
         )
         many_sign = AID.surround_tuple_with_affix("\\:", many_sign)
      elif (label_tip == "ORDER_RIGHT"):
         self.LATERAL = False
         many_sign = (
            "\\geq", "&gt;", "\\gtrsim", "\\gg",
            "\\supseteq", "\\supsetneq", "\\notin",
            "\\succeq", "\\succneqq", "\\vdash",
         )
         many_sign = AID.surround_tuple_with_affix("\\:", many_sign)

      elif (label_tip == "ABSTRACTION"):
         many_sign = (
            "\\displaystyle\\sum\\limits",
            "\\displaystyle\\prod\\limits",
            "\\displaystyle\\int\\limits",
            "\\displaystyle\\oint\\limits",
            "\\displaystyle\\bigoplus\\limits",
            "\\displaystyle\\bigodot\\limits",
            "\\displaystyle\\bigotimes\\limits",
            "\\displaystyle\\bigcup\\limits",
            "\\displaystyle\\bigcap\\limits",
            "\\displaystyle\\bigsqcup\\limits",
         )

      if many_sign:
         table_sign = AID.get_table_sign(many_sign)
      if tail.isdigit():
         sign = table_sign.get(tail)

      if not sign:
         data = self.give_data(0, len(self.source))
         from .caution import Token_invalid_as_symbol as creator
         creator(**data).panic()
      if self.accent:
         sign_accent = AID.write_latex(self.accent, sign)
      else:
         sign_accent = sign
      sink = self.write_math_outside(sign_accent)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_plain(Leaf):

   KIND = "math-plain"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)
      self.accent = ''

   def write(self):
      assert (len(self.source) == 2 or len(self.source) == 4)
      content = ''
      symbol = ''
      tip = self.source[0]
      tail = self.source[1]
      label_tip = AID.get_label_math(tip)
      label_tail = AID.get_label_math(tail)

      if (len(self.source) >= 4):
         accent = self.source[2:4]
         self.accent = AID.get_accent(accent)

      if (tail.isalnum()):
         symbol = tail
      else:
         table_symbol = {
            "PLAIN": ".",
            "BOLD": "\\aleph",
            "BLACK": "\\forall",
            "CURSIVE": "\\leftthreetimes",
            "GREEK": "\\exists",
            "ABSTRACTION": "\\wp",
            #
            "CUT_PAIR": ("," + "\\,"),
            "CUT_TRIPLET": (":" + "\\,"),
            "CUT_TUPLE": (";" + "\\,"),
            #
            "LINE": "\\,/\\,",
            "OPERATION_ONE": "\\,+\\,",
            "OPERATION_TWO": "\\,-\\,",
            "OPERATION_THREE": "\\,\\cdot\\,",
            #
            "ARROW_MIDDLE": ("\\:" + "\\uparrow" + "\\:"),
            "ARROW_LEFT": ("\\:" + "\\leftarrow" + "\\:"),
            "ARROW_RIGHT": ("\\:" + "\\rightarrow" + "\\:"),
            "EQUIVALENCE_ONE": ("\\;" + "=" + "\\;"),
            "EQUIVALENCE_TWO": ("\\;" + "\\sim" + "\\;"),
            #
            "SERIF": "\\prime",
            "SANS": "\\prime\\prime",
            "MONO": "\\prime\\prime\\prime",
            "CHECK": "\\quad",
            "ACCENT_ONE": "!",
            "ACCENT_TWO": "?",
         }
         symbol = table_symbol.get(label_tail)

      if not symbol:
         data = self.give_data(0, len(self.source))
         from .caution import Token_invalid_as_symbol as creator
         creator(**data).panic()
      if self.accent:
         symbol_accent = AID.write_latex(self.accent, symbol)
      else:
         symbol_accent = symbol
      sink = self.write_math_outside(symbol_accent)
      label_tail_straight = (
         "BOLD",
         "BLACK",
         "CURSIVE",
         "GREEK",
         "EQUIVALENCE_ONE",
         "EQUIVALENCE_TWO",
      )
      if (label_tail in label_tail_straight):
         self.LATERAL = False
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_bracket_round(Leaf):

   KIND = "math-bracket-round"
   TAG = "span"
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

   KIND = "math-bracket-square"
   TAG = "span"
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

   KIND = "math-bracket-curly"
   TAG = "span"
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

   KIND = "math-bracket-angle"
   TAG = "span"
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

   KIND = "math-bracket-line"
   TAG = "span"
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

# # boxes: pair, triplet, tuple

class Math_pair(Leaf):

   KIND = "math-pair"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      kind_cut = "math-cut-pair"
      many_kind_cut = {
         "math-cut-pair",
         "math-cut-triplet",
         "math-cut-tuple",
      }
      head = self.move_right(0, 0)
      boxes = [[]]
      data = self.give_data(0, len(self.source))
      while (head < len(self.source)):
         tissue, head = self.snip_tissue_math(head)
         head = self.move_right(0, head)
         kind = tissue.KIND
         if (kind in many_kind_cut):
            if (kind == kind_cut):
               boxes.append([])
               continue
            else:
               from .caution import Conflicting_delimiter as creator
               creator(**data).panic()
         else:
            boxes[-1].append(tissue)
      if not (len(boxes) == 2):
         from .caution import Wrong_number_boxes as creator
         creator(**data).panic()

      box_top, box_bottom = boxes
      top = AID.unite([tissue.write() for tissue in box_top])
      bottom = AID.unite([tissue.write() for tissue in box_bottom])
      command = "\\dfrac"
      content = AID.write_latex(command, top, bottom)
      sink = self.write_math_outside(content)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_triplet(Leaf):

   KIND = "math-triplet"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True
   
   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      kind_cut = "math-cut-triplet"
      many_kind_cut = {
         "math-cut-pair",
         "math-cut-triplet",
         "math-cut-tuple",
      }
      head = self.move_right(0, 0)
      boxes = [[]]
      data = self.give_data(0, len(self.source))
      while (head < len(self.source)):
         tissue, head = self.snip_tissue_math(head)
         head = self.move_right(0, head)
         kind = tissue.KIND
         if (kind in many_kind_cut):
            if (kind == kind_cut):
               boxes.append([])
               continue
            else:
               from .caution import Conflicting_delimiter as creator
               creator(**data).panic()
         else:
            boxes[-1].append(tissue)
      if not (len(boxes) == 3):
         data = self.give_data(0, len(self.source))
         from .caution import Wrong_number_boxes as creator
         creator(**data).panic()

      box_top, box_main, box_bottom = boxes
      whether_lateral = True
      if (len(box_main) == 1) and (not box_main[0].LATERAL):
         whether_lateral = False
      top = AID.unite([tissue.write() for tissue in box_top])
      main = AID.unite([tissue.write() for tissue in box_main])
      bottom = AID.unite([tissue.write() for tissue in box_bottom])
      content = ''
      if (whether_lateral):
         many_content = []
         if main:
            many_content.append(main)
         else:
            many_content.append('\\;')
         if top:
            many_content.append(AID.write_latex('^', top))
         if bottom:
            many_content.append(AID.write_latex('_', bottom))
         content = AID.unite(many_content)
      else:
         if bottom:
            underset = AID.write_latex("\\underset", bottom, main)
            if top:
               content = AID.write_latex("\\overset", top, underset)
            else:
               content = underset
         elif content:
            overset = AID.write_latex("\\overset", top, main)
      sink = self.write_math_outside(content)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_tuple(Leaf):

   KIND = "math-tuple"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      kind_cut = "math-cut-tuple"
      many_kind_cut = {
         "math-cut-pair",
         "math-cut-triplet",
         "math-cut-tuple",
      }
      head = self.move_right(0, 0)
      boxes = [[]]
      data = self.give_data(0, len(self.source))
      while (head < len(self.source)):
         tissue, head = self.snip_tissue_math(head)
         head = self.move_right(0, head)
         kind = tissue.KIND
         if (kind in many_kind_cut):
            if (kind == kind_cut):
               boxes.append([])
               continue
            else:
               from .caution import Conflicting_delimiter as creator
               creator(**data).panic()
         else:
            boxes[-1].append(tissue)

      many_content = []
      many_content.append(AID.write_latex("\\begin", "matrix"))
      for box in boxes:
         sink_tissue = AID.unite([tissue.write() for tissue in box])
         many_content.append(sink_tissue + "\\\\")
      many_content.append(AID.write_latex("\\end", "matrix"))
      content = AID.unite(many_content, cut = '')
      content = AID.insert_space_wide_latex(content)
      sink = self.write_math_outside(content)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_cut_pair(Leaf):

   KIND = "math-cut-pair"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      return ''

class Math_cut_triplet(Leaf):

   KIND = "math-cut-triplet"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      return ''

class Math_cut_tuple(Leaf):

   KIND = "math-cut-tuple"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      return ''

class Math_check(Leaf):

   KIND = "math-check"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      return ''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # texts: serif, sans, mono

class Math_serif(Leaf):

   KIND = "math-serif"
   TAG = "span"
   OUTSIDE = False
   LATERAL = False

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      command = "\\mathrm"
      if not self.source.replace('_', '').isalnum():
         data = self.give_data(0, len(self.source) - 1)
         from .caution import Allowing_only_alphabet as creator
         creator(**data).panic()
      content = AID.write_latex(command, self.source.replace('_', '\\_'))
      content = AID.insert_space_narrow_latex(content)
      sink = self.write_math_outside(content)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_sans(Leaf):

   KIND = "math-sans"
   TAG = "span"
   OUTSIDE = False
   LATERAL = False

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      command = "\\mathsf"
      if not self.source.replace('_', '').isalnum():
         data = self.give_data(0, len(self.source) - 1)
         from .caution import Allowing_only_alphabet as creator
         creator(**data).panic()
      content = AID.write_latex(command, self.source.replace('_', '\\_'))
      content = AID.insert_space_narrow_latex(content)
      sink = self.write_math_outside(content)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_mono(Leaf):

   KIND = "math-mono"
   TAG = "span"
   OUTSIDE = False
   LATERAL = False

   def __init__(self, **data):
      self.fill_basic(**data)

   def write(self):
      command = "\\mathtt"
      if not self.source.replace('_', '').isalnum():
         data = self.give_data(0, len(self.source) - 1)
         from .caution import Allowing_only_alphabet as creator
         creator(**data).panic()
      content = AID.write_latex(command, self.source.replace('_', '\\_'))
      content = AID.insert_space_wide_latex(content)
      sink = self.write_math_outside(content)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Math_void(Leaf):

   KIND = "math-void"
   TAG = "span"
   OUTSIDE = False
   LATERAL = True

   def __init__(self):
      pass

   def write(self):
      return ''
