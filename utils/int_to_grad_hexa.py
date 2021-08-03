import colorsys


def int_to_grad_hexa(nb_value: int):
    maxi = 280
    grad = []
    for i in range(nb_value):
        v = (i + 1) * maxi / nb_value
        if v > maxi:
            v = maxi
        v = v / 360
        rgb = colorsys.hsv_to_rgb(v, 1, 1)
        hexa = "".join("%02X" % round(i * 255) for i in rgb)
        hexa = '#' + hexa
        grad.append(hexa)
    return grad