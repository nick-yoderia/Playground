import time

start_time = time.perf_counter()

def intersect(a, b):
    (ax0, ax1), (ay0, ay1), (az0, az1) = a
    (bx0, bx1), (by0, by1), (bz0, bz1) = b
    x0, x1 = max(ax0, bx0), min(ax1, bx1)
    y0, y1 = max(ay0, by0), min(ay1, by1)
    z0, z1 = max(az0, bz0), min(az1, bz1)

    # verify the cuboids actually intersect and return a cuboid of that intersection
    if x0 <= x1 and y0 <= y1 and z0 <= z1:
        return ((x0, x1), (y0, y1), (z0, z1))
    return None

def volume(cuboid):
    (x0, x1), (y0, y1), (z0, z1) = cuboid
    return (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1)

commands = []
with open('./input', 'r') as f:
    for line in f:
        state = line.split()[0]
        x_range = line.split()[1].split(',')[0].split('=')[1].split('..')
        y_range = line.split()[1].split(',')[1].split('=')[1].split('..')
        z_range = line.split()[1].split(',')[2].split('=')[1].split('..')
        cuboid = (
            (int(x_range[0]), int(x_range[1])),
            (int(y_range[0]), int(y_range[1])),
            (int(z_range[0]), int(z_range[1]))
        )
        commands.append((state, cuboid))

cuboids = []  # Each entry is a tuple (cuboid, sign)
for state, cuboid in commands:
    additions = []
    for prev_cuboid, sign in cuboids:
        intersection = intersect(prev_cuboid, cuboid)
        if intersection:
            additions.append((intersection, -sign))
    cuboids.extend(additions)
    if state == "on":
        cuboids.append((cuboid, 1))

total_volume = 0
for cuboid, sign in cuboids:
    total_volume += volume(cuboid) * sign

end_time = time.perf_counter()

print("Total volume:", total_volume)
print("Runtime: {:f} seconds".format(end_time - start_time))