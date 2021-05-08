import stem as STEM
import leaf as LEAF
import caution as CAUTION

# Stem: Document
# Stem (bough): Section, Stanza, Table, Image, Break,
# Stem (twig): Paragraph, Line, Row,
# Stem (frond): Sentence, Verse, Cell
# Leaf: Math old, Math new, Mono
# Leaf: Serif roman, Serif italic, Serif bold, Sans roman, Sans bold

class Organ(object):

   def __init__(self, **data):
      self.source = data.pop("source", '')
      self.leftmost = data.pop("leftmost", '')
      self.rightmost = data.pop("rightmost", '')
      self.count_line = data.pop("count_line", 0)
      self.count_glyph = data.pop("count_glyph", 0)
      self.sinks = []
      self.address = ''

   # # # # # # # # # # # # # # # #

   def snip_bough(self, head_mark_left):
      bough = None
      source = self.source[head_mark_left:]
      mark = probe_mark(source)
      label = get_label(mark)
      head_content_left = head + mark.size
      data_caution = {
         "token": mark,
         "leftmost": get_left(head_mark_left),
         "rightmost": get_right(head_content_left),
         "count_line": count_next_line(head_mark_left),
         "count_glyph": count_next_glyph(head_mark_left),
      }

      if (label == "BREAK"):
         segments = source.split(mark, 1)
         head_mark_right = head_mark_right + mark.size
         data_organ = {
            "leftmost": get_left(head_mark_left),
            "rightmost": get_right(head_mark_right),
            "count_line": self.count_line,
            "count_glyph": self.count_glyph,
         }
         bough = STEM.Break(**data_organ)
         return bough, head_mark_right

      segments = source.split(mark, 2)
      content = segments[1]
      head_content_right = head_mark_right + content.size
      head_mark_right = head_content_right + mark.size

      if (label == None):
         caution = CAUTION.Not_matching_mark_bough(**data_caution)
         caution.panic()
      if not (label in self.give_labels_bough()):
         caution = CAUTION.Disallowing_non_leaf(**data_caution)
         caution.panic()

      data_organ = {
         "source": content,
         "leftmost": get_left(head_content_left),
         "rightmost": get_right(head_content_right),
         "count_line": count_next_line(head_content_left),
         "count_glyph": count_next_glyph(head_content_left),
      }
      if (label == "SECTION"):
         bough = STEM.Section(**data_organ)
      if (label == "STANZA"):
         bough = STEM.Stanza(**data_organ)
      if (label == "TABLE"):
         bough = STEM.Table(**data_organ)
      if (label == "IMAGE"):
         bough = STEM.Image(**data_organ)
      if (label == "BREAK"):
         bough = STEM.Break(**data_organ)

      return bough, head_mark_right

   def snip_leaf(self, head_mark_left):
      leaf = None
      source = self.source[head_mark_left:]
      mark = probe_mark(source)
      label = get_label(mark)
      head_content_left = head_mark_left + mark.size
      data_caution = {
         "token": mark,
         "leftmost": get_left(head_mark_left),
         "rightmost": get_right(head_content_left),
         "count_line": count_next_line(head_mark_left),
         "count_glyph": count_next_glyph(head_mark_left),
      }

      if (label == "SPACE") or (label == "NEWLINE"):
         segments = source.split(mark, 1)
         head_mark_right = head_mark_right + mark.size
         data_organ = {
            "leftmost": get_left(head_mark_left),
            "rightmost": get_right(head_mark_right),
            "count_line": self.count_line,
            "count_glyph": self.count_glyph,
         }
      if (label == "SPACE"):
         leaf = LEAF.Space(**data_organ)
         return leaf, head_mark_right
      if (label == "NEWLINE"):
         leaf = LEAF.Newline(**data_organ)
         return leaf, head_mark_right

      segments = source.split(mark, 2)
      content = segments[1]
      head_content_right = head_mark_right + content.size
      head_mark_right = head_content_right + mark.size

      if (label == None):
         caution = CAUTION.Not_matching_mark_leaf(**data_caution)
         caution.panic()
      if not (label in self.give_labels_leaf()):
         caution = CAUTION.Disallowing_non_leaf(**data_caution)
         caution.panic()

      data_organ = {
         "source": content,
         "leftmost": get_left(head_content_left),
         "rightmost": get_right(head_content_right),
         "count_line": count_next_line(head_content_left),
         "count_glyph": count_next_glyph(head_content_left),
      }
      if (label == "LINK"):
         if (self.sinks.size = 0):
            self.address = content
         else:
            sinks[-1].address = content
         return None, head_mark_right
      if (label == "SERIF_NORMAL"):
         leaf = LEAF.Serif_normal(**data_organ)
      if (label == "SERIF_ITALIC"):
         leaf = LEAF.Serif_italic(**data_organ)
      if (label == "SERIF_BOLD"):
         leaf = LEAF.Serif_bold(**data_organ)
      if (label == "SANS_NORMAL"):
         leaf = LEAF.Sans_normal(**data_organ)
      if (label == "SANS_BOLD"):
         leaf = LEAF.Sans_bold(**data_organ)
      if (label == "MONO"):
         leaf = LEAF.Mono(**data_organ)
      if (label == "TRADITIONAL"):
         leaf = LEAF.Traditional(**data_organ)
      if (label == "ALTERNATIVE"):
         leaf = LEAF.Alternative(**data_organ)

      return leaf, head_mark_right

   def shatter(self, constructor, kind_stop, head_left):
      branch = None
      source = self.source
      head_right = head_left
      while head_left <= source.size() - 1:
         organ, head_right = self.snip_leaf(head_middle)
         if (organ.KIND == kind_stop):
            break
         head_middle = head_right
      content = source[head_left: head_middle]
      data_organ = {
         "source": content,
         "leftmost": get_left(head_left),
         "rightmost": get_right(head_middle),
         "count_line": count_next_line(head_left),
         "count_glyph": count_next_glyph(head_left),
      }
      branch = constructor(
         source = content,
         leftmost = get_left(head_left),
         rightmost = get_right(head_middle),
         count_line = count_next_line(head_left),
         count_glyph = count_next_glyph(head_left),
      )
      return branch, head_right

   def split_word(self, head_left):
      sink = None
      source = self.source
      head_middle = head_left
      group = self.give_set_delimiter()
      while (head_middle < source.size):
         if (source[head] not in group):
            head_middle += 1
      head_right = head_middle
      while (head_right < self.source.size):
         if (source[head] in group):
            head_right += 1
      sink = source[head_left, head_middle]
      return sink, head_right

   def probe_mark(source):
      glyph = source[0]
      probe = 0
      for probe in range(source.size):
         if (source[probe] == glyph):
            probe += 1
      return source[: probe]

   def get_left(self, head):
      left = self.source[: head]
      segments = self.left.split('\n')
      return segments[-1]

   def get_right(self, head):
      right = self.source[head :]
      segments = self.right.split('\n')
      return segments[0]

   # # # # # # # # # # # # # # # # 

   def count_next_glyph(self, source):
      result = self.count_glyph
      segments = source.split('\n')
      if (not segments.size == 0):
         result += segments[-1].size + 1
      return result

   def count_next_line(self, source):
      segments = source.split('\n')
      return self.count_line + segments.size

   def emit_place(self):
      result = ''
      result += "line " + self.count_line
      result += ", glyph " + self.count_glyph
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def write_tag_block(element, kind):
  return write_tag(
     content = element,
     tag = "div",
     attributes = ["class"],
     values = [kind],
  )

