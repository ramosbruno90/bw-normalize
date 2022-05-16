from normalize.dates.dates import NormalizeDates

data = "20/03/1990"
# data = "20-03-1990"
# data = "March 3rd, 1990"
# data = "20 de março de 1990"
norm = NormalizeDates()

print(norm.normalize(data))
