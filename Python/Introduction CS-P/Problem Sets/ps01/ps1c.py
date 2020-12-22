"""
    * We are looking for a saving rate
    * we have a set number of months to arrive at the desires sum
    * Binary Tree between 1/10000 to 1
    * yield results in 36 steps (months)
    * if steps == 36 and current savings are within $100 of downpayment, success
    * if higher than 36 steps and midian rate equals 1, output error
    * IF THE AMMOUNT SAVED EXCEEDS THE DOWNPAYMENT AND THE DIFFERENCE BETWEEN THE HIGH BORDER TO THE LOW BORDER IS MORE THAN TO 0.0001, sets the new high border to midian rate
    * if AFTER 36 STEPS THE AMOUNT SAVED IS LOWER THAN DOWNPAYMENT, sets the new low border to midian rate
    
"""

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
        func_steps+=1
        #========================
        # COMPUTING LOOP
        #========================  
        while current_savings < portion_down_payment-100:
            if steps >= months_to_save:
                break
            steps +=1
            current_savings += current_savings*annual_rate/12+monthly_salary*rate_optimal
            current_savings = savings_truncator(current_savings)
            if steps % 6 == 0:
                annual_salary += annual_salary*semi_annual_raise
                monthly_salary = annual_salary/12
        #========================
        # CONDITION TO QUIT WHEN EXCEEDED THE AMOUNT NEEDED TO SAVE
        #========================  
            if current_savings >= portion_down_payment-100:
                break
        if steps == months_to_save and current_savings >= portion_down_payment - 100 and current_savings <= portion_down_payment + 100:
            print("============\n== SUCCESS==\n============")
            print("Best savings rate:", rate_optimal)
            print("Steps in bisection search:", func_steps)
            break
        elif rate_high == rate_low and current_savings >= portion_down_payment - 100:
            print("============\n== SUCCESS==\n============")
            print("Best savings rate:", rate_optimal)
            print("Steps in bisection search:", func_steps)
            break
        elif steps >= months_to_save and rate_optimal >= 1-0.0001:
            print("============\n== FAILURE==\n============")
            print("It is not possible to pay the down payment in three years.")
            break
        elif rate_high - rate_low <=0.0001 and current_savings < portion_down_payment - 100:
            print("============\n== SUCCESS==\n============")
            print("Best savings rate:", rate_high)
            print("Steps in bisection search:", func_steps)
            break
        elif current_savings >= portion_down_payment-100:
            steps = 0
            current_savings = 0.0
            annual_salary = init_annual_salary
            monthly_salary = compute_monthly(annual_salary)
            rate_high = rate_optimal
            rate_optimal = find_rate(rate_low, rate_high)
        elif current_savings < portion_down_payment - 100:
            if round(rate_high - rate_low, 4) <=0.0002:
                steps = 0
                current_savings = 0.0
                annual_salary = init_annual_salary
                monthly_salary = compute_monthly(annual_salary)
                rate_low +=0.0001
                rate_optimal = find_rate(rate_low, rate_high)
            else:
                steps = 0
                current_savings = 0.0
                annual_salary = init_annual_salary
                monthly_salary = compute_monthly(annual_salary)
                rate_low = rate_optimal
                rate_optimal = find_rate(rate_low, rate_high)
           
problem() 
        # #========================
        # # CONDITIONS FOR TESTING MULTIPLE CASES
        # #========================
legal_answers = ["y", "Y", "yes", "Yes", "YES"]
while True:
    try:
        print(legal_answers.index(input("Do you want to calculate other values?(y\\n)\n>>>"))+1)
    except ValueError:
        print("Goodbye!")
        break
    else:
        problem()