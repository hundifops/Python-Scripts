# Initial list
values = [1, [2, 3], 4, 'code']

for i in range(len(values)):
    print('Index', i)
    print('Value', values[i])
    print('----') # delimiter


countries = [['USA', 9629091, 331002651], ['Canada', 9984670, 37742154], ['Germany', 357114, 83783942], ['Brazil', 8515767, 212559417], ['India', 3166391, 1380004385]]

for country in countries:
    for j in countries: # j is a new variable
        print(j, end= '') 
        print('\n') # to print a new line after nested loop finish
