#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import sys

sys.path.append(os.pardir)
from EFT import TwoProductFMA

eps = 2**-53

def test_TwoProductFMA_1():
	[x, y] = TwoProductFMA(1.0 + 2*eps, 1.0 + 2*eps)
	# (1+epse)(1+epse) = 1 + 4eps + 4eps^2
	# 1 + 2eps is approximate result, eps^2 is error.
	assert (x, y) == (1.0 + 4*eps, 4*eps*eps)

def test_TwoProductFMA_2():
	[x, y] = TwoProductFMA(1.0 - eps, 1.0 + 2*eps)
	# (1-eps)(1+2eps) = 1 + eps - 2eps^2
	# 1 is approximate result, eps - 2eps^2 is erroor.
	assert (x, y) == (1.0,  eps - 2*eps**2)
