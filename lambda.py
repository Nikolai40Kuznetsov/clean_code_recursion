# Yusupov

import sys


sys.set_int_max_str_digits(666666)
# Lambda-function
func = lambda x: pow(pow(pow(x,x),x),x)


# Main function
def main():
    print(func(100))

if __name__ == "__main__":
    main()