#! /usr/bin/env python3

import porphyrin.organ as ORGAN
import porphyrin.stem as STEM
import porphyrin.leaf as LEAF
import porphyrin.aid as AID

class Flower(object):
   def __init__(self, color):
      self.color = color
   
   class Leaf(object):
   

''
class Cat():
   KIND = "cat"
   def __init__(self, color):
      self.color = color
   def call(self):
      print("meow")
   def copy(self):
      return Cat(self.color)

class Dog():
   KIND = "dog"
   def __init__(self, color):
      self.color = color
   def call(self):
      print("bark")

class Bird():
   def __init__(self, **args):
      self.a = args.pop("a", 0)
      self.b = args.pop("b", 0)
'''

