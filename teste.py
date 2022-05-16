from normalize.dates.convert_dates import ConvertDates
from normalize.dates.normalize_dates import NormalizeDates

# data = "20/03/1990"
# data = "20-03-1990"
# data = "March 30th, 1990"
# data = "20 de MARÇO de 1990"
data = "1990-03-20"
norm = NormalizeDates()
format = "full_us"
conv = ConvertDates()
# print(norm.normalize(data))
print(conv.convert(data, format="full_us"))

# /br = 20/03/1990
# -us = 20-03-1990
# full_br = 20 de março de 1990
# full_us = March 30th, 1990
