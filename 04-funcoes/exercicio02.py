def inverter_numero(n):
    try:
        print (int(str(n)[::-1]))
    except ValueError:
        print('Digite um número válido.')

inverter_numero(321)
