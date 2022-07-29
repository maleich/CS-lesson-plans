def circle_info(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return (c, a)

radius = float(input('Enter a radius: '))
output = circle_info(radius)
print(output)

circumference = output[0]
area = output[1]
print(f'The circumference is {circumference}.')
print(f'The area is {area}.')