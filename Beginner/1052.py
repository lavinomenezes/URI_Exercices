import datetime
X = int(input())
month = datetime.datetime(2000,X,1)
print(month.strftime("%B"))