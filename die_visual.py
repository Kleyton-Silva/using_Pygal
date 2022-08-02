from die import Die


# Cria um daado de 6 lados
die = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)
