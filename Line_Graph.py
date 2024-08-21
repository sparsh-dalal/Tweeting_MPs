import pandas as pd
import matplotlib.pyplot as plt
import calendar

# Load the data from the pickle file
df = pd.read_csv(r'C:\Users\dalal\PycharmProjects\Tweepy\Runining_Files\Party_Tweet.csv')

# Extract the columns of interest
cols_of_interest = df.columns[1:]  # Exclude the first column
data = df[cols_of_interest]

# Convert month index to month name and year
month_names = [calendar.month_name[(i + 5) % 12 + 1] + ' ' + str(2019 + (i + 5) // 12) for i in range(len(df))]

# Set up the plot
plt.figure(figsize=(8, 6))
plt.xlabel('Month')
plt.ylabel('Number')
plt.title('Numbers by Month')

# Plot each column as a separate line with a different color and label
for i, col in enumerate(data.columns):
    plt.plot(month_names, data[col], label=col, color=f'C{i}')

# Enable the legend
plt.legend()

# Show the plot
plt.show()
