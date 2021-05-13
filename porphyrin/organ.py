import stem as STEM
import leaf as LEAF
import caution as CAUTION

# Stem: Document
# Stem (bough): Paragraphs, Lines, Rows, Image, Break,
# Stem (twig): Paragraph, Line, Row,
# Stem (frond): Sentence, Verse, Cell
# Leaf: Math, Pseudo, code
# Leaf: Serif_roman, Serif_italic, Serif_bold, Sans_roman, Sans_bold

class Organ(object):

   def __init__(self, **data):
      self.fill_basic(**data)
   
   def fill_basic(**data):
      self.source = data.pop("source", '')
      self.leftmost = data.pop("leftmost", '')
      self.rightmost = data.pop("rightmost", '')
      self.count_line = data.pop("count_line", 0)
      self.count_glyph = data.pop("count_glyph", 0)

   def get_data_modified(self, **changes):
      data = {
         "source": self.source,
         "leftmost": self.leftmost,
         "rightmost": self.rightmost,
         "count_line": self.count_line,
         "count_glyph": self.count_glyph,
      }
      source = changes.pop("source")
      leftmost = changes.pop("leftmost")
      rightmost = changes.pop("rightmost")
      count_line = changes.pop("count_line")
      count_glyph = changes.pop("count_glyph")
      if (source): data[source] = source
      if (leftmost): data[leftmost] = leftmost
      if (rightmost): data[rightmost] = rightmost
      if (count_line): data[count_line] = count_line
      if (count_glyph): data[count_glyph] = count_glyph
      return data

   # # # # # # # # # # # # # # # #

   # # for empty organs:
   # `head_left`, `mark_left`, `probe`
   # # for inhabited organs:
   # `head_left`, `mark_left`,
   # `probe`, `content`,
   # `mark_right`, `head_right`
   def clip_organ(self, head_left):
      results = []
      source = self.source
      tip = source[head_left]
      label = get_label(tip)
      while (probe <= len(source)):
         if (source[probe] == tip):
            probe += 1
      mark_left = source[head_left: probe]

      if (label in {"BREAK", "SPACE", "NEWLINE"}):
         results = [mark_left]
         return result

      mark_right = get_mark_right(mark_left)
      content = source[mark_middle:]
      content = content.split(mark_right, 1)[0]
      result = [mark_left, content]
      return result

   def clip_math(self, head_left):
      results = []
      source = self.source
      tip = source[head_left]
      label = get_label_math(tip)
      if be_letter_math(label) or be_sign_math(label):
         head_right = head_left + 2
         return head_right

      probe_left = head_left + 1
      probe_right = probe_left
      count_round = 1
      count_square = 1
      while (probe_right <= len(source)):
          segments = clip_math(probe_right)
          probe_right += sum(len(segment) for segment in segments)
      head_right = probe_right + 1
      mark_left = source[head_left: head_middle]

   # # # # # # # # # # # # # # # #

   def get_left(self, head):
      left = self.source[: head]
      result = self.left.split('\n')[-1]
      return result

   def get_right(self, head):
      right = self.source[head :]
      result = self.right.split('\n')[0]
      return result

   def count_next_glyph(self, source):
      count = self.count_glyph
      segments = source.split('\n')
      if (len(segments) == 1):
         count += len(segments[0])
         return count
      count = len(segments[-1])
      return count

   def count_next_line(self, source):
      count = self.count_line
      segments = source.split('\n')
      count += len(segments) - 1
      return count

   def emit_place(self):
      result = ''
      result += "line " + self.count_line + ", "
      result += "glyph " + self.count_glyph
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Leaf(Leaf):

   # # for empty organs:
   # `head_left`, `mark_left`, `head_right`
   # # for inhabited organs:
   # `head_left`, `mark_left`,
   # `probe_left`, `content`, `probe_right`,
   # `mark_right`, `head_right`
   def snip_leaf(self, head_left):
      leaf = None
      source = self.source
      segments = clip_organ(head_left)
      mark_left = segments[0]
      mark_right = get_mark_right(mark_left)
      label = get_label(mark_left[0])

      if (label in {"SPACE", "NEWLINE"}):
         head_right = head_left + len(mark_right)
         data_leaf = self.get_data_modified(
            leftmost = get_left(head_left),
            rightmost = get_right(head_right),
         )
         if (label == "SPACE"):
            leaf = LEAF.Space(**data_leaf)
            return leaf, head_right
         if (label == "NEWLINE"):
            leaf = LEAF.Newline(**data_leaf)
            return leaf, head_right

      assert(len(segments) = 3)
      content = segments[1]
      probe_left = head_left + len(mark_left)
      probe_right = probe_left + len(content)
      head_right = probe_right + len(mark_right)

      data_caution = self.get_data_modified(
         "source": mark_left,
         "leftmost": get_left(head_left),
         "rightmost": get_right(probe_left),
      )
      if (probe_right > len(source)):
         caution = CAUTION.Not_matching_mark_leaf(**data_caution)
         caution.panic()
      if not self.be_label_leaf(label)):
         caution = CAUTION.Allowing_only_leaf(**data_caution)
         caution.panic()

      if (label == "LINK"):
         if (self.KIND == "image"):
            self.address = content
            return None, head_right
         elif (hasattr(self, sinks) and len(sinks)):
            self.sinks[-1].address = content
            return None, head_right
         else:
            caution = CAUTION.Disallowing_link(**data_caution)
            caution.panic()

      data_leaf = {
         "source": content,
         "leftmost": get_left(probe_left),
         "rightmost": get_right(probe_right),
         "count_line": count_next_line(mark_left),
         "count_glyph": count_next_glyph(mark_left),
      }
      if (label == "SERIF_NORMAL"):
         leaf = LEAF.Serif_normal(**data_leaf)
      if (label == "SERIF_ITALIC"):
         leaf = LEAF.Serif_italic(**data_leaf)
      if (label == "SERIF_BOLD"):
         leaf = LEAF.Serif_bold(**data_leaf)
      if (label == "SANS_NORMAL"):
         leaf = LEAF.Sans_normal(**data_leaf)
      if (label == "SANS_BOLD"):
         leaf = LEAF.Sans_bold(**data_leaf)
      if (label == "CODE"):
         leaf = LEAF.Code(**data_leaf)
      if (label == "PSEUDO"):
         leaf = LEAF.Pseudo(**data_leaf)
      if (label == "MATH"):
         leaf = LEAF.Math(**data_leaf)
      if (label == "COMMENT_LEFT"):
         leaf = None
      return leaf, head_right

   def snip_tissue_math(self, head_left):
      tissue = None
      source = self.source
      tip = source[head_left]
      label = get_label_math(tip)

      if (be_symbol_math(label)):
         head_right = head_left + 2
         head_right = head_left + len(mark_right)
         mark = source[head_left, head_right]
         data = self.get_data_modified(
            leftmost = get_left(head_left),
            rightmost = get_right(head_right),
         )
         tissue = LEAF.Math_letter(**data)
         return tissue, head_right

      if (be_sign_math(label)):
         head_right = head_left + len(mark_right)
         mark = source[head_left, head_right]
         data = self.get_data_modified(
            leftmost = get_left(head_left),
            rightmost = get_right(head_right),
         )
         tissue = LEAF.Math_sign(**data)
         return tissue, head_right

      mark_left = tip
      mark_right = get_mark_right_math(mark_left)
      content = source[head_left:]
      content = content.split(mark_left, 1)[1]
      content, remain, *_ = content.split(mark_right, 1)[0]
      probe_left = head_left + len(mark_left)
      probe_right = head_left + len(content)
      head_right = probe_right + len(mark_right)

      data_caution = {
         "source": mark_left,
         "leftmost": get_left(head_left),
         "rightmost": get_right(probe_left),
         "count_line": count_next_line(head_left),
         "count_glyph": count_next_glyph(head_left),
      }
      if (remain is None):
         caution = CAUTION.Not_matching_bracket(**data_caution)
         caution.panic()

      data_tissue = {
         "source": content,
         "leftmost": get_left(probe_left),
         "rightmost": get_right(probe_right),
         "count_line": count_next_line(probe_left),
         "count_glyph": count_next_glyph(probe_left),
      }
      tissue = LEAF.Bracket_math(**data_tissue)
      return tissue, head_right

   def snip_tissue_pseudo(self, head_left):
      tissue = None
      source = self.source
      tip = source[head_left]
      label = get_label_pseudo(tip)

      if (be_symbol_pseudo(label)):
         head_right = head_left + 2
         head_right = head_left + len(mark_right)
         mark = source[head_left, head_right]
         data = self.get_data_modified(
            leftmost = get_left(head_left),
            rightmost = get_right(head_right),
         )
         tissue = LEAF.Math_letter(**data)
         return tissue, head_right

      if (be_sign_pseudo(label)):
         head_right = head_left + len(mark_right)
         mark = source[head_left, head_right]
         data = self.get_data_modified(
            leftmost = get_left(head_left),
            rightmost = get_right(head_right),
         )
         tissue = LEAF.Math_sign(**data)
         return tissue, head_right

      mark_left = tip
      mark_right = get_mark_right_pseudo(mark_left)
      content = source[head_left:]
      content = content.split(mark_left, 1)[1]
      content, remain, *_ = content.split(mark_right, 1)[0]
      probe_left = head_left + len(mark_left)
      probe_right = head_left + len(content)
      head_right = probe_right + len(mark_right)

      data_caution = {
         "source": mark_left,
         "leftmost": get_left(head_left),
         "rightmost": get_right(probe_left),
         "count_line": count_next_line(head_left),
         "count_glyph": count_next_glyph(head_left),
      }
      if (remain is None):
         caution = CAUTION.Not_matching_bracket(**data_caution)
         caution.panic()

      data_tissue = {
         "source": content,
         "leftmost": get_left(probe_left),
         "rightmost": get_right(probe_right),
         "count_line": count_next_line(probe_left),
         "count_glyph": count_next_glyph(probe_left),
      }
      tissue = LEAF.Bracket_pseudo(**data_tissue)
      return tissue, head_right

   def snip_tissue_text(self, head_left):
      tissue = None
      source = self.source
      head_middle = head_left
      glyphs_space = set([' ', '\t', '\n'])
      while (head_middle < len(source)):
         if (source[head_middle] not in glyphs_space):
            head_middle += 1
      head_right = head_middle
      while (head_right < len(source)):
         if (source[head_middle] in glyphs_space):
            head_right += 1
      tissue = source[head_left, head_middle]
      return tissue, head_right

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Stem(ORGAN.Organ):

   # # for empty organs:
   # `head_left`, `mark_left`, `head_right`
   # # for inhabited organs:
   # `head_left`, `mark_left`,
   # `probe_left`, `content`, `probe_right`,
   # `mark_right`, `head_right`
   def snip_bough(self, head_left):
      bough = None
      source = self.source
      segments = clip_organ(head_left)
      mark_left = segments[0]
      mark_right = get_mark_right(mark_left)
      label = get_label(mark_left[0])

      if (label == "BREAK"):
         head_right = head_left + len(mark_right)
         data = self.get_data_modified(
            leftmost = get_left(head_left),
            rightmost = get_right(head_right),
         )
         bough = STEM.Break(**data)
         return bough, head_right

      assert(len(segments) = 3)
      content = segments[1]
      probe_left = head_left + len(mark_left)
      probe_right = probe_left + len(content)
      head_right = probe_right + len(mark_right)

      data_caution = self.get_data_modified(
         "source": mark_left,
         "leftmost": get_left(head_left),
         "rightmost": get_right(probe_left),
      )
      labels_macro = {"INSTRUCTION", "DEFINITION_LEFT"}
      if not self.be_label_bough(label)):
         caution = CAUTION.Allowing_only_bough(**data_caution)
         caution.panic()
      if (probe_right > len(source)):
         caution = CAUTION.Not_matching_mark_bough(**data_caution)
         caution.panic()
      if (label in labels_macro and self.expanded):
         caution = CAUTION.Macro_not_gathered(**data_caution)
         caution.panic()

      if (label == "INSTRUCTION"):
         self.instructions.append(content)
         return None, head_right
      if (label == "DEFINITION_LEFT"):
         self.definitions.append(content)
         return None, head_right
      if not self.expanded:
         self.expand()
         self.expanded = True

      data_bough = {
         "source": content,
         "leftmost": get_left(probe_left),
         "rightmost": get_right(probe_right),
         "count_line": count_next_line(mark_left),
         "count_glyph": count_next_glyph(mark_left),
      }
      if (label == "SECTION"):
         bough = STEM.Paragraphs(**data_bough)
      if (label == "STANZA"):
         bough = STEM.Lines(**data_bough)
      if (label == "TABLE"):
         bough = STEM.Rows(**data_bough)
      if (label == "IMAGE"):
         bough = STEM.Image(**data_bough)
      if (label == "BREAK"):
         bough = STEM.Break(**data_bough)
      if (label == "COMMENT_LEFT"):
         bough = None
      return bough, head_right


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

