from load_data import load_data
from sort import bubble_sort
import matplotlib.pyplot as plt

data = load_data('data/activity.csv')

power_W = data['PowerOriginal']

sorted_power_W = bubble_sort(power_W)

plt.plot(sorted_power_W[::-1])
plt.title('Power Consumption')
plt.xlabel('Time (s)')
plt.ylabel('Power (W)')
plt.savefig('figures/power_curve.png')
plt.show()
