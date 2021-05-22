import stem as STEM
import leaf as LEAF
import tissue as TISSUE
import caution as CAUTION
import aid as AID

# # Stem: Document
# # Stem (bough): Paragraphs, Lines, Rows, Image, Break,
# # Stem (twig): Paragraph, Line, Row,
# # Stem (frond): Phrase, Verse, Cell
# # Leaf: Math, Pseudo, Mono
# # Leaf: Serif_roman, Serif_italic, Serif_bold, Sans_roman, Sans_bold

class Organ(object):

   def __init__(self, **data):
      self.fill_basic(**data)
   
   def fill_basic(**data):
      self.source = data.pop("source", '')
      self.leftmost = data.pop("leftmost", '')
      self.rightmost = data.pop("rightmost", '')
      self.count_line = data.pop("count_line", 0)
      self.count_glyph = data.pop("count_glyph", 0)

   def get_data(head_left, head_right):
      data = {
         "source" : mark_left,
         "leftmost" : get_left(head_left),
         "rightmost" : get_right(head_right),
         "count_line" : count_next_line(head_left),
         "count_glyph" : count_next_glyph(head_left),
      }
      return data

   def shift(size, head_left):
      source = self.source
      head_right = head_left
      positive = True
      if (size < 0):
         positive = False
      for _ in range(size):
         whitespaces = {' ', '\t', '\n'}
         head_right += 1
         while (head_right <= len(source)):
            if (source[head_right] in whitespaces):
               if (positive):
                  head_right += 1
               else:
                  head_right -= 1
            else:
               break
      return head_right

   def find_greedy(self, mark_left, mark_right, head_left):
      head_right = head_left
      fragment = self.source[head_left:]
      fragment = fragment.split(mark_left, 1)[1]
      content = fragment.split(mark_right, 1)[0]
      head_right = head_left + len(mark_left) + len(content) + len(mark_right)
      return head_right

   def find_balanced(self, tip_left, tip_right, head_left):
      head_right = head_left
      if not (source[head_left] == tip_left):
         return head_left

      count = 0
      while (head_right <= len(source)):
         tip_probe = source[head_right]
         if (tip_probe == tip_left):
            count += 1
         if (tip_probe == tip_right):
            count -= 1
         head_right += 1
         if (count == 0):
            break
      return head_right

   def probe_mark(self, head_left):
      mark = ''
      source = self.source
      tip = source[head_left]
      head_right = head_left
      while (head_right <= len(source)):
         if not (source[head_right] == tip):
            break
         head_right += 1
      mark_left = source[head_left: head_right]

   def balance_math(self, head_left):
      tip_left = self.source[head_left]
      tip_right = get_tip_right_math(tip_left)
      if not tip_right:
         return head_left
      return self.balance(tip_left, tip_right, head_left)

   def get_fragment_left(self, head):
      left = self.source[: head]
      result = self.left.split('\n')[-1]
      return result

   def get_fragment_right(self, head):
      right = self.source[head :]
      result = self.right.split('\n')[0]
      return result

   def count_next_glyph(self, head):
      count = self.count_glyph
      left = self.source[: head]
      segments = left.split('\n')
      if (len(segments) == 1):
         count += len(segments[0])
         return count
      count = len(segments[-1])
      return count

   def count_next_line(self, head):
      count = self.count_line
      left = self.source[: head]
      segments = left.split('\n')
      count += len(segments) - 1
      return count

   def compare(self, target, head):
      token = self.source[head: head + len(target)]
      return (token == target)

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
      bough = None
      source = self.source
      mark_left = probe_mark(head_left)
      mark_right = get_mark_right(mark_left)
      label = get_label(mark_left[0])

      if (label == "BREAK"):
         head_right = head_left + len(mark_right)
         data = self.get_data(head_left, head_left)
         bough = STEM.Break(**data)
         return bough

      head_right = self.find_greedy(mark_left, mark_right, head_left)
      probe_left = head_left + len(mark_left)
      probe_right = probe_left + len(content)
      content = source[probe_left, probe_right]

      data = self.get_data(head_left, probe_left)
      if not AID.be_label_bough(label)):
         caution = CAUTION.Allowing_only_bough(**data)
         caution.panic()
      if (probe_right > len(source)):
         caution = CAUTION.Not_matching_mark_bough(**data)
         caution.panic()
      if (AID.be_macro_start(label) and self.expanded):
         caution = CAUTION.Macro_not_gathered(**data)
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

      data = self.get_data(probe_left, probe_right)
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
      leaf = None
      source = self.source
      mark_left = probe_mark(head_left)
      mark_right = get_mark_right(mark_left)
      label = get_label(mark_left[0])

      if (label in AID.be_hollow_leaf(label)):
         head_right = head_left + len(mark_right)
         data = self.get_data(head_left, head_left)
         if (label == "SPACE"):
            leaf = LEAF.Space(**data)
            return leaf
         if (label == "NEWLINE"):
            leaf = LEAF.Newline(**data)
            return leaf

      head_right = self.find_greedy(mark_left, mark_right, head_left)
      probe_left = head_left + len(mark_left)
      probe_right = probe_left + len(content)
      content = source[probe_left, probe_right]

      data = self.get_data(head_left, probe_left)
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
         elif (hasattr(self, sinks) and len(sinks) is not None):
            self.sinks[-1].address = content
            return None, head_right
         else:
            caution = CAUTION.Disallowing_link(**data_caution)
            caution.panic()

      data_leaf = {
         "source" : content,
         "leftmost" : get_left(probe_left),
         "rightmost" : get_right(probe_right),
         "count_line" : count_next_line(probe_left),
         "count_glyph" : count_next_glyph(probe_left),
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
      if (label == "mono"):
         leaf = LEAF.Mono(**data_leaf)
      if (label == "PSEUDO"):
         leaf = LEAF.Pseudo(**data_leaf)
      if (label == "MATH"):
         leaf = LEAF.Math(**data_leaf)
      if (label == "COMMENT_LEFT"):
         leaf = None
      return leaf, head_right

   def shatter_stem(self, kind_stop, constructor, head_left):
      branch = None
      source = self.source
      head_right = head_left
      head_middle = head_left
      while head_right <= len(source) - 1:
         head_middle = head_right
         head_right, leaf = self.snip_leaf(head_right)
         size_leaf = len(leaf.source)
         if (leaf.KIND == kind_stop):
            break
         head_middle += size_leaf
      data = self.get_data(head_left, head_middle)
      branch = constructor(**data)
      return branch, head_right

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Leaf(Organ):

   def tune_text(self):
      sink = self.source
      glyphs_mark = set([])
      glyphs_mark.add(AID.get_tip("SERIF_NORMAL"))
      glyphs_mark.add(AID.get_tip("SERIF_ITALIC"))
      glyphs_mark.add(AID.get_tip("SERIF_BOLD"))
      glyphs_mark.add(AID.get_tip("SANS_NORMAL"))
      glyphs_mark.add(AID.get_tip("SANS_BOLD"))
      glyphs_mark.add(AID.get_tip("COMMENT_LEFT"))
      glyphs_mark.add(AID.get_tip("COMMENT_RIGHT"))
      glyphs_space = set([' ', '\t', '\n'])
      sink = self.remove_token(glyphs_mark, sink)
      sink = self.erase_token(glyphs_space, sink)
      return sink

   def tune_code(self):
      sink = self.source
      glyphs_space = set([' ', '\t', '\n'])
      sink = self.erase_token(glyphs_space)
      return sink

   def tune_hypertext(self):
      sink = self.source
      escapes = {
         '<': "&lt;",
         '>': "&gt;",
         '&': "&amp;",
         '\"': "&quote;",
         '\'': "&apos;",
      }
      sink = self.replace_token(sink, escapes)
      return sink

   def tune_comment(self):
      sink = self.source
      escapes = {
         '----': '-',
         '---': '-',
         '--': '-',
      }
      sink = self.replace_token(sink, escapes)
      return sink

   def remove_token(self, tokens):
      sink = self.source
      for glyph in tokens:
         table = sink.maketrans(glyph, '')
         sink = sink.translate(table)
      return sink

   def erase_token(self, tokens):
      sink = self.source
      for glyph in tokens:
         table = sink.maketrans(glyph, ' ')
         sink = sink.translate(table)
      ' '.join(sink.split())
      return sink

   def replace_token(self, tokens):
      sink = self.source
      for glyph in tokens:
         table = sink.maketrans(glyph, tokens[glyph])
         sink = sink.translate(table)
      return sink

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

   def write_text(self):
      result = ''
      result += write_element(
         content = sink,
         tag = self.give_tag_text(),
         attributes = self.give_attributes_text(),
         values = self.give_values_text(),
      )
      return result

   def give_tag_text(self):
      assert(hasattr(self, 'address'))
      if self.address:
         tag = self.TAG_PLAIN
      else:
         tag = 'a'

   def give_attributes_text(self):
      assert(hasattr(self, 'address'))
      attributes = ["class"]
      if self.address:
         attributes.append("href")
      return attributes

   def give_values_text(self):
      assert(hasattr(self, 'KIND'))
      assert(hasattr(self, 'address'))
      values = [self.KIND]
      if self.address:
         values.append(self.address)
      return values

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Tissue(Organ):

   def snip_tissue_math(self, head_left):
      tissue = None
      source = self.source
      tip_left = source[head_left]
      label_left = AID.get_label_math(tip_left)
      head_right = self.move(1, head_left)
      if not AID.be_start_math(label_left):
         data = self.give_data(head_left, head_right)
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()

      if (AID.be_start_symbol_math(label_right)):
         head_right = self.move(2, head_left)
      if (AID.be_accent_math(label_right)):
         head_right = self.move(2, head_right)
      if (head_right > len(source)):
         data = self.give_data(head_left, len(source))
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      data = self.give_data(head_left, head_right)
      tissue = TISSUE.Math_symbol(**data)
      return tissue, head_right

      if (AID.be_start_box_math(label_left)):
         tip_right = AID.get_tip_right_math(tip_left)
         head_right = self.find_balanced(tip_left, tip_right, head_left)
         probe_left = self.move(1, head_left)
         probe_right = self.move(-1, head_right)
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

   def snip_tissue_pseudo(self, head_left):
      tissue = None
      source = self.source
      tip_left = source[head_left]
      label_left = AID.get_label_math(tip_left)
      head_right = self.move(1, head_left)
      if not AID.be_start_pseudo(label_left):
         data = self.give_data(head_left, head_right)
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()

      if (AID.be_start_symbol_pseudo(label_right)):
         head_right = self.move(2, head_left)
      if (head_right > len(source)):
         data = self.give_data(head_left, len(source))
         caution = CAUTION.Not_being_valid_symbol(**data)
         caution.panic()
      data = self.give_data(head_left, head_right)
      tissue = TISSUE.Pseudo_symbol(**data)
      return tissue, head_right

      if (AID.be_start_box_pseudo(label_left)):
         tip_right = AID.get_tip_right_pseudo(tip_left)
         head_right = self.find_balanced(tip_left, tip_right, head_left)
         probe_left = self.move(1, head_left)
         probe_right = self.move(-1, head_right)
         data = give_data(probe_left, probe_right)
         if (label_left = "ROUND_LEFT"):
            tissue = TISSUE.Pseudo_pair(**data)
         if (label_left = "SQUARE_LEFT"):
            tissue = TISSUE.Pseudo_triplet(**data)
         if (label_left = "CURLY_LEFT"):
            tissue = TISSUE.Pseudo_tuple(**data)
         if (label_left = "SANS"):
            tissue = TISSUE.Pseudo_sans(**data)
         if (label_left = "SERIF"):
            tissue = TISSUE.Pseudo_serif(**data)
         if (label_left = "MONO"):
            tissue = TISSUE.Pseudo_mono(**data)
         if (label_left = "MONO"):
            tissue = TISSUE.Pseudo_mono(**data)
         if (label_left = "CHECK"):
            tissue = None
      return tissue, head_right


