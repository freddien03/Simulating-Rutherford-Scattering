#Temporary file for mockup of Particle class and testing

import numpy as np
import matplotlib.pyplot as plt
from random import random

class Particle:
    E0 = 8.85e-12
    u = 1.66e-27
    e = 1.602e-19

    def __init__(self, mass: float, charge: float, position: np.array, velocity: np.array):
        self.mass = mass*self.u
        self.charge = charge*self.e
        self.position = position
        self.velocity = velocity
        self.initialVel = np.array(velocity)

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
    
    def updatePosVel(self, particles, TIMESTEP):
        a = self.netForce(particles)/self.mass
        self.velocity += a*TIMESTEP
        self.position += self.velocity*TIMESTEP
    
    def calcTimeStep(self, particles):
        magA = np.linalg.norm(self.netForce(particles)/self.mass)
        # minDistance = np.inf
        # for particle in particles:
        #     minDistance = min(minDistance, self.distance(particle))
        # halfStep = np.linalg.norm(minDistance/(4*self.velocity))
        # print(minDistance)
        # print(np.linalg.norm(self.velocity))
        # print(magA**-1)
        # print(halfStep)
        return min((magA**-1),1e-12)
    
    def calcAngle(self):
        dot = np.dot(self.velocity, self.initialVel)
        angle = np.arccos(dot/(np.linalg.norm(self.velocity)*np.linalg.norm(self.initialVel)))
        return np.degrees(angle)

def randomPoint(maxRad):
    # np.random.seed(2)
    theta = np.random.uniform(0,2*np.pi, 1)
    radius = np.random.uniform(0,maxRad, 1) ** 0.5
    return np.array([radius[0]*np.cos(theta[0]), radius[0]*np.sin(theta[0]), 0.])

alphaCount = 1
# alpha = Particle(4, 2, np.array([0.0, 0, 0]), np.array([0.0, 0, 1.5e7]))
alphas = [Particle(4, 2, randomPoint(0.0000000005), np.array([0.0, 0, 1.5e7]))]
nuclei = [Particle(197, 79, np.array([0., 0, 0.025]), np.zeros(3))]
# print(randomPoint(0.0000000005))
positions = np.array([alphas[0].position])
# while alpha.distance(nuclei[0]) <= 1e-7:
#     timeStep = alpha.calcTimeStep(nuclei)
#     # print(alpha.calcTimeStep(nuclei))
#     alpha.updatePosVel(nuclei, timeStep)
#     positions = np.concatenate(([alpha.position], positions))
# print(alpha.calcAngle())
timeElapsed = 0
angles = []
activity = 37e9
while alphaCount < 20:
    timeStep = np.inf
    for alpha in alphas:
        timeStep = min(timeStep, alpha.calcTimeStep(nuclei))
    timeElapsed += timeStep
    
    for alpha in alphas:
        alpha.updatePosVel(nuclei, timeStep)
        if alpha.distance(nuclei[0]) <= 1e-7:
            angles.append(alpha.calcAngle())
            alphas.remove(alpha)

    if random() < activity*timeStep:
        alphas.append(Particle(4, 2, randomPoint(0.0000000005), np.array([0.0, 0, 1.5e7])))
        alphaCount += 1

while len(alphas) !=  0:
    timeStep = np.inf
    for alpha in alphas:
        timeStep = min(timeStep, alpha.calcTimeStep(nuclei))
    # print(timeStep)

    for alpha in alphas:
        alpha.updatePosVel(nuclei, timeStep)
        positions = np.concatenate(([alpha.position], positions))
        if alpha.distance(nuclei[0]) > 0.05:
            angles.append(alpha.calcAngle())
            alphas.remove(alpha)
    
# hist = plt.hist(angles, 50, facecolor='g', alpha=0.75)
# plt.xlabel('Angles')
# plt.ylabel('Frequency')
# plt.title('Histogram of Angles')
# plt.xlim(0, 180)
# plt.ylim(0, 100)
# plt.grid(True)
# plt.show()

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.scatter(positions[...,0], positions[...,2], marker = "o")
ax.scatter(nuclei[0].position[0], nuclei[0].position[2], marker = "X")
plt.show()