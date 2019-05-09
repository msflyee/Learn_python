import matplotlib.pyplot as plot

from Chapter15_RandomWalk_class import RandomWalk
rw = RandomWalk()
rw.fill_walk()
plot.scatter(rw.x_values,rw.y_values,s = 1)
plot.show()
