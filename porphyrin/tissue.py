#! /usr/bin/env python3

import sys

import tree
import bough
import leaf
import error


filename_in = sys.argv[1]
filename_out = sys.argv[2]
convert(filename_in, filename_out)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Tree > Bough > Twig > Frond >
#    Leaflet
#    Leaf > Vein > Apex

# `parse`, and `write` are:
# inherited for Bough, Twig, Frond
# virtual for Leaf, Leaflet, Vein, Apex


class Flesh(Tissue):

   def __init__(self, **data):
      super().__init__(**data)
      self.sinks = []

   def write(self):
      result = ''
      for sink in self.sinks:
         result += tree.write()
      return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Skin(Tissue):

   def __init__(self, **data):
      super().__init__(**data)
      self.sink = ''

   def write(self):
      pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Tissue(object):

   def __init__(self, **data):
      self.source = data.pop("source", '')
      self.leftmost = data.pop("leftmost", '')
      self.rightmost = data.pop("rightmost", '')
      self.count_line = data.pop("count_line", 0)
      self.count_character = data.pop("count_character", 0)

   def copy(self):
      data = {
         source = self.source,
         place = self.place,
         leftmost = self.leftmost,
         rightmost = self.rightmost
      }
      return Tissue(**data)

   def snip(self):
      head = 0
      # head_mark_left, head_mark_right
      # head_source_left, head_source_right
      mark = probe_mark(source)
      tip = mark[0]
      label = get_label(tip)
      segments = source.split(mark, 2)
      content = segments[1]
      leftmost_mark = get_left(self.head + mark.size)
      rightmost_mark = get_right(self.head + mark.size)
      rightmost_content = get_right(self.head + mark.size + content.size)
      place_content = self.place.increase(2 * mark.size + content.size)
      data_tissue = {
         source = content,
         place = self.place,
         left = self.get_left(head),
         right = self.get_right(head))
      }
      data_caution = {
         place = self.place,
         place = self.place,
         left = self.get_left(head),
         right = self.get_right(head))
      }
      if (label = None):
         error.Match_boundary_bough(**data)
      # if not mark ...
      self.place.increase(thing)
      return content, label


   def find_left(self, head):
      left = self.source[: head + 1] + self.leftmost
      segments = self.left.rsplit('\n')
      return segments[-1]

   def find_right(self, head):
      right = self.source[: head + 1] + self.rightmost
      segments = self.right.split('\n')
      return segments[0]

   def probe_mark[(self, source):
      tip = source[0]
      probe = 0
      for probe in range(source.size):
         if (source[probe] == tip):
            probe += 1
      mark = source[: probe]

   def increase_place(self, thing):
      segments = thing.split('\n')
      size = segments.size
      if (segments.size == 0):
         self.count_character += segments[-1].size - 1
      elif
         self.count_line += size - 1
         self.count_character = segments[-1].size - 1

   def emit_place():
      result = ''
      result += "line " + self.count_line
      result += ", character " + self.count_character
      return result


   def get_label(tip):
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
         '+': "highlight",
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



