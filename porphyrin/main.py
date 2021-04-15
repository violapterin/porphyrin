#! /usr/bin/env python3

import sys

import branch
import twig
import leaf
import error

class Tree(object):

   tag = "TREE"

   def __init__(self, **arguments):
      self.source = arguments.pop("source", ''),
      self.place = Place()
      self.pile = []
      self.fragment_left_global = ''
      self.fragment_right_global = ''
      self.head = 0

   def process(self):
      while not self.source:
         mark, content = self.snip()
         tag = get_tag_from_mark(mark)
         if (tag == 0):
             error.Outer_leaf(
                   place = self.place,
                   fragment_left = get_fragment_left(self),
                   mark = mark,
                   fragment_right = get_fragment_right(self))

         if (tag == "SERIF_ROMAN"): leaf = Serif_roman(content)
         elif (tag == "SERIF_ITALIC"): leaf = Serif_roman(content)
         # ...

         self.push(leaf)

   def snip(self):
      right = self.get_right()
      mark = probe_mark(right)
      if (segments.size == 1):
         error.Match_boundary_twig(
               place = self.place,
               fragment_left = get_left_fragment(self),
               mark = mark,
               fragment_right = get_right_fragment(self))
      segments = right.split(mark, 2)
      content = segments[1]
      content = self.trim(content)
      whole = mark + content + mark
      head += whole.size
      self.place.increase(whole)
      return mark, content


   def get_left(self):
      return self.source[: self.head + 1]

   def get_right(self):
      return self.source[self.head + 1: ]

   def get_left_fragment(self):
      left = self.get_left()
      segments = self.left.rsplit('\n')
      return segments[-1]

   def get_right_fragment(self):
      right = self.get_right()
      segments = self.right.split('\n')
      return segments[0]

   def probe_mark(self, source):
      probe = 0
      for probe in range(right.size):
         if (probe == right[0]):
            probe += 1
      mark = right[: probe]


   def write(self):
      result = ''
      for branch in self.branches:
         result += branch.write()
      return result




class Place(object):

   def __init__(self, line, character):
      self.count_line = count_line
      self.count_character = count_character

   def increase(self, source):
      segments = source.split('\n')
      self.count_line += segments.size
      self.count_character = segments[-1].size - 1

   def emit():
      result = ''
      result += "line " + self.count_line
      result += ", character " + self.count_character
      return result


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def trim(source):
   result = source.translate(source.maketrans({'\n': ' ', '\t': ' '}))
   return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


'''
text_in = sys.argv[1]
file_out = sys.argv[2]


with open(sys.argv[1], 'r') as file:
    for line in file:
       pass
'''




