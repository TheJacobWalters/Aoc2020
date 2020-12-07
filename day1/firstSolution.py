def solution ():
    list = None
    with open ('./input.txt','r') as f:
        list = [int(x.strip('\n')) for x in f]
    list.sort()
    for x in list:
        for y in reversed(list):
            if x + y == 2020:
                print(f"x is {x} y is {y} the answer is {x*y}")
                return
            elif (x + y) < 2020:
                break
            
solution()