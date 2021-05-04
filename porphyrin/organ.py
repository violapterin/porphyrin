import stem as STEM
import leaflet as LEAFLET
import caution as CAUTION

# Stem: Document
# Stem (bough): Section, Stanza, Table, Image, Break,
# Stem (twig): Paragraph, Line, Row,
# Stem (frond): Sentence, Verse, Cell
# Stem (leaf): Math old, Math new, Monospace
# Leaflet: Serif roman, Serif italic, Serif bold, Sans roman, Sans bold

class Organ(object):

   def __init__(self, **data):
      self.source = data.pop("source", '')
      self.leftmost = data.pop("leftmost", '')
      self.rightmost = data.pop("rightmost", '')
      self.count_line = data.pop("count_line", 0)
      self.count_character = data.pop("count_character", 0)

   def snip_bough(self, head_mark_left):
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
         return LEAFLET.Space(**data_organ), head_mark_right
      if (label == "NEWLINE"):
         segments = source.split(mark, 1)
         head_mark_right = head_mark_right + mark.size
         return LEAFLET.Newline(**data_organ), head_mark_right

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
         sinks.append(LEAFLET.Serif_normal(**data_organ))
      if (label == "SERIF_ITALIC"):
         sinks.append(LEAFLET.Serif_italic(**data_organ))
      if (label == "SERIF_BOLD"):
         sinks.append(LEAFLET.Serif_bold(**data_organ))
      if (label == "SANS_NORMAL"):
         sinks.append(LEAFLET.Sans_normal(**data_organ))
      if (label == "SANS_BOLD"):
         sinks.append(LEAFLET.Sans_bold(**data_organ))

      if (label == "MATH_OLD"):
         sinks.append(LEAFLET.Math_old(**data_organ))
      if (label == "MATH_NEW"):
         sinks.append(LEAFLET.Math_new(**data_organ))
      if (label == "MONOSPACE"):
         sinks.append(LEAFLET.Monospace(**data_organ))

      return content, head_mark_right

   # # # # # # # # # # # # # # # # 

   def get_left(self, head):
      left = self.source[: head]
      segments = self.left.split('\n')
      return segments[-1]

   def get_right(self, head):
      right = self.source[head :]
      segments = self.right.split('\n')
      return segments[0]

   def probe_mark(self, source):
      tip = source[0]
      probe = 0
      for probe in range(source.size):
         if (source[probe] == tip):
            probe += 1
      mark = source[: probe]

   def get_next_count_character(self, source):
      result = self.count_character
      segments = source.split('\n')
      if not (segments.size == 0):
         result += segments[-1].size + 1
      return result

   def get_next_count_line(self, source):
      segments = source.split('\n')
      return self.count_line + segments.size

   def emit_place(self):
      result = ''
      result += "line " + self.count_line
      result += ", character " + self.count_character
      return result

   def write_block_tag(self, element, kind):
      return write_tag(element, kind, "div")

   def write_inline_tag(self, element, kind):
      return write_tag(element, kind, "span")

   def write_tag(self, element, kind, tag):
      result = ''
      result += '<' + tag + ' '
      result += "class=" + kind + '>'
      result += element
      result += "</" + tag + '>'
      return result

   def write_comment(self, element):
      result = ''
      result += "<!-- "
      result += element
      result += " -->"
      return result

   def get_label(self, mark):
      tip = mark[0]
      labels = get_labels()
      if tip not in labels:
         return None
      return labels[tip]

   def get_tip(self, label):
      tips = get_tips()
      if label not in tips:
         return None
      return tips[label]

   def give_labels(self):
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

   def give_data(self):
      return {
         "source": self.source,
         "leftmost": self.leftmost,
         "rightmost": self.rightmost,
         "count_line": self.count_line,
         "count_character": self.count_character,
      }

   def leaf_be_label(self, leaf):
      labels_leaf = set([
         "SERIF_NORMAL",
         "SERIF_ITALIC",
         "SERIF_BOLD",
         "SANS_NORMAL",
         "SANS_BOLD",
         "MONOSPACE",
         "MATH_NEW",
         "MATH_OLD",
      ])
      return (label in labels_leaf)

   def bough_be_label(self, leaf):
      labels_bough = set([
         "PARAGRAPH",
         "SECTION",
         "STANZA",
         "IMAGE",
         "BREAK",
      ])
      return (label in labels_bough)

   def give_tips(self):
      labels = give_labels()
      tips = {label: tip for tip, label in labels.items()}
      return tips

   def tune_text(self, source):
      result = ignore_mark_text(source)
      result = adjust_space(result)
      return result

   def tune_code(self, source):
      result = adjust_space(source)
      return result

   def adjust_space(self, source):
      spaces = {'\n', '\t'}
      result = erase_character(source, spaces)
      result = ' '.join(result.split())
      return result

   def ignore_mark_text(self, source):
      marks_ignored = {'<', '>', '@', '#', '$', '%', '&'}
      result = erase_character(source, marks_ignored)
      return result

   def remove_character(self, source, group):
      for symbol in group:
         source = source.translate(source.maketrans(symbol, ''))
      return source

   def erase_character(self, source, group):
      for symbol in group:
         source = source.translate(source.maketrans(symbol, ' '))
      return source




