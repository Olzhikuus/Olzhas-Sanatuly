def converting_to_centigrade(temperature):
    centigrade = (5 / 9) * (temperature - 32)
    return centigrade

def main():
    temperature_in_F = int(input("Fahrenheit: "))
    result = converting_to_centigrade(temperature_in_F)
    print("The equivalent Centigrade temperature: ", result)

if __name__ == "__main__":
    main()