#Temporary file for mockup of Particle class

import numpy as np

class Particle:
    E0 = 8.85e-12

    def __init__(self, mass: float, charge: float, position: np.array, velocity: np.array):
        self.mass = mass
        self.charge = charge
        self.position = position
        self.velocity = velocity

    def distance(self, other):
         return (((self.position[0]-other.position[0])**2)+((self.position[1]-other.position[1])**2))**0.5

    def attraction(self, other):
        return (self.charge*other.charge)/(4*np.pi*self.E0*(self.distance(other)**2))
