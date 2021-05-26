from . import aid as AID

# # Stem: Document
# # Stem (bough): Paragraphs, Lines, Rows, Image, Break,
# # Stem (twig): Paragraph, Line, Row, Newline
# # Stem (frond): Phrase, Verse, Cell, Space
# # Leaf: Math, Pseudo,
# # Leaf: Serif_roman, Serif_italic, Serif_bold,
# # Leaf: Sans_roman, Sans_bold, Mono,

class Organ(object):

   def __init__(self, **data):
      self.fill_basic(**data)
   
   def fill_basic(self, **data):
      self.source = data.pop("source", '').rstrip()
      self.leftmost = data.pop("leftmost", '')
      self.rightmost = data.pop("rightmost", '')
      self.count_line = data.pop("count_line", 0)
      self.count_glyph = data.pop("count_glyph", 0)
      if (hasattr(self, "KIND")):
         print(f"Creating a \"{self.KIND}\"...", flush = True)
      print(f"    Source: {self.source}", flush = True)

   def give_data(self, head_left, head_right):
      data = {
         "source" : self.source[head_left, head_right],
         "leftmost" : self.get_fragment_left(head_left),
         "rightmost" : self.get_fragment_right(head_right),
         "count_line" : self.count_next_line(head_left),
         "count_glyph" : self.count_next_glyph(head_left),
      }
      return data

   def move(self, size, head_left):
      head_right = head_left
      positive = True
      if (size < 0):
         positive = False
      for _ in range(abs(size)):
         whitespaces = {' ', '\t', '\n'}
         head_right += 1
         while (head_right <= len(self.source)):
            if (self.source[head_right] in whitespaces):
               if (positive): head_right += 1
               else: head_right -= 1
            else: break
      return head_right

   def find_greedy(self, mark_left, mark_right, head_left):
      head_right = head_left
      fragment = self.source[head_left:]
      fragment = fragment.split(mark_left, 1)[1]
      content = fragment.split(mark_right, 1)[0]
      head_right = len(mark_left) + len(content) + len(mark_right) + head_left
      return head_right

   def find_balanced(self, mark_left, mark_right, head_left):
      probe_left = self.move(len(mark_left), head_left)
      probe_right = probe_left
      token = self.source[head_left: head_left + len(mark_left)]
      if not (token == mark_left):
         return head_left
      count = 0
      while (probe_right <= len(self.source) - len(mark_right)):
         head_right = probe_right + len(mark_right)
         mark_probe = self.source[head_right: probe_right]
         if (mark_probe == mark_left):
            count += 1
         if (mark_probe == mark_right):
            count -= 1
         head_right = self.move(1, head_right)
         if (count == 0):
            break
      return head_right

   def probe_mark(self, head_left):
      mark = ''
      tip = self.source[head_left]
      head_right = head_left
      while (head_right <= len(self.source)):
         if not (self.source[head_right] == tip):
            break
         head_right = self.move(1, head_right)
      mark_left = self.source[head_left: head_right]

   def get_fragment_left(self, head):
      left = self.source[: head]
      sink = self.left.split('\n')[-1]
      return sink

   def get_fragment_right(self, head):
      right = self.source[head :]
      sink = self.right.split('\n')[0]
      return sink

   def count_next_glyph(self, head):
      left = self.source[: head]
      fragments = left.split('\n')
      if (len(fragments) == 1):
         self.count_glyph += len(fragments[0])
         return self.count_glyph
      self.count_glyph = len(fragments[-1])
      return self.count_glyph

   def count_next_line(self, head):
      count = self.count_line
      left = self.source[: head]
      fragments = left.split('\n')
      count += len(fragments) - 1
      return count

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Stem(Organ):

   # # for empty organs:
   # `head_left`, `mark_left`, `head_right`
   # # for inhabited organs:
   # `head_left`, `mark_left`,
   # `probe_left`, `content`, `probe_right`,
   # `mark_right`, `head_right`
   def snip_bough(self, head_left):
      from .organ import Stem as STEM
      bough = None
      mark_left = self.probe_mark(head_left)
      mark_right = AID.get_mark_right(mark_left)
      label = AID.get_label(mark_left[0])

      if (label == "BREAK"):
         head_right = self.move(len(mark_left), head_left)
         data = self.give_data(head_left, head_left)
         bough = STEM.Break(**data)
         return bough

      head_right = self.find_greedy(mark_left, mark_right, head_left)
      probe_left = self.move(len(mark_left), head_left)
      probe_right = self.move(-len(mark_right), head_right)
      content = self.source[probe_left, probe_right]

      data = self.give_data(head_left, probe_left)
      if not AID.be_start_bough(label):
         from .caution import Allowing_only_bough
         caution = Allowing_only_bough(**data)
         caution.panic()
      elif (probe_right > len(self.source)):
         from .caution import Not_matching_mark_bough
         caution = Not_matching_mark_bough(**data)
         caution.panic()
      elif (AID.be_macro_start(label) and self.expanded):
         from .caution import Macro_not_gathered
         caution = Macro_not_gathered(**data)
         caution.panic()

      if (label == "INSTRUCTION"):
         self.instructions.append(content)
         return None, head_right
      elif (label == "DEFINITION_LEFT"):
         self.definitions.append(content)
         return None, head_right
      elif not self.expanded:
         self.expand()
         self.expanded = True

      data = self.give_data(probe_left, probe_right)
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
      if (label == "COMMENT_LEFT"):
         bough = None
      return bough, head_right

   # # for empty organs:
   # `head_left`, `mark_left`, `head_right`
   # # for inhabited organs:
   # `head_left`, `mark_left`,
   # `probe_left`, `content`, `probe_right`,
   # `mark_right`, `head_right`
   def snip_leaf(self, head_left):
      from .organ import Leaf as LEAF
      leaf = None
      mark_left = probe_mark(head_left)
      mark_right = AID.get_mark_right(mark_left)
      label = AID.get_label(mark_left[0])

      if (label in AID.be_hollow_leaf(label)):
         head_right = self.move(len(mark_left), head_left)
         data = self.give_data(head_left, head_right)
         if (label == "SPACE"):
            leaf = LEAF.Space(**data)
            return leaf
         if (label == "NEWLINE"):
            leaf = LEAF.Newline(**data)
            return leaf

      head_right = self.find_greedy(mark_left, mark_right, head_left)
      probe_left = self.move(len(mark_left), head_left)
      probe_right = self.move(-len(mark_right), head_right)
      content = self.source[probe_left, probe_right]

      data = self.give_data(head_left, probe_left)
      if (probe_right > len(self.source)):
         from .caution import Not_matching_mark_leaf
         caution = Not_matching_mark_leaf(**data)
         caution.panic()
      if not self.be_start_leaf(label):
         from .caution import Allowing_only_leaf
         caution = Allowing_only_leaf(**data)
         caution.panic()

      if (label == "LINK"):
         data = self.give_data(probe_left, probe_right)
         if (self.KIND == "image"):
            self.address = self.tune_hypertext(content)
            return None, head_right
         elif (len(sinks) > 0):
            self.sinks[-1].address = self.tune_hypertext(content)
            return None, head_right
         else:
            from .caution import Disallowing_link
            caution = Disallowing_link(**data)
            caution.panic()

      data = self.give_data(probe_left, probe_right)
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
      if (label == "PSEUDO"):
         leaf = LEAF.Pseudo(**data)
      if (label == "MATH"):
         leaf = LEAF.Math(**data)
      if (label == "COMMENT_LEFT"):
         leaf = None
      return leaf, head_right

   def shatter_stem(self, kind_stop, constructor, head_left):
      branch = None
      head_right = head_left
      head_middle = head_left
      while head_right < len(self.source):
         head_middle = head_right
         leaf, head_right = self.snip_leaf(head_right)
         if (leaf.KIND == kind_stop):
            break
         head_middle = head_right
      data = self.give_data(head_left, head_middle)
      branch = constructor(**data)
      return branch, head_right

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Leaf(Organ):

   def write_text(self, content):
      sink = ''
      sink += write_element(
         content = content,
         tag = self.give_tag_text(),
         attributes = self.give_attributes_text(),
         values = self.give_values_text(),
      )
      return sink

   def give_tag_text(self):
      assert(hasattr(self, "address"))
      assert(hasattr(self, "TAG_PLAIN"))
      if self.address:
         tag = self.TAG_PLAIN
      else:
         tag = 'a'

   def give_attributes_text(self):
      assert(hasattr(self, "address"))
      attributes = ["class"]
      if self.address:
         attributes.append("href")
      return attributes

   def give_values_text(self):
      assert(hasattr(self, "KIND"))
      assert(hasattr(self, "address"))
      values = [self.KIND]
      if self.address:
         values.append(self.address)
      return values

   def write_math_bracket(self, mark_left, mark_right):
      sink = ''
      content = ''
      head = 0
      content += mark_left
      while (head < len(self.source)):
         tissue, head = self.snip_tissue_math(head)
         content = tissue.write() + ' '
      content += mark_right
      sink = self.write_math_outside(content)
      return sink

   def write_math_outside(self, content):
      assert(hasattr(self, "OUTSIDE"))
      kind = "math"
      tag = "span"
      sink = ''
      if (self.OUTSIDE):
         content = "\\( " + content + " \\)"
         sink = write_element(
            content = content,
            tag = tag,
            attributes = ["class"],
            values = [kind],
         )
      else:
         sink = content
      return sink

   # # # # # # # # # # # # # # # #

   def snip_tissue_math(self, head_left):
      from .organ import Tissue as TISSUE
      tissue = None
      tip_left = self.source[head_left]
      label_left = AID.get_label_math(tip_left)
      head_right = self.move(1, head_left)
      if not AID.be_start_math(label_left):
         data = self.give_data(head_left, head_right)
         from .caution import Not_being_valid_symbol
         caution = Not_being_valid_symbol(**data)
         caution.panic()

      if (label_left == "PLAIN"):
         probe_left = self.move(1, head_left)
         tip_left = self.source[probe_left]
         label_left = AID.get_label_math(tip_left)
         if not AID.be_bracket_math(label_left):
            head_right = self.move(1, probe_left)
            data = self.give_data(head_left, head_right)
            tissue = TISSUE.Math_plain(**data)
            return tissue, head_right

         tip_right = AID.get_tip_right_math(tip_left)
         head_right = self.find_balanced(tip_left, tip_right, probe_left)
         probe_left = self.move(1, probe_left)
         probe_right = self.move(-2, head_right)
         data = give_data(probe_left, probe_right)
         if (label_left == "START_PAIR"):
            tissue = TISSUE.Math_bracket_round(**data)
         if (label_left == "START_TRIPLET"):
            tissue = TISSUE.Math_bracket_square(**data)
         if (label_left == "START_TUPLE"):
            tissue = TISSUE.Math_bracket_curly(**data)
         if (label_left == "ORDER_LEFT"):
            tissue = TISSUE.Math_bracket_angle(**data)
         if (label_left == "ARROW_LEFT"):
            tissue = TISSUE.Math_bracket_line(**data)
         return tissue, head_right

      if (AID.be_start_symbol_math(label_left)):
         head_right = self.move(2, head_left)
         tip_right = self.source[head_right]
         label_right = AID.get_label_math(tip_right)
         if (AID.be_accent_math(label_right)):
            head_right = self.move(2, head_right)
         if (head_right > len(self.source)):
            data = self.give_data(head_left, len(self.source))
            from .caution import Not_being_valid_symbol
            caution = Not_being_valid_symbol(**data)
            caution.panic()
         data = self.give_data(head_left, head_right)
         if (AID.be_letter_math(label_left)):
            tissue = TISSUE.Math_letter(**data)
         elif (AID.be_sign_math(label_left)):
            tissue = TISSUE.Math_sign(**data)
         return tissue, head_right
      return tissue, head_right

      assert(AID.be_start_box_math(label_left))
      data = give_data(probe_left, probe_right)
      if (label_left == "PAIR_LEFT"):
         tissue = TISSUE.Math_pair(**data)
      if (label_left == "TRIPLET_LEFT"):
         tissue = TISSUE.Math_triplet(**data)
      if (label_left == "TUPLE_LEFT"):
         tissue = TISSUE.Math_tuple(**data)
      if (label_left == "SERIF"):
         tissue = TISSUE.Math_serif(**data)
      if (label_left == "SANS"):
         tissue = TISSUE.Math_sans(**data)
      if (label_left == "MONO"):
         tissue = TISSUE.Math_mono(**data)
      if (label_left == "CHECK"):
         tissue = None
      return tissue, head_right

   # # # # # # # # # # # # # # # #

   def snip_tissue_pseudo(self, head_left):
      from .organ import Tissue as TISSUE
      tissue = None
      tip_left = self.source[head_left]
      label_left = AID.get_label_math(tip_left)
      head_right = self.move(1, head_left)
      if not AID.be_start_pseudo(label_left):
         data = self.give_data(head_left, head_right)
         from .caution import Not_being_valid_symbol
         caution = Not_being_valid_symbol(**data)
         caution.panic()

      if (AID.be_start_symbol_pseudo(label_left)):
         head_right = self.move(2, head_left)
         if (head_right > len(self.source)):
            data = self.give_data(head_left, len(self.source))
            from .caution import Not_being_valid_symbol
            caution = Not_being_valid_symbol(**data)
            caution.panic()
         data = self.give_data(head_left, head_right)
         if (AID.be_letter_pseudo(label_left)):
            tissue = TISSUE.Pseudo_letter(**data)
         elif (AID.be_sign_pseudo(label_left)):
            tissue = TISSUE.Pseudo_letter(**data)
         return tissue, head_right

      if (AID.be_start_bracket_pseudo(label_left)):
         tip_left = self.source[head_left]
         tip_right = AID.get_tip_right_pseudo(tip_left)
         head_right = self.find_balanced(tip_left, tip_right, head_left)
         probe_left = self.move(1, head_left)
         probe_right = self.move(-1, head_right)
         data = give_data(probe_left, probe_right)
         if (label_left == "START_ROUND"):
            tissue = TISSUE.Pseudo_round(**data)
         if (label_left == "START_SQUARE"):
            tissue = TISSUE.Pseudo_square(**data)
         if (label_left == "START_CURLY"):
            tissue = TISSUE.Pseudo_curly(**data)
         if (label_left == "START_COMMENT"):
            tissue = TISSUE.Pseudo_curly(**data)
         if (label_left == "SERIF"):
            tissue = TISSUE.Pseudo_serif(**data)
         if (label_left == "SANS"):
            tissue = TISSUE.Pseudo_sans(**data)
         if (label_left == "MONO"):
            tissue = TISSUE.Pseudo_mono(**data)
         if (label_left == "CHECK"):
            tissue = None
      return tissue, head_right

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Caution(Organ):

   def __init__(self, **data):
      source = data.pop("source", '').rstrip()
      leftmost = data.pop("leftmost", '')
      rightmost = data.pop("rightmost", '')
      count_line = data.pop("count_line", 0)
      count_glyph = data.pop("count_glyph", 0)
      message_left = ''
      message_right = ''

   def panic(self):
      self.warn()
      raise SystemExit()

   def warn(self):
      color_stress = "\033[93m"
      color_normal = "\033[0m"
      print("At ", place.emit(), ":\n")
      print(
         "      ", leftmost, ' ',
         color_stress, token_error,
         color_normal, rightmost, '\n'
      )
      print(
         message_left,
         color_stress, token_error,
         color_normal, message_right
      )
