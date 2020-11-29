#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matrix import *

if __name__ == "__main__":
  matr = [
    [0.6897, -0.0908, 0.0182, 0.0363, 0.1271],
    [0.0944, 1.0799, 0.0000, -0.0726, 0.0726],
    [0.0545, 0.0000, 0.8676, -0.2541, 0.1452],
    [-0.1089, 0.2287, 0.0000, 0.8531, -0.0363],
    [0.4538, 0.0000, 0.1634, 0.0182, 1.0164]
  ]
  a1, x1 = Matrix.danMethod(matr)
  print('Собственное значение a1(единственное): ' + str(a1))
  print('Собственный вектор x1:')
  print(x1)
  print('A * x1:')
  print(Matrix.mulVector(matr, x1))
  print('a1 * x1:')
  x1 = [a1 * i for i in x1]
  print(x1)
