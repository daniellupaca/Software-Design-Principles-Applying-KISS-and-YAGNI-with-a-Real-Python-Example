from models import Order
from order_repository import OrderRepository


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create_order(self, order_id, customer, total):
        if total <= 0:
            raise ValueError("Total must be greater than zero")
        order = Order(order_id, customer, total)
        self.repository.add(order)
        return order

    def approve_order(self, order_id):
        for order in self.repository.list_all():
            if order.id == order_id:
                order.approve()
                return order
        raise ValueError("Order not found")
