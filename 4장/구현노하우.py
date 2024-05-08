# ------조기반환-----
def total_price(quantity, price):
    total = quantity * price
    if total > 100:
        return total * 0.9  # 조기반환
    return total

print(total_price(4, 50))

#-----보호구문-----
def calculate_average(numbers):
    if numbers is None:   # 예외처리
        return None
    
    if not isinstance(numbers, list):
        return None
    
    if len(numbers) == 0:
        return None

    total = sum(numbers)
    average = total / len(numbers)
    return average

print(calculate_average(1))

#---합성함수---
def add_three(x):
    
    return x + 3

def square(x):
    
    return x*x

composed_function = lambda x : square(add_three(x))    # lambda 를 이용해 구현
print(composed_function(3))
