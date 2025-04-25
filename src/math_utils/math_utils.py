# maybe like euler's langrange go here.

import numpy as np

def cos(theta):
    return np.cos(theta)


def sin(theta):
    return np.sin(theta)


pi = np.pi


def fk(l, theta1, theta2):
    c1 = cos(3 * pi/2 + theta1)
    c2 = cos(theta2)
    s1 = np.sin(3 * pi/2 + theta1)
    s2 = np.sin(theta2)

    

