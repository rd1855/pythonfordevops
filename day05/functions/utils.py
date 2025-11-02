def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

if __name__ == "__main__":
    result = check_even_odd(10)
    print(result)