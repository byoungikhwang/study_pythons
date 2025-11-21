# class class_name():
# 초기화
class FourCal:
    first = 0 
    second = 0  

    def __init__(self):
        self.first = 4
        self.second = 6
        pass

    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        if b == 0:
            return "0으로 나눌 수 없습니다."
        return a / b

if __name__ == "__main__":
    fourcal = FourCal()
    print(f"3 + 5 = {fourcal.add(3, 5)}")
    print(f"10 - 4 = {fourcal.sub(10, 4)}")
    print(f"7 * 8 = {fourcal.mul(7, 8)}")
    print(f"20 / 5 = {fourcal.div(20, 5)}")
    print(f"10 / 0 = {fourcal.div(10, 0)}")

    pass