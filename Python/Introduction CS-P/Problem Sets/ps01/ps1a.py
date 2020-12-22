# annual_salary = float(input("Enter your annual salary:\n>>>"))
# portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ​)\n>>>"))
# total_cost = float(input("Enter the cost of your dream home:​\n>>>"))
# portion_down_payment = float(total_cost)*0.25
# current_savings = 0.0
# annual_rate = 1.04
# months = 0
# while current_savings < portion_down_payment:
#     if months == 0:
#         print("only starting")
#         months +=1
#         current_savings += annual_salary/12*portion_saved
#         print(current_savings, months)
#     else:
#         print("getting close")
#         months +=1
#         current_savings = current_savings*annual_rate/12+annual_salary/12*portion_saved
#         print(current_savings, months)
    
# print("Number of months:", months)

def problem():
    annual_salary = float(input("Enter your annual salary:\n>>>"))
    monthly_salary = annual_salary/12.0
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ​\n>>>"))
    total_cost = float(input("Enter the cost of your dream home:​\n>>>"))
    portion_down_payment = float(total_cost)*0.25
    current_savings = 0.0
    annual_rate = 0.04
    months = 0


    while current_savings < portion_down_payment:
        if months == 0:
            print("only starting")
            months +=1
            current_savings += monthly_salary*portion_saved
            print(current_savings, months)
            
        else:
            print("getting close")
            months +=1
            current_savings += current_savings*annual_rate/12+monthly_salary*portion_saved
            print(current_savings, months)
            
        
    print("Number of months:", months)

problem()

while input("Do you want to calculate other values?(Y\\N)\n>>>") == "Y":
    problem()
print("Goodbye!")