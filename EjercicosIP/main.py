IP = '148.216.188.199/18'

subnet_mask = [0, 0, 0, 0]
ip_address = [0, 0, 0, 0]

sufijo = 0


def mascara_subred(ip):
    global subnet_mask, sufijo
    unos = []
    sufijo = ip[ip.find('/')+1:]
    if int(sufijo) <= 32:
        for _ in range(int(sufijo)):
            unos.append(1)
        if len(unos) < 32:
            for _ in range(32-len(unos)):
                unos.append(0)
        subnet_mask[0] = int(''.join(map(str, unos[:8])), 2)
        subnet_mask[1] = int(''.join(map(str, unos[8:16])), 2)
        subnet_mask[2] = int(''.join(map(str, unos[16:24])), 2)
        subnet_mask[3] = int(''.join(map(str, unos[24:])), 2)

    print(subnet_mask)
    # Bin a Dec int(mask1,2)
    # Dec a Bin format(num,'b')


def octetos(ip):
    global ip_address
    puntos = []

    for pos, char in enumerate(ip):
        if char == '.':
            puntos.append(pos)

    ip_address[0] = ip[:puntos[0]]
    ip_address[1] = ip[puntos[0]+1:puntos[1]]
    ip_address[2] = ip[puntos[1]+1:puntos[2]]
    ip_address[3] = ip[puntos[2]+1:ip.find('/')]
    print(ip_address)


def redes(sufijo):
    num_redes = 2**(int(sufijo) % 8)

    subred = ''

    print()


def main():
    mascara_subred(IP)
    octetos(IP)
    redes(sufijo)


if __name__ == '__main__':
    main()
