import matplotlib.pyplot as plt
import numpy as np

# Define a range of x values
x = [1, 2, 3]

# Calculate y values using the equation y = 10x
y = [10 * val for val in x]

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = 10x', color='blue', marker='o')

# Add labels and title
plt.title('Graph of y = 10x')
plt.xlabel('x-axis (Number of notebooks)')
plt.ylabel('y-axis (Price)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)  # Add x-axis line
plt.axvline(0, color='black', linewidth=0.5)  # Add y-axis line
plt.legend()
plt.show()