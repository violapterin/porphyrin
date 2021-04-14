#! /usr/bin/env python3

import sys


import branch
import twig
import leaf
import error

class Porphyrin(Piece):

   def __init__(self, **arguments):
      self.source = arguments.pop("source", ''),
      self.place = Place()
      self.pile = []
      self.remain_global_left = ''
      self.remain_global_right = ''
      self.head = 0

   def process(self):
      while not self.source:
         mark, content = self.snip()
         leaf = Leaf(mark = mark, content = content)
         self.push(leaf)

         leaf = Leaf()
         tag = get_tag_from_mark(mark)
         if (tag == "SERIF_ROMAN"): leaf = Serif_roman(content)



   def get_left(self):
      return self.source[: self.head + 1]

   def get_right(self):
      return self.source[self.head + 1: ]

   def get_left_remain(self):
      left = self.get_left()
      segments = self.left.rsplit('\n')
      return segments[-1]

   def get_right_remain(self):
      right = self.get_right()
      segments = self.right.split('\n')
      return segments[0]



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

   def write():
      result = ''
      result += "line " + self.count_line
      result += ", character " + self.count_character
      return result



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Piece(object):

   def __init__(self):
      self.source = arguments.pop("source", ''),
      self.place = Place()
      self.pile = []
      self.remain_global_left = ''
      self.remain_global_right = ''
      self.head = 0

   def snip(self):
      right = self.get_right()
      mark = probe_mark(right)
      if (segments.size == 1):
         error.Error_match_boundary_twig(
               place = self.place,
               remain_left = get_left_remain(self),
               mark = mark,
               remain_right = get_right_remain(self))
      segments = right.split(mark, 2)
      content = segments[1]
      content = self.trim(content)
      whole = mark + content + mark
      head += whole.size
      self.place.increase(whole)
      return mark, content

   def probe_mark(self, source):
      probe = 0
      for probe in range(right.size):
         if (probe == right[0]):
            probe += 1
      mark = right[: probe]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def trim(source):
   table = source.maketrans({'\n': ' ', '\t': ' '})
   return source.translate(table)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


'''
inFile = sys.argv[1]
outFile = sys.argv[2]


with open(sys.argv[1], 'r') as file:
    for line in file:
       pass
'''




