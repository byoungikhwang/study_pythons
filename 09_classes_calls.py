# 09_classes_calls.py 에서 호출
from codes.classes_fourcals import FourCal

if __name__ == "__main__":
    fourcal = FourCal()
    
    print(f"3 + 5 = {fourcal.add(3, 5)}")
    print(f"10 - 4 = {fourcal.sub(10, 4)}")
    print(f"7 * 8 = {fourcal.mul(7, 8)}")
    print(f"20 / 5 = {fourcal.div(20, 5)}")
    print(f"10 / 0 = {fourcal.div(10, 0)}")

    pass