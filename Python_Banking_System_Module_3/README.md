# Python Banking System

## Codomax Digital Solutions – Module 3: Object-Oriented Python

A beginner-friendly command-line banking application designed to demonstrate Python Object-Oriented Programming concepts.

## Features

- Account creation
- Savings and Current account types
- Deposit
- Withdrawal
- Transaction history
- Account listing
- Input validation
- Exception handling
- Unit tests
- Class diagram

## OOP Concepts Demonstrated

### Classes and Objects
`Account`, `SavingsAccount`, `CurrentAccount`, and `Bank` are classes. Objects are created from these classes.

### Constructor
The `__init__()` method initializes account details.

### Encapsulation
Account data such as balance and transaction records are stored in protected attributes such as `_balance` and `_transactions`.

### Inheritance
`SavingsAccount` and `CurrentAccount` inherit common behavior from `Account`.

### Polymorphism
Both account types implement their own `withdraw()` method with different rules.

### Abstraction
`Account` is an abstract base class and requires subclasses to implement `withdraw()`.

### Clean Code
The application uses meaningful names, small functions, validation, exception handling, and separation between account logic and the bank manager.

## How to Run

Open the project folder in VS Code and run:

```bash
python banking_system.py
```

## Run Tests

```bash
python -m unittest test_banking_system.py
```

## Project Structure

```text
Python_Banking_System_Module_3/
├── banking_system.py
├── test_banking_system.py
├── diagram.md
├── README.md
├── notes.md
└── requirements.txt
```

## Example Operations

1. Create a savings or current account.
2. Deposit money.
3. Withdraw money according to the account rules.
4. View transaction history.
