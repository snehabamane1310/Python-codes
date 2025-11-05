# histogram.py
import matplotlib.pyplot as plt
import numpy as np

# Generate random data (normal distribution)
data = np.random.randn(1000)

# Create histogram
plt.figure(figsize=(8, 5))
plt.hist(data, bins=20, color='orange', edgecolor='black')

# Add labels and title
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the histogram
plt.show()
