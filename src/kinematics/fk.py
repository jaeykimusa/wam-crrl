# forward kinematics with homogeneous matrix translation

import numpy as np
from src.math_utils.trig import sin, cos, tan, asin, acos, atan


def rot(theta):
    '''
    rotation matrix for 2d
    '''
    return np.array([
        [cos(theta), sin(theta)],
        [sin(theta), cos(theta)],
    ])

def trans(theta, L):
    return np.array([L * np.cos(theta), L * np.sin(theta)])

def H(theta, L):
    '''
    homogeneous transformation matrix for a revolute joint
    '''

    H = np.identity(3)
    H[:2, :2] = rot(theta)
    H[:2, 2] = np.transpose(trans(theta, L))
    H[2, 2] = 1

    return H

def fk(q, l1, l2):
    # define homogeneous trans matrices for each frame assignment
    H01 = H(q[0], 0)
    H12 = H(0, l1)
    H23 = H(q[1], 0)
    H34 = H(0, l2)

    # joint 1 position
    j1_pos = H01[:2, 2]

    # h trans from frame 0 to 2
    H02 = H01 @ H12 

    # joint 2 position
    j2_pos = H02[:2, 2]
    
    # h trans from from 0 to 4
    H04 = H02 @ H23 @ H34

    # end effector position
    ee_pos = H04[:2, 2]

    # H04 = H01 @ H12 @ H23 @ H34

    # return f"Joint 1 position: x={j1_pos[0]: .3f}, y={j1_pos[1]: .3f} \nJoint 2 position: x={j2_pos[0]: .3f}, y={j2_pos[1]: .3f} \nEnd-eff position: x={ee_pos[0]: .3f}, y={ee_pos[1]: .3f} \n"
    return ee_pos

# q = np.array([0.4,0.2])

# print(fk(q, 1, 1))
# '''
# Expected output:
# Joint 1 position: x=0.000, y=0.000
# Joint 2 position: x=0.921, y=0.389
# End-eff position: x=1.746, y=0.954
# '''