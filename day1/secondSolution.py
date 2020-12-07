def solution ():
    list = None
    with open ('./input.txt','r') as f:
        list = [int(x.strip('\n')) for x in f]
    list.sort()
    for x in list:
        for y in list:
            for z in list:
                if x + y + z == 2020:
                    print(f"x is {x} y is {y} z is {z} the answer is {x*y*z}")
                    return

            
solution()