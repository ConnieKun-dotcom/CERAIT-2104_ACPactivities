import re
import os

class Employee:
    def __init__(self, emp_id, name, job_title, email, phone, department, manager, hire_date, birth_date):
        self.emp_id = emp_id
        self.name = name
        self.job_title = job_title
        self.email = email
        self.phone = phone
        self.department = department
        self.manager = manager
        self.hire_date = hire_date
        self.birth_date = birth_date

    def __str__(self):
        return (f"ID: {self.emp_id}, Name: {self.name}, Job Title: {self.job_title}, Email: {self.email}, "
                f"Phone: {self.phone}, Department: {self.department}, Manager: {self.manager}, "
                f"Hire Date: {self.hire_date}, Birth Date: {self.birth_date}")
class Colors:
    RESET = "\033[0m"  # Reset to default color
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m" 

def print_centered(text, color = Colors.RESET):
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80
    print((color + text + Colors.RESET).center(width))

def print_prompt(prompt):
    """Print the prompt centered with space for user input."""
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80  # Fallback width

    prompt_with_space = prompt + " "  # Add space after the prompt for input
    prompt_length = len(prompt_with_space)  # Length of the prompt with space

    # Calculate the space needed to center the prompt
    total_padding = (width - prompt_length) // 2
    padding = " " * total_padding

    # Print the prompt with padding
    print(padding + prompt_with_space, end='')  # Use end='' to stay on the same line



