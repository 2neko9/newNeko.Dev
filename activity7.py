manager_hourly = 200
junior_manager_hourly = 180
employee_hourly = 150


print("\n\nThis program will display the rate's per hour and computes the salary.")
print("User will input the following: number of days worked: overtime worked: deduction fee ")
print("\nManager's hourly wage: 200 :: Junior Manager Hourly wage: 180 :: Employee Hourly wage: 150")

print("\n:Manager:")
manager_days = int(input("Enter the employee's number of days worked: "))
manager_overtime = int(input("Enter the employee's overtime worked: "))
manager_deduction = int(input("Enter the employee's deduction fee: "))

compensation_rate_manager = manager_hourly * (manager_days *(8 + manager_overtime))  - manager_deduction

print("\n:Junior Manager:")
junior_manager_days = int(input("Enter the employee's number of days worked: "))
junior_manager_days_overtime = int(input("Enter the employee's overtime worked: "))
junior_manager_days_deduction = int(input("Enter the employee's deduction fee: "))

compensation_rate_junior_manager = junior_manager_hourly * (junior_manager_days *(8 + junior_manager_days_overtime)) - manager_deduction

print("\n:Employee:")
employee_days = int(input("Enter the employee's number of days worked: "))
employee_overtime = int(input("Enter the employee's overtime worked: "))
employee_deduction = int(input("Enter the employee's deduction fee: "))

compensation_rate_employee = employee_hourly * (employee_days *(8 + employee_overtime)) - manager_deduction


print("\nThe Manager's Compensation Rate is: "+ str(compensation_rate_manager))
print("The Junior Manager's Compensation Rate is: "+ str(compensation_rate_junior_manager))
print("The Employee's Compensation Rate is: "+ str(compensation_rate_employee) + "\n\n")