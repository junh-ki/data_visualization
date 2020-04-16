from matplotlib import pyplot as plt

# Define data.
x_values = list(range(5001))
cubes = [x**3 for x in x_values]
#x_values = [1, 2, 3, 4, 5]
#cubes = [1, 8, 27, 64, 125]

# Make plot.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, cubes, c=cubes, cmap=plt.cm.Greens, s=10)
#ax.scatter(x_values, cubes, edgecolor='none', s=40)

# Set chart title and label axes.
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 5100, 0, 5100**3])

# Show or save plot.
plt.show()
#plt.savefig('cube_plot.png', bbox_inches='tight')
