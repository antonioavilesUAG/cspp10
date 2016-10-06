secs = input("What number do you want to convert: ") 
hrs= int(float(secs))/3600
mins = (int(float(secs))/60)%60
secs2 = int(float(secs))%60 
print (str(hrs) + "hours " + str(mins) + "min " + str(secs2) + "seconds ")