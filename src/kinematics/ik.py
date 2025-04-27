# inverse kinematics

import numpy as np
from src.math_utils.trig import sin, cos, tan, asin, acos, atan


def ik(ee, l1, l2):
    # desired position
    x_d = ee[0]
    y_d = ee[1]

    # compute the distance from the global origin to desired position
    r = np.sqrt(x_d**2 + y_d**2)

    # Check if the target position is reachable (within the workspace)
    if r > (l1 + l2) or r < abs(l1 - l2):
        raise ValueError("Target position is infeasible.")
    
    # compute theta 2 using law of cosine
    theta2 = acos((r**2 - l1**2 - l2**2) / (2 * l1 * l2))

    # compute theta 1 using inverse tangent
    theta1 = atan(y_d / x_d) - atan((l2 * sin(theta2)) / (l1 + l2 * cos(theta2)))

    # adjust if theta 1 is nan
    if np.isnan(theta1):
        theta1 = 0

    # desired q
    q_d = np.array([theta1, theta2])
    
    # return f"theta1: {q_d[0]: .3f} rad \ntheta2: {q_d[1]: .3f} rad \n"
    return q_d


# test:
# ee = np.array([0, 0])
# print(ik(ee, 1, 1))

# input and expected outputs:

# '''
# when l1 = l2 = 1 and (x_d, y_d) = (1.746, 0.954) 
# theta1: 0.400 rad (approxi.)
# theta2: 0.200 rad (approxi.)

# when l1 = l2 = 1 and (x_d, y_d) = (2, 0) 
# theta1: 0.000 rad 
# theta2: 0.000 rad 

# when l1 = l2 = 1 and (x_d, y_d) = (0, 2) 
# theta1: 1.571 rad (approxi.)
# theta2: 0.000 rad 

# when l1 = l2 = 1 and (x_d, y_d) = (1, 1) 
# theta1: 0.785 rad (approxi.)
# theta2: 0.000 rad 

# when l1 = l2 = 1 and (x_d, y_d) = (2, 2) 
# Target position is infeasible.

# when l1 = l2 = 1 and (x_d, y_d) = (0, 0) 
# theta1: 0.000 rad
# theta2: 3.142 rad (approxi.)
# '''