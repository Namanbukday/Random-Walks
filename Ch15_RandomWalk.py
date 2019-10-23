from random import choice


class RandomWalk():
    """ A class to generate random walks. """

    def __init__(self, num_points=5000):
        """ Initialize attributes of a walk. """
        self.num_points = num_points

        # All walks should start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ Calculate all the points in the walk. """
        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            # Decide in which direction to go and how far in that direction.
            # For 'x-axis'
            x_direction = choice([-1, 1])  # move in left or right direction.
            x_distance = choice([0, 1, 2, 3, 4])  # the number of steps taken.
            x_steps = x_direction * x_distance

            # Similarly for 'y-axis'
            y_direction = choice([-1, 1])  # move up or down.
            y_distance = choice([0, 1, 2, 3, 4])  # steps taken in that direction
            y_steps = y_direction * y_distance

            # Reject moves that go nowhere
            if x_steps == 0 and y_steps == 0:
                continue

            # Calculate the next x- and y- values:
            next_x = self.x_values[-1] + x_steps
            next_y = self.y_values[-1] + y_steps

            self.x_values.append(next_x)
            self.y_values.append(next_y)
