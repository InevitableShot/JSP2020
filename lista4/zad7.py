def pascal(n):
    row = [1]
    y = [0]
    for _ in range(n):
        print(row)
        row=[left+right for left,right in zip(row+y, y+row)]
pascal(11)