def write_tag_inline(element, kind):
  return write_tag(
     content = element,
     tag = "span",
     attributes = ["class"],
     values = [kind],
  )

def write_tag_image(address, kind):
  return write_tag(
     content = '',
     tag = "img",
     attributes = ["src", "class"],
     values = [address, kind],
  )

def write_tag(**data):
  size = min(attributes.size, values.size)
  result = '<' + tag + 
  for index in range(size)
     result += ' ' + data[attributes][index]
     result += "=\"" + data[values][index]
  result += "\">"
  result += data[content] + ' '
  result += "</" + tag + '>'
  return result

def write_comment(element):
  result = ''
  result += "<!--- "
  result += element + ' '
  result += "--->"
  return result

# # # # # # # # # # # # # # # # 


def get_glyph(label):
  glyphs = get_glyphs()
  if label not in glyphs:
     return None
  return glyphs[label]

def get_label(mark):
  glyph = mark[0]
  labels = get_labels()
  if glyph not in labels:
     return None
  return labels[glyph]

def give_map_glyphs():
  labels = give_labels()
  glyphs = {label: glyph for glyph, label in labels.items()}
  return glyphs

def give_map_labels(self):
   labels = {
      '@': "SERIF_NORMAL",
      '%': "SERIF_ITALIC",
      '#': "SERIF_BOLD",
      '$': "SANS_NORMAL",
      '&': "SANS_BOLD",
      '+': "MONOSPACE",
      '*': "MATH_NEW",
      '^': "MATH_OLD",
      '=': "SECTION",
      '/': "STANZA",
      '\"': "TABLE",
      '|': "IMAGE",
      '_': "SPACE",
      '\'': "NEWLINE",
      '~': "BREAK",
      '\\': "LINK",
      '<': "COMMENT_LEFT",
      '>': "COMMENT_RIGHT",
   }
   return labels

