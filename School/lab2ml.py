# Import necessary modules
import numpy as np
import time
import matplotlib.pyplot as plt

# PART 1: Matrix Addition and Timing

# Create two 100 x 100 arrays filled with random numbers
A = np.random.rand(100, 100)
B = np.random.rand(100, 100)

# Initialize empty lists to store timings
times_for_loop = []
times_plus_operator = []

# Add matrices using a double for loop and time it
for _ in range(1000):
    start_time = time.time()
    result_for_loop = np.zeros((100, 100))
    for i in range(100):
        for j in range(100):
            result_for_loop[i, j] = A[i, j] + B[i, j]
    times_for_loop.append(time.time() - start_time)

# Add matrices using the '+' operator and time it
for _ in range(1000):
    start_time = time.time()
    result_plus_operator = A + B
    times_plus_operator.append(time.time() - start_time)

# Calculate the average and standard deviation of the running times
avg_time_for_loop = np.mean(times_for_loop)
std_dev_for_loop = np.std(times_for_loop)

avg_time_plus_operator = np.mean(times_plus_operator)
std_dev_plus_operator = np.std(times_plus_operator)

# Print the average and standard deviation of running times
print("For loop method - Average time: {:.5f} seconds, Standard deviation: {:.5f}".format(avg_time_for_loop, std_dev_for_loop))
print("Plus operator method - Average time: {:.5f} seconds, Standard deviation: {:.5f}".format(avg_time_plus_operator, std_dev_plus_operator))

# Plot histograms of the running times
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(times_for_loop, bins=30, color='blue', alpha=0.7)
plt.title("For Loop Method Timing")
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.hist(times_plus_operator, bins=30, color='green', alpha=0.7)
plt.title("Plus Operator Method Timing")
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# PART 2: Custom Example Program
# Description: This program creates a sine wave and a cosine wave using NumPy, then plots both waves on the same graph.

# Generate x values from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 500)

# Calculate the sine and cosine of x values
sine_wave = np.sin(x)
cosine_wave = np.cos(x)

# Plot the sine and cosine waves
plt.figure(figsize=(8, 6))
plt.plot(x, sine_wave, label='Sine Wave', color='blue')
plt.plot(x, cosine_wave, label='Cosine Wave', color='red', linestyle='--')

# Add labels and title
plt.title('Sine and Cosine Waves')
plt.xlabel('x values')
plt.ylabel('Amplitude')

# Add a legend
plt.legend()

# Display the plot
plt.show()
