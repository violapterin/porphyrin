#! /usr/bin/env python3

import json

import porphyrin.organ as ORGAN
import porphyrin.stem as STEM
import porphyrin.leaf as LEAF
import porphyrin.aid as AID

a = [8,3.0,-5,4,4,9]
print(min(a))
print(a.index(min(a)))



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

'''
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
'''
