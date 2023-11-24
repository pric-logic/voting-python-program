# Voting System for School Head Elections

## Introduction
This project is a voting system developed for conducting school head elections. The system is designed to manage the voting process, analyze voting patterns, and declare winners based on the received votes. The project includes features such as recording votes, analyzing voter demographics, and determining winners in different categories.

## Technologies Used
- Python
- MySQL

## Project Structure
The project consists of two main components:

### 1. Voting System
The `voting_system.py` file contains the implementation of the voting system. This part of the project includes the following functionalities:

- **User-Defined Functions for Vote Analysis:**
  - `division(sub)`: Analyzes the votes based on a particular division.
  - `cla_ss(std)`: Analyzes the votes based on a particular class.
  - `cla_div(std, sub)`: Analyzes the votes based on a specific class and division.
  - `Gender()`: Analyzes the votes based on gender.
  - `absentees()`: Calculates the number of absentees.
  - `winner(win)`: Retrieves the winner's name based on the candidate code.

- **MySQL Database Connection:**
  - Establishes a connection to the MySQL database for storing and retrieving voting data.

- **Voting Process:**
  - Validates voters and allows them to cast their votes.
  - Checks for duplicate votes.
  - Updates the database with the cast votes.

### 2. Analysis and Winner Declaration
The `analysis_winner.py` file contains functions for analyzing the voting data and declaring winners. This part of the project includes the following functionalities:

- **Analysis Functions:**
  - `gender(year)`: Analyzes the votes based on gender for a specific year.
  - `Class(year)`: Analyzes the votes based on class for a specific year.
  - `Division(year)`: Analyzes the votes based on division for a specific year.
  - `house(year)`: Analyzes the votes based on the house for a specific year.

- **Winner Analysis:**
  - Analyzes and declares winners for different positions, considering factors such as gender, house, class, and division.

## How to Use
1. Ensure that Python and MySQL are installed on your system.
2. Import the MySQL connector in the `voting_system.py` file.
3. Set up the MySQL database with the required tables for storing voter and candidate information.
4. Run the `voting_system.py` file to initiate the voting process.
5. Follow the on-screen prompts to cast votes and terminate the voting process.
6. Run the `analysis_winner.py` file to analyze the voting data and declare winners in various categories.

## Note
- This project was developed as part of a class assignment during the 12th grade.
- It is recommended to customize the MySQL database connection details and queries based on your specific setup and requirements.
- The code assumes that the necessary tables and data are present in the MySQL database.
- For a more comprehensive and secure voting system, additional features and security measures should be implemented.

Feel free to modify and extend the code as needed for your specific use case.
