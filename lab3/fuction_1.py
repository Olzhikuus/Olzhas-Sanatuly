def function_to_convert(your_grams):
    ounces = float(your_grams) * 28.3495231
    return ounces
    
def main():
    your_grams = input("Enter the weight in grams: ")
    converted_result = function_to_convert(your_grams)
    print("Result of conversion:", converted_result)

if __name__ == "__main__":
    main()