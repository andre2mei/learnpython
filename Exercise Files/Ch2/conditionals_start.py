#
# Example file for working with conditional statements
#


from re import X


def main():
    x, y = 990, 100

    # conditional flow uses if, elif, else
    if (x < y):
        st = "x is less than y"
    elif (x == y):
        st = "x is equal y"
    else:
        st = "x is greater than y"
    
    print(st)
    # conditional statements let you use "a if C else b"
    st ="x is less then y" if (x<y) else "x is greater than y or the same"
    print(st) 

if __name__ == "__main__":
    main()
