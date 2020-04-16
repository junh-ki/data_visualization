import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # 1. Make a random walk.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # 2. Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    #fig, ax = plt.subplots(figsize=(15, 9))
    #fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
        edgecolors='none', s=1)
    #ax.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)

    # 3. Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100, zorder=2)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', 
        s=100, zorder=2)

    # 4. Remove the axes.
    #ax.get_xaxis().set_visible(False)
    #ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
