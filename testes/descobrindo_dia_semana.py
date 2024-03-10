from datetime import date

DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

# primeira forma
dia_atual = date.today()  # O metodo 'today' retorna o dia atual

indice = dia_atual.weekday()
# O metodo 'weekday' deve ser usado em um data e retorna um indice para o dia da semana (0-6)
# e pordemos usar esse indice para lisata de dias 'DIAS'

dia_atual = DIAS[indice]
print(dia_atual)

# segunda forma
data = date(day=9, month=3, year=2024)
indice_da_semana = data.weekday()
dia_da_semana = DIAS[indice_da_semana]
print(dia_da_semana)
