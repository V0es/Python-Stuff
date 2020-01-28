from math import sqrt

DOTS = []
vectors = []

def vector():
    basic_dot = DOTS[0]
    for j in range(1, 8):
        vec = sqrt((DOTS[j][0] - basic_dot[0])**2 + (DOTS[j][1] - basic_dot[1])**2 + (DOTS[j][2] - basic_dot[2])**2)
        vectors.append(vec)


for i in range(8):
    x, y, z = map(float, input().split())
    DOTS.append((x, y, z))

vector()
vectors.sort()

main_diag = vectors[-1]
st_side = vectors[0]
scnd_side = vectors[1]
rd_side = sqrt(main_diag**2 - st_side**2 - scnd_side**2)

volume = st_side*scnd_side*rd_side
print(volume)