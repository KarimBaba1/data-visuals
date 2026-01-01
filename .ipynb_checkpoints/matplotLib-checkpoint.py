import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()

# Generate random data (normal distribution)
x = np.random.randn(10000)

# Plot histogram
ax.hist(x, bins=100)

# Add title with LaTeX-style math
ax.set_title("Normal distribution with $\mu=0, \sigma=1$")

# Show the plot interactively
plt.show()
