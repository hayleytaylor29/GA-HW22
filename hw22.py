#Create a list named students containing some student names (strings)
students = ['Hayley', 'Peiyi', 'Maria', 'Jorge', 'Rafael',
'Michael', 'Asher', 'Handsome', 'Chris']
#Print out the second student's name.
print(students[1])
#Print out the last student's name.
print(students[-1])
#Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
foods = ('apples', 'oranges', 'grapes', 'peaches', 'bananas', 'plums', 'tangerines',
'watermelon', 'pumpkin')
#Use a for loop to print out the string "food goes here is a good food".
for i in foods:
    print(f"{i} is a good food")
#Using a for loop, print just the last two food strings from foods.
print(foods[-2:])
#Create a dictionary named home_town containing the keys of city, state and population.
home_town = {
    'city': 'Port Washinton',
    'state': 'New York',
    'population': 15808
}
#Print a string with this format: "I was born in city, state - population of population"
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")
#Iterate over the key: value pairs in home_town and print a string for each item
for key,val in home_town.items():
    print(f"{key} = {val}")