import datetime
import matplotlib.pyplot as plt

# Collect user input
last_period_date = input("Enter the date of your last period (YYYY-MM-DD): ")
cycle_length = int(input("Enter the length of your menstrual cycle (in days): "))
period_length = int(input("Enter the length of your period (in days): "))

# Calculate cycle data
last_period = datetime.datetime.strptime(last_period_date, "%Y-%m-%d").date()
next_period = last_period + datetime.timedelta(days=cycle_length)
luteal_phase = cycle_length - period_length
avg_cycle_length = cycle_length

# Visualize data
cycle_dates = [last_period + datetime.timedelta(days=x) for x in range(0, cycle_length)]
plt.plot(cycle_dates, [1 if x < period_length else 0 for x in range(0, cycle_length)])
plt.title("Menstrual Cycle")
plt.xlabel("Date")
plt.ylabel("Menstruating (1=yes, 0=no)")
plt.show()

# Save data
# Code to save data goes here
