from datetime import datetime, timedelta

now = datetime.now()
print(f"it is {now } now ")

# this is custom date 

dt = datetime(2025,5,6)
print("custom date",dt)

#  7 days from now
future = now + timedelta(days=7)
print("7 days from now will be ",future)

