import math

def is_power_of_3(n):
    if n <= 0:
        return False
    
    log_result = math.log(n, 3)
    
    rounded = round(log_result)
    
    return 3 ** rounded == n

n = 56
print(f"Is {n} a power of 3? {is_power_of_3(n)}")