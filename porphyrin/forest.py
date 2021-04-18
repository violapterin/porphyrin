#! /usr/bin/env python3

import sys

import tree
import bough
import leaf
import error

# section, paragraph, sentence
# stanza, line, verse
# table, row, cell

class Forest(Piece):

   def __init__(self, **arguments):
      self.source = arguments.pop("source", ''),
      self.place = Place()
      self.pile = []
      self.fragment_left_global = ''
      self.fragment_right_global = ''
      self.head = 0

   def process(self):
      while not self.source:
         self.content, self.mark = self.snip()
         kind = get_kind_tree_from_mark(mark)
         fragment_left = self.get_fragment_left()
         fragment_right = self.get_fragment_right()
         if (kind == 0):
             error.outer_scope_leaf(
                   place = self.place,
                   fragment_left = fragment_left,
                   mark = mark,
                   fragment_right = fragment_right)
         if (kind == "SERIF_ROMAN"):
            leaf = Serif_roman(content, place, )
         elif (kind == "SERIF_ITALIC"):
            leaf = Serif_roman(content)
         # ...

         self.push(leaf)

   def write(self):
      result = ''
      for tree in self.treees:
         result += tree.write()
      return result

class Piece(object):

   def __init__(self, **arguments):
      self.source = '',
      self.place = Place()
      self.pile = []
      self.fragment_left_global = ''
      self.fragment_right_global = ''
      self.head = 0

   def snip(self):
      right = self.get_right()
      mark = probe_mark(right)
      if (segments.size == 1):
         error.Match_boundary_bough(
               place = self.place,
               fragment_left = get_left_fragment(self),
               mark = mark,
               fragment_right = get_right_fragment(self))
      segments = right.split(mark, 2)
      content = segments[1]
      content = self.trim(content)
      thing = mark + content + mark
      self.head += thing.size
      self.place.increase(thing)
      return content, mark

   def get_left(self):
      return self.source[: self.head + 1] + self.fragment_left_global

   def get_right(self):
      return self.source[self.head + 1: ] + self.fragment_right_global

   def get_fragment_left(self):
      left = self.get_left()
      segments = self.left.rsplit('\n')
      return segments[-1]

   def get_fragment_right(_self):
      right = self.get_right()
      segments = self.right.split('\n')
      return segments[0]

   def probe_mark(self, source):
      probe = 0
      for probe in range(right.size):
         if (probe == right[0]):
            probe += 1
      mark = right[: probe]


class Place(object):

   def __init__(self, line, character):
      self.count_line = count_line
      self.count_character = count_character

   def increase(self, thing):
      segments = thing.split('\n')
      size = segments.size
      if (segments.size == 0):
         self.count_character += segments[-1].size - 1
      elif
         self.count_line += size - 1
         self.count_character = segments[-1].size - 1

   def emit():
      result = ''
      result += "line " + self.count_line
      result += ", character " + self.count_character
      return result




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


text_in = sys.argv[1]
file_out = sys.argv[2]


with open(sys.argv[1], 'r') as text_in:
    for line in file:
       pass




