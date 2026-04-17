# Parte de Ramiro
# Verificación de código ICD10, suponemos que el codigo siempre es correcto

"""
Variables usadas en esta funcion:
    1. Letra: Refiere a la primera letra del codigo icd10
    2. Bloque: Refiere a la parte siguente del codigo icd10 x## en cullo caso son dos que van despues de la letra, y serian numeros.
    3. Subgrupo: Refiere a que subgrupo pertenece, hasta ahora solo lo uso por si llega a pedir que se use el subgrupo
### (Subgrupo es una variable sin uso) ### 
"""

letra = codigoicd10[0]
Bloque = codigoicd10[1:3]
Subgrupo = codigoicd10[4:]

bloque = int(Bloque)
subgrupo = int(Subgrupo)

if letra == "A" or letra == "B":
    capitulo = "Ciertas enfermedades infecciosas y parasitarias"

elif letra == "C" or letra == "D":
    if letra == "D":
        if bloque <= 48:
            capitulo = "Tumores [neoplasias]"
        else:
            capitulo = "Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan el mecanismo de la inmunidad"
    else:
        capitulo = "Tumores [neoplasias]"

elif letra == "E":
    capitulo =  "Enfermedades endocrinas, nutricionales y metabólicas"

elif letra == "F":
    capitulo = "Trastornos mentales y del comportamiento"

elif letra == "G":
    capitulo = "Enfermedades del sistema nervioso"

elif letra == "H":
    if bloque <= 59:
        capitulo = "Enfermedades del ojo y sus anexos"
    else:
        capitulo = "Enfermedades del oído y de la apófisis mastoides"

elif letra == "I":
    capitulo = "Enfermedades del sistema circulatorio" 

elif letra == "J":
    capitulo = "Enfermedades del sistema respiratorio"

elif letra == "K":
    capitulo = "Enfermedades del sistema digestivo"

elif letra == "L":
    capitulo = "Enfermedades de la piel y del tejido subcutáneo"

elif letra == "M":
    capitulo = "Enfermedades del sistema osteomuscular y del tejido conjuntivo"

elif letra == "N":
    capitulo = "Enfermedades del sistema genitourinario"

elif letra == "O":
    capitulo =  "Embarazo, parto y puerperio"

elif letra == "P":
    capitulo = "Ciertas afecciones originadas en el período perinatal"

elif letra == "Q":
    capitulo = "Malformaciones congénitas, deformidades y anomalías cromosómicas"

elif letra == "R":
    capitulo = "Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte"

elif letra == "S" or letra == "T":
    capitulo = "Traumatismos, envenenamientos y algunas otras consecuencias de causas externas" 

elif letra == "V" or letra == "W" or letra == "X" or letra == "Y":
    capitulo = "Causas externas de morbilidad y de mortalidad"

elif letra == "Z":
    capitulo = "Factores que influyen en el estado de salud y contacto con los servicios de salud"

else:
    capitulo = "Códigos para propósitos especiales"

monto_fijo = monto_base + 25000

if letra == "U":
    monto_parcial = monto_fijo + 100000
    
elif "A" <= letra <= "L":
    monto_parcial = monto_fijo + 25000
    
else "M" <= letra <= "Z":
    monto_parcial = monto_fijo + 40000
