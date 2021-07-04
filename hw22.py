#Exercise 1
#Create a list named students containing some student names (strings)
students = ['Hayley', 'Peiyi', 'Maria', 'Jorge', 'Rafael',
'Michael', 'Asher', 'Handsome', 'Chris']
#Print out the second student's name.
print(students[1])
#Print out the last student's name.
print(students[-1])
#Exercise 2
#Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
foods = ('apples', 'oranges', 'grapes', 'peaches', 'bananas', 'plums', 'tangerines',
'watermelon', 'pumpkin')
#Use a for loop to print out the string "food goes here is a good food".
for i in foods:
    print(f"{i} is a good food")
#Exercise 3
#Using a for loop, print just the last two food strings from foods.
print(foods[-2:])
#Exercise 4
#Create a dictionary named home_town containing the keys of city, state and population.
home_town = {
    'city': 'Port Washinton',
    'state': 'New York',
    'population': 15808
}
#Print a string with this format: "I was born in city, state - population of population"
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")
#Exercise 5
#Iterate over the key: value pairs in home_town and print a string for each item
for key,val in home_town.items():
    print(f"{key} = {val}")
#Exercise 6
#Create an empty list named cohort
cohort = []
#Using a for loop, add one dictionary to the cohort list for each student name.
'''Each dictionary should have this shape:

 {
 	'student': 'Tina',
 	'fav_food' 'Cheeseburger'
 }'''
#Iterate over cohort printing out each element.
f = 0
for x in students:
     i = {'student': x, 'fav_food': foods[f]}
     f += 1
     cohort.append(i)
print(cohort)
#Exercise 7
'''Using the list of students and list comprehension, assign to a variable
named awesome_students a new list containing strings similar to this:
#["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
Iterate over awesome_students printing out each string.'''
awesome_students = []
for x in students:
    awesome_students.append(x)
print(awesome_students)
for x in awesome_students:
    print(f"{x} is awesome!")
#Exercise 8
#Using the tuple foods and list comprehension within a for loop, 
#print each food string that contains the letter a.
for x in foods:
    if 'a' in x:
        print(x)

