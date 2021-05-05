import organ as ORGAN
import leaf as leaf
import caution as CAUTION


class Document(object):

   kine = "document"

   def parse(self):
      head = 0
      while head <= self.source.size() - 1:
         organ, head = self.snip_bough(head)
         sinks.append(organ)

   def write(self):
      result = ''
      for bough in self.sinks:
         result += bough.write()
      return result

   def snip(self, head_mark_left):
      source = self.source
      mark = probe_mark(source)
      label = get_label(mark)
      segments = source.split(mark, 2)
      content = segments[1]
      head_content_left = head + mark.size
      head_content_right = head + mark.size + content.size
      head_mark_right = head + 2 * mark.size + content.size

      data_organ = {
         "source": content,
         "leftmost": get_left(head_content_left),
         "rightmost": get_right(head_content_right),
         "count_line": get_next_count_line(head_content_left),
         "count_character": get_next_count_character(head_content_left),
      }
      data_caution = {
         "token": mark,
         "fragment_left": get_left(head_mark_left),
         "fragment_right": get_right(head_content_left),
         "count_line": get_next_count_line(head_mark_left),
         "count_character": get_next_count_character(head_mark_left),
      }

      if (label == None):
         caution = Not_match_boundary_bough(**data_caution)
         CAUTION.panic()
      if (self.be_label_leaf(label)):
         caution = Occurring_outer_scope_leaf(**data_caution)
         CAUTION.panic()

      if (label == "SECTION"):
         sinks.append(STEM.Section(**data_organ))
      if (label == "STANZA"):
         sinks.append(STEM.Stanza(**data_organ))
      if (label == "TABLE"):
         sinks.append(STEM.Table(**data_organ))
      if (label == "IMAGE"):
         sinks.append(STEM.Image(**data_organ))
      if (label == "BREAK"):
         sinks.append(STEM.Break(**data_organ))

      return content, head_mark_right


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Section(object):

   kind = "section"

   def parse(self):
      head = 0
      BE_SPACE = False
      BE_NEWLINE = False
      while head <= self.source.size() - 1:
         organ, head = self.snip_twig(head)
         if (organ.kind == "newline"):
            BE_NEWLINE = True
            continue
         elif (organ.kind == "space"):
            BE_SPACE = True
            continue
         elif (BE_NEWLINE == True):
            paragraph = Paragraph(**(organ.give_data))
            sinks.append(paragraph)
         elif (BE_SPACE == True):
            sinks[-1].push(organ)
         else:
            sinks[-1].restart(organ)
         BE_SPACE = False
         BE_NEWLINE = False

   def write(self):
      element = ''
      for twig in self.sinks:
         element += twig.write()
      return self.write_block_tag(element, self.kind)

   def snip_twig(self, head_mark_left):
      mark = probe_mark(source)
      label = get_label(mark)

      data_organ = {
         "leftmost": get_left(head_mark_left),
         "rightmost": get_right(head_mark_right),
         "count_line": self.count_line,
         "count_character": self.count_character,
      }
      if (label == "SPACE"):
         segments = source.split(mark, 1)
         head_mark_right = head_mark_right + mark.size
         return LEAF.Space(**data_organ), head_mark_right
      if (label == "NEWLINE"):
         segments = source.split(mark, 1)
         head_mark_right = head_mark_right + mark.size
         return LEAF.Newline(**data_organ), head_mark_right

      segments = source.split(mark, 2)
      content = segments[1]
      head_content_left = head_mark_left + mark.size
      head_content_right = head_mark_left + mark.size + content.size
      head_mark_right = head_mark_left + 2 * mark.size + content.size

      data_organ = {
         "source": content,
         "leftmost": get_left(head_content_left),
         "rightmost": get_right(head_content_right),
         "count_line": get_next_count_line(head_content_left),
         "count_character": get_next_count_character(head_content_left),
      }
      data_caution = {
         "token": mark,
         "fragment_left": get_left(head_mark_left),
         "fragment_right": get_right(head_content_left),
         "count_line": get_next_count_line(head_mark_left),
         "count_character": get_next_count_character(head_mark_left),
      }

      if (label == None):
         caution = CAUTION.Not_match_boundary_bough(**data_caution)
         caution.panic()
      if (self.be_label_bough(label)):
         caution = CAUTION.Occurring_inner_scope_bough(**data_caution)
         caution.panic()

      if (label == "SERIF_NORMAL"):
         sinks.append(LEAF.Serif_normal(**data_organ))
      if (label == "SERIF_ITALIC"):
         sinks.append(LEAF.Serif_italic(**data_organ))
      if (label == "SERIF_BOLD"):
         sinks.append(LEAF.Serif_bold(**data_organ))
      if (label == "SANS_NORMAL"):
         sinks.append(LEAF.Sans_normal(**data_organ))
      if (label == "SANS_BOLD"):
         sinks.append(LEAF.Sans_bold(**data_organ))

      if (label == "MATH_OLD"):
         sinks.append(LEAF.Math_old(**data_organ))
      if (label == "MATH_NEW"):
         sinks.append(LEAF.Math_new(**data_organ))
      if (label == "MONOSPACE"):
         sinks.append(LEAF.Monospace(**data_organ))

      return content, head_mark_right

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Stanza(object):

   kind = "stanza"

   def write(self):
      element = ''
      for twig in self.sinks:
         element += twig.write()
      return self.write_block_tag(element, self.kind)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Table(object):

   kind = "table"

   def write(self):
      element = ''
      for twig in self.sinks:
         element += twig.write()
      return self.write_block_tag(element, self.kind)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Image(ORGAN.Leaf):

   kind = "image"

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Break(ORGAN.Leaf):

   kind = "break"

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Paragraph(object):

   kind = "paragraph"

   def parse(self):
      pass

   def write(self):
      return self.write_tag("paragraph")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Line(object):

   kind = "line"

   def parse(self):
      pass

   def write(self):
      return self.write_tag("line")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Row(object):

   kind = "row"

   def parse(self):
      pass

   def write(self):
      return self.write_tag("row")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Sentence(object):

   def parse(self):
      while not self.source:
         self.element, self.mark = self.snip()
         label = get_label_from_mark(mark)
         fragment_left = self.find_fragment_left()
         fragment_right = self.find_fragment_right()
         data = {
             "place" : self.place,
             "fragment_left" : fragment_left,
             "mark" : mark,
             "fragment_right" : fragment_right
         }
         if (be_leaf_label(label)):
             error.outer_scope_leaf(**data)
         if (label == "serif-roman"):
            leaf = Serif_roman()
         elif (label == "serif-italic"):
            label = Serif_italic
         elif (label == "serif-bold"):
            label = Serif_bold
         elif (label == "sans-normal"):
            label = Sans_normal
         elif (label == "sans-bold"):
            label = Sans_bold
         # ...

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Verse(object):

   def parse(self):
      while not self.source:
         self.element, self.mark = self.snip()
         label = get_label_from_mark(mark)
         fragment_left = self.find_fragment_left()
         fragment_right = self.find_fragment_right()
         data = {
             "place" : self.place,
             "fragment_left" : fragment_left,
             "mark" : mark,
             "fragment_right" : fragment_right
         }
         if (be_leaf_label(label)):
             error.outer_scope_leaf(**data)
         if (label == "serif-roman"):
            leaf = Serif_roman()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Cell(object):

   def parse(self):
      while not self.source:
         self.element, self.mark = self.snip()
         label = get_label_from_mark(mark)
         fragment_left = self.find_fragment_left()
         fragment_right = self.find_fragment_right()
         data = {
             "place" : self.place,
             "fragment_left" : fragment_left,
             "mark" : mark,
             "fragment_right" : fragment_right
         }
         if (be_leaf_label(label)):
             error.outer_scope_leaf(**data)
         if (label == "serif-roman"):
            leaf = Serif_roman()

