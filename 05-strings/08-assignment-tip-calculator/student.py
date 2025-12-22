# write your code here
def tip_calculator():
    total_price=(input("Enter total price "))
    tip_percentage=(input("Enter tip percentage (default=20) "))
    defult_tip=20

    if tip_percentage=="":
        tip_percentage=defult_tip
        
    tip_amount=(float(total_price)*float(tip_percentage))/100
    final_price=float(total_price)+tip_amount
    return print(f"You have to pay {round(final_price)}")
tip_calculator()
