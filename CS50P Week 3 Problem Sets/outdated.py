months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}

def main():
    # while loop to keep prompting until user gives valid input
    while True:
        try:
            date = input("Date: ")
            date = date.strip()
            
            # created list of chars of the input
            date_list = list(date)
            
            # if the first two chars of the list are digits, calls the method used for digit dates
            if date_list[0].isdigit():
                result = middle_endian_digit(date)
                
                if result == False:
                    continue
                else:
                    print(str(result))
                    break
            
            # if the first char is a letter, calls the method used for string dates
            elif date_list[0].isalpha():
                result = middle_endian(date)
                
                if result == False:
                    continue
                else:
                    print(str(result))
                    break
            
            # if it isn't a valid input, continues the program
            else:
                continue
            
        except ValueError:
            continue

# function to convert middle-endian dates to ISO 8601 format
def middle_endian(date):
    
    if "," not in date:
        return False
    
    # removes the comma
    date = date.replace(",", "")
    
    # splits by whitespace and assigns variables for the respective month day and year values
    month, day, year = date.split(" ")
    month = int(months[month])
    day = int(day)
    year = int(year)
    
    if day > 31:
        return False
    
    if month > 12:
        return False
    
    if month < 10:
        month = (f"0{month}")
        
    if day < 10:
        day = (f"0{day}")
    
    # concatenates the year, month, and day into ISO format and returns it
    iso = (f"{year}-{month}-{day}")
    return iso

# function to convert middle-endian dates using digits to ISO 8601 format
def middle_endian_digit(date_digit):
    
    # splits by whitespace and assigns variables for the respective month day and year values
    month, day, year = date_digit.split("/")
    
    month = int(month)
    day = int(day)
    year = int(year)
    
    if day > 31:
        return False
    
    if month > 12:
        return False
    
    # boolean expression to determine whether the month should have a 0 added in front of it, 
    # thenconcatenates the year, month, and day into ISO format and returns it
    if month < 10:
        month = (f"0{month}")
        
    if day < 10:
        day = (f"0{day}")
    
        iso = (f"{year}-{month}-{day}")
    
    return iso

main()