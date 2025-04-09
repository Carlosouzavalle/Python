# uso basico do datetime

# from datetime import datetime

# date_and_hour = datetime(2025, 4, 7, 9,9,10)

# print(date_and_hour)


#===================timedelta============================

# from datetime import timedelta
# delta =timedelta(days=5, hours=3, minutes=30)
# print(delta)

# Parâmetros que você pode usar:
# days
# seconds
# microseconds
# milliseconds
# minutes
# hours
# weeks



# from datetime import datetime, timedelta

# hoje = datetime.now()
# print("Hoje", hoje)

# daqui_7Dias = hoje + timedelta(days=7)
# print("daqui a: ", daqui_7Dias)






#======================strftime e strptime

# from datetime import datetime

# data_hora_atual = datetime.now()
# data_hora_str = '2025-10-25 05:41'
# mascara_pt_br = '%d/%m/%Y'
# mascara_en  = '%Y-%m-%d %H:%M'


# print(data_hora_atual.strftime(mascara_pt_br))

# print(datetime.strptime(data_hora_str, mascara_en))



#=======================timezone

import pytz
from datetime import datetime

data = datetime.now(pytz.timezone('Japan'))
data2 = datetime.now(pytz.timezone('America/Sao_Paulo'))

print(data)
print(data2)