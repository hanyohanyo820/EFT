#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from pyfma import fma

def FastTwoSum(a, b):
	x = a + b
	y = b - (x - a)
	return [x, y]

def TwoSum(a, b):
	x = a + b
	tmp = x - a
	y = (a - (x - tmp)) + (b - tmp)
	return [x, y]

def split(a):
	# s is a constant that can be calculated by (mantissa bit number t // 2) + 1.
	# Python's floating point precision is double by default, so t = 53.
	t = 53
	s = (t // 2) + 1
	tmp = a * (s + 1)

	tmp = s * a
	ah = tmp - (tmp - a)
	al = a - ah
	return [ah, al]


def TwoProduct(a, b):
	x = a * b
	[ah, al] = split(a)
	[bh, bl] = split(b)
	y =(al * bl) - ((x - (ah * bh) - al * bh) - ah * bl)
	return [x, y]

def TwoProductFMA(a, b):
	x = a * b
	y = fma(a, b, -x)
	return [x, y]
