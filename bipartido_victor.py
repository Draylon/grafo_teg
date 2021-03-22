import numpy as np

# F familias com varios integrantes, N carros com M vagaas
# cada carro so pode levar 1 pessoa de cada familia

# Numero de familias
# Numero de integrantes de cada familia
# Numero de Carros
# Numero de vagas em cada carro

# familia 0 = 2 integrantes, 1 = 3 etc..
familias = [2, 3, 3, 9]
# 3 veiculos com 4, 5, 5 lugares disponiveis respectivamente
veiculos = [2, 7, 3, 4]

'''
par_veiculo = {0: [0, 1, 2]}  # familia -> [1,2,5]
par_veiculo = {0: [0, 1, 2]}
'''

# Fazer no formato de matriz mesmo

total_familias = len(familias)
total_veiculos = len(veiculos)

par = np.zeros((total_familias, total_veiculos))
'''
count_aux = 0
for i in range(total_veiculos):
    for j in range(total_familias):
        if count_aux < total_veiculos and par[count_aux][j] == 0:
            if familias[j] != 0 and veiculos[i] != 0:
                par[i][j] = 1
                familias[j] = familias[j] - 1
                veiculos[i] = veiculos[i] - 1
                count_aux += 1
        else:
            break;
'''

count_aux = 0
for i in range(total_familias):
    for j in range(total_veiculos):
        if par[i][j] == 0:
            if familias[i] != 0 and veiculos[j] != 0:
                par[i][j] = 1
                familias[i] = familias[i] - 1
                veiculos[j] = veiculos[j] - 1
        else:
            break

print(familias, veiculos)
print(f' Matriz resultado: \n {par}')

count_family = 0
for i in range(total_familias):
    if familias[i] != 0:
        count_family += 1
        break

if count_family == 0:
    print("Alocado uma pessoa por familia nos carros")
else:
    print("Não foi possivel alocar uma pessoa por familia nos carros")
