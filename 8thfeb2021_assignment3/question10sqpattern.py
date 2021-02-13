def pattern():
    print('Square pattern')
    item=9
    for row in range(1,4):
        for column in range(1,4):
            print(item,end= ' ')
            item-=1
        print('\n')
if __name__ == "__main__" :
    pattern()