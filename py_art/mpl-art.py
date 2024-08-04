import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk(100) # Edit here to change no. of dots.
rw.fill_walk() 

plt.style.use('classic')
fig, ax = plt.subplots(dpi=128) 
point_numbers = range(rw.num_points) 
ax.plot(rw.x_values, rw.y_values, linewidth=6, color="mediumvioletred") # Edit here to change line color and width.
ax.set_facecolor("deepskyblue") # Edit here to change bg color.
ax.set_aspect('equal') 

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
