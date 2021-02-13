def pattern():
    item=2
    for i in range (1,4):
        for j in range (1,4):
            print(item, end='')
            item += 2
            print('\n')
if __name__ == "__main__" :
    pattern()