from datetime import datetime, timedelta
presentday = datetime.now() 
yesterday = presentday - timedelta(1)
tomorrow = presentday + timedelta(1)
day_after = presentday + timedelta(2)
print("Yesterday = ", yesterday.strftime('%d-%m-%Y'))
print("Today = ", presentday.strftime('%d-%m-%Y'))
print("Tomorrow = ", tomorrow.strftime('%d-%m-%Y'))
print("day after = ", day_after.strftime('%d-%m-%Y'))
