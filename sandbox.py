#! /usr/bin/env python3

import json

import porphyrin.organ as ORGAN
import porphyrin.stem as STEM
import porphyrin.leaf as LEAF
import porphyrin.aid as AID

def prune_space(source):
   sink = source
   spot = 0
   while (True):
      if (spot >= len(sink) - 2):
         break
      if (
         be_ideograph(sink[spot])
         and (sink[spot + 1] == ' ') 
         and be_ideograph(sink[spot + 2])
      ):
         sink = sink[:spot + 1] + sink[spot + 2:]
         continue
      spot += 1
   spot = 0
   while (True):
      if (spot >= len(sink) - 1):
         break
      if (
         (be_ideograph(sink[spot]) and be_latin(sink[spot + 1]))
         or (be_latin(sink[spot]) and be_ideograph(sink[spot + 1]))
      ):
         sink = sink[:spot + 1] + ' ' + sink[spot + 1:]
         spot += 2
         continue
      spot += 1
   return sink

def be_ideograph(glyph):
   if (u'\u4e00' <= glyph <= u'\u9fff'):
      return True # CJK Unified Ideographs
   if (u'\u3400' <= glyph <= u'\u4dbf'):
      return True # CJK Unified Ideographs Extension A
   if (u'\u00020000' <= glyph <= u'\u0002a6df'):
      return True # CJK Unified Ideographs Extension B
   if (u'\u0002a700' <= glyph <= u'\u0002b73f'):
      return True # CJK Unified Ideographs Extension C
   if (u'\u0002b740' <= glyph <= u'\u0002b81f'):
      return True # CJK Unified Ideographs Extension D
   if (glyph in "。，、；：「」『』（）？！─…‥《》〈〉．"):
      return True # Fullwidth forms
   return False

def be_latin(glyph):
   if (glyph in {' ', '\t', '\n'}):
      return False
   if (u'\u0000' <= glyph <= u'\u007F'):
      return True # Basic Latin
   if (u'\u0080' <= glyph <= u'\u00FF'):
      return True # Latin-1 Supplement
   if (u'\u0100' <= glyph <= u'\u017F'):
      return True # Latin Extended-A
   if (u'\u0180' <= glyph <= u'\u024F'):
      return True # Latin Extended-B
   if (u'\u0250' <= glyph <= u'\u02AF'):
      return True # IPA Extensions
   return False

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

s0 = "All human beings are born free and equal in dignity and rights."
s1 = "人生而自由；在尊嚴及權利上均各平等。"
s2 = "人 生 而 自 由 ； 在 尊 嚴 及 權 利 上 均 各 平 等 。"
s3 = "human beings 人 are born free 生 而 自 由"
s4 = "human beings人are born free生 而 自 由"

print (s0)
print (prune_space(s0))
print (s1)
print (prune_space(s1))
print (s2)
print (prune_space(s2))
print (s3)
print (prune_space(s3))
print (s4)
print (prune_space(s4))

