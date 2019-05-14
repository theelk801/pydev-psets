"""
Selecting Data II - Access a Column
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')


# Return the winery column in a variable called "wineries".

wineries = wine_reviews['winery']

# Run a command to return the type of wineries.

print(type(wineries)) # <class 'pandas.core.series.Series'>