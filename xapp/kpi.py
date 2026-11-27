class KPI:

    def __init__(self, cell_id, users, capacity):
        self.cell_id = cell_id
        self.users = users
        self.capacity = capacity

    def get_load(self):
        return (self.users / self.capacity) * 100