# full body forward dynamics

import numpy as np
from src.math_utils.trig import sin, cos, tan, asin, acos, atan


# robot parameters
l1 = 1.0  # Length of link 1 (meters)
l2 = 1.0  # Length of link 2 (meters)
m1 = 1.0  # Mass of link 1 (kg)
m2 = 1.0  # Mass of link 2 (kg)
r1 = 0.06  # Radius of link 1 (meters)
r2 = 0.06  # Radius of link 2 (meters)
g = 9.81  # Gravitational acceleration (m/s^2)


def inertia_of_link(m, r, L):
    # Moment of inertia about the joint axis (using the parallel axis theorem)
    I = (1/2) * m * r**2 + m * L**2
    return I


# mass matrix M(q)
def mass_matrix(q):
    I1 = inertia_of_link(m1, r1, l1)
    I2 = inertia_of_link(m2, r2, l2)
    
    # Compute the elements of the mass matrix
    m11 = I1 + I2 + m2 * l1 * l2 * cos(q[1])
    m12 = I2 + m2 * l2 * cos(q[1])
    m22 = I2
    
    return np.array([[m11, m12], [m12, m22]])


# Coriolis and Centripetal matrix C(q, q_dot)
def coriolis_matrix(q, q_dot):
    c11 = -m2 * l1 * l2 * np.sin(q[1]) * (2 * q_dot[1] + q_dot[0])
    c12 = -m2 * l1 * l2 * np.sin(q[1]) * q_dot[1]
    c21 = m2 * l1 * l2 * np.sin(q[1]) * q_dot[0]
    c22 = 0.0
    return np.array([[c11, c12], [c21, c22]])

# Gravitational forces G(q)
def gravitational_forces(q):
    g1 = (m1 * l1 + m2 * l1) * g * np.cos(q[0]) + m2 * l2 * g * np.cos(q[0] + q[1])
    g2 = m2 * l2 * g * np.cos(q[0] + q[1])
    return np.array([g1, g2])

# Equation of motion: M(q) * q_ddot + C(q, q_dot) * q_dot + G(q) = tau
def dynamics(q, q_dot, tau):
    M = mass_matrix(q)
    C = coriolis_matrix(q, q_dot)
    G = gravitational_forces(q)
    
    # Solving the equation of motion: M(q) * q_ddot = tau - C(q, q_dot) * q_dot - G(q)
    q_ddot = np.linalg.inv(M) @ (tau - C @ q_dot - G)
    return q_ddot

# Runge-Kutta 4th Order (RK4) integration