# Sample of EFT (Error Free Transformation) algorithms

This repository contains sample programs of EFT implemented by Python3.
(We will also add C and C ++ implementations in the future.)
The implemented EFT algorithm is as follows.

* FastTwoSum
* TwoSum
* TwoProduct
* TwoProductFMA

## Implementation by Python3

There is an implementation of each EFT in the python directory.
To use FMA, we need to install pyfma with `pip3 install pyfma` in advance.
If we use the EFT algorithm, you can import and use it as follows.

```python3
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from EFT import TwoSum

eps = 2**-53
a = 1.0 
b = 3 * eps

[x, y] = TwoSum(a, b)
print(x, y) # correct result is x = 1+4eps, y = -eps
```

Inside the test directory is a test program for the EFT implementation.
If you have pytest installed, you can run the test program by executing `pytest` in the test directory.
(If you want to install pytest, please exec `pip3 install pytest`.)
