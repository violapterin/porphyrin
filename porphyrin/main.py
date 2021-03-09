#! /usr/bin/env python3

import porphyrin.convert as Ppr.convert

str_in_1 = "@ Hello % World, % who am I? @"
str_out_1 = "<p> Hello <em> World, </em> who am I? </p>"

str_parse_1 = f.parse(str_in_1)
print(str_parse_1)

