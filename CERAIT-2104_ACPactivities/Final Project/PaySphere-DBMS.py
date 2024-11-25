import re
import os
import sqlite3
from datetime import datetime
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, name, job_title, email, phone, department, manager, hire_date, birth_date):
        self.__emp_id = emp_id
        self.__name = name
        self.__job_title = job_title
        self.__email = email
        self.__phone = phone
        self.__department = department
        self.__manager = manager
        self.__hire_date = hire_date
        self.__birth_date = birth_date
    
    # Getter methods
    def get_emp_id(self): return self.__emp_id
    def get_name(self): return self.__name
    def get_job_title(self): return self.__job_title
    def get_email(self): return self.__email
    def get_phone(self): return self.__phone
    def get_department(self): return self.__department
    def get_manager(self): return self.__manager
    def get_hire_date(self): return self.__hire_date
    def get_birth_date(self): return self.__birth_date

    @abstractmethod
    def calculate_salary(self, total_hours_worked, over_hours):
        pass

    def __str__(self):
        return (f"ID: {self.__emp_id}, Name: {self.__name}, Job Title: {self.__job_title}, "
                f"Email: {self.__email}, Phone: {self.__phone}, Department: {self.__department}, "
                f"Manager: {self.__manager}, Hire Date: {self.__hire_date}, "
                f"Birth Date: {self.__birth_date}")
    def get_department_code(self):
        department_mapping = {
            "HUMAN RESOURCES": "HR",
            "INFORMATION TECHNOLOGY": "IT",
            "FINANCE": "FIN",
            "MARKETING": "MKT",
            "ENGINEERING": "ENG"
        }
        return department_mapping.get(self.get_department().upper())
        
class FullTimeEmployee(Employee):
    def calculate_salary(self, total_hours_worked, over_hours):
        hourly_rates = {
            "HR": 67.13, "IT": 117.00, "FIN": 168.00,
            "MKT": 111.00, "ENG": 144.00
        }
        base_rate = hourly_rates.get(self.get_department(), 100.00)
        regular_pay = total_hours_worked * base_rate
        overtime_pay = over_hours * (base_rate * 1.5)
        return regular_pay + overtime_pay

class PartTimeEmployee(Employee):
    def calculate_salary(self, total_hours_worked, over_hours):
        hourly_rates = {
            "HR": 33.57, "IT": 58.50, "FIN": 84.00,
            "MKT": 55.50, "ENG": 72.00
        }
        base_rate = hourly_rates.get(self.get_department(), 50.00)
        regular_pay = total_hours_worked * base_rate
        overtime_pay = over_hours * (base_rate * 1.25)
        return regular_pay + overtime_pay

class ContractEmployee(Employee):
    def calculate_salary(self, total_hours_worked, over_hours):
        hourly_rates = {
            "HR": 50.35, "IT": 87.75, "FIN": 126.00,
            "MKT": 83.25, "ENG": 108.00
        }
        base_rate = hourly_rates.get(self.get_department(), 75.00)
        return (total_hours_worked + over_hours) * base_rate

class InternEmployee(Employee):
    def calculate_salary(self, total_hours_worked, over_hours):
        hourly_rates = {
            "HR": 25.17, "IT": 43.88, "FIN": 63.00,
            "MKT": 41.63, "ENG": 54.00
        }
        base_rate = hourly_rates.get(self.get_department(), 37.50)
        return total_hours_worked * base_rate
    
class Colors:
    RESET = "\033[0m"  
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
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80  # This is a Fallback width. 

    prompt_with_space = prompt + " "  
    prompt_length = len(prompt_with_space)  

    #Space needed to center the prompt for better user readability and presentation
    total_padding = (width - prompt_length) // 2
    padding = " " * total_padding

    print(padding + prompt_with_space, end='')  

