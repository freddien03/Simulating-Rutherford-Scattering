#Temporary file for mockup of Particle class

import numpy as np
import matplotlib.pyplot as plt

class Particle:
    E0 = 8.85e-12
    u = 1.66e-27
    e = 1.602e-19
    TIMESTEP = 1e-19

    def __init__(self, mass: float, charge: float, position: np.array, velocity: np.array):
        self.mass = mass*self.u
        self.charge = charge*self.e
        self.position = position
        self.velocity = velocity

    def distance(self, particle):
         return np.linalg.norm(self.position-particle.position)

    def attraction(self, particle):
        return (self.charge*particle.charge)/(4*np.pi*self.E0*(self.distance(particle)**2))

    def netForce(self, particles):
        force = np.zeros(3)
        for particle in particles:
            forceMag = self.attraction(particle)
            direction = self.position-particle.position
            force += (forceMag/np.linalg.norm(direction))*direction

        return force
    
    def updatePosVel(self, particles):
        a = self.netForce(particles)/self.mass
        self.position += self.velocity*self.TIMESTEP
        self.velocity += a*self.TIMESTEP


alpha = Particle(4, 2, np.array([0.0, 0, 0]), np.array([0.0, 0, 1.5e7]))
nuclei = [Particle(197, 79, np.array([1e-50, 0, 1e-7]), np.zeros(3))]


# positions = np.array([alpha.position])
# while alpha.distance(nuclei[0]) <= 1.1e-7:
#     alpha.updatePosVel(nuclei)
#     positions = np.concatenate(([alpha.position], positions))

# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.scatter(positions[...,0], positions[...,2], marker = "o")
# ax.scatter(nuclei[0].position[0], nuclei[0].position[2], marker = "X")
# plt.show()
x = np.array([2,3,4])
print(2*x)