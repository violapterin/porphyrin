#! /usr/bin/env python3

import sys

import stem
import leaf
import leaflet
import error

# Document
# Section, Stanza, Table, Image, Break,
# Paragraph, Line, Row,
# Sentence, Verse, Cell
# Serif_roman, Serif_italic, Serif_bold, Serif_roman, Serif_bold
# Traditional, Alternative, Verbatim

filename_in = sys.argv[1]
filename_out = sys.argv[2]
convert(filename_in, filename_out)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Stem(Organ):

   def __init__(self, **data):
      super().__init__(**data)
      self.sinks = []

class Leaf(Organ):

   def __init__(self, **data):
      super().__init__(**data)
      self.sink = ''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Organ(object):

   def __init__(self, **data):
      self.source = data.pop("source", '')
      self.leftmost = data.pop("leftmost", '')
      self.rightmost = data.pop("rightmost", '')
      self.count_line = data.pop("count_line", 0)
      self.count_character = data.pop("count_character", 0)

   def parse(self):
      pass

   def write(self):
      pass

   def snip(self, head_mark_left):
      mark = probe_mark(source)
      label = get_label(mark)
      segments = source.split(mark, 2)
      content = segments[1]
      head_content_left = head + mark.size
      head_content_right = head + mark.size + content.size
      head_mark_right = head + 2 * mark.size + content.size
      data_organ = {
         source = content,
         leftmost = get_left(head_content_left)
         rightmost = get_right(head_content_right)
         count_line = increase_count_line(head, mark)
         count_character = increase_count_character(head, mark)
      }
      data_caution = {
         source = content,
         fragment_left = get_left(head_mark_left)
         fragment_right = get_right(head_content_left)
         count_line = self.count_line
         count_character = self.count_character
      }
      if (label = None):
         error.Match_boundary_bough(**data_caution)
      if (label = "serif_normal"):
         sinks.append(Serif_normal(data_organ))
    
      return content, label


   def find_left(self, head):
      left = self.source[: head + 1] + self.leftmost
      segments = self.left.rsplit('\n')
      return segments[-1]

   def find_right(self, head):
      right = self.source[: head + 1] + self.rightmost
      segments = self.right.split('\n')
      return segments[0]

   def probe_mark(self, source):
      tip = source[0]
      probe = 0
      for probe in range(source.size):
         if (source[probe] == tip):
            probe += 1
      mark = source[: probe]

   def increase_count_character(self, count_in, source):
      count_out = count_in
      segments = source.split('\n')
      size = segments.size
      if (segments.size == 0):
         count_out += segments[-1].size - 1
      elif
         count_out = segments[-1].size - 1
      return count_out
      

   def increase_count_line(self, count_in, source):
      count_out = count_in
      segments = source.split('\n')
      size = segments.size
      if not (segments.size == 0):
         count_out += size - 1
      return count_out

   def emit_place():
      result = ''
      result += "line " + self.count_line
      result += ", character " + self.count_character
      return result

   def write_tag(self, tag, kind):
      result = ''
      result += '<' + tag + ' '
      result += "class=" + kind + ">"
      result += self.write_element()
      result += "<class" + "/>"
      return result

   def get_label(mark):
      tip = mark[0]
      labels = get_labels()
      if tip not in labels:
         return None
      return labels[tip]

   def get_tip(label):
      tips = get_tips()
      if label not in tips:
         return None
      return tips[label]

   def give_labels():
      labels = {
         '@': "serif_normal",
         '%': "serif_italic",
         '#': "serif_bold",
         '$': "sans_normal",
         '&': "sans_bold",
         '`': "monospace",
         '+': "verbatim",
         '*': "alternative",
         '^': "traditional",
         '=': "section",
         '/': "stanza",
         '\"': "table",
         '|': "image",
         '_': "tab",
         '\'': "pause",
         '~': "break",
         '\\': "link",
         '<': "comment_left",
         '>': "comment_right",
      }
      return labels


   def give_tips():
      labels = give_labels()
      tips = {label: tip for tip, label in labels.items()}
      return tips

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def convert(name_in, name_out)
   file_in = open(sys.argv[1], mode = 'r')
   source = file_in.read()
   file_in.close()
   document = Document(source)
   document.process()
   sink = document.write()
   file_out = open(sys.argv[2], mode = 'w')
   file_out.write(sink)
   file_out.close()



