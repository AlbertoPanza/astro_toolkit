'''
astro.py
This module contains basic astrodynamics functions.
'''
# Lesson 1: Gravitational Force

G = 6.67430e-11 # gravitational contant in N·m²/kg²

def gravitational_force(m1, m2, r):
    """
    Calculate the grav. force between 2 masses.

    Parameters:
    m1 -- mass of the first object in kilograms
    m2 -- mass of the second object in kilograms
    r -- distance between the center of the masses in meters

    Returns:
    Gravitational force in newtons
    """
    if r <= 0:
        raise ValueError("Distance must be greater than zero.")
    return G * (m1 * m2)/r**2