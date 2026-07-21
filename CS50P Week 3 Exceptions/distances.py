distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    try:
        spacecraft = input("Enter a spacecraft: ")
        
    except KeyError:
        print(f"'{spacecraft}' is not in dictionary")
        return
            
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return
    
    au = float(distances[spacecraft])    
    m = convert(au)
    print(f"{m} m away")
        
def convert(au):
    return au * 149597870700

main()