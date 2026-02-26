def fibonacci(n, dic = {}):
    if n == 0:
        dic = {}
        dic[0] = 0
        return 0
    if n == 1:
        dic[1] = 1
        return 1
    if n in dic:
        return dic[n]
    dic[n] =  fibonacci(n-1, dic) + fibonacci(n-2, dic)
    return dic[n]
    