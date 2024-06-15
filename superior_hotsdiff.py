from data_loader import load_data
import pandas as pd

# Load data
listings, _ = load_data()

# Define criteria for superior hosts
superior_hosts = listings[(listings['host_is_superhost'] == 't') & (listings['host_listings_count'] > 5)]

# Calculate mean prices for superior hosts and non-superhosts who do not meet superior criteria
mean_price_superior = superior_hosts['price'].mean()

# Non-superhosts who do not meet superior criteria
non_superior_hosts = listings[(listings['host_is_superhost'] == 'f') | (listings['host_listings_count'] <= 5)]
mean_price_non_superior = non_superior_hosts['price'].mean()

# Find the difference in mean prices
mean_difference = mean_price_superior - mean_price_non_superior

print(f"Mean price of superior hosts: {mean_price_superior}")
print(f"Mean price of non-superior hosts: {mean_price_non_superior}")
print(f"Difference in means: {mean_difference}")
