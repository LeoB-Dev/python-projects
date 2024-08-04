# Random walks have practical applications in nature, physics, biology,
# chemistry, and economics. For example, Molecular motion in a water drop is random,so the path a pollen grain traces on the surface is a random walk. The code we’ll write next models many real-world situations.

from random import choice

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """initialise attributes of a walk"""
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]
        # x and y coordinates also store each point on a walk
        
    def fill_walk(self):
        """Calculate all points in the walk."""
        # Keep taking steps until the walk (in terms of x_values) reaches the desired length (5_000). 
        while len(self.x_values) < self.num_points:

            # Decide which direction to go, and how far to go. 
            x_direction = choice([1, -1]) #1
            x_distance = choice ([0, 1, 2, 3, 4]) #2
            x_step = x_direction * x_distance #3 
            
            y_direction = choice([1, -1])
            y_distance = choice ([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance #4

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0: #5
                continue

            # Calculate the new position
            x = self.x_values[-1] +  x_step #6
            y = self.y_values[-1] + y_step

            self.x_values.append(x) #7
            self.y_values.append(y)

            
# Notes: 
# 1: We use choice([1, -1]) to choose a value for x_direction, which returns either 1 for movement to the right or −1 for movement to the left

# 2: choice([0, 1, 2, 3, 4]) randomly selects a distance to move in that direction. We assign this value to x_distance. The inclusion of a 0 allows for the possibility of steps that have movement along only one axis.

# 3: We determine the length of each step in the x- and y-directions by multiplying the direction of movement by the distance chosen. A positive result for x_step means move to the right, a negative result means move to the left, and 0 means move vertically. 

# 4: A positive result for y_step means move up, negative means move down, and 0 means move horizontally. 

# 5: If the values of both x_step and y_step are 0, the walk doesn’t go anywhere; when this happens, we continue the loop

# 6: To get the next x-value for the walk, we add the value in x_step to the last value stored in x_values 6 and do the same for the y-values. (presumably its -1 to counteract the indexing)

# 7: When we have the new point’s coordinates, we append them to x_values and y_values.