class upper_str():
    def __init__(self,getString):
        self.getString=getString
    def print_upper_str(self):
        print(self.getString.upper())
word=upper_str(input())
word.print_upper_str()