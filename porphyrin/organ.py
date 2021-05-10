import stem as STEM
import leaf as LEAF
import caution as CAUTION

# Stem: Document
# Stem (bough): Paragraphs, Lines, Rows, Image, Break,
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

   def get_changed_data(self, **change):
      data = {
         source = self.source,
         leftmost = self.leftmost,
         rightmost = self.rightmost,
         count_line = self.count_line,
         count_glyph = self.count_glyph,
      }
      source = change.pop("source")
      leftmost = change.pop("leftmost")
      rightmost = change.pop("rightmost")
      count_line = change.pop("count_line")
      count_glyph = change.pop("count_glyph")
      if (source): data.source = source
      if (leftmost): data.leftmost = leftmost
      if (rightmost): data.rightmost = rightmost
      if (count_line): data.count_line = count_line
      if (count_glyph): data.count_glyph = count_glyph
      return data

   # # # # # # # # # # # # # # # #

   def snip_bough(self, head_mark_left):
      bough = None
      source = self.source[head_mark_left:]
      mark_left, content = probe(head_mark_left)
      label = get_label(mark_left)
      mark_right = get_mark_right(mark_left)

      if (label == "BREAK"):
         head_mark_right = head_mark_right + len(mark_right)
         data = self.get_changed_data(
            leftmost = get_left(head_mark_left),
            rightmost = get_right(head_mark_right),
         )
         bough = STEM.Break(**data)
         return bough, head_mark_right

      content = source
      content = content.split(mark_left, 2)[1]
      head_content_left = head_mark_left + len(mark_left)
      head_content_right = head_mark_left + len(content)
      head_mark_right = head_content_right + len(mark_right)

      data = {
         "source": mark_left,
         "leftmost": get_left(head_mark_left),
         "rightmost": get_right(head_content_left),
         "count_line": count_next_line(head_mark_left),
         "count_glyph": count_next_glyph(head_mark_left),
      }
      if (label == None):
         caution = CAUTION.Not_matching_mark_bough(**data)
         caution.panic()
      if not self.be_label_bough(label)):
         caution = CAUTION.Allowing_only_bough(**data)
         caution.panic()

      data = {
         "source": content,
         "leftmost": get_left(head_content_left),
         "rightmost": get_right(head_content_right),
         "count_line": count_next_line(head_content_left),
         "count_glyph": count_next_glyph(head_content_left),
      }
      if (label == "SECTION"):
         bough = STEM.Paragraphs(**data)
      if (label == "STANZA"):
         bough = STEM.Lines(**data)
      if (label == "TABLE"):
         bough = STEM.Rows(**data)
      if (label == "IMAGE"):
         bough = STEM.Image(**data)
      if (label == "BREAK"):
         bough = STEM.Break(**data)
      if (label == "COMMENT"):
         bough = STEM.Comment(**data)

      return bough, head_mark_right

   def snip_leaf(self, head_mark_left):
      leaf = None
      source = self.source[head_mark_left:]
      mark_left, content = probe(head_mark_left)
      label = get_label(mark_left)
      mark_right = get_mark_right(mark_left)

      if (label == "SPACE") or (label == "NEWLINE"):
         head_mark_right = head_mark_right + len(mark_right)
         data_organ = self.get_changed_data(
            leftmost = get_left(head_mark_left),
            rightmost = get_right(head_mark_right),
         )
      if (label == "SPACE"):
         leaf = LEAF.Space(**data_organ)
         return leaf, head_mark_right
      if (label == "NEWLINE"):
         leaf = LEAF.Newline(**data_organ)
         return leaf, head_mark_right

      content = source
      content = content.split(mark_left, 2)[1]
      head_content_left = head_mark_left + len(mark_left)
      head_content_right = head_mark_left + len(content)
      head_mark_right = head_content_right + len(mark_right)

      data = {
         "source": mark_left,
         "leftmost": get_left(head_mark_left),
         "rightmost": get_right(head_content_left),
         "count_line": count_next_line(head_mark_left),
         "count_glyph": count_next_glyph(head_mark_left),
      }
      if (label == None):
         caution = CAUTION.Not_matching_mark_leaf(**data)
         caution.panic()
      if not self.be_label_bough(label)):
         caution = CAUTION.Allowing_only_leaf(**data)
         caution.panic()

      data = {
         "source": content,
         "leftmost": get_left(head_content_left),
         "rightmost": get_right(head_content_right),
         "count_line": count_next_line(head_content_left),
         "count_glyph": count_next_glyph(head_content_left),
      }
      if (label == "LINK"):
         if (len(self.sinks) = 0):
            self.address = content
         else:
            sinks[-1].address = content
         return None, head_mark_right
      if (label == "SERIF_NORMAL"):
         leaf = LEAF.Serif_normal(**data)
      if (label == "SERIF_ITALIC"):
         leaf = LEAF.Serif_italic(**data)
      if (label == "SERIF_BOLD"):
         leaf = LEAF.Serif_bold(**data)
      if (label == "SANS_NORMAL"):
         leaf = LEAF.Sans_normal(**data)
      if (label == "SANS_BOLD"):
         leaf = LEAF.Sans_bold(**data)
      if (label == "MONO"):
         leaf = LEAF.Mono(**data)
      if (label == "TRADITIONAL"):
         leaf = LEAF.Traditional(**data)
      if (label == "ALTERNATIVE"):
         leaf = LEAF.Alternative(**data)
      if (label == "COMMENT"):
         bough = STEM.Comment(**data)

      return leaf, head_mark_right

   def shatter(self, kind_stop, constructor, head_left):
      branch = None
      source = self.source
      head_right = head_left
      while head_left <= len(source) - 1:
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
      group = self.give_group_cut()
      while (head_middle < len(source)):
         if (source[head] not in group):
            head_middle += 1
      head_right = head_middle
      while (head_right < len(self.source)):
         if (source[head] in group):
            head_right += 1
      sink = source[head_left, head_middle]
      return sink, head_right

   def probe(self, head_mark_left):
      tip = source[0]
      probe = 0
      for probe in range(len(source) - head_mark_left):
         if (self.source[head_mark_left + probe] == tip):
            probe += 1
      mark_left = source[: probe]
      content = source
      content = content.split(mark_left, 1)[1]
      content = content.split(mark_right, 1)[0]
      return mark, content

   def get_left(self, head):
      left = self.source[: head]
      result = self.left.split('\n')[-1]
      return result

   def get_right(self, head):
      right = self.source[head :]
      result = self.right.split('\n')[0]
      return result

   def count_next_glyph(self, source):
      result = self.count_glyph
      segments = source.split('\n')
      if (not len(segments) == 0):
         result += len(segments[-1]) + 1
      return result

   def count_next_line(self, source):
      result = self.count_glyph
      segments = source.split('\n')
      result = self.count_line + len(segments)
      return result

   def emit_place(self):
      result = ''
      result += "line " + self.count_line + ", "
      result += "glyph " + self.count_glyph
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def get_mark_right(self, mark_left):
   assert(len([glyph for glyph in mark_left]) == 1)
   tip = mark_left[0]
   mark_right = mark_left
   comment_left = get_tip("COMMENT_LEFT")
   comment_right = get_tip("COMMENT_RIGHT")
   if (tip == comment_left):
      mark_right = mark_left.translate(
         mark_left.maketrans(comment_left, comment_right)
      )
   return mark_right

def write_element(**data):
  size = min(len(attributes), len(values))
  result = '<' + tag + 
  for index in range(size)
     result += ' ' + data[attributes][index]
     result += "=\"" + data[values][index]
  result += "\">"
  result += data[content] + ' '
  result += "</" + tag + '>'
  return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def get_tip(label):
  tips = get_tips()
  if label not in tips:
     return None
  return tips[label]

def get_label(mark):
  tip = mark[0]
  labels = get_labels()
  if tip not in labels:
     return None
  return labels[tip]

def give_table_tip():
  labels = give_group_label()
  tips = {label: tip for tip, label in labels.items()}
  return tips

def give_table_label(self):
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

def label_be_bough(label):
   labels = set([
      "SECTION",
      "STANZA",
      "TABLE",
      "IMAGE",
      "BREAK",
   ])
   return label in labels

def label_be_leaf(label):
   labels = set([
      "SERIF_NORMAL",
      "SERIF_ITALIC",
      "SERIF_BOLD",
      "SANS_NORMAL",
      "SANS_BOLD",
      "MONO",
      "ALTERNATIVE",
      "TRADITIONAL",
      "LINK",
      "COMMENT_LEFT",
   ])
   return label in labels



