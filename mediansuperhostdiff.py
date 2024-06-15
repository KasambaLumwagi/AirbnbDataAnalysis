import pandas as pd
from data_loader import load_data

# Assuming listings is your DataFrame
# Example data

listings = load_data()

# Convert price to numeric if needed
listings['price'] = pd.to_numeric(listings['price'], errors='coerce')

# Separate data into superhosts and non-superhosts
superhosts = listings[listings['host_is_superhost'] == 't']
non_superhosts = listings[listings['host_is_superhost'] == 'f']

# Calculate medians
median_superhosts = superhosts['price'].median()
median_non_superhosts = non_superhosts['price'].median()

# Find the difference between medians
median_difference = median_superhosts - median_non_superhosts

print(f"Median price of superhosts: {median_superhosts}")
print(f"Median price of non-superhosts: {median_non_superhosts}")
print(f"Difference in medians: {median_difference}")
