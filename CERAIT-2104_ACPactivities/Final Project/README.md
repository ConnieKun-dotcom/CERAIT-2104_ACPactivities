# PaySphere Pro Payroll Management System
<div align="center">
    <img src="https://github.com/user-attachments/assets/b08ab016-4408-4a7a-8d0d-f4d23e3a699c" alt="Alt text" />
</div>




## Table of Contents
* [I. Project Overview](#i-project-overview)
* [II. Application of Python Concepts and Libraries](#ii-application-of-python-concepts-and-libraries)
* [III. Sustainable Development Goal (SDG)](#iii-sustainable-development-goal-(sdg))
* [IV. Instructions for Running the Program](#iv-instructions-for-running-the-program)
* [Conclusion](#conclusion)
  

## I. Project Overview
The PaySphere Pro Management System is a console-based application designed to streamline the management
of employee records, payslips, and payroll calculations. This program allows users to register employees,
view and manage their details, create payslips, and generate payroll reports. It aims to simplify payroll
processes, enhance employee data management, and provide a user-friendly interface for HR professionals.

### Integration into the Project
* The system emphasizes accurate payroll processing, which is essential for ensuring that employees 
receive fair compensation for their work.
* By facilitating better management of employee records and payments, it helps organizations maintain
a motivated workforce, contributing to sustainable economic growth.

### Key Features:
<div align="center">
    <img src="https://github.com/user-attachments/assets/26c1be97-dcb1-4b4d-abad-ed2e99d57cc0" alt="Alt text" />
</div>

* **Employee Management:**
  
  <div align="center">
    <img src="https://github.com/user-attachments/assets/be8af8f6-cca6-46ef-beb2-d104d6e69ab1" alt="Alt text" />
</div>

  * Employee registration with different types (Full-time, Part-time, Contract, Intern)
  * Unique ID generation system (Department-Type-Number format)
  * View all employees
  * Update employee information
  * Delete employee records
  * Comprehensive data validation for all employee field

* **Payslip Management:**
  
  <div align="center">
    <img src="https://github.com/user-attachments/assets/6414918d-adf4-4b59-a37e-6c1e58ff3336" alt="Alt text"/>
</div>

  * Detailed payslip creation
  * Employee information display
  * Earnings breakdown
  * Deductions breakdown
  * Net pay calculation
  * Payslip storage and retrieval
* **Payroll Reports:**
  
  <div align="center">
    <img src="https://github.com/user-attachments/assets/29b81c81-ba18-4c38-9917-c2253f4320b7" alt="Alt text"/>
</div>

  * Calculate basic salary based on hours worked
  * Overtime calculation with different rates per employee type
  * Additional earnings (incentives, bonuses)
  * Mandatory deductions:
    * *SSS* (4.5% of base salary)
    * *PhilHealth* (2.25% of base salary)
    * *Pag-IBIG* (2% of base salary)
  * Salary advance deductions
  * Net pay calculation

## II. Application of Python Concepts and Libraries
This project utilizes various Python concepts and libraries to achieve its functionality. These principles work together to create a maintainable, scalable, and well-organized payroll system with clear separation of concerns and reusable code components.

* **Classes and Objects:** The program employs Object-Oriented Programming (OOP) principles by defining 
  classes such as Employee, PayrollSystem, and Colors. Each class encapsulates specific attributes and
  methods relevant to its purpose.
* **Encapsulation:**
  * Private attributes in Employee class (using double underscores like
    ```__emp_id, __name ```)
  * Getter methods to access private data (like
   ```get_emp_id(), get_name()```)
  * Protected data from direct external access while providing controlled access through methods
* **Inheritance:**
  * Base
    ```Employee ``` class inherited by specialized employee types
  * ```FullTimeEmployee, PartTimeEmployee, ContractEmployee,``` and InternEmployee all inherit from ```Employee```
  * Common attributes and methods shared through parent class while allowing specific implementations in child classes
* **Abstraction:**
  * Abstract base class ```Employee``` (using ABC module)
  * Abstract method ```calculate_salary()``` defined in base class
  * Hides complex implementation details while providing simple interface for salary calculations
* **Polymorphism:**
  * Different implementations of ```calculate_salary()``` in each employee type
  * System treats all employee types uniformly while executing type-specific calculations
* **Regular Expressions:** The re library is used for input validation, ensuring that user inputs for names, 
  emails, phone numbers, and dates conform to specified formats.
* **Error Handling:** The program includes error handling mechanisms to manage invalid user inputs gracefully,
  prompting users to re-enter data when necessary.
* **Data Structures:** The program uses dictionaries to store employee and payslip details, allowing for
  efficient data retrieval and management.

## III. Sustainable Development Goal (SDG)
  This project aligns with SDG 8: Decent Work and Economic Growth. By providing a tool that simplifies 
  payroll management, the system promotes fair and efficient work practices. It enables organizations 
  to accurately track employee contributions, ensure timely payments, and maintain transparent records,
  ultimately contributing to economic growth and decent work conditions.

### IV. Instructions for Running the Program
To run the Payroll Management System, follow these steps:
**1. Prerequisites:**
   * Ensure you have Python 3.x installed on your machine. You can download it from python.org.
**2. Clone the Repository:**
   * Open your terminal or command prompt.
   * Clone the repository to your local machine using the following command:
      ```bash
       git clone <repository-url>
   * Replace ```<repository-url>``` with the actual URL of the repository-[https://github.com/ConnieKun-dotcom/CERAIT-2104_ACPactivities/tree/main/CERAIT-2104_ACPactivities/Final%20Project]
       
**3. Navigate to the Project Directory:**
   * Open your terminal or command prompt and navigate to the project directory.
   * Change your directory to the project folder:
     ```bash
     cd <project-directory>
   * Replace <project-directory> with the name of the cloned repository folder.
    
**4. Run the Program:**
   * Execute the program using Python:
     ```bash
     python PaySphere-Pro.py 
   * If you're using a different filename, replace PaySphere-Pro.py with the appropriate filename.
   * Make sure to enter the required information as prompted.
     
**5. Interact with the Console:**
   * Follow the on-screen prompts to manage employees, create payslips, and generate payroll reports.

### Conclusion
The Payroll Management System is a comprehensive tool designed to enhance the efficiency of payroll 
processing and employee management. By leveraging Python's powerful features and aligning with sustainable
development goals, this project serves as a valuable resource for organizations aiming to improve their
HR practices.









