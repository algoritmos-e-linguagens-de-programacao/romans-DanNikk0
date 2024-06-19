def int_to_roman(numero):
   
    if not isinstance(numero, int):
        raise ValueError
    if numero < 1 or numero > 3999:
        raise ValueError
    
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    resultado = '' 

    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    
    return resultado

def contar_em_romano(limite):
  
    for numero in range(1, limite + 1):
        romano = int_to_roman(numero)
        print(f"{numero}: {romano}")

contar_em_romano(3999)
