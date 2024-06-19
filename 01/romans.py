def int_to_roman(num):
    if not isinstance(num, int):
        raise ValueError("O valor deve ser um número inteiro.")
    if num < 1 or num > 3999:
        raise ValueError("O valor deve estar entre 1 e 3999.")
    
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    resultado = ''
    
    for valor, simbolo in valores:
        while num >= valor:
            resultado += simbolo
            num -= valor
    
    return resultado

def roman_to_int(s):
    if not isinstance(s, str):
        raise ValueError("O valor deve ser uma string representando um numeral romano.")
    
    simbolos = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
    }
    
    i = 0
    total = 0
    
    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in simbolos:
            total += simbolos[s[i:i+2]]
            i += 2
        else:
            total += simbolos[s[i]]
            i += 1
    
    return total

print(int_to_roman(3999))  # Deve retornar "MCMXCIV"
print(roman_to_int("MMMCMXCIX"))  # Deve retornar 1994
