# Service Layer Pattern in Python

This repository contains a simple and educational implementation of the **Service Layer Pattern**, one of the enterprise application architecture patterns described by *Martin Fowler*.

## What is the Service Layer Pattern?

The Service Layer acts as a mediator between the application's input interface (like a UI or controller) and the domain logic. It encapsulates business logic in one place, keeping models and controllers clean and focused.

---

##  Project Structure

```
project/
├── models.py
├── order_repository.py
├── order_service.py
└── main.py
```

---

## Example Code Overview

### `models.py`

```python
class Order:
    def __init__(self, order_id, customer, total):
        self.id = order_id
        self.customer = customer
        self.total = total
        self.status = "PENDING"

    def approve(self):
        if self.total > 0:
            self.status = "APPROVED"
```

### `order_service.py`

```python
class OrderService:
    def create_order(self, order_id, customer, total):
        if total <= 0:
            raise ValueError("Total must be greater than zero")
        ...
```

### `main.py`

```python
order = service.create_order(1, "Client A", 150.0)
approved = service.approve_order(1)
print(approved.status)
```

---

## How to Run

Make sure Python 3 is installed. Then run:

```bash
python main.py
```



## 🔍 Key Concepts Demonstrated

- 📦 Business logic centralized in a service layer
- 🧼 Separation of concerns: clean models, clean controllers
- 🧪 Prepared for unit testing and CI integration


## Articulo



## 📽️ Video 

🔗 


