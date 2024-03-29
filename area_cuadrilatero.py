import math

#se tiene que modificar las variables 'a', 'b' y 'e' con los parametros dados
a=6378388.0
b=64665
e=0.00672267002278908

lo_grad_1 = float(input("Ingrese el valor de λ en grados: "))
lo_min_1 = float(input("Ingrese el valor de λ en minutos: "))
lo_seg_1 = float(input("Ingrese el valor de λ en segundos: "))

lo_grad_2 = float(input("Ingrese el valor de λ en grados: "))
lo_min_2 = float(input("Ingrese el valor de λ en minutos: "))
lo_seg_2 = float(input("Ingrese el valor de λ en segundos: "))


la_grad_1 = float(input("Ingrese el valor de ϕ en grados: "))
la_min_1 = float(input("Ingrese el valor de ϕ en minutos: "))
la_seg_1 = float(input("Ingrese el valor de ϕ en segundos: "))

la_grad_2 = float(input("Ingrese el valor de ϕ en grados: "))
la_min_2 = float(input("Ingrese el valor de ϕ en minutos: "))
la_seg_2 = float(input("Ingrese el valor de ϕ en segundos: "))


Longitud_1_decimal = lo_grad_1 + lo_min_1/60 + lo_seg_1/3600
Longitud_2_decimal = lo_grad_2 + lo_min_2/60 + lo_seg_2/3600
Latitud_1_decimal = la_grad_1 + la_min_1/60 + la_seg_1/3600
Latitud_2_decimal = la_grad_2 + la_min_2/60 + la_seg_2/3600

Latitud_1_decimal_rad = Latitud_1_decimal * math.pi / 180
Latitud_2_decimal_rad = Latitud_2_decimal * math.pi / 180
Longitud_1_decimal_rad = Longitud_1_decimal * math.pi / 180
Longitud_2_decimal_rad = Longitud_2_decimal * math.pi / 180


#Calculo area decimales 

calculo_area=b**2 * (Longitud_2_decimal-Longitud_1_decimal) * (((1 / 2) * (math.sin(Latitud_2_decimal) / (1 - e ** 2 * (math.sin(Latitud_2_decimal)**2))) + (1 / (4 * e)) * math.log(abs((e * math.sin(Latitud_2_decimal) + 1) / (e * math.sin(Latitud_2_decimal) - 1))))-((1 / 2) * (math.sin(Latitud_1_decimal) / (1 - e ** 2 * (math.sin(Latitud_1_decimal)**2))) + (1 / (4 * e)) * math.log(abs((e * math.sin(Latitud_1_decimal) + 1) / (e * math.sin(Latitud_1_decimal) - 1)))))

#todo en radianes

calculo_area_radianes=b**2 * (Longitud_2_decimal_rad-Longitud_1_decimal_rad) * (((1 / 2) * (math.sin(Latitud_2_decimal_rad) / (1 - e ** 2 * (math.sin(Latitud_2_decimal_rad)**2))) + (1 / (4 * e)) * math.log(abs((e * math.sin(Latitud_2_decimal_rad) + 1) / (e * math.sin(Latitud_2_decimal_rad) - 1))))-((1 / 2) * (math.sin(Latitud_1_decimal_rad) / (1 - e ** 2 * (math.sin(Latitud_1_decimal_rad)**2))) + (1 / (4 * e)) * math.log(abs((e * math.sin(Latitud_1_decimal_rad) + 1) / (e * math.sin(Latitud_1_decimal_rad) - 1)))))

print ("area en decimales", calculo_area)

print ("area en radaines", calculo_area_radianes)