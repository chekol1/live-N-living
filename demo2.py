

def show_love(num):
    if num%2 == 0:
        print("is even")
    else:
        print("is not even")


if __name__ == "__main__":
    input1 = int(input("write your number"))
    show_love(input1)