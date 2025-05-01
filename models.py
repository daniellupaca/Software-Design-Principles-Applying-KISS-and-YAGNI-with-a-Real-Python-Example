class Order:
    def __init__(self, order_id, customer, total):
        self.id = order_id
        self.customer = customer
        self.total = total
        self.status = "PENDING"

    def approve(self):
        if self.total > 0:
            self.status = "APPROVED"
