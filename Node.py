class Node:
    def __init__(self):
        self.g_value = 0
        self.h_value = 0

    def get_f_value(self):
        return self.h_value + self.g_value