class PayrollSystem:
    def __init__(self):
        self.employees = {}
        self.payslips = {}
        self.unique_id_counter = 1 #To keep track of unique employee IDs

        #Predefined employees and their payslip details
        self.setup_predefined_employees()
    #Menu method implementation
    def menu(self):
        while True:
            print_centered("~" * 130)  # Separator line
            print_centered("Welcome to PaySphere Pro", Colors.GREEN)
            print_centered("~" * 130)  # Separator line
            print_centered("\"Simplifying Payroll, Empowering People\"", Colors.YELLOW)
            print_centered("1. Manage Employees")
            print_centered("2. Manage Payslip")
            print_centered("3. Manage Payroll")

            # Call the print_prompt function to display the prompt
            print_prompt("Choose an option:" )
            choice = input()  # Get user input
            
            """self.manage_employees - call the method to manage employees
               self.manage_payslip - call the method to manage payslip
               self.manage_payroll - call the method to manage payroll
            """
            if choice == '1':
                self.manage_employees()
            elif choice == '2':
                self.manage_payslip()
            elif choice == '3':
                self.manage_payroll()
            else:
                print("Invalid choice. Please try again.", Colors.RED)
    
    def manage_employees(self):
        while True:
            print_centered("~" * 130)  # Separator line
            print_centered("Manage Employees", Colors.GREEN)
            print_centered("~" * 130)  # Separator line
            print_centered("1. Register Employee")
            print_centered("2. View Employees")
            print_centered("3. Update Employee")
            print_centered("4. Delete Employee")
            print_centered("5. Exit to Main Menu")

            print_prompt("Choose an option:")
            choice = input()  # Get user input

            if choice == '1':
                self.register_employee()
            elif choice == '2':
                self.view_employees()
            elif choice == '3':
                self.update_employee()
            elif choice == '4':
                self.delete_employee()
            elif choice == '5':
                break  # Exit to the main menu
            else:
                print("Invalid choice. Please try again.", Colors.RED)
            
    def manage_payslip(self):
        while True:
            print_centered("~" * 130)  
            print_centered("Manage Payslip", Colors.GREEN)
            print_centered("~" * 130)  
            print_centered("1. Create Payslip")
            print_centered("2. View Payslip")
            print_centered("3. Exit to Main Menu")

            print_prompt("Choose an option:")
            choice = input()  

            if choice == '1':
                self.create_payslip()  # Placeholder for creating a payslip
            elif choice == '2':
                self.view_payslip()  # Placeholder for viewing payslip
            elif choice == '3':
                break  # Exit to the main menu
            else:
                print("Invalid choice. Please try again.", Colors.RED)

    def manage_payroll(self):
        while True:
            print_centered("~" * 130)  
            print_centered("Manage Payroll")
            print_centered("~" * 130)  
            print_centered("1. View Payroll")
            print_centered("2. Exit to Main Menu")

            print_prompt("Choose an option:")
            choice = input()  # Get user input

            if choice == '1':
                self.view_payroll()  # Placeholder for creating payroll
            elif choice == '2':
                break  # Exit to the main menu
            else:
                print_centered("Invalid choice. Please try again.", Colors.RED)    

    #Validation methods
    def validate_department_code(self, code):
        return code in ["HR", "IT", "FIN", "MKT", "ENG"]
    
    def validate_employee_type_code(self, code):
        return code in ["F", "P", "C", "I"]
    
    def validate_unique_identifier(self, identifier):
        return identifier.isdigit() and len(identifier) == 4 and 1 <= int(identifier) <= 9999
    
    def validate_name(self, name):
        return bool(re.match("^[A-Za-z ]+$", name))

    def validate_job_title(self, job_title):
        return bool(re.match("^[A-Za-z ]+$", job_title))

    def validate_email(self, email):
        return bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email))

    def validate_phone(self, phone):
        return phone.isdigit() and len(phone) == 10

    def validate_department(self, department):
        return bool(re.match("^[A-Za-z ]+$", department))

    def validate_manager(self, manager):
        return bool(re.match("^[A-Za-z ]+$", manager))

    def validate_date(self, date):
        return bool(re.match(r"^\d{4}-\d{2}-\d{2}$", date))

    #Employee management methods
    """
    Format for ID number: [Department Code(3 letters)-HR:Human Resources, IT:Infomation Technology, FIN: Finance, MKT: Marketing, ENG: Engineering]
                      [Employee Type Code(1 letter)-F:Full-time, P:Part-time, C:Contract, I:Intern]
                      [Unique Identifier (4 digits)-This start from 0001 and increment for each new employee]
    """
    def register_employee(self):
        while True:
            print_centered("." * 130)
            department_code = input("\t\t\t\tEnter Department Code (3 letters): ")
            if self.validate_department_code(department_code):
                break
            print("\t\t\t\tInvalid department code. Please enter HR, IT, FIN, MKT, or ENG.", Colors.RED)

        while True:
            employee_type_code = input("\t\t\t\tEnter Employee Type Code (1 letter): ")
            if self.validate_employee_type_code(employee_type_code):
                break
            print("\t\t\t\tInvalid employee type code. Please enter F, P, C, or I.", Colors.RED)

        while True:
            unique_identifier = input("\t\t\t\tEnter Unique Identifier (4 digits): ")
            if self.validate_unique_identifier(unique_identifier):
                # Ensure the unique identifier is not already used
                if f"{int(unique_identifier):04d}" in [emp_id.split('-')[-1] for emp_id in self.employees.keys()]:
                    print("\t\t\t\tUnique Identifier already in use. Please enter a different one.", Colors.RED)
                else:
                    break
            print("\t\t\t\tInvalid unique identifier. It must be a 4-digit number.", Colors.RED)

        emp_id = f"{department_code}-{employee_type_code}-{unique_identifier.zfill(4)}"
        print_centered(f"Employee ID registered: {emp_id}", Colors.YELLOW)

        while True:
            name = input("\t\t\t\tEnter Employee Name: ")
            if self.validate_name(name):
                break
            print("\t\t\t\tInvalid name. Please use letters and spaces only.", Colors.RED)

        while True:
            job_title = input("\t\t\t\tEnter Job Title: ")
            if self.validate_job_title(job_title):
                break
            print("\t\t\t\tInvalid job title. Please use letters and spaces only.", Colors.RED)

        while True:
            email = input("\t\t\t\tEnter Email Address: ")
            if self.validate_email(email):
                break
            print("\t\t\t\tInvalid email format. Please try again.", Colors.RED)

        while True:
            phone = input("\t\t\t\tEnter Phone Number: +63- ")
            if self.validate_phone(phone):
                break
            print("\t\t\t\tInvalid phone number. Please use numbers only.", Colors.RED)

        while True:
            department = input("\t\t\t\tEnter Department: ")
            if self.validate_department(department):
                break
            print("\t\t\t\tInvalid department. Please use letters and spaces only.", Colors.RED)

        while True:
            manager = input("\t\t\t\tEnter Manager Name: ")
            if self.validate_manager(manager):
                break
            print("\t\t\t\tInvalid manager name. Please use letters and spaces only.", Colors.RED)

        while True:
            hire_date = input("\t\t\t\tEnter Hire Date (yyyy-mm-dd): ")
            if self.validate_date(hire_date):
                break
            print("\t\t\t\tInvalid hire date format. Please use yyyy-mm-dd format.", Colors.RED)

        while True:
            birth_date = input("\t\t\t\tEnter Birth Date (yyyy-mm-dd): ")
            if self.validate_date(birth_date):
                break
            print("\t\t\t\tInvalid birth date format. Please use yyyy-mm-dd format.", Colors.RED)

        new_employee = Employee(emp_id, name, job_title, email, phone, department, manager, hire_date, birth_date)
        self.employees[emp_id] = new_employee
        print_centered("Employee registered successfully.", Colors.YELLOW)
        print()
        
    def view_employees(self):
        print("-" * 199)
        if not self.employees:
            print("\t\t\t\tNo employees registered.", Colors.RED)
            return
        for emp in self.employees.values():
            print(emp)
            print("-" * 199)
        

    def update_employee(self):
        print_centered("." * 199)
        print()
        emp_id = input("\t\t\t\tEnter Employee ID to update: ")
        if emp_id in self.employees:
            emp = self.employees[emp_id]
            print(f"Current details: {emp}")
            print_centered("." * 199)

            while True:
                name = input("\t\t\t\tEnter new Employee Name (leave blank to keep current): ")
                if not name or self.validate_name(name):
                    emp.name = name if name else emp.name
                    break
                print("\t\t\t\tInvalid name. Please use letters and spaces only.", Colors.RED)

            while True:
                job_title = input("\t\t\t\tEnter new Job Title (leave blank to keep current): ")
                if not job_title or self.validate_job_title(job_title):
                    emp.job_title = job_title if job_title else emp.job_title
                    break
                print("\t\t\t\tInvalid job title. Please use letters and spaces only.", Colors.RED)

            while True:
                email = input("\t\t\t\tEnter new Email Address (leave blank to keep current): ")
                if not email or self.validate_email(email):
                    emp.email = email if email else emp.email
                    break
                print("\t\t\t\tInvalid email format. Please try again.", Colors.RED)

            while True:
                phone = input("\t\t\t\tEnter new Phone Number (leave blank to keep current): ")
                if not phone or self.validate_phone(phone):
                    emp.phone = phone if phone else emp.phone
                    break
                print("\t\t\t\tInvalid phone number. Please use numbers only.", Colors.RED)

            while True:
                department = input("\t\t\t\tEnter new Department (leave blank to keep current): ")
                if not department or self.validate_department(department):
                    emp.department = department if department else emp.department
                    break
                print("\t\t\t\tInvalid department. Please use letters and spaces only.", Colors.RED)

            while True:
                manager = input("\t\t\t\tEnter new Manager Name (leave blank to keep current): ")
                if not manager or self.validate_manager(manager):
                    emp.manager = manager if manager else emp.manager
                    break
                print("\t\t\t\tInvalid manager name. Please use letters and spaces only.", Colors.RED)

            while True:
                hire_date = input("\t\t\t\tEnter new Hire Date (yyyy-mm-dd, leave blank to keep current): ")
                if not hire_date or self.validate_date(hire_date):
                    emp.hire_date = hire_date if hire_date else emp.hire_date
                    break
                print("\t\t\t\tInvalid hire date format. Please use yyyy-mm-dd format.", Colors.RED)

            while True:
                birth_date = input("\t\t\t\tEnter new Birth Date (yyyy-mm-dd, leave blank to keep current): ")
                if not birth_date or self.validate_date(birth_date):
                    emp.birth_date = birth_date if birth_date else emp.birth_date
                    break
                print("\t\t\t\tInvalid birth date format. Please use yyyy-mm-dd format.", Colors.RED)

            print_centered("Employee updated successfully.", Colors.YELLOW)
            print_centered("." * 130)
            print()
        else:
            print("\t\t\t\tEmployee not found.", Colors.RED)
         

    def delete_employee(self):
        print_centered("." * 130)
        emp_id = input("\t\t\t\tEnter Employee ID to delete: ")
        if emp_id in self.employees:
            del self.employees[emp_id]
            print_centered("Employee deleted successfully.", Colors.YELLOW)
            print_centered("." * 130)
        else:
            print("\t\t\t\tEmployee not found.", Colors.RED)
      

    def create_payslip(self):
        # Step 1: Get Employee ID
        print()
        emp_id = input("\t\t\t\tEnter Employee ID to create payslip: ")
    
        if emp_id not in self.employees:
           print("\t\t\t\tEmployee not found.", Colors.RED)
           return
    
        # Step 2: Retrieve employee details
        emp = self.employees[emp_id]
    
        # Step 3: Display employee details
        print_centered("=" * 65)
        print_centered("Payslip", Colors.BLUE)
        print_centered("=" * 65)
        print_centered(f"Employee ID: {emp.emp_id}")
        print_centered(f"Name: {emp.name}")
        print_centered(f"Job Title: {emp.job_title}")
        print_centered(f"Phone Number: +63-{emp.phone}")
        print_centered(f"Department: {emp.department}")
        print_centered("-" * 130)
        
        print("\t\t\t\tGathering payslip details")
        total_hours_worked = self.get_numeric_input("\t\t\t\tEnter Total Hours Worked: ")
        over_hours = self.get_numeric_input("\t\t\t\tEnter Over Hours: ")
        salary_in_advance = self.get_numeric_input("\t\t\t\tEnter Salary in Advance: ")
        incentives = self.get_numeric_input("\t\t\t\tEnter Incentives: ")
        bonus = self.get_numeric_input("\t\t\t\tEnter Bonus: ")

        # Step 5: Define hourly rates based on department
        hourly_rates = {
            "HR": 67.13,
            "IT": 117.00,
            "FIN": 168.00,
            "MKT": 111.00,
            "ENG": 144.00
        }

        # Get the hourly rate for the employee's department
        base_salary_per_hour = hourly_rates.get(emp.department, 0.00)
    
        # Step 6: Calculate total salary
        # Calculate the overtime pay
        overtime_pay = over_hours * (base_salary_per_hour * 1.25)

        # Calculate monthly salary
        monthly_salary = (total_hours_worked * base_salary_per_hour ) + overtime_pay

        # Calculate mandatory benefits
        sss_employee_contribution = monthly_salary * 0.045  # Employee's SSS contribution
        philhealth_employee_contribution = monthly_salary * 0.0225  # Employee's PhilHealth contribution
        pagibig_employee_contribution = monthly_salary * 0.02  # Employee's Pag-ibig contribution

        # Total salary calculation
        total_earnings = (total_hours_worked * base_salary_per_hour) + overtime_pay + incentives + bonus
        total_deductions = (
            salary_in_advance +
            sss_employee_contribution +
            philhealth_employee_contribution +
            pagibig_employee_contribution
        )
        net_pay = total_earnings - total_deductions

        #Storing payslip details in the payslip dictionary
        self.payslips[emp_id] = {
            "total_hours_worked": total_hours_worked,
            "over_hours": over_hours,
            "basic_salary": (total_hours_worked * base_salary_per_hour),
            "incentives": incentives,
            "bonus": bonus,
            "overtime_pay": overtime_pay,
            "total_earnings": total_earnings,
            "salary_in_advance": salary_in_advance,
            "sss_employee_contribution": sss_employee_contribution,
            "philhealth_employee_contribution": philhealth_employee_contribution,
            "pagibig_employee_contribution": pagibig_employee_contribution,
            "total_deductions": total_deductions,
            "net_pay": net_pay,
        }

        # Step 7: Display the payslip
        print_centered("=" * 65)
        print_centered("Payslip", Colors.BLUE)
        print_centered("=" * 65)

        # Earnings Section
        print_centered("Earnings:", Colors.GREEN)
        print_centered(f"  Basic Salary:               ₱{(total_hours_worked * base_salary_per_hour):.2f}")
        print_centered(f"  Incentives:                 ₱{incentives:.2f}")
        print_centered(f"  Bonus:                      ₱{bonus:.2f}")
        print_centered(f"  Overtime Pay:               ₱{overtime_pay:.2f}")
        print_centered(f"  TOTAL EARNINGS:             ₱{total_earnings:.2f}")
    
        # Deductions Section
        print_centered("Deductions:", Colors.GREEN)
        print_centered(f"  Salary in Advance:          ₱{salary_in_advance:.2f}")
        print_centered(f"  SSS Contribution:           ₱{sss_employee_contribution:.2f}")
        print_centered(f"  PhilHealth Contribution:    ₱{philhealth_employee_contribution:.2f}")
        print_centered(f"  Pag-ibig Contribution:      ₱{pagibig_employee_contribution:.2f}")
        print_centered(f"  TOTAL DEDUCTIONS:           ₱{total_deductions:.2f}")

        # Final Net Pay
        print_centered(f"Net Pay:                      ₱{net_pay:.2f}")

    def get_numeric_input(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a numeric value.", Colors.RED)
    
    def setup_predefined_employees(self):
        # Adding some predefined employees
        self.employees = {
            "HR-F-0001": Employee("HR-F-0001", "Dwayne Johnson", " Chief HR Manager", "dwayne.johnson@example.com", "09123456789", "Human Resources", "Bob Smith", "2015-01-15", "1990-05-20"),
            "HR-F-0002": Employee("HR-F-0002", "Evelyn Carter", "HR Manager", "evelyn.carter@example.com", "09123456789", "Human Resources", "Bob Smith", "2020-01-15", "1999-09-20"),
            "IT-F-0003": Employee("IT-F-0003", "Kit Mayson", "Programmer", "kit.mayson@example.com", "09123456788", "Info. Technology", "Jane Doe", "2021-03-10", "1992-07-30"),
            "IT-P-0004": Employee("IT-P-0004", "Liam Thompson", "Data Analyst", "liam.thompson@example.com", "09123456788", "Info. Technology", "Jane Doe", "2022-05-10", "1996-07-30"),
            "FIN-C-0005": Employee("FIN-C-0005", "Mary Merrier", "Financial Analyst", "mary.merrier@example.com", "09123456787", "Finance", "Robert Brown", "2013-06-20", "1988-4-11"),
            "FIN-F-0006": Employee("FIN-F-0006", "Sofia Martinez", "Assistant Financial Analyst", "sofia.martinez@example.com", "09123456787", "Finance", "Robert Brown", "2019-06-20", "1994-11-15"),
            "MKT-F-0007": Employee("MKT-F-0007", "James Delaware", "Executive Marketing Manager", "james.delaware@example.com", "09123456786", "Marketing", "Emily Davis", "2014-09-21", "1991-01-10"),
            "MKT-I-0008": Employee("MKT-I-0008", "Noah Patel", "Intern", "noah.patel@example.com", "09123456786", "Marketing", "Emily Davis", "2022-09-01", "1999-01-10"),
            "ENG-F-0009": Employee("ENG-F-0009", "Ethan Garcia", "Software Engineer", "ethan.garcia@example.com", "09123456786", "Engineering", "Aiden Kim", "2018-09-01", "1984-01-10"),
            "ENG-C-0010": Employee("ENG-C-0010", "Lucas Nguyen", "Computer Engineer", "lucas.nguyen@example.com", "09123456786", "Engineering", "Aiden Kim", "2020-2-01", "1992-03-25"),

        }

        # Predefined payslip details for each employee
        self.payslips = {
            "HR-F-0001": {
                "total_hours_worked": 254,
                "over_hours": 10,
                "basic_salary": 17051.02,
                "incentives": 1500,
                "bonus": 5000,
                "overtime_pay": 839.12,
                "total_earnings": 24390.14, 
                "salary_in_advance": 2000,
                "sss_employee_contribution": 767.30,
                "philhealth_employee_contribution": 383.65,
                "pagibig_employee_contribution": 341.02,  
                "total_deductions": 3565.39,  
                "net_pay": 20824.76,  
            },
            "HR-F-0002": {
                "total_hours_worked": 250,
                "over_hours": 10,
                "basic_salary": 16782.5,
                "incentives": 1500,
                "bonus": 2000,
                "overtime_pay": 839.12,
                "total_earnings": 21121.62, 
                "salary_in_advance": 1000,
                "sss_employee_contribution": 755.21,
                "philhealth_employee_contribution": 377.60,
                "pagibig_employee_contribution": 335.65,  
                "total_deductions": 2468.46,  
                "net_pay": 18652.54,  
            },
            "IT-F-0003": {
                "total_hours_worked": 250,
                "over_hours": 8,
                "basic_salary": 29250,
                "incentives": 1500,
                "bonus": 2000,
                "overtime_pay": 1170,
                "total_earnings": 33920, 
                "salary_in_advance": 0,
                "sss_employee_contribution": 1316.25,
                "philhealth_employee_contribution": 658.13 ,
                "pagibig_employee_contribution": 585,  
                "total_deductions": 2559.38,  
                "net_pay": 31360.62,  
            },
            "IT-P-0004": {
                "total_hours_worked": 200,
                "over_hours": 10,
                "basic_salary": 23400,
                "incentives": 1500,
                "bonus": 1000,
                "overtime_pay": 1462.5,
                "total_earnings": 27362.5, 
                "salary_in_advance": 1000,
                "sss_employee_contribution": 1053,
                "philhealth_employee_contribution": 526.5,
                "pagibig_employee_contribution": 468,  
                "total_deductions": 3047.5,  
                "net_pay": 24315,  
            },
            "FIN-C-0005": {
                "total_hours_worked": 254,
                "over_hours": 10,
                "basic_salary": 42672,
                "incentives": 1500,
                "bonus": 1000,
                "overtime_pay": 2100,
                "total_earnings": 47272, 
                "salary_in_advance": 0,
                "sss_employee_contribution": 1920.24,
                "philhealth_employee_contribution": 960.12,
                "pagibig_employee_contribution": 853.44,  
                "total_deductions": 3733.8,  
                "net_pay": 43538.2,  
            },
            "FIN-F-0006": {
                "total_hours_worked": 250,
                "over_hours": 10,
                "basic_salary": 42000,
                "incentives": 1500,
                "bonus": 3000,
                "overtime_pay": 2100,
                "total_earnings": 48600, 
                "salary_in_advance": 0,
                "sss_employee_contribution": 1890,
                "philhealth_employee_contribution": 945,
                "pagibig_employee_contribution": 840,  
                "total_deductions": 3675,  
                "net_pay": 44925,  
            },
            "MKT-F-0007": {
                "total_hours_worked": 254,
                "over_hours": 5,
                "basic_salary": 28194,
                "incentives": 1500,
                "bonus": 3000,
                "overtime_pay": 693.75,
                "total_earnings": 33387.75, 
                "salary_in_advance": 1000,
                "sss_employee_contribution": 1268.73,
                "philhealth_employee_contribution": 634.36,
                "pagibig_employee_contribution": 563.88,  
                "total_deductions": 3466.97,  
                "net_pay": 29920.78, 
            },
            "MKT-I-0008": {
                "total_hours_worked": 200,
                "over_hours": 10,
                "basic_salary": 22200,
                "incentives": 1500,
                "bonus": 1000,
                "overtime_pay": 1387.5,
                "total_earnings": 26087.5, 
                "salary_in_advance": 1000,
                "sss_employee_contribution": 999,
                "philhealth_employee_contribution": 499.5,
                "pagibig_employee_contribution": 444,  
                "total_deductions": 2942.5,  
                "net_pay": 23145, 
            },
            "ENG-F-0009": {
                "total_hours_worked": 254,
                "over_hours": 10,
                "basic_salary": 36576,
                "incentives": 1500,
                "bonus": 2000,
                "overtime_pay": 1800,
                "total_earnings": 41876, 
                "salary_in_advance": 1000,
                "sss_employee_contribution": 1645.92,
                "philhealth_employee_contribution": 822.96,
                "pagibig_employee_contribution": 731.52,  
                "total_deductions": 4200.4,  
                "net_pay": 37675.6, 
            },
            "ENG-C-0010": {
                "total_hours_worked": 250,
                "over_hours": 5,
                "basic_salary": 36000,
                "incentives": 1500,
                "bonus": 2000,
                "overtime_pay": 900,
                "total_earnings": 40400, 
                "salary_in_advance": 1000,
                "sss_employee_contribution": 1620,
                "philhealth_employee_contribution": 810,
                "pagibig_employee_contribution": 720,  
                "total_deductions": 4150,  
                "net_pay": 36250, 
            }
        }

    def view_payslip(self):
        emp_id = input("\t\t\t\tEnter Employee ID to view payslip: ")
        if emp_id in self.payslips:
            payslip = self.payslips[emp_id]
            emp = self.employees[emp_id]
            
            print_centered("=" * 65)
            print_centered("Payslip", Colors.BLUE)
            print_centered("=" * 65)
            print_centered(f"Employee ID: {emp.emp_id}")
            print_centered(f"Name: {emp.name}")
            print_centered(f"Job Title: {emp.job_title}")
            print_centered(f"Phone Number: {emp.phone}")
            print_centered(f"Department: {emp.department}")
            print_centered("-" * 65)

            # Display the stored payslip details
            print_centered("Earnings:", Colors.GREEN)
            print_centered(f"  Total Hours Worked:         {payslip['total_hours_worked']}")
            print_centered(f"  Overtime Hours:             {payslip['over_hours']}")
            print_centered(f"  Basic Salary:               ₱{payslip['basic_salary']:.2f}")
            print_centered(f"  Incentives:                 ₱{payslip['incentives']:.2f}")
            print_centered(f"  Bonus:                      ₱{payslip['bonus']:.2f}")
            print_centered(f"  Overtime Pay:               ₱{payslip['overtime_pay']:.2f}")
            print_centered(f"  TOTAL EARNINGS:             ₱{payslip['total_earnings']:.2f}")

            print_centered("\nDeductions:", Colors.GREEN)
            print_centered(f"  Salary in Advance:          ₱{payslip['salary_in_advance']:.2f}")
            print_centered(f"  SSS Contribution:           ₱{payslip['sss_employee_contribution']:.2f}")
            print_centered(f"  PhilHealth Contribution:    ₱{payslip['philhealth_employee_contribution']:.2f}")
            print_centered(f"  Pag-ibig Contribution:      ₱{payslip['pagibig_employee_contribution']:.2f}")
            print_centered(f"  TOTAL DEDUCTIONS:           ₱{payslip['total_deductions']:.2f}")

            # Final Net Pay
            print_centered(f"\nNet Pay:                   ₱{payslip['net_pay']:.2f}")
        else:
            print_centered("Payslip not found for this Employee ID.", Colors.RED) 

    def view_payroll(self):
        if not self.payslips:
            print_centered("No payslips available.", Colors.RED)
            return

        print("=" * 199)
        print_centered("Payroll Report", Colors.BLUE)
        print("=" * 199)
        payroll_date = input("Enter Payroll Date (YYYY-MM-DD): ")
        print(payroll_date)
        print("-" * 199)

        # Initialize totals
        total_basic_salary = 0
        total_incentives = 0
        total_bonus = 0
        total_overtime_pay = 0
        total_earnings = 0
        total_sss = 0
        total_philhealth = 0
        total_pagibig = 0
        total_salary_in_advance = 0
        total_deductions = 0
        total_net_pay = 0
        total_hours_worked = 0
        total_overtime_hours = 0

        # Print header for the report
        print_centered(f"{'Name':<20} {'Department':<20} {'Total Hours Worked':<20} {'Overtime Hours':<15} {'Total Earnings':<20} {'Total Deductions':<20} {'Net Pay':<25}", Colors.YELLOW)
        print()

        # Iterate through predefined payslips
        for emp_id, payslip in self.payslips.items():
            emp = self.employees[emp_id]
        
            #Print employee details
            print_centered(f"{emp.name:<20} {emp.department:<20} {payslip['total_hours_worked']:<20} {payslip['over_hours']:<15} ₱{payslip['total_earnings']:<20.2f} ₱{payslip['total_deductions']:<20.2f} ₱{payslip['net_pay']:<15.2f}")

            
            # Accumulate totals
            total_basic_salary += payslip['basic_salary']
            total_incentives += payslip['incentives']
            total_bonus += payslip['bonus']
            total_overtime_pay += payslip['overtime_pay']
            total_earnings += payslip['total_earnings']
            total_salary_in_advance += payslip['salary_in_advance']
            total_sss += payslip['sss_employee_contribution']
            total_philhealth += payslip['philhealth_employee_contribution']
            total_pagibig += payslip['pagibig_employee_contribution']
            total_deductions += payslip['total_deductions']
            total_net_pay += payslip['net_pay']
            total_hours_worked += payslip['total_hours_worked']
            total_overtime_hours += payslip['over_hours']


        # Print totals
        print("=" * 199)
        print_centered(f"{'Total':<20} {'':<20} {total_hours_worked:<20} {total_overtime_hours:<15} ₱{total_earnings:<20.2f} ₱{total_deductions:<20.2f} ₱{total_net_pay:<15.2f}", Colors.YELLOW)
        print("=" * 199)

if __name__ == "__main__":
       # This will call __init__ automatically
        system = PayrollSystem()  
        system.menu()  