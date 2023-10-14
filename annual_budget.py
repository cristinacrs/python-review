budget = []

for i in range(1,13):
    monthly_budget = int(input(f"Whats your budget for {i} month? "))
    budget.append(monthly_budget)

def Average(lst): 
    return sum(lst) / len(lst) 

budget = Average(budget)

print(f"Average = {budget}")