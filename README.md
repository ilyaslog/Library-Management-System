# Library Management System

## What's This?

Hey there! This project aims to improve library management by automating administrative processes like managing loans, returns, and keeping records. Our goal is to enhance coordination, increase data accuracy, and make planning library activities easier.

## How We Built It

### Problem Statement
How can we improve the efficiency of library management by automating administrative processes such as loan management, returns, and record-keeping to optimize coordination, increase data accuracy, and facilitate library activity planning?

### Objectives
- Facilitate student account management.
- Implement a comprehensive traceability system for loans.
- Simplify loan processes and tracking to optimize efficiency and improve user experience.

### Tools Used
- **IDE**: Visual Studio Code, PyCharm
- **Language**: Python
- **Libraries**: MySQL Connector, CustomTkinter
- **Tools**: Git, GitHub, Discord

### System Design

#### Use Case Diagram
![Use Case Diagram](path_to_use_case_diagram_image)

## How to Use It

### Interfaces

#### 1. Login Interface
This interface allows users to log in and directs them to the appropriate interface based on their role.

#### 2. Admin Window
- **Student Management Page**: Lists active users and allows for basic functions such as adding, suspending, and deleting users.
  ![Student Management](path_to_student_management_image)

- **Loan Management Page**: Enables the admin to oversee all current and past loans and validate new ones.
  ![Loan Management](path_to_loan_management_image)

- **Book Management Page**: Allows the admin to manage the book inventory by creating, deleting, or modifying books.
  ![Book Management](path_to_book_management_image)

#### 3. User Window
- **Profile Page**: Lists all the user's information.
  ![Profile Page](path_to_profile_page_image)

- **Catalog Page**: Displays the list of books and allows students to borrow them.
  ![Catalog Page](path_to_catalog_page_image)

- **Loan Page**: Lists current loans and the history of previous loans.
  ![Loan Page](path_to_loan_page_image)

## Example Usage

### Adding a User
- Admin logs in and navigates to the Student Management Page.
- Clicks "Add User" and fills in the required details.
- New user is added to the system.

### Borrowing a Book
- User logs in and goes to the Catalog Page.
- Selects a book and clicks "Borrow".
- The loan is recorded, and the book is marked as borrowed.

### Managing Loans
- Admin logs in and navigates to the Loan Management Page.
- Reviews and validates pending loan requests.
- Updates the status of ongoing and past loans.

## Conclusion

This library management application, developed with CustomTkinter, provides a user-friendly interface for both administrators and users. The implemented features allow easy addition of new books and efficient management of the entire library. CustomTkinter's extensive customization options enhance the overall user experience, making the application intuitive and practical for optimal library management.

## Who Made This?

This project was created by Ilias Issaf, Ilyas Himit, Rayane Lalaoui Hassani, and Ammar Kassbaoui under the guidance of Guermah Bassma. We are university students passionate about coding and learning new things. We hope this application helps improve library management! 😊
