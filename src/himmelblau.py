import random
from functools import partial
from base import *
from algorithms import psoAlgorithm, init_swarm


w = 0.8
c1 = 3.5
c2 = 0.5
BIT_LEN = 2
GENERATION = 100
SWARM_LEN = 100

Fitness.weight = -1

def himmelblau(ind):#функция для подсчета приспасобленности
    x, y = ind
    return ((x**2 + y - 11)**2 + (x + y**2 - 7)**2)

creator_w = lambda: random.uniform(-5, 5)

creator_particle = partial(generate_repeat, Particle, BIT_LEN, creator_w)
creator_swarm = partial(generate_repeat, list, SWARM_LEN, creator_particle)

swarm = creator_swarm()

swarm, p_best = init_swarm(swarm, himmelblau)



print(psoAlgorithm(swarm, p_best, himmelblau, GENERATION, BIT_LEN, SWARM_LEN, w, c1, c2, True))

"""right answer
(3.0; 2.0), (-2.805118; 3.131312), (-3.779310; -3.283186), (3.584458; -1.848126)
"""