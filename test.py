from datetime import datetime

timestamp = datetime.now()
am6 = datetime.now().replace(hour=6, minute=0, second=0, microsecond=0)
pm12 = datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
pm18 = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)
am0 = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
print(am6, pm12, pm18, am0)

greeting_text = ''  

if am6 <= timestamp <= pm12:
        greeting_text = f"Доброе утро!"

elif pm12 <= timestamp <= pm18:
        greeting_text = f"Добрый день!"
else:
        print(False)
print(greeting_text)