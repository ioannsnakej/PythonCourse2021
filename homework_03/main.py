def get_simple(*numbers):
    results=[]
    for num in numbers:
        if num > 1:
            for i in range(2, int(num / 2) + 1):
                if (num % i) == 0:
                    break
            else:
                results.append(num)
    return results

print(get_simple(-3,-7,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,-5))

def get_symbol(strings):
    list_of_symbols =[]
    for symbol in strings:
        if symbol in list_of_symbols:
            continue
        list_of_symbols.append(symbol)
    return list_of_symbols

print(get_symbol("Если ты чувствуешь, что сдаешься, вспомни, ради чего ты держался все это время"))