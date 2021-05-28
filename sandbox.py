#! /usr/bin/env python3

import porphyrin.organ as ORGAN
import porphyrin.stem as STEM
import porphyrin.leaf as LEAF
import porphyrin.aid as AID

class Cat():
   KIND = "cat"
   def __init__(self, color):
      self.color = color
   def call(self):
      print("meow")
      print(f"I am a {self.color} cat.")
   def copy(self):
      return Cat(self.color)

class Dog():
   KIND = "dog"
   def __init__(self, color):
      self.color = color
   def call(self):
      print("bark")
      print(f"I am a {self.color} dog.")

#Cat("white").call()

sinks = ["  apple", "banana ", " cake", "  dog "]
sink = AID.join(sinks)
print(sink[0])
print(sink[-1])
