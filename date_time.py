from datetime import datetime , timedelta
#today's time
today = datetime.now()
print("today is " + str(today))
one_day = timedelta(days=1)
#yest time
yest= today - one_day
print('yest was '+ str(yest))
#birthday
birthday = input("Enter your birthday in dd/mm/yy format: ")
date = datetime.strptime(birthday, "%d/%m/%Y")
print ("your birthday is on " + str(date) )