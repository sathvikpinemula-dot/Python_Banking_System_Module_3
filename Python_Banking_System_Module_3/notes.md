# Object-Oriented Python – Module 3 Notes

## 1. Class and Object
A class is a blueprint for creating objects. An object is an instance of a class.

Example:
```python
class Student:
    pass

student = Student()
```

## 2. Constructor
The `__init__()` method runs when an object is created and initializes its attributes.

## 3. Methods
Methods are functions defined inside a class and operate on objects.

## 4. Encapsulation
Encapsulation keeps related data and methods together and controls direct access to internal data.

## 5. Inheritance
Inheritance allows a child class to reuse and extend a parent class.

## 6. Polymorphism
Polymorphism allows the same method name to behave differently in different classes.

## 7. Abstraction
Abstraction hides implementation details and exposes required behavior. Python supports abstraction through the `abc` module.

## 8. Clean Code Principles
Use meaningful names, keep functions focused, avoid unnecessary duplication, validate inputs, and handle errors clearly.

## Banking System Design
The `Bank` class manages accounts. `Account` provides common behavior. `SavingsAccount` and `CurrentAccount` specialize withdrawal rules.

Two examples of polymorphism in this project:
1. `SavingsAccount.withdraw()` enforces a minimum balance.
2. `CurrentAccount.withdraw()` allows an overdraft up to a defined limit.
