
from currency import NormalizeCurrency

# money = " R$ 5.000,00"
# money = " R$5000,00"
# money = " R$5,000,000"
money = " $5000.00"

normalize_currency = NormalizeCurrency(locale="en_US")
result = normalize_currency.normalize_currency(money)

print(result)
