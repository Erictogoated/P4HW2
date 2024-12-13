# Eric Corbett
# 11/08/2024
# P4HW2
# A program that calculates pay for multiple employees including overtime and totals


def main():
    # Initialize totals
    total_overtime_pay = 0
    total_regular_pay = 0
    total_gross_pay = 0
    num_employees = 0
    
    while True:
        # Get employee name
        print("\nEnter employee's name or \"Done\" to terminate: ", end="")
        name = input()
        
        # Check for program termination
        if name.lower() == "done":
            break
            
        # Get hours and pay rate
        hours = float(input("\nHow many hours did " + name + " work? "))
        pay_rate = float(input("What is " + name + "'s pay rate? "))
        
        # Calculate overtime hours and regular hours
        if hours > 40:
            overtime_hours = hours - 40
            regular_hours = 40
        else:
            overtime_hours = 0
            regular_hours = hours
            
        # Calculate pay
        regular_pay = regular_hours * pay_rate
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        gross_pay = regular_pay + overtime_pay
        
        # Add to totals
        total_regular_pay += regular_pay
        total_overtime_pay += overtime_pay
        total_gross_pay += gross_pay
        num_employees += 1
        
        # Display employee results
        print('\n-------------------------------------------------')
        print('Employee name:', name)
        print('\nHours Worked   Pay Rate   OverTime   OverTime Pay     RegHour Pay     Gross Pay')
        print('-------------------------------------------------')
        print(f'{hours:<14.1f}${pay_rate:<10.2f}{overtime_hours:<11.1f}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:<10.2f}')
        print('-------------------------------------------------')
        
    # Display final totals if any employees were processed
    if num_employees > 0:
        print('\n**************************************************************************')
        print(f'Total number of employees entered: {num_employees}')
        print(f'Total amount paid for overtime: ${total_overtime_pay:.2f}')
        print(f'Total amount paid for regular hours: ${total_regular_pay:.2f}')
        print(f'Total amount paid in gross: ${total_gross_pay:.2f}')
        print('**************************************************************************')

if __name__ == "__main__":
    main()
