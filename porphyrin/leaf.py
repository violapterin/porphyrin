import organ as ORGAN
import stem as STEM
import caution as CAUTION

class Serif_roman(ORGAN.Organ):

   KIND = "serif-roman"
   TAG = "span"

   def parse(self):
      self.tune_text()
      head = 0
      while head <= self.self.source.size() - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_tag(
            content = sink,
            tag = tag,
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
      while head <= self.self.source.size() - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_tag(
            content = sink,
            tag = tag,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      result = self.write_tag(result, TAG)
      return result

class Serif_bold(ORGAN.Organ):

   KIND = "serif-bold"
   TAG = 'b'

   def parse(self):
      self.tune_text()
      head = 0
      while head <= self.self.source.size() - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_tag(
            content = sink,
            tag = tag,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      result = self.write_tag(result, TAG)
      return result

class Sans_roman(ORGAN.Organ):

   KIND = "sans-roman"

   def parse(self):
      self.tune_text()
      head = 0
      while head <= self.self.source.size() - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_tag(
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
      while head <= self.self.source.size() - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_tag(
            content = sink,
            tag = tag,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      result = self.write_tag(result, self.TAG)
      return result

class Mono(ORGAN.Organ):

   KIND = "sans-bold"
   TAG = "pre"

   def parse(self):
      self.tune_text()
      head = 0
      while head <= self.self.source.size() - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def write(self):
      result = ''
      tag = self.TAG
      if not (self.address == None):
         tag = 'a'
      for sink in self.sinks:
         result += write_tag(
            content = sink,
            tag = tag,
            attributes = ["class"],
            values = [self.KIND],
         )
         result += ' '
      result = self.write_tag(result, self.TAG)
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Alternative(ORGAN.Organ):

   def parse(self):
      pass

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Code_kana(ORGAN.Organ):

   def parse(self):
      map_symbol = {}
      map_symbol['~'] = {
         '0': 'い', '1': 'ろ', '2': 'は', '3': 'に', '4': 'ほ',
         '5': 'へ', '6': 'と', '7': 'ち', '8': 'り', '9': 'ぬ',
      }
      # # い ろ は に ほ へ と ち り ぬ 
      # # る を わ か よ た れ そ つ ね
      # # な ら む う ゐ の お く や ま
      # # け ふ こ え て あ さ き ゆ め
      # # み し ゑ ひ も
      # # ... ...

      first = source[0]
      second = source[1]
      sink = map_symbol[first][second]

      if (sink == None):
         caution = CAUTION.Not_valid_symbol(
            "token": source,
            "leftmost": self.leftmost,
            "rightmost": self.rightmost,
            "count_line": self.count_line,
            "count_glyph": self.count_glyph,
         )
         caution.panic()
      self.sinks[0] = sink

   def write(self):
      return self.sinks[0]

class Code_kanji(ORGAN.Organ):

   def parse(self):
      map_symbol = {}
      map_symbol['?'] = {
         'A': '零', 'B': '壹', 'C': '貳', 'D': '參', 'E': '肆',
      }
      map_symbol['?'] = {
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


      first = source[0]
      second = source[1]
      sink = map_symbol[first][second]

      if (sink == None):
         caution = CAUTION.Not_valid_symbol(
            "token": source,
            "leftmost": self.leftmost,
            "rightmost": self.rightmost,
            "count_line": self.count_line,
            "count_glyph": self.count_glyph,
         )
         caution.panic()
      self.sinks[0] = sink

   def write(self):
      return self.sinks[0]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Traditional(ORGAN.Organ):

   BOLD = 1
   BLACK = 2
   CURSIVE = 3
   EXTENDED = 4
   ABSTRACTION = 11
   EQUIVALENCE = 21
   ARITHMETICS = 22
   OPERATION = 23
   SHAPE = 24
   LINE = 25
   ARROW_LEFT = 31
   ARROW_RIGHT = 32
   ORDER_LEFT = 33
   ORDER_RIGHT = 34
   DIACRITICS = 40
   PAIR = 41
   TRIPLET = 42
   TUPLE = 43
   ROMAN = 50
   SANS = 51
   MONO = 51

   def parse(self):
      pass

   def write(self):
      pass

   # # # # # # # # # # # # # # # #

   def snip_tissue(self, head_left):
      tissue = None
      while head <= self.self.source.size() - 1:
         text, head = self.split_word(head)
         sinks.append(text)

   def give_labels_tissue():
      return {
         '[': self.
      }

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

   # #     a  A  b  B  0  1  .
   # # .  .a .A .b .B .0 .1 ..
   # # &  &a &A &b &B       &.
   # # *              *0 *1 *.

class Code_plain(ORGAN.Organ):

   def parse(self):
      first = source[0]
      second = source[1]
      if (second = '.')
        self.sinks[0] = '.'
      self.sinks[0] = second

   def write(self):
      return self.sinks[0]

class Code_letter(ORGAN.Organ):

   def parse(self):
      first = source[0]
      second = source[1]
      command = None
      if (second = '&')
        command = "\\fraktur"
      self.sink = second

   def write(self):
      return self.sinks[0]

class Code_Sign(object):

   def __init__(self, number):
      self.number = number

# # # # # # # # # # # # # # # #

class Code_pair(ORGAN.Organ):

   def __init__(self, down, up):
      self.down = down
      self.up = up

class Code_triplet(ORGAN.Organ):

   def __init__(self, down, middle, up):
      self.down = down
      self.middle = middle
      self.up = up

class Code_tuple(ORGAN.Organ):

   def __init__(self, **entries):
      self.entries = list(entries)

class Code_box(object):

   def __init__(self, *entries):
      self.entries = list(entries)

# # # # # # # # # # # # # # # #

class Code_diacritics(object):

   def __init__(self, symbol, number):
      self.symbol = symbol
      self.number = number

class Code_roman(object):

   def __init__(self, text):
      self.text = text

class Code_sans(object):

   def __init__(self, text):
      self.text = text

class Code_mono(object):

   def __init__(self, text):
      self.text = text

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def tune_text(source):
  result = ignore_mark_text(source)
  result = adjust_whitespace(result)
  return result

def tune_code(source):
  result = adjust_whitespace(source)
  return result

def adjust_whitespace(source):
  spaces = give_set_delimiter()
  result = erase_glyph(source, spaces)
  result = ' '.join(result.split())
  return result

def ignore_mark_text(source):
  return remove_glyph(
     source, give_glyphs_text_ignored()
  )

def remove_glyph(source, group):
  for glyph in group:
     source = source.translate(
        source.maketrans(glyph, '')
     )
  return source

def erase_glyph(source, group):
  for glyph in group:
     source = source.translate(
        source.maketrans(glyph, ' ')
     )
  return source

def replace_glyph(source, group):
  for glyph in group:
     source = source.translate(
        source.maketrans(glyph, group[glyph])
     )
  return source

def escape_hypertext(source):
  return replace_glyph(source, give_escapes())

# # # # # # # # # # # # # # # # 

def give_map_escapes_hypertext():
  return {'<': "&lt;",
     '>': "&gt;",
     '&': "&amp;",
     '\"': "&quote;",
     '\'': "&apos;",
  }

def give_glyphs_text_ignored():
  return set([
     '<',
     '>',
     '@',
     '#',
     '$',
     '%',
     '&',
  ])

def give_labels_leaf():
  return set([
     "SERIF_NORMAL",
     "SERIF_ITALIC",
     "SERIF_BOLD",
     "SANS_NORMAL",
     "SANS_BOLD",
     "MONO",
     "ALTERNATIVE",
     "TRADITIONAL",
     "LINK",
  ])


