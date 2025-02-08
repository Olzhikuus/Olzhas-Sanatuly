def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return None

def main():
    num_heads = int(input("Enter the number of heads: "))
    num_legs = int(input("Enter the number of legs: "))

    result = solve(num_heads, num_legs)
    if result:
        chickens, rabbits = result
        print("Number of chickens:", chickens)
        print("Number of rabbits:", rabbits)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()