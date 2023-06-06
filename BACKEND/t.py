from datetime import datetime


x = str(datetime.utcnow().isoformat())
y = datetime.utcnow().isoformat()

print(x == y)
