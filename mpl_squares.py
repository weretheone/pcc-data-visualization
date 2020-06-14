import matplotlib.pyplot as plt

# Define the values
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Choose the style, before other definitions
plt.style.use('seaborn-white')

# Define the plot
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set the chart totle and labels
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set the tick labels
ax.tick_params(axis='both', labelsize=14)

# Show the plot
plt.show()