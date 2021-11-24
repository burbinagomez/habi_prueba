class Status:
    def __init__(self):
        self.status = {
            "pre_venta":3,
            "en_venta":4,
            "vendido":5,
        }
    
    def verify_status(self, status):
        if status in self.status:
            return True
        return False

    def get_value_by_status(self, status):
        return self.status[status]

    def get_status_by_value(self, value):
        for st in self.status:
            if self.status[st] == value:
                return st
        return None