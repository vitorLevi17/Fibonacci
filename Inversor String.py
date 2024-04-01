def inverter_string(s):
    caracteres = list(s)


    caracteres_reversos = []
    for i in range(len(caracteres) - 1, -1, -1):
        caracteres_reversos.append(caracteres[i])

    string_reversa = ''.join(caracteres_reversos)

    return string_reversa


string_original = "O Brasil é o pais do futebol"
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)