from definition import Tuple, Length

class Cluster:
    """Define a cluster of galaxy"""
    def __init__(self, size: Tuple[Length, Length], quantity: int):
        self.size = size
        self.quantity = quantity
        self.body = None
        self.field = None
        self.τ = None
        self.bodies = None

    def unpack(self):
        return (self.body, self.field, self.τ)