# Banking System Class Diagram

```mermaid
classDiagram
    class Account {
        <<abstract>>
        -_account_number
        -_holder_name
        -_balance
        -_transactions
        +deposit(amount)
        +withdraw(amount)
        +transaction_history()
        +display_details()
    }

    class SavingsAccount {
        +MIN_BALANCE
        +withdraw(amount)
    }

    class CurrentAccount {
        +OVERDRAFT_LIMIT
        +withdraw(amount)
    }

    class Bank {
        -_accounts
        +create_account()
        +get_account()
        +list_accounts()
    }

    Account <|-- SavingsAccount
    Account <|-- CurrentAccount
    Bank o-- Account
```

## Architecture

- `Bank` manages accounts.
- `Account` defines common account behavior.
- `SavingsAccount` and `CurrentAccount` implement different withdrawal rules.
- Private attributes beginning with `_` demonstrate encapsulation.
- `Account` is an abstract class, demonstrating abstraction.
- Overridden `withdraw()` methods demonstrate polymorphism.
