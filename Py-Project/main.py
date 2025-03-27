MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


# deposit
def deposit():
    while True:
        amount = input("Deposit ?: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit more than 0.")
        else:
            print("Enter the valid amount number ")        
    return amount        


#  number of lines

def get_number_of_lines():
    while True:
        lines = input("Enter the no.of lines (1 -to-)"+ str(MAX_LINES)+")? :")
        
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the Valid No. of Lines: ")
        else:
            print("Enter the number ")        
    return lines        


# Betting

def get_bet():
    while True:
        amount = input("Bet like you ?: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - to - ${MAX_BET}.")
        else:
            print("Enter the valid amount ")        
    return amount  



# Main for all functions
def main():
    balance = deposit()
    lines = get_number_of_lines()
    
    # Amount is present in my Deposit..[balance].. or not
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You needed amount: ${total_bet - balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines. Total bet is : ${total_bet}")
    
        
main()    
    