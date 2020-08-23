# -*- coding: utf-8 -*-
"""=============================================================================
   Ex2: MATRICES - Câu 2
       Cho các ma trận A = [[1, 3, 3], [4, 5, 6], [7, 8, 9]] và 
               ma trận B = [[2, 3], [6, 8], [5, 7]]
       Thực hiện nhân 2 ma trận 
============================================================================="""

import numpy as np

A = np.matrix([[1, 3, 3], [4, 5, 6], [7, 8, 9]])
print('A     =\n', A)

B = np.matrix( [[2, 3], [6, 8], [5, 7]])
print('M2     =\n', B)

## A.dot(B)
print('A.dot(B) =\n', A.dot(B))

## A @ B
print('A @ B =\n', A @ B)


