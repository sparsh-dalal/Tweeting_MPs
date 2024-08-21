import pandas as pd
import matplotlib.pyplot as plt
import calendar

# Load the data from the pickle file
df = pd.read_pickle('BJP.csv')
#df['CAA'] = df['Caa']

#df.drop(df.columns[[0,3]], axis=1, inplace=True)


# Extract the columns of interest
cols_of_interest = df.columns[0:]  # Exclude the first column
data = df[cols_of_interest]

# data.iloc[:, 0] = data.iloc[:, 0] / 36
# data.iloc[:, 1] = data.iloc[:, 1] / 242
# data.iloc[:, 2] = data.iloc[:, 2] / 12
# data.iloc[:, 3] = data.iloc[:, 3] / 11
# data.iloc[:, 4] = data.iloc[:, 4] / 10
# data.iloc[:, 5] = data.iloc[:, 5] / 7
# data.iloc[:, 6] = data.iloc[:, 6] / 5

# Convert month index to month name and year
month_names = [calendar.month_name[(i + 6) % 12 + 1] + ' ' + str(2019 + (i + 6) // 12) for i in range(len(df))]

# Plot only the first month of each quarter
quarter_starts = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42]
month_names_quarter_starts = [month_names[i] for i in quarter_starts]
data_quarter_starts = data.iloc[quarter_starts]

# Set up the plot
plt.figure(figsize=(4, 4))
plt.xlabel('Month')
plt.ylabel('Frequency of Hashtags')
plt.title('Hashtags used by BJP over time')

# Plot each column as a separate line with a different color and label
plt.rcParams['figure.figsize'] = [2, 2]
for i, col in enumerate(data.columns):
    plt.plot(month_names, data[col], label=col, color=f'C{i}')

# Plot quarter starts with different marker style and size
plt.plot(month_names_quarter_starts, data_quarter_starts.values, marker='o', markersize=0, linestyle='None', color='black')

# Enable the legend
plt.legend()

# Rotate the x-axis labels to prevent overlapping
plt.xticks(rotation=90)

# Show the plot
plt.show()
