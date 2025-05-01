from order_repository import OrderRepository
from order_service import OrderService

repo = OrderRepository()
service = OrderService(repo)

# Create valid order
order = service.create_order(1, "Client A", 150.0)
print(f"Created order: {order.customer}, total: {order.total}, status: {order.status}")

# Approve the order
approved = service.approve_order(1)
print(f"Updated order: {approved.customer}, status: {approved.status}")
