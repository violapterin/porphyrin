#! /usr/bin/env python3

import branch
import twig
import leaf
import error
import main

s1 = "apple , banana , cake"
s2 = ", banana , cake"
s3 = ","
s4 = "apple ,, banana , cake"

t1 = "@@ apple @ banana @@ cake"
t2 = "@@ apple @ banana @@ cake"
t3 = "apple @@ banana , cake"

'''
print (s1.split(','))
print (s2.split(','))
print (s3.split(','))
print (s4.split(','))
'''

print (t1.split('@'))
print (t2.split('@@'))
print (t3.split('@@'))

