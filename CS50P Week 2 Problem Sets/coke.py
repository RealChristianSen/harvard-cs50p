def main():
    amount_due = 50
    
    # while true statement to keep program running until user meets pay requirement
    while amount_due > 0:
        
        # outputs amount due
        print(f"Amount due: {amount_due}")
        
        # prompts for user pay
        customer_pay = int(input("Insert Coin: "))
        
        # boolean expression to only take required denominations of pay and subtract for amount due
        if customer_pay == 5 or customer_pay == 25 or customer_pay == 10:
            amount_due = amount_due - customer_pay
    
    # converts the extra paid to positive and outputs the change owed            
    change_owed = abs(amount_due)
    print(f"Change owed: {change_owed}")
    
main()