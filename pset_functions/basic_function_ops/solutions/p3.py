"""
Function Basics III - Default Arguments
"""

# Now write a and call function called "fave_colors" that separately intakes a person's first name, a person's last name, and **optionally** their favorite color.

# The function should create and return a dict with the full name as a key and the favorite color as the value. If the person does not enter a favorite color, you should assume they have no favorite color and assign theirs to None. Try both use cases.

def fave_colors(first,last,color=None):
	full_name = first + ' ' + last
	fave_colors = {full_name: color}

	return fave_colors

taq = fave_colors('Taq','Karim','blue')
ricardo = fave_colors('Ricardo','Galbis')

print(taq,'\n',ricardo)
# {'Taq Karim': 'blue'}
# {'Ricardo Galbis': None}