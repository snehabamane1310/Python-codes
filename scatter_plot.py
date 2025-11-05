# scatter_plot.py
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# Create scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')

# Add labels and title
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add color bar
plt.colorbar(label='Color scale')

# Show plot
plt.show()
