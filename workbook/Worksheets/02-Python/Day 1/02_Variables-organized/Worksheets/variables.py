# Creates a variable with a string "Frankfurter"
title = "Frankfurter"
years = 23
hourly_wage = 65.40
expert_status = True

# Print the variables
print(title)
print(years)
print(hourly_wage)
print(expert_status)

# Prints the data type of each declared variable
print("The data type of variable title is", type(title))
print("The data type of variable years is", type(years))
print("The data type of variable hourly_wage is", type(hourly_wage))
print("The data type of variable expert_status is", type(expert_status))

# Using variable names in calculations
total_miles = 257
gallons_gas = 7
miles_per_gallon = total_miles / gallons_gas
print(miles_per_gallon)
# Updating variables using assignment
miles = 48
kilometers = miles / 0.621371

# Substituting/formatting variable
message = f"The total kilometers driven was: {kilometers}"
print(message)

# Variable naming conventions
# Bad Example
mpg = 24
# Better Example
miles_per_gallon = 24

original_price = 198.87
current_price = 254.32
increase = current_price - original_price
percent_increase = (increase / original_price) * 100
print(percent_increase)
print(increase)
print(original_price)
print(current_price)