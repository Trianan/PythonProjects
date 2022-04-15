# BUDGETING SOFTWARE Version 0.1 (Crash Course Alpha)
# This section adds a deposit value, and records the amount before dividing it 
# into separate budgets.
deposit_raw = input("Deposit: $")
deposit_history = []
deposit_history.append(deposit_raw)
# Displays deposit_history list, while continuing to work with value.
print(deposit_history)

# This section divides the raw value into separate budgets, defines a 
# history-list, and displays each budget.
computable_value = float(deposit_raw)
budget_history = []

needs = computable_value * 0.50
print(f"\n  You have: ${needs.__round__(6)} available for housing, food, utilities, health-care, and insurance,")
wants = computable_value * 0.30
print(f"${wants.__round__(6)} for personal-care, entertainment, and hobbies,")
savings = computable_value * 0.20
print(f"and ${savings.__round__(6)} for emergencies, savings, and investing.\n")

# This creates a string of the current date and time, for use as a timestamp on deposit history.
import datetime
current_date_time = datetime.datetime.now()

budget_history.append(f'Deposit:{deposit_raw}, Needs:{needs}, Wants:{wants}, Savings:{savings}. / {current_date_time}')
print(budget_history)
# The history lists are strictly for if I wish to add a data-saving feature to the program later on.
# END.
