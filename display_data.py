import pandas as pd
from dataLoader import load_data

def main():
    # Load the datasets
    listings, reviews = load_data()

    # Display the first few rows of each dataset
    print("Listings Data:")
    print(listings.head())

    print("\nReviews Data:")
    print(reviews.head())

    # Optionally, you could provide some basic statistics or information
    print("\nListings Data Information:")
    print(listings.info())

    print("\nReviews Data Information:")
    print(reviews.info())

    print("\nListings Data Description:")
    print(listings.describe())

    print("\nReviews Data Description:")
    print(reviews.describe())

if __name__ == "__main__":
    main()
