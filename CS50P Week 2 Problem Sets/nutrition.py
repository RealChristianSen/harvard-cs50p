# dict of fruits as keys and calories as values
fruits = {
    
    "Apple": "130",
    "Avocado": "50",
    "Banana": "110",
    "Cantaloupe": "50",
    "Grapefruit": "60",
    "Grapes": "90",
    "Honeydew Melon": "50",
    "Kiwifruit": "90",
    "Lemon": "15",
    "Lime": "20",
    "Nectarine": 60,
    "Orange": 80,
    "Peach": "60",
    "Pear": "100",
    "Pineapple": "50",
    "Plums": "70",
    "Strawberries": "50",
    "Sweet Cherries": "100",
    "Tangerine": "50",
    "Watermelon": "80"
    
}

# main fnc to prompt user for fruit and output caloric count
def main():
    fruit = input("Item: ")
    fruit = fruit.title()
    
    if fruit not in fruits:
        print("")
        
    else:
        print(f"Calories: {calories(fruit)}")

# calories fnc to parse through fruits dict and returns 
# the calorie count of the matching user input and fruit key value
def calories(fruit):
    
    # for loop indicing through fruits
    for i in fruits:
        
        # boolean expression returning the calorie count of the matching fruit's respective value
        if fruit == i:
            return fruits[i]
        
main()