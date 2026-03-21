import numpy as np
import matplotlib.pyplot as plt

# Assume we have this data: hours of advertisement vs weekly sales
ad_hours = np.array([10, 20, 30, 40, 50])
weekly_sales = np.array([200, 420, 650, 800, 950])
ad_hours = np.array([10, 20, 30, 40, 50])
x = ad_hours
y = weekly_sales
mean_x = np.mean(ad_hours)
mean_y = np.mean(weekly_sales)
# TODO: calculate both the slope (m) and y-intercept (c)
m = np.sum((x - mean_x)*(y - mean_y)) / np.sum((x - mean_x)**2)
c = mean_y - m * mean_x
print(f"Sales = {c:.2f} + {m:.2f}*Ad_Hours")

# Plotting data and line
plt.scatter(ad_hours, weekly_sales, color='blue')  # Scatter plot of actual data
plt.plot(ad_hours, c + m * ad_hours, 'r')  # Line plot of the regression line
plt.xlabel("Ad Hours")
plt.ylabel("Weekly Sales")
plt.title("Hours of advertisement vs. Weekly Sales")
plt.show()