def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    
    for name in names:
        print(write_letter(name, "Princess Peach"))
        
    
def write_letter(reciever, sender):
    return f"""

    _________________________________________
    
    Dear {reciever},
    
    You are cordially invited to a ball 
    at Peach's Castle this evening, 7:00 PM.
    
    Sincerely,
    {sender}
    _________________________________________
    """
    
main()