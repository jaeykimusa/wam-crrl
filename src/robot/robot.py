# this is whole arm manipulator.

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
