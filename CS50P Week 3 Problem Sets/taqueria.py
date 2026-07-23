entrees = {
    
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    
}

def main():
    
    # defines total cost
    totalCost = 0
    
    # while loop to keep program looping until control d is entered
    while True:
            
            # try except block to catch EOFError from control d and keep looping if not
            try:
            
                item = input("Item: ")
                
                # normalizes casing
                item = item.lower().title()
                
                # if item is not in entree list continues loop
                if item not in entrees:
                    continue
                
                # adds item cost to total cost
                totalCost += entrees[item]
                
                print(f"Total: ${totalCost:.2f}")
                
            except EOFError:
                break

main()