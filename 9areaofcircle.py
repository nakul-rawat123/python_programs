def area_of_circle(radius):
    area = 3.14159265*(radius**2)
    print(f'area of circle with radius {radius} is {area}')
radii = [2,4,5,7,8,10,20,15,100,50]
for i in radii:
    area_of_circle(i)
    