# line_graph.py
import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create line plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, color='red', linewidth=2, label='sin(x)')

# Add labels and title
plt.title('Line Graph Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add legend and grid
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Show plot
plt.show()
