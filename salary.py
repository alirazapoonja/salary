from datetime import date

def generate_payslip(employee_name, emp_id, basic_salary, allowances, deductions):
    # Calculate net salary
    gross_salary = basic_salary + allowances
    net_salary = gross_salary - deductions

    # Generate payslip
    payslip = f"""
    ---------------------------------------
                SALARY PAYSLIP
    ---------------------------------------
    Date: {date.today().strftime("%d-%m-%Y")}
    
    Employee Name : {employee_name}
    Employee ID   : {emp_id}
    
    Basic Salary  : ${basic_salary:,.2f}
    Allowances    : ${allowances:,.2f}
    Deductions    : ${deductions:,.2f}
    
    Gross Salary  : ${gross_salary:,.2f}
    Net Salary    : ${net_salary:,.2f}
    ---------------------------------------
    """

    return payslip

# Example usage
employee_name = "John Doe"
emp_id = "E12345"
basic_salary = 3500.00
allowances = 500.00
deductions = 300.00

print(generate_payslip(employee_name, emp_id, basic_salary, allowances, deductions))
