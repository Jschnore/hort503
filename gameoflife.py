class cell (object):
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        if state != 0 or state != 1:
            print("Enter a 0 or 1 you moron")
            exit(1)
    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        if state != 0 or state != 1:
            print("Enter a 0 or 1 you moron")
            exit(1)
def test_cell():
    test_cell = cell (1, 0, 1)

test_cell()
