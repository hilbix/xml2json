#!/usr/bin/env python3
#
# Convert XML to JSON:
#
# <a>b<c>d</c>e<f/>g</a>		becomes	{"a":{"$":["b","e","g"],"c":"d","f":""}}
# <a b="c"/>				becomes	{"a":{"b":"c"}}
# <a><b>c</b></a>			becomes	{"a":{"b":"c"}}
# <a><b>x</b><c>y</c><b>z</b></a>	becomes	{"a":{"b":["x","z"],"c":"y"}}
# <a><b>x<c>y</c>z</b></a>		becomes	{"a":{"b":{"$":["x","z"],"c":"y"}}}
# <a><b>x<c>y</c></b><b>z</b></a>	becomes	{"a":{"b":[{"$":"x","c":"y"},"z"]}}
# Attributen names and elements are merged and attributes come first:
# <a b="c"><b>d</b></a>			becomes	{"a":{"b":["c","d"]}}
# <a b="c"><b>d</b><b>c</b></a>		becomes	{"a":{"b":["c","d","c"]}}
# <a><b c="x">y<c>z</c></b></a>		becomes	{"a":{"b":{"$":"y","c":["x","z"]}}}
# <a><b c="x">y<c>z</c>w</b></a>	becomes	{"a":{"b":{"$":["y","w"],"c":["x","z"]}}}
# $ replaces . in XML tags (as XML tags must not start with . the "$" for text cannot be mistaken):
# <a><b.c/></a>				becomes {"a":{"b$c":""}}
# @ denotes namespaces:
# <n:a xmlns:n="b"><n:c/></n:a>		becomes {"a":{"@":"b","c":{"@":"b"}}}
# <a xmlns:n="b"><c>d</c><n:c/></a>	becomes {"a":{"c":["d",{"@":"b"}]}}
#
# Conversion does not preserve the original XML nor spaces within text of tags.
# (Spaces in attributes are preserved!) Also some matching json2xml is missing.

import sys
import json
import xml.etree.ElementTree as ET

def add(d, t, v):
	if t in d:
		a	= d[t]
		if type(a) is not list:
			a	= [ a ]
			d[t]	= a
		a.append(v)
	else:
		d[t]	= v

def tag(x):
	return '$'.join(x.tag.split('}')[-1].split('.'))

def get(x):
	d	= {}
	if x.tag[0] == '{': d['@'] = '}'.join(x.tag[1:].split('}')[:-1])
	t	= (x.text or '').strip()
	if len(t): d['$'] = t
	for k,v in x.items():
		d[k] = v
	for y in x:
		add(d, tag(y), get(y))
		t	= (y.tail or '').strip()
		if len(t): add(d, '$', t)
	# optimize the node
	# text-only nodes become the text
	# empty nodes become '' instead of {}
	return d['$'] if len(d) == 1 and '$' in d else d if len(d) else ''

def root(x):
	x	= x.getroot()
	return {tag(x):get(x)}

print(json.dumps(root(ET.parse(sys.stdin)), separators=(',',':')))

