# Yusupov
# Take a number from user and print the Pascal's triangle of this level

# Draving function
def Packals_triangle(n):
    if n == 1:
        return [[1]] 
    else:
        result = Packals_triangle(n-1) 
        current_row = [1]
        previous_row = result[-1] 
        for i in range(len(previous_row)-1):
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]
        result.append(current_row)
        return result
    

# Main function
def main():
    level = input("Введите уровень треугольника Паскаля ")
    triangle = Packals_triangle(int(level))
    for row in triangle:
        print(row)

if __name__ == "__main__":
    main()