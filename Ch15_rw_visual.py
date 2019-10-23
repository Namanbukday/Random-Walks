import matplotlib.pyplot as plt

from Ch15_RandomWalk import RandomWalk

# Keep making new walk, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()  # Getting x_values and y_values for scatter()

    # Set the size of the plotting window/ screen
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    # Emphasize the first and the last points
    plt.scatter(0, 0, c='pink', edgecolor='none', s=100)  # Starting point(0,0)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow', edgecolor='none', s=100)  # last point of x- and y- values

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input(" Make another walk? (y/n) :")
    if keep_running == 'n':
        break
