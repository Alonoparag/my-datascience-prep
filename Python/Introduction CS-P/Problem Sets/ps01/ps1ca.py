"""
    * We are looking for a saving rate
    * we have a set number of months to arrive at the desires sum
    * Binary Tree between 1/10000 to 1
    * yield results in 36 steps (months)
    * if steps == 36 and current savings are within $100 of downpayment, success
    * if higher than 36 steps and midian rate equals 1, output error
    * if lower than 36 steps, sets the new high border to midian rate
    * if higher than 36 steps, sets the new low border to midian rate
    
"""
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
    def savings_truncator(num):
        decimal_part = num - int(num)
        decimal_part = float(str(decimal_part)[0:4])
        return int(num) + decimal_part

    def find_rate(rate_low, rate_high):
        rate_median = (float(rate_low)+float(rate_high))/2
        #truncating the rate into 5th order
        rate_median=float(str(rate_median)[0:6])
        return rate_median
    def compute_monthly(salary):
        return salary/12.0
    #========================
    # INITIAL PROGRAM VALUES
    #========================
    init_annual_salary = float(input("Enter your annual salary:\n>>>"))
    annual_salary = init_annual_salary
    monthly_salary = compute_monthly(annual_salary)
    total_cost = 10**6
    semi_annual_raise = 0.07
    portion_down_payment = float(total_cost)*0.25
    current_savings = 0.0
    annual_rate = 0.04
    months_to_save = 36
    steps = 0
    func_steps=0
    rate_low = 0
    rate_high = 1.0
    rate_optimal = find_rate(rate_low, rate_high)
    while True:
        #========================
        # INFINTE LOOP GUARD
        #========================
        if func_steps > 15:
            print("Infinite loop error. Exceeding function steps limit\nBreak function")
            break
        #========================
        # ITERATION DETAILS
        #========================   
        print("============\nNew Iteration")
        print("the low bar is: ",rate_low)
        print("the high bar is: ",rate_high)
        print("current savings are: ", current_savings)
        print("step: ",func_steps)
        print("current rate: ", rate_optimal)
        #========================
        # COMPUTING LOOP
        #========================  
        while current_savings < portion_down_payment-100:
            if steps >= months_to_save:
                print("!!!exceeding 36 months!!!")
                break
        #========================
        # DEBUGGING COMPUTATION LOOP
        #========================  
            # if func_steps == 5:
            #     print("month: #"+str(steps))
            #     print("current savings before: ", current_savings)
            #     print("annual rate: ", annual_rate)
            #     print("monthly salary: ", monthly_salary)
            #     print("current rate: ", rate_optimal)
            steps +=1
            current_savings += current_savings*annual_rate/12+monthly_salary*rate_optimal
            current_savings = savings_truncator(current_savings)
        #========================
        # DEBUGGING COMPUTATION LOOP
        #========================  
            # if func_steps == 5:
            #     print("current savings after: ", current_savings)
            if steps % 6 == 0:
                annual_salary += annual_salary*semi_annual_raise
                monthly_salary = annual_salary/12
        #========================
        # CONDITION TO QUIT WHEN EXCEEDED THE AMOUNT NEEDED TO SAVE
        #========================  
            if current_savings >= portion_down_payment-100:
                print("!!!WARNING!!!            Ammount exceeded")
                break
        #========================
        # SAVING DETAILS
        #========================  
        print("The downpayment is: ",portion_down_payment)
        print("You managed to save: ",current_savings)
        print("Distance from downpayment", savings_truncator(portion_down_payment - current_savings))
        print('it took', steps, "steps - months to save")
        #========================
        # RECUSION LOGIC
        #========================
        #========================
        # DEBUGGING COMPUTATION LOOP
        #========================
        if steps == months_to_save and current_savings >= portion_down_payment - 100:
            print("DEBUGGING SUCCESS CONDITION")
            print("have we saved for 36 month? ", str(steps == months_to_save))
            print("ARE THE CURRENT SAVINGS ARE AT LEAST $100 UNDER THE DOWN PAYMNET? ", str(current_savings >= portion_down_payment - 100))
            print("ARE THE CURRENT SAVINGS ARE AT MOST $100 OVER THE DOWN PAYMNET? ", str(current_savings <= portion_down_payment + 100))

        if steps == months_to_save and current_savings >= portion_down_payment - 100 and current_savings <= portion_down_payment + 100:
            print("============\n== SUCCESS==\n============")
            print("Best savings rate:", rate_optimal)
            print("Steps in bisection search:", func_steps)
            break
        elif steps > months_to_save and rate_optimal >= 1-0.00001:
            print("============\n== FAILURE==\n============")
            print("It is not possible to pay the down payment in three years.")
            break
        elif steps <= months_to_save:
            print("too,much")
            func_steps +=1
            steps = 0
            current_savings = 0.0
            annual_salary = init_annual_salary
            monthly_salary = compute_monthly(annual_salary)
            rate_high = rate_optimal
            rate_optimal = find_rate(rate_low, rate_high)
        elif steps >= months_to_save:
            print("not enough")
            func_steps +=1
            steps = 0
            current_savings = 0.0
            annual_salary = init_annual_salary
            monthly_salary = compute_monthly(annual_salary)
            rate_low = rate_optimal
            rate_optimal = find_rate(rate_low, rate_high)
        #========================
        # INFINTE LOOP GUARD
        #========================
        if steps == months_to_save: func_steps+=1

           
problem()

while input("Do you want to calculate other values?(Y\\N)\n>>>") == "y":
    problem()
print("Goodbye!")