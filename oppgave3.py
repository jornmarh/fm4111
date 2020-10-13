import matplotlib.pyplot as plt
import numpy as np
import sys

def expression(xj) :
    return (3 + np.sin(xj))

solution = 0
n = int(sys.argv[1])
for j in range(int(n)) :
    solution += expression(j*(np.pi/n))*(np.pi/n)

solution_an = 3.0*np.pi + 2.0

print("Numerical answer: {}, Analytical answer: {}".format(solution, solution_an))
