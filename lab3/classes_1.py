class string():
    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

x = string()
x.get_string()
x.print_string()