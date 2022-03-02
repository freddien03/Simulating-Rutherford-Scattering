import numpy as np

class Particle:

    def __init__(self, mass: float, charge: float, position: np.array, velocity: np.array):
        self.mass = mass
        self.charge = charge
        self.position = position
        self.velocity = velocity

    def distance(self, other):
         return (((self.position[0]-other.position[0])**2)+((self.position[1]-other.position[1])**2))**0.5
