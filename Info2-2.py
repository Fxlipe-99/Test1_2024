VLAN = int(input("Ingrese el rango de VLAN: "))
if VLAN >= 1 and VLAN <= 1005:
    print("Esta es una VLAN de rango normal.")
elif VLAN >=1006 and VLAN <= 4095:
    print("Esta es una VLAN de rango extendido")
else:
    print("Esta VLAN no es normal ni extendida.")

