"""
Cleaning Data II - Find Null Values
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')

# Use the below df for these problems:

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]


# Return a count of the null values in wine_ratings.
print(wine_ratings.isnull().sum())
"""
title         0
country      63
rating        0
price      8996
"""

# Print out the number of rows in wine_ratings.
print(len(wine_ratings)) # 129971

