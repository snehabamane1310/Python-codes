# bar_chart.py
import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 33]

# Create a bar chart
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color='skyblue', edgecolor='black')

# Add labels and title
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# Add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the chart
plt.show()
