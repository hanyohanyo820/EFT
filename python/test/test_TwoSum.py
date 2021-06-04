#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import sys

sys.path.append(os.pardir)
from EFT import TwoSum

eps = 2**-53

def test_TwoSum_1():
	[x, y] = TwoSum(1.0, eps)
	assert (x, y) == (1.0, eps)

def test_TwoSum_2():
	[x, y] = TwoSum(1.0, 2*eps)
	assert (x, y) == (1.0 + 2*eps, 0)

def test_TwoSum_3():
	[x, y] = TwoSum(1.0, 3*eps)
	assert (x, y) == (1.0 + 4*eps, -eps)
