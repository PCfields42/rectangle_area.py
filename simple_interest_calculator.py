# Ask the user for the principal amount, interest rate, and time period
principal = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate (in %): "))
time_period = float(input("Enter the time period (in years): "))

# Calculate the simple interest
simple_interest = (principal * interest_rate * time_period) / 100

# Calculate the total amount to be repaid
total_amount = principal + simple_interest

# Print the results
print(f"Simple Interest: {simple_interest}")
print(f"Total Amount to be Repaid: {total_amount}")

