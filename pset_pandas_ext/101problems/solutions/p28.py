"""
28. How to find all the local maxima (or peaks) in a numeric series?
"""
"""
Difficiulty Level: L3
"""
"""
Get the positions of peaks (values surrounded by smaller values on both sides) in ser.
"""
"""
Input
"""
"""
ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])
"""
"""
Desired output
"""
"""
array([1, 5, 7])
"""

# Input
ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])

# Solution
dd = np.diff(np.sign(np.diff(ser)))
peak_locs = np.where(dd == -2)[0] + 1
peak_locs