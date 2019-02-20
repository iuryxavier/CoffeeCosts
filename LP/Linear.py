from scipy.optimize import (
    linprog,
    linprog_verbose_callback)
import numpy as np


#O padrão de entrada dos dados deve ser feita para um problema de maximização

# c = np.array([-3, -5])
# A = np.array([[1,0], [0,1], [3,2]])
# b = np.array([4, 6, 18])
# res = linprog(c, A, b,
#               options={'maxiter':10000})
# print(res)
# linprog_verbose_callback(res)
# print(f'\n DUAL \n')
# A_T_n = -A.transpose()
# resd = linprog(-b, A_T_n, c,
#               options={'maxiter':10000}
#               )
# print(f' Os multplicadores de lagrange são:')
# print(resd)
# #
####################################################################

# ask = input ('The original problem is a maximization?: Y/N')
# if ask == 'Y' or 'y':
#     resd = linprog(b, Ad, c)
#     print(f' Os multplicadores de lagrange são:{resd}')
# else:
#     resd = linprog(b, Ad, -c)
#     print(f' Os
#multplicadores de lagrange são:{resd}')
#
# c = np.array([4, 6, 18])
# A = np.array([[-1, 0, -3],[0, -1, -2]])
# b = np.array([-3, -5])
# res = linprog(c, A, b)
# print(res)
# print(f'\n DUAL \n')
# A_T = -A.transpose()
#
# resd = linprog(-b, A_T, c)
# print(f' Os multplicadores de lagrange são:')
# print(resd)


c = np.array([-40, -60, -20])
A = np.array([[80, 30, 10], [40, 100, 60], [20, 70, 90]])
b = np.array([800, 1000, 600])
res = linprog(c, A, b)
print(res)
print(f'\n DUAL \n')
A_T_n = -A.transpose()
resd = linprog(b, A_T_n, c)
print(f' Os multplicadores de Lagrange são:')
print(resd)
#
#
