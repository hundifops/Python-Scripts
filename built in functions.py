# Now we're getting into the math of things :)

# Using the same countries from before 

countries = [["USA", 9629091, 331002651], ["Canada", 9984670, 37742154], ["Germany", 357114, 83783942], ["Brazil", 8515767, 212559417], ["India", 3166391, 1380004385]]

for i in range(len(countries)):
    if type(countries[i]) is list:
        # computing population density for a country
        pop_dens = countries[i][2]/countries[i][1]
        print(countries[i][0], pop_dens, 'people per km²')

# reducing numbers given to 2 decimal places

countries = [["USA", 9629091, 331002651], ["Canada", 9984670, 37742154], ["Germany", 357114, 83783942], ["Brazil", 8515767, 212559417], ["India", 3166391, 1380004385]]
for i in range(len(countries)):
    if type(countries[i]) is list:
        pop_dens = round(countries[i][2]/countries[i][1], 2)
        print(countries[i][0], pop_dens, 'people per km²')

# List of functions
# min(x, y, ......) - returns the smallest number
# max(x, y, ......) - returns the largest number
# abs(x) - returns the absolute value
# round (x,n) -  rounds the number x to n decimal places
# pow(x, n) - raises the number x to the n power
