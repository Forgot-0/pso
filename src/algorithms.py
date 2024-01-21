from base import Array
import random


def init_swarm(swarm, fitfunc):
    p_best = random.choice(swarm).best
    
    for i in range(len(swarm)):
        f = fitfunc(swarm[i])
        swarm[i].fitness.setValues(f)

        swarm[i].best.update(swarm[i])
        swarm[i].best.fitness.setValues(f)

        p_best.update(swarm[i])

    return swarm, p_best


def psoAlgorithm(swarm, p_best, fitfunc, gen, bitl, swarml, w=0.8, c1=2.05, c2=2.05, update_coef=False):
    for t in range(1, gen+1):
        for i in range(swarml):
            r1 = Array([random.random() for _ in range(bitl)])
            r2 = Array([random.random() for _ in range(bitl)])

            swarm[i].velocity = w*swarm[i].velocity + \
                (c1*r1*(swarm[i].best - swarm[i])) + \
                (c2*r2*(p_best - swarm[i]))

            swarm[i][:] = swarm[i][:] + swarm[i].velocity
            swarm[i].fitness.setValues(fitfunc(swarm[i]))

            if swarm[i].best.update(swarm[i]):
                p_best.update(swarm[i])

        if update_coef:
            w = ((0.4/(gen**2))*(t-gen)**2 + 0.4)
            c1 = ((-3*t)/gen + 3.5)
            c2 = ((3*t)/gen + 0.5)
    
    return swarm, p_best