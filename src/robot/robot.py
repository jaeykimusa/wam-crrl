# this is whole arm manipulator.

# from math_utils import math_utils as mu

from math_utils.trig import cos, sin

# number of links
links = 3

linkLength = [0] * links
linkMass = [0] * links

def setLinkLength(link, length):
    linkLength[link] = length

def getLinkLength(link):
    return linkLength[link]

def setLinkMass(link, mass):
    linkMass[link] = mass

def getLinkMass(link):
    return linkMass[link]

setLinkLength(0, 3)

theta = 3.14

print(cos(theta))
print(sin(theta))
