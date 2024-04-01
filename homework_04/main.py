def power_numbers(*numbers):
    my_list=[]
    for num in numbers:
        my_list.append(num**3)
    return my_list

print(power_numbers(1,3,4,6,2,5))

def power_numbers_alt(*numbers):
    return [num ** 3 for num in numbers]

print(power_numbers_alt(1,2,3,4,5,6,7))

ODD = {
    "ODD": "odd"
}

EVEN = {
    "EVEN": "even"
}

PRIME = {
    "PRIME": "prime"
}

def filter_numbers(numbers, **filt):
    result=[]
    for key, value in filt.items():
        if value == "odd":
            for num in numbers:
                if (num % 2) != 0:
                    result.append(num)
        if value == "even":
            for num in numbers:
                if (num % 2) == 0:
                    result.append(num)
        if value == "prime":
            for num in numbers:
                if num > 1:
                    for i in range(2, int(num/2)+1):
                        if (num % i) == 0:
                            break
                    else:
                        result.append(num)
    return result

list=[1,3,6,-5,7,21,23,8,-4,-8,9,15,13]
print(filter_numbers(list, **ODD))
print(filter_numbers(list, **EVEN))
print(filter_numbers(list, **PRIME))