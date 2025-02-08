def volume_of_sphere(radius):
    v_sphere = 4/3*3.14*radius**3
    return v_sphere 

def main():
    radius = int(input("Enter the radius: "))
    result = volume_of_sphere(radius)
    print("The volume of a sphere is:", result)
if __name__ == "__main__":
    main()