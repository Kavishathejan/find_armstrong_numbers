def count_armstrong(number):
    final_num = str(number)
    armstrong_sum = sum(int(digit)**len(final_num) for digit in final_num)
    
    return armstrong_sum == number

def select_armstrong_numbers(start, end):
    
    armstrong_numbers = []
    for num in range(start, end+1):
        if count_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

if __name__ == "__main__":
    start = 0
    end = 100000
    armstrong_numbers = select_armstrong_numbers(start, end)
    print("Armstrong numbers in the range of 0 to 100,000:")
    print(armstrong_numbers)
