```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> CoffeeSelected
    CoffeeSelected --> Processing
    Processing --> Dispensing
    Dispensing --> Idle
    CoffeeSelected --> Cancelled
    Cancelled --> Idle
```  

```mermaid
sequenceDiagram
    participant User
    participant CoffeeMachine
    User->>CoffeeMachine: Select coffee
    CoffeeMachine->>User: Display options
    User->>CoffeeMachine: Choose an option
    CoffeeMachine->>CoffeeMachine: Process coffee
    CoffeeMachine-->>User: Dispense coffee
```  

```mermaid
classDiagram
    class CoffeeMachine {
        +start()
        +selectCoffee()
        +cancel()
    }
    class User {
        +selectCoffee()
        +cancel()
    }
```  

| State          | Next State       |
|----------------|------------------|
| Idle           | CoffeeSelected    |
| CoffeeSelected | Processing       |
| Processing     | Dispensing       |
| Dispensing     | Idle             |
| CoffeeSelected  | Cancelled       |
| Cancelled      | Idle             |