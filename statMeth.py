class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n
    
    @staticmethod # by this we can create methods without using self  **IMPORTANT**
    def add(a, b):
        return a+b
    
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)