class PayrollSystem:
    def __init__(self):
        self.__employees = {}
        self.__payslips = {}
        self.__unique_id_counter = 1
        self.db_path = 'paysphere.db'
        from database import init_db
        init_db()  # Initialize database first
        self.setup_predefined_employees()  # Then setup predefined employees

    def setup_database(self):
        """Initialize the database connection and create necessary tables"""
        from database import init_db
        init_db()


    #Menu method implementation
    def menu(self):
        while True:
            print_centered("~" * 130)  
            print_centered("Welcome to PaySphere Pro", Colors.GREEN)
            print_centered("~" * 130) 
            print_centered("\"Simplifying Payroll, Empowering People\"", Colors.YELLOW)
            print_centered("1. Manage Employees")
            print_centered("2. Manage Payslip")
            print_centered("3. Manage Payroll")

            # Call the print_prompt function to display the prompt
            print_prompt("Choose an option:" )
            choice = input() 
            if choice == '1':
                self.manage_employees()
            elif choice == '2':
                self.manage_payslip()
            elif choice == '3':
                self.manage_payroll()
            else:
                print("Invalid choice. Please try again.", Colors.RED)

    #This is the function for managing employees
    def manage_employees(self):
        while True:
            print_centered("~" * 130)  
            print_centered("Manage Employees", Colors.GREEN)
            print_centered("~" * 130)  
            print_centered("1. Register Employee")
            print_centered("2. View Employees")
            print_centered("3. Update Employee")
            print_centered("4. Delete Employee")
            print_centered("5. Exit to Main Menu")

            print_prompt("Choose an option:")
            choice = input()  
            if choice == '1':
                self.register_employee()
            elif choice == '2':
                self.view_employees()
            elif choice == '3':
                self.update_employee()
            elif choice == '4':
                self.delete_employee()
            elif choice == '5':
                break  
            else:
                print("Invalid choice. Please try again.", Colors.RED)

    #This is the function for managing payslip       
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
                self.create_payslip() 
            elif choice == '2':
                self.view_payslip()
            elif choice == '3':
                break  
            else:
                print("Invalid choice. Please try again.", Colors.RED)

    #This is the function for managing payroll
    def manage_payroll(self):
        while True:
            print_centered("~" * 130)  
            print_centered("Manage Payroll", Colors.GREEN)
            print_centered("~" * 130)  
            print_centered("1. View Payroll")
            print_centered("2. Exit to Main Menu")

            print_prompt("Choose an option:")
            choice = input()  
            if choice == '1':
                self.view_payroll() 
            elif choice == '2':
                break
            else:
                print_centered("Invalid choice. Please try again.", Colors.RED)    

    #This is the function for employee record under managing employee 
    def create_employee(self, emp_type, name, job_title, email, phone, department, manager, hire_date, birth_date):
        try:
            # Extract department code based on the department name
            department_mapping = {
                "HUMAN RESOURCES": "HR",
                "INFORMATION TECHNOLOGY": "IT",
                "FINANCE": "FIN",
                "MARKETING": "MKT",
                "ENGINEERING": "ENG"
            }
            department_code = department_mapping.get(department.upper())
            if not department_code:
                raise ValueError("Invalid department")
                
            emp_type_code = emp_type[0].upper()
            
            # Validate department code
            if not self.validate_department_code(department_code):
                raise ValueError("Invalid department code")
                
            # Validate employee type
            if not self.validate_employee_type_code(emp_type_code):
                raise ValueError("Invalid employee type code")
                
            emp_id = f"{department_code}-{emp_type_code}-{str(self.__unique_id_counter).zfill(4)}"
            
            employee_classes = {
                'F': FullTimeEmployee,
                'P': PartTimeEmployee,
                'C': ContractEmployee,
                'I': InternEmployee
            }
            
            employee_class = employee_classes.get(emp_type_code)
            if not employee_class:
                raise ValueError("Invalid employee type")
                
            employee = employee_class(emp_id, name, job_title, email, phone, department, manager, hire_date, birth_date)
            self.__employees[emp_id] = employee

            # Add database storage alongside existing code
            try:
                from database import get_db
                with get_db() as conn:
                    cursor = conn.cursor()
                    cursor.execute('''
                        INSERT INTO employees 
                        (emp_id, name, job_title, email, phone, department, manager, hire_date, birth_date, employee_type)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (emp_id, name, job_title, email, phone, department, manager, hire_date, birth_date, emp_type))
                    conn.commit()

                self.__unique_id_counter += 1
                return emp_id

            except sqlite3.IntegrityError as e:
                print_centered("Error: Email address already exists!", Colors.RED)
                return None

            except Exception as e:
                print_centered(f"Error creating employee: {str(e)}", Colors.RED)
                return None
        except ValueError as e:
            print_centered(f"Error: {str(e)}", Colors.RED)
            return None
        except Exception as e:
            print_centered(f"Unexpected error: {str(e)}", Colors.RED)
            return None

    #These are input validation function for employee record to filter errors during input 
    def validate_department_code(self, code):
        return code.upper() in ["HR", "IT", "FIN", "MKT", "ENG"]
    
    def validate_employee_type_code(self, code):
        return code.upper() in ["F", "P", "C", "I"]
    
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

        emp_id = f"{department_code}-{employee_type_code}-{str(self.__unique_id_counter).zfill(4)}"
        self.__unique_id_counter += 1
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

        # Employee based on type
        employee_classes = {
            'F': FullTimeEmployee,
            'P': PartTimeEmployee,
            'C': ContractEmployee,
            'I': InternEmployee
        }
        employee_class = employee_classes.get(employee_type_code)
        if not employee_class:
            print("\t\t\t\tInvalid employee type.", Colors.RED)
            return
            
        new_employee = employee_class(emp_id, name, job_title, email, phone, department, manager, hire_date, birth_date)
        self.__employees[emp_id] = new_employee
        print_centered("Employee registered successfully.", Colors.YELLOW)
        print()

    # This function is used to display all employees
    def view_employees(self):
        print("-" * 199)
        if not self.__employees:
            print_centered("No employees registered.", Colors.RED)
            return
        for emp in self.__employees.values():
            print(emp)
            print("-" * 199)

        # Show employees from database
        from database import get_db
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM employees')
            db_employees = cursor.fetchall()
            
            if db_employees:
                print_centered("Database Records:", Colors.BLUE)
                for emp in db_employees:
                    print(f"ID: {emp[0]}, Name: {emp[1]}, Job Title: {emp[2]}, "
                          f"Email: {emp[3]}, Phone: {emp[4]}, Department: {emp[5]}, "
                          f"Manager: {emp[6]}, Hire Date: {emp[7]}, Birth Date: {emp[8]}, "
                          f"Type: {emp[9]}")
                    print("-" * 199)
        
    # This function is used for updating employee details
    def update_employee(self):
        print_centered("." * 199)
        emp_id = input("\t\t\t\tEnter Employee ID to update: ")
        if emp_id in self.__employees:
            emp = self.__employees[emp_id]
            print(f"Current details: {emp}")
            print_centered("." * 199)
            
            # Get and validate new name
            name = input("\t\t\t\tEnter new Employee Name (leave blank to keep current): ")
            if not name:
                name = emp.get_name()
            elif not self.validate_name(name):
                print("\t\t\t\tInvalid name. Please use letters and spaces only.", Colors.RED)
                return
    
            # Get and validate new job title
            job_title = input("\t\t\t\tEnter new Job Title (leave blank to keep current): ")
            if not job_title:
                job_title = emp.get_job_title()
            elif not self.validate_job_title(job_title):
                print("\t\t\t\tInvalid job title. Please use letters and spaces only.", Colors.RED)
                return
    
            # Get and validate new email
            email = input("\t\t\t\tEnter new Email Address (leave blank to keep current): ")
            if not email:
                email = emp.get_email()
            elif not self.validate_email(email):
                print("\t\t\t\tInvalid email format. Please try again.", Colors.RED)
                return
    
            # Get and validate new phone number
            phone = input("\t\t\t\tEnter new Phone Number (leave blank to keep current): ")
            if not phone:
                phone = emp.get_phone()
            elif not self.validate_phone(phone):
                print("\t\t\t\tInvalid phone number. Please use numbers only.", Colors.RED)
                return
    
            # Get and validate new department
            department = input("\t\t\t\tEnter new Department (leave blank to keep current): ")
            if not department:
                department = emp.get_department()
            elif not self.validate_department(department):
                print("\t\t\t\tInvalid department. Please use letters and spaces only.", Colors.RED)
                return
    
            # Get and validate new manager
            manager = input("\t\t\t\tEnter new Manager Name (leave blank to keep current): ")
            if not manager:
                manager = emp.get_manager()
            elif not self.validate_manager(manager):
                print("\t\t\t\tInvalid manager name. Please use letters and spaces only.", Colors.RED)
                return
    
            # Get and validate new hire date
            hire_date = input("\t\t\t\tEnter new Hire Date (yyyy-mm-dd, leave blank to keep current): ")
            if not hire_date:
                hire_date = emp.get_hire_date()
            elif not self.validate_date(hire_date):
                print("\t\t\t\tInvalid hire date format. Please use yyyy-mm-dd format.", Colors.RED)
                return
    
            # Get and validate new birth date
            birth_date = input("\t\t\t\tEnter new Birth Date (yyyy-mm-dd, leave blank to keep current): ")
            if not birth_date:
                birth_date = emp.get_birth_date()
            elif not self.validate_date(birth_date):
                print("\t\t\t\tInvalid birth date format. Please use yyyy-mm-dd format.", Colors.RED)
                return
    
            # Get employee type from ID
            emp_type = emp_id.split('-')[1]
            
            # Create new employee object with updated information
            employee_classes = {
                'F': FullTimeEmployee,
                'P': PartTimeEmployee,
                'C': ContractEmployee,
                'I': InternEmployee
            }
            
            employee_class = employee_classes.get(emp_type)
            if not employee_class:
                print("\t\t\t\tInvalid employee type.", Colors.RED)
                return
                
            # Create new employee with updated information
            new_emp = employee_class(emp_id, name, job_title, email, phone, department, 
                                   manager, hire_date, birth_date)
            
            # Replace old employee details with new employee details
            self.__employees[emp_id] = new_emp
            
            # Update database
            try:
                from database import get_db
                with get_db() as conn:
                    cursor = conn.cursor()
                    cursor.execute('''
                        UPDATE employees 
                        SET name = ?, job_title = ?, email = ?, phone = ?, 
                            department = ?, manager = ?, hire_date = ?, birth_date = ?
                        WHERE emp_id = ?
                    ''', (name, job_title, email, phone, department, manager, hire_date, birth_date, emp_id))
                    conn.commit()
            except sqlite3.Error as e:
                print_centered(f"Database error: {str(e)}", Colors.RED)
            except Exception as e:
                print_centered(f"Error updating employee: {str(e)}", Colors.RED)
            
            print_centered("Employee updated successfully.", Colors.YELLOW)
            print_centered("." * 130)
            print()
        else:
            print("\t\t\t\tEmployee not found.", Colors.RED)
         
    # This function is used to delete an employee from the system
    def delete_employee(self):  # Only indented 4 spaces from the left
        print_centered("Delete Employee", Colors.BLUE)
        print_centered("." * 130)
        print()
        
        emp_id = input("\t\t\t\tEnter Employee ID to delete: ").strip().upper()
        
        if emp_id in self.__employees:
            try:
                # Delete from database first
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                
                # Delete from employees table
                cursor.execute("DELETE FROM employees WHERE emp_id = ?", (emp_id,))
                
                # Delete associated payslips
                cursor.execute("DELETE FROM payslips WHERE emp_id = ?", (emp_id,))
                
                conn.commit()
                conn.close()
                
                # Delete from memory
                del self.__employees[emp_id]
                if emp_id in self.__payslips:
                    del self.__payslips[emp_id]
                
                print_centered(f"Employee {emp_id} has been deleted successfully.", Colors.GREEN)
                
            except sqlite3.Error as e:
                print_centered(f"Database error: {str(e)}", Colors.RED)
            except Exception as e:
                print_centered(f"Error deleting employee: {str(e)}", Colors.RED)
        else:
            print_centered("Employee ID not found.", Colors.RED)
        
        print_centered("." * 130)
        print()
    # This function is used for creating payslip for employee(s)
    def create_payslip(self):
        try:
            emp_id = input("\t\t\t\tEnter Employee ID to create payslip: ")
            
            if emp_id not in self.__employees:
                print_centered("Employee not found.", Colors.RED)
                return 
            emp = self.__employees[emp_id]
            
            # Displaying employee details
            print_centered("=" * 130)
            print_centered("Payslip", Colors.BLUE)
            print_centered("=" * 130)
            print(f"\t\t\t\t\t\tEmployee ID: {emp.get_emp_id()}")
            print(f"\t\t\t\t\t\tName: {emp.get_name()}")
            print(f"\t\t\t\t\t\tJob Title: {emp.get_job_title()}")
            print(f"\t\t\t\t\t\tPhone Number: +63-{emp.get_phone()}")
            print(f"\t\t\t\t\t\tDepartment: {emp.get_department()}")
            print_centered("-" * 130)
            
            # Getting payslip details with validation
            try:
                total_hours_worked = self.get_numeric_input("\t\t\t\tEnter Total Hours Worked: ")
                if total_hours_worked < 0:
                    raise ValueError("\t\t\t\t\t\tHours worked cannot be negative", Colors.RED)
                    
                over_hours = self.get_numeric_input("\t\t\t\tEnter Over Hours: ")
                if over_hours < 0:
                    raise ValueError("\t\t\t\t\t\tOvertime hours cannot be negative", Colors.RED)
                    
                salary_advance = self.get_numeric_input("\t\t\t\tEnter Salary in Advance: ")
                if salary_advance < 0:
                    raise ValueError("\t\t\t\t\t\tSalary advance cannot be negative", Colors.RED)
                    
                incentives = self.get_numeric_input("\t\t\t\tEnter Incentives: ")
                if incentives < 0:
                    raise ValueError("\t\t\t\t\t\tIncentives cannot be negative", Colors.RED)
                    
                bonus = self.get_numeric_input("\t\t\t\tEnter Bonus: ")
                if bonus < 0:
                    raise ValueError("\t\t\t\t\t\tBonus cannot be negative", Colors.RED)
                    
            except ValueError as e:
                print_centered(f"Invalid input: {str(e)}", Colors.RED)
                return
    
            # These are the calcualtions for the payslip
            try:
                # Get base salary calculation from employee type-specific implementation
                base_salary = emp.calculate_salary(total_hours_worked, over_hours)
                
                # Calculate mandatory benefits
                sss_employee_contribution = base_salary * 0.045
                philhealth_employee_contribution = base_salary * 0.0225
                pagibig_employee_contribution = base_salary * 0.02
    
                # Calculate totals
                overtime_pay = over_hours * (base_salary/total_hours_worked) * 1.25 if total_hours_worked > 0 else 0
                total_earnings = base_salary + incentives + bonus + overtime_pay
                total_deductions = (salary_advance + sss_employee_contribution + 
                                  philhealth_employee_contribution + pagibig_employee_contribution)
                net_pay = total_earnings - total_deductions
    
                # Store payslip
                self.__payslips[emp_id] = {
                    "total_hours_worked": total_hours_worked,
                    "over_hours": over_hours,
                    "basic_salary": base_salary,
                    "incentives": incentives,
                    "bonus": bonus,
                    "overtime_pay": overtime_pay,
                    "total_earnings": total_earnings,
                    "salary_advance": salary_advance,
                    "sss_employee_contribution": sss_employee_contribution,
                    "philhealth_employee_contribution": philhealth_employee_contribution,
                    "pagibig_employee_contribution": pagibig_employee_contribution,
                    "total_deductions": total_deductions,
                    "net_pay": net_pay
                }
                # Store payslip in database
                try:
                    from database import get_db
                    with get_db() as conn:
                        cursor = conn.cursor()
                        cursor.execute('''
                            INSERT INTO payslips (
                                emp_id, pay_period, total_hours, overtime_hours,
                                basic_salary, incentives, bonus, overtime_pay,
                                total_earnings, salary_advance,
                                sss_contribution, philhealth_contribution, pagibig_contribution,
                                total_deductions, net_pay, creation_date
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (
                            emp_id, datetime.now().strftime('%Y-%m'),
                            total_hours_worked, over_hours,
                            base_salary, incentives, bonus, overtime_pay,
                            total_earnings, salary_advance,
                            sss_employee_contribution, philhealth_employee_contribution, 
                            pagibig_employee_contribution, total_deductions, net_pay,
                            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        ))
                        conn.commit()
                except sqlite3.Error as e:
                    print_centered(f"Database error: {str(e)}", Colors.RED)
                except Exception as e:
                    print_centered(f"Error storing payslip in database: {str(e)}", Colors.RED)
    
                # Display payslip
                self.display_payslip(emp_id)
                
            except Exception as e:
                print_centered(f"Error calculating payslip: {str(e)}", Colors.RED)
                
        except Exception as e:
            print_centered(f"Error creating payslip: {str(e)}", Colors.RED)

    def display_payslip(self, emp_id):
        """Helper method to display a formatted payslip"""
        if emp_id in self.__payslips and emp_id in self.__employees:
            payslip = self.__payslips[emp_id]
            emp = self.__employees[emp_id]

            print_centered("=" * 130)
            print_centered("Payslip", Colors.BLUE)
            print_centered("=" * 130)
        
            # Employee Details
            print(f"\t\t\t\t\t\tEmployee ID: {emp.get_emp_id()}")
            print(f"\t\t\t\t\t\tName: {emp.get_name()}")
            print(f"\t\t\t\t\t\tJob Title: {emp.get_job_title()}")
            print(f"\t\t\t\t\t\tDepartment: {emp.get_department()}")
            print_centered("-" * 130)
        
            # Earnings Section
            print_centered("Earnings:", Colors.GREEN)
            print_centered(f"  Total Hours Worked:         {payslip['total_hours_worked']}")
            print_centered(f"  Overtime Hours:             {payslip['over_hours']}")
            print_centered(f"  Basic Salary:               ₱{payslip['basic_salary']:.2f}")
            print_centered(f"  Incentives:                 ₱{payslip['incentives']:.2f}")
            print_centered(f"  Bonus:                      ₱{payslip['bonus']:.2f}")
            print_centered(f"  Overtime Pay:               ₱{payslip['overtime_pay']:.2f}")
            print_centered(f"  TOTAL EARNINGS:             ₱{payslip['total_earnings']:.2f}")
        
            # Deductions Section
            print_centered("Deductions:", Colors.GREEN)
            print_centered(f"  Salary in Advance:          ₱{payslip['salary_advance']:.2f}")
            print_centered(f"  SSS Contribution:           ₱{payslip['sss_employee_contribution']:.2f}")
            print_centered(f"  PhilHealth Contribution:    ₱{payslip['philhealth_employee_contribution']:.2f}")
            print_centered(f"  Pag-ibig Contribution:      ₱{payslip['pagibig_employee_contribution']:.2f}")
            print_centered(f"  TOTAL DEDUCTIONS:           ₱{payslip['total_deductions']:.2f}")
        
            # Net Pay
            print_centered(f"  Net Pay:                    ₱{payslip['net_pay']:.2f}")
        else:
            print_centered("Payslip or employee not found.", Colors.RED)

    def get_numeric_input(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a numeric value.", Colors.RED)
    
    def setup_predefined_employees(self):
        # Adding some predefined employees using concrete classes based on employee type code
        predefined_employees = {
            # Full-time employees (F)
            "HR-F-0001": FullTimeEmployee("HR-F-0001", "Dwayne Johnson", "Chief HR Manager", "dwayne.johnson@example.com", "09123456789", "Human Resources", "Bob Smith", "2015-01-15", "1990-05-20"),
            "HR-F-0002": FullTimeEmployee("HR-F-0002", "Evelyn Carter", "HR Manager", "evelyn.carter@example.com", "09123456789", "Human Resources", "Bob Smith", "2020-01-15", "1999-09-20"),
            "IT-F-0003": FullTimeEmployee("IT-F-0003", "Kit Mayson", "Programmer", "kit.mayson@example.com", "09123456788", "Info. Technology", "Jane Doe", "2021-03-10", "1992-07-30"),
            
            # Part-time employee (P)
            "IT-P-0004": PartTimeEmployee("IT-P-0004", "Liam Thompson", "Data Analyst", "liam.thompson@example.com", "09123456788", "Info. Technology", "Jane Doe", "2022-05-10", "1996-07-30"),
            
            # Contract employees (C)
            "FIN-C-0005": ContractEmployee("FIN-C-0005", "Mary Merrier", "Financial Analyst", "mary.merrier@example.com", "09123456787", "Finance", "Robert Brown", "2013-06-20", "1988-04-11"),
            "ENG-C-0010": ContractEmployee("ENG-C-0010", "Lucas Nguyen", "Computer Engineer", "lucas.nguyen@example.com", "09123456786", "Engineering", "Aiden Kim", "2020-02-01", "1992-03-25"),
            
            # More full-time employees
            "FIN-F-0006": FullTimeEmployee("FIN-F-0006", "Sofia Martinez", "Assistant Financial Analyst", "sofia.martinez@example.com", "09123456787", "Finance", "Robert Brown", "2019-06-20", "1994-11-15"),
            "MKT-F-0007": FullTimeEmployee("MKT-F-0007", "James Delaware", "Executive Marketing Manager", "james.delaware@example.com", "09123456786", "Marketing", "Emily Davis", "2014-09-21", "1991-01-10"),
            "ENG-F-0009": FullTimeEmployee("ENG-F-0009", "Ethan Garcia", "Software Engineer", "ethan.garcia@example.com", "09123456786", "Engineering", "Aiden Kim", "2018-09-01", "1984-01-10"),
            
            # Intern employee (I)
            "MKT-I-0008": InternEmployee("MKT-I-0008", "Noah Patel", "Intern", "noah.patel@example.com", "09123456786", "Marketing", "Emily Davis", "2022-09-01", "1999-01-10"),
        }
        
        self.__employees = predefined_employees
        
        # Save predefined employees to database
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                for emp_id, employee in predefined_employees.items():
                    # Validate employee ID format and type
                    parts = emp_id.split('-')
                    if len(parts) != 3:
                        print(f"Invalid employee ID format for {emp_id}")
                        continue
                        
                    emp_type = parts[1]
                    if emp_type not in ['F', 'P', 'C', 'I']:
                        print(f"Invalid employee type {emp_type} for {emp_id}")
                        continue

                    try:
                        # Check if employee already exists
                        cursor.execute('SELECT emp_id FROM employees WHERE emp_id = ?', (emp_id,))
                        if cursor.fetchone() is None:
                            # Format dates consistently
                            hire_date = datetime.strptime(employee.get_hire_date(), '%Y-%m-%d').strftime('%Y-%m-%d')
                            birth_date = datetime.strptime(employee.get_birth_date(), '%Y-%m-%d').strftime('%Y-%m-%d')
                            
                            # Insert only if employee doesn't exist
                            cursor.execute('''
                                INSERT INTO employees (emp_id, name, job_title, email, phone, department, 
                                                    manager, hire_date, birth_date, employee_type)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            ''', (
                                employee.get_emp_id(),
                                employee.get_name(),
                                employee.get_job_title(),
                                employee.get_email(),
                                employee.get_phone(),
                                employee.get_department(),
                                employee.get_manager(),
                                hire_date,
                                birth_date,
                                emp_type
                            ))
                            print(f"Successfully added employee {emp_id}")
                    except sqlite3.IntegrityError as e:
                        print(f"Database integrity error for {emp_id}: {e}")
                    except ValueError as e:
                        print(f"Date format error for {emp_id}: {e}")
                    except sqlite3.Error as e:
                        print(f"Error inserting employee {emp_id}: {e}")
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return
        # Predefined payslip details for each employee
        self.__payslips = {
            "HR-F-0001": {
                "total_hours_worked": 254,
                "over_hours": 10,
                "basic_salary": 17051.02,
                "incentives": 1500,
                "bonus": 5000,
                "overtime_pay": 839.12,
                "total_earnings": 24390.14, 
                "salary_advance": 2000,
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
                "salary_advance": 1000,
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
                "salary_advance": 0,
                "sss_employee_contribution": 1316.25,
                "philhealth_employee_contribution": 658.13 ,
                "pagibig_employee_contribution": 585,  
                "total_deductions": 2559.38,  
                "net_pay": 31360.62,  
            },
            "IT-P-0004": {
                "total_hours_worked": 200,
                "over_hours": 10,
                "basic_salary": 11700,
                "incentives": 1500,
                "bonus": 1000,
                "overtime_pay": 731.25,
                "total_earnings": 14200, 
                "salary_advance": 1000,
                "sss_employee_contribution": 639,
                "philhealth_employee_contribution": 319.5,
                "pagibig_employee_contribution": 284,  
                "total_deductions": 2242.5,  
                "net_pay": 11957.5,  
            },
            "FIN-C-0005": {
                "total_hours_worked": 254,
                "over_hours": 10,
                "basic_salary": 32004,
                "incentives": 1500,
                "bonus": 1000,
                "overtime_pay": 1575,
                "total_earnings": 36079, 
                "salary_advance": 0,
                "sss_employee_contribution": 1440.18,
                "philhealth_employee_contribution": 720.09,
                "pagibig_employee_contribution": 640.08,  
                "total_deductions": 2800.35,  
                "net_pay": 33278.65,  
            },
            "FIN-F-0006": {
                "total_hours_worked": 250,
                "over_hours": 10,
                "basic_salary": 42000,
                "incentives": 1500,
                "bonus": 3000,
                "overtime_pay": 2100,
                "total_earnings": 48600, 
                "salary_advance": 0,
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
                "salary_advance": 1000,
                "sss_employee_contribution": 1268.73,
                "philhealth_employee_contribution": 634.36,
                "pagibig_employee_contribution": 563.88,  
                "total_deductions": 3466.97,  
                "net_pay": 29920.78, 
            },
            "MKT-I-0008": {
                "total_hours_worked": 200,
                "over_hours": 10,
                "basic_salary": 8326,
                "incentives": 1500,
                "bonus": 1000,
                "overtime_pay": 520.37,
                "total_earnings": 11346.37, 
                "salary_advance": 1000,
                "sss_employee_contribution": 374.67,
                "philhealth_employee_contribution": 187.33,
                "pagibig_employee_contribution": 166.52,  
                "total_deductions": 1728.49,  
                "net_pay": 9617.88, 
            },
            "ENG-F-0009": {
                "total_hours_worked": 254,
                "over_hours": 10,
                "basic_salary": 36576,
                "incentives": 1500,
                "bonus": 2000,
                "overtime_pay": 1800,
                "total_earnings": 41876, 
                "salary_advance": 1000,
                "sss_employee_contribution": 1645.92,
                "philhealth_employee_contribution": 822.96,
                "pagibig_employee_contribution": 731.52,  
                "total_deductions": 4200.4,  
                "net_pay": 37675.6, 
            },
            "ENG-C-0010": {
                "total_hours_worked": 250,
                "over_hours": 5,
                "basic_salary": 27000,
                "incentives": 1500,
                "bonus": 2000,
                "overtime_pay": 675,
                "total_earnings": 31175, 
                "salary_advance": 1000,
                "sss_employee_contribution": 1215,
                "philhealth_employee_contribution": 607.5,
                "pagibig_employee_contribution": 540,  
                "total_deductions": 3362.5,  
                "net_pay": 27812.5, 
            }
        }

    def view_payslip(self):
        emp_id = input("\t\t\t\tEnter Employee ID to view payslip: ")
        if emp_id in self.__payslips:
            payslip = self.__payslips[emp_id]
            emp = self.__employees[emp_id]
            
            # First check in-memory payslips (preserving existing functionality)
            payslip = self.__payslips.get(emp_id)
        
            # Then check database
            try:
                from database import get_db
                db = get_db()
                cursor = db.cursor()
            
                # Get the latest payslip from database
                cursor.execute("""
                    SELECT * FROM payslips 
                    WHERE emp_id = ? 
                    ORDER BY creation_date DESC 
                    LIMIT 1
                """, (emp_id,))
                db_payslip = cursor.fetchone()
            
                if payslip or db_payslip:
                    # If employee exists, display their information
                    if emp_id in self.__employees:
                        emp = self.__employees[emp_id]
                    
                        print_centered("=" * 130)
                        print_centered("Payslip", Colors.BLUE)
                        print_centered("=" * 130)
                        print(f"\t\t\t\t\t\tEmployee ID: {emp.get_emp_id()}")
                        print(f"\t\t\t\t\t\tName: {emp.get_name()}")
                        print(f"\t\t\t\t\t\tJob Title: {emp.get_job_title()}")
                        print(f"\t\t\t\t\t\tPhone Number: {emp.get_phone()}")
                        print(f"\t\t\t\t\t\tDepartment: {emp.get_department()}")
                        print_centered("-" * 130)
                        

                        # Display payslip details - prioritize in-memory if available
                        if payslip:
                            # Display the stored payslip details
                            print_centered("Earnings:", Colors.GREEN)
                            print_centered(f"  Total Hours Worked:         {payslip['total_hours_worked']}")
                            print_centered(f"  Overtime Hours:             {payslip['over_hours']}")
                            print_centered(f"  Basic Salary:               ₱{payslip['basic_salary']:.2f}")
                            print_centered(f"  Incentives:                 ₱{payslip['incentives']:.2f}")
                            print_centered(f"  Bonus:                      ₱{payslip['bonus']:.2f}")
                            print_centered(f"  Overtime Pay:               ₱{payslip['overtime_pay']:.2f}")
                            print_centered(f"  TOTAL EARNINGS:             ₱{payslip['total_earnings']:.2f}")

                            print_centered("Deductions:", Colors.GREEN)
                            print_centered(f"  Salary in Advance:          ₱{payslip['salary_advance']:.2f}")
                            print_centered(f"  SSS Contribution:           ₱{payslip['sss_employee_contribution']:.2f}")
                            print_centered(f"  PhilHealth Contribution:    ₱{payslip['philhealth_employee_contribution']:.2f}")
                            print_centered(f"  Pag-ibig Contribution:      ₱{payslip['pagibig_employee_contribution']:.2f}")
                            print_centered(f"  TOTAL DEDUCTIONS:           ₱{payslip['total_deductions']:.2f}")

                            # Final Net Pay
                            print_centered(f"  Net Pay:                    ₱{payslip['net_pay']:.2f}")
                        else:
                            # Display database payslip details
                            print_centered("Earnings:", Colors.GREEN)
                            print_centered(f"  Total Hours Worked:         {db_payslip['total_hours']}")
                            print_centered(f"  Overtime Hours:             {db_payslip['overtime_hours']}")
                            print_centered(f"  Basic Salary:               ₱{db_payslip['basic_salary']:.2f}")
                            print_centered(f"  Incentives:                 ₱{db_payslip['incentives']:.2f}")
                            print_centered(f"  Bonus:                      ₱{db_payslip['bonus']:.2f}")
                            print_centered(f"  Overtime Pay:               ₱{db_payslip['overtime_pay']:.2f}")
                            print_centered(f"  TOTAL EARNINGS:             ₱{db_payslip['total_earnings']:.2f}")

                            print_centered("Deductions:", Colors.GREEN)
                            print_centered(f"  Salary in Advance:          ₱{db_payslip['salary_advance']:.2f}")
                            print_centered(f"  SSS Contribution:           ₱{db_payslip['sss_contribution']:.2f}")
                            print_centered(f"  PhilHealth Contribution:    ₱{db_payslip['philhealth_contribution']:.2f}")
                            print_centered(f"  Pag-ibig Contribution:      ₱{db_payslip['pagibig_contribution']:.2f}")
                            print_centered(f"  TOTAL DEDUCTIONS:           ₱{db_payslip['total_deductions']:.2f}")

                            # Final Net Pay
                            print_centered(f"  Net Pay:                    ₱{db_payslip['net_pay']:.2f}")
                    else:
                        print_centered("Employee not found.", Colors.RED)
                else:
                    print_centered("No payslip found for this Employee ID.", Colors.RED)        

            except Exception as e:
                print_centered(f"Error retrieving payslip: {str(e)}", Colors.RED)
                if payslip:
                # If database fails but in-memory exists, still show in-memory payslip
                    self.display_payslip(emp_id)
                
    def view_payroll(self):
        if not self.__payslips:
            print_centered("No payslips available.", Colors.RED)
            return

        print("=" * 199)
        print_centered("Payroll Report", Colors.BLUE)
        print("=" * 199)
        payroll_date = input("\t\t\t\tEnter Payroll Date (YYYY-MM-DD): ")
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
        total_salary_advance = 0
        total_deductions = 0
        total_net_pay = 0
        total_hours_worked = 0
        total_overtime_hours = 0

        # Print header for the report
        print_centered(f"{'Name':<20} {'Department':<20} {'Total Hours Worked':<20} {'Overtime Hours':<15} {'Total Earnings':<20} {'Total Deductions':<20} {'Net Pay':<25}", Colors.YELLOW)
        print()

        # Iterate through payslips
        for emp_id, payslip in self.__payslips.items():
            emp = self.__employees[emp_id]
        
            #Print employee details
            print_centered(f"{emp.get_name():<20} {emp.get_department():<20} {payslip['total_hours_worked']:<20} {payslip['over_hours']:<15} ₱{payslip['total_earnings']:<20.2f} ₱{payslip['total_deductions']:<20.2f} ₱{payslip['net_pay']:<15.2f}")

            # Accumulate totals
            total_basic_salary += payslip['basic_salary']
            total_incentives += payslip['incentives']
            total_bonus += payslip['bonus']
            total_overtime_pay += payslip.get('overtime_pay', 0)
            total_earnings += payslip['total_earnings']
            total_salary_advance += payslip['salary_advance']
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