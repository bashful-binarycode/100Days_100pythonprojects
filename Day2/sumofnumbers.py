def sumof(a:str):
    nums = [int(i) for i in a]
    final = 0
    for _ in nums:
        final += _
    return final

print(sumof('1234567890'))
