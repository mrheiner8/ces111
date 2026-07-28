import math
def main():
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    can_eff(name, radius, height)

    name = "#1 Tall"
    radius = 7.78
    height = 11.91
    can_eff(name, radius, height)

    can_eff("#2",8.73,11.59)

    can_eff("#2.5",10.32,11.91)

    can_eff("#3 Cylinder",10.79,17.78)

    can_eff("#5",13.02,14.29)

    can_eff("#6Z",5.4,8.89)

    can_eff("#8Z short",6.83,7.62)

    can_eff("#10",15.72,17.78)

    can_eff("#211",6.83,12.38)

    can_eff("#300",7.62,11.27)

    can_eff("#303",8.1,11.11)


def can_eff(name, radius, height):
    volume = can_vol(radius, height)
    area = can_area(radius, height)
    eff = volume/area
    print (f"{name}, Volume={volume:.2f}, Area={area:.2f}, Efficiency={eff:.2f}")

def can_vol(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

def can_area(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    return area

main()



"""compute_volume

compute_surface_area"""