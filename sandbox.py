#! /usr/bin/env python3

import json

import porphyrin.organ as ORGAN
import porphyrin.stem as STEM
import porphyrin.leaf as LEAF
import porphyrin.aid as AID

source = ''
source += "["
source += "   {\"cat\": \"white\"},\n"
source += "   {\"dog\": \"black\"},\n"
source += "   {\"sheep\": \"gray\"}\n"
source += "]"

sink = json.loads(source)
print(sink[0]["cat"])
print(sink[1]["dog"])

