from __future__ import division
import csv
import math
import sys

#Calculating prior probability for the given dataset
def prior():
	global Tab_len, count_yes, count_no, prob_yes, prob_no	
	Tab_len = len(weather_PlayTennis)
	for i in range(len(weather_PlayTennis)):
		if weather_PlayTennis[i]==1: count_yes = count_yes+1
		elif weather_PlayTennis[i]==0: count_no = count_no+1
	prob_yes = count_yes/Tab_len
	prob_no = count_no/Tab_len



#Calculating count for the weather dataset
def count_calc(outlook, temp, hum, wind, PlayTennis):
	global countsunny0, countsunny1, countoc0, countoc1, countrain0, countrain1
	global totalsunny, totaloc, totalrain	
	countsunny0, countsunny1, countoc0, countoc1, countrain0, countrain1 = 0,0,0,0,0,0
	totalsunny, totaloc, totalrain = 0,0,0
	for i in range(len(outlook)):
		if outlook[i]==1 and PlayTennis[i]==0: countsunny0 += 1  
		elif outlook[i]==1 and PlayTennis[i]==1: countsunny1 += 1
		if outlook[i]==2 and PlayTennis[i] == 0: countoc0+=1
		elif outlook[i]==2 and PlayTennis[i] == 1: countoc1+=1
		if outlook[i]==3 and PlayTennis[i]==0:countrain0+=1
		elif outlook[i]==3 and PlayTennis[i]==1: countrain1+=1

	totalsunny = countsunny0 + countsunny1
	totaloc = countoc0 + countoc1
	totalrain = countrain0 + countrain1


	global countcool0, countcool1, countmild0, countmild1, counthot0, counthot1
	global totalcool, totalmild, totalhot	
	
	countcool0, countcool1, countmild0, countmild1, counthot0, counthot1 = 0,0,0,0,0,0
	totalcool, totalmild, totalhot = 0,0,0
	for i in range(len(temp)):
		if temp[i]==1 and PlayTennis[i]==0: countcool0 += 1  
		elif temp[i]==1 and PlayTennis[i]==1: countcool1 += 1
		if temp[i]==2 and PlayTennis[i] == 0: countmild0 +=1
		elif temp[i]==2 and PlayTennis[i] == 1: countmild1 +=1
		if temp[i]==3 and PlayTennis[i]== 0: counthot0 += 1
		elif temp[i]==3 and PlayTennis[i]==1: counthot1 += 1

	totalcool = countcool0 + countcool1
	totalmild = countmild0 + countmild1
	totalhot = counthot0 + counthot1



	global countnor0, countnor1, counthigh0, counthigh1
	global totalnor, totalhigh
	
	countnor0, countnor1, counthigh0, counthigh1=0,0,0,0
	totalnor, totalhigh = 0,0
	for i in range(len(hum)):
		if hum[i]==1 and PlayTennis[i]==0: countnor0 += 1  
		elif hum[i]==1 and PlayTennis[i]==1: countnor1 += 1
		if hum[i]==2 and PlayTennis[i] == 0: counthigh0+=1
		elif hum[i]==2 and PlayTennis[i] == 1: counthigh1+=1

	totalnor = countnor0 + countnor1
	totalhigh = counthigh0 + counthigh1
	


	global countweak0, countweak1, countstrong0, countstrong1
	global totalweak, totalstrong

	countweak0, countweak1, countstrong0, countstrong1 = 0,0,0,0
	totalweak, totalstrong  = 0,0

	for i in range(len(wind)):
		if wind[i]==1 and PlayTennis[i]==0: countweak0 += 1  
		elif wind[i]==1 and PlayTennis[i]==1: countweak1 += 1
		if wind[i]==2 and PlayTennis[i] == 0: countstrong0+=1
		elif wind[i]==2 and PlayTennis[i] == 1: countstrong1+=1

	totalweak = countweak0 + countweak1
	totalstrong = countstrong0 + countstrong1


#Calculating the conditional probability for the weather dataset
def cond_prob():
	global prob_sunny0, prob_sunny1, prob_oc0,prob_oc1, prob_rain0, prob_rain1, prob_cool0, prob_cool1, prob_mild0, prob_mild1, prob_hot0,prob_hot1, prob_normal0,prob_normal1, prob_high0,prob_high1, prob_weak0,prob_weak1, prob_strong0,prob_strong1

	prob_sunny0 = countsunny0/count_no
	prob_sunny1 = countsunny1/count_yes

	prob_oc0 = countoc0/count_no
	prob_oc1 = countoc1/count_yes

	prob_rain0 = countrain0/count_no
	prob_rain1 = countrain1/count_yes

	prob_cool0 = countcool0/count_no
	prob_cool1 = countcool1/count_yes

	prob_mild0 = countmild0/count_no
	prob_mild1 = countmild1/count_yes

	prob_hot0 = counthot0/count_no
	prob_hot1 = counthot1/count_yes
	
	prob_normal0 = countnor0/count_no
	prob_normal1 = countnor1/count_yes

	prob_high0 = counthigh0/count_no
	prob_high1 = counthigh1/count_yes
	
	prob_weak0 = countweak0/count_no
	prob_weak1 = countweak1/count_yes

	prob_strong0 = countstrong0/count_no
	prob_strong1 = countstrong1/count_yes

#Determining the best case based on the Naive Bayes Classifier value to make the prediciton
def bestCase(arg1, arg2, arg3, arg4):
	if arg1 == 'sunny' or arg1 =='Sunny' or arg1=='SUNNY':
		param10 = prob_sunny0 
		param11 = prob_sunny1
	elif arg1 == 'Overcast' or arg1 == 'overcast' or arg1 == 'OVERCAST':
		param10= prob_oc0
		param11 = prob_oc1
	elif arg1 == 'Rain' or arg1 == 'rain' or arg1 == 'RAIN':
		param10= prob_rain0
		param11 = prob_rain1
	elif arg1 == 'cool' or arg1 =='Cool' or arg1=='COOL':
		param10 = prob_cool0 
		param11 = prob_cool1
	elif arg1 == 'Mild' or arg1 == 'mild' or arg1 == 'MILD':
		param10= prob_mild0
		param11 = prob_mild1
	elif arg1 == 'Hot' or arg1 == 'hot' or arg1 == 'HOT':
		param10= prob_hot0
		param11 = prob_hot1
	elif arg1 == 'Normal' or arg1 =='NORMAL' or arg1=='normal':
		param10 = prob_normal0 
		param11 = prob_normal1
	elif arg1 == 'High' or arg1 == 'high' or arg1 == 'HIGH':
		param10= prob_high0
		param11 = prob_high1
	elif arg1 == 'Weak' or arg1 =='weak' or arg1=='WEAK'or arg1=='FALSE' or arg1=='False' or arg1 == 'false':
		param10 = prob_weak0 
		param11 = prob_weak1
	elif arg1 == 'Strong' or arg1 == 'strong' or arg1 == 'STRONG'or arg1=='TRUE' or arg1=='True' or arg1 == 'true':
		param10= prob_strong0
		param11 = prob_strong1
#arg2
	if arg2 == 'sunny' or arg2 =='Sunny' or arg2=='SUNNY':
		param20 = prob_sunny0 
		param21 = prob_sunny1
	elif arg2 == 'Overcast' or arg2 == 'overcast' or arg2 == 'OVERCAST':
		param20= prob_oc0
		param21 = prob_oc1
	elif arg2 == 'Rain' or arg2 == 'rain' or arg2 == 'RAIN':
		param20= prob_rain0
		param21 = prob_rain1
	elif arg2 == 'cool' or arg2 =='Cool' or arg2=='COOL':
		param20 = prob_cool0 
		param21 = prob_cool1
	elif arg2 == 'Mild' or arg2 == 'mild' or arg2 == 'MILD':
		param20= prob_mild0
		param21 = prob_mild1
	elif arg2 == 'Hot' or arg2 == 'hot' or arg2 == 'HOT':
		param20= prob_hot0
		param21 = prob_hot1
	elif arg2 == 'Normal' or arg2 =='NORMAL' or arg2=='normal':
		param20 = prob_normal0 
		param21 = prob_normal1
	elif arg2 == 'High' or arg2 == 'high' or arg2 == 'HIGH':
		param20= prob_high0
		param21 = prob_high1
	elif arg2 == 'Weak' or arg2 =='weak' or arg2=='WEAK'or arg2=='FALSE' or arg2=='False' or arg2 == 'false':
		param20 = prob_weak0 
		param21 = prob_weak1
	elif arg2 == 'Strong' or arg2 == 'strong' or arg2 == 'STRONG'or arg2=='TRUE' or arg2=='True' or arg2 == 'true':
		param20= prob_strong0
		param21 = prob_strong1	

#arg3
	if arg3 == 'sunny' or arg3 =='Sunny' or arg3=='SUNNY':
		param30 = prob_sunny0 
		param31 = prob_sunny1
	elif arg3 == 'Overcast' or arg3 == 'overcast' or arg3 == 'OVERCAST':
		param30= prob_oc0
		param31 = prob_oc1
	elif arg3 == 'Rain' or arg3 == 'rain' or arg3 == 'RAIN':
		param30= prob_rain0
		param31 = prob_rain1
	elif arg3 == 'cool' or arg3 =='Cool' or arg3=='COOL':
		param30 = prob_cool0 
		param31 = prob_cool1
	elif arg3 == 'Mild' or arg3 == 'mild' or arg3 == 'MILD':
		param30= prob_mild0
		param31 = prob_mild1
	elif arg3 == 'Hot' or arg3 == 'hot' or arg3 == 'HOT':
		param30= prob_hot0
		param31 = prob_hot1
	elif arg3 == 'Normal' or arg3 =='NORMAL' or arg3=='normal':
		param30 = prob_normal0 
		param31 = prob_normal1
	elif arg3 == 'High' or arg3 == 'high' or arg3 == 'HIGH':
		param30= prob_high0
		param31 = prob_high1
	elif arg3 == 'Weak' or arg3 =='weak' or arg3=='WEAK'or arg3=='FALSE' or arg3=='False' or arg3 == 'false':
		param30 = prob_weak0 
		param31 = prob_weak1
	elif arg3 == 'Strong' or arg3 == 'strong' or arg3 == 'STRONG'or arg3=='TRUE' or arg3=='True' or arg3 == 'true':
		param30= prob_strong0
		param31 = prob_strong1
#arg4
	if arg4 == 'sunny' or arg4 =='Sunny' or arg4=='SUNNY':
		param40 = prob_sunny0 
		param41 = prob_sunny1
	elif arg4 == 'Overcast' or arg4 == 'overcast' or arg4 == 'OVERCAST':
		param40= prob_oc0
		param41 = prob_oc1
	elif arg4 == 'Rain' or arg4 == 'rain' or arg4 == 'RAIN':
		param40= prob_rain0
		param41 = prob_rain1
	elif arg4 == 'cool' or arg4 =='Cool' or arg4=='COOL':
		param40 = prob_cool0 
		param41 = prob_cool1
	elif arg4 == 'Mild' or arg4 == 'mild' or arg4 == 'MILD':
		param40= prob_mild0
		param41 = prob_mild1
	elif arg4 == 'Hot' or arg4 == 'hot' or arg4 == 'HOT':
		param40= prob_hot0
		param41 = prob_hot1
	elif arg4 == 'Normal' or arg4 =='NORMAL' or arg4=='normal':
		param40 = prob_normal0 
		param41 = prob_normal1
	elif arg4 == 'High' or arg4 == 'high' or arg4 == 'HIGH':
		param40= prob_high0
		param41 = prob_high1
	elif arg4 == 'Weak' or arg4 =='weak' or arg4=='WEAK' or arg4=='FALSE' or arg4=='False' or arg4 == 'false':
		param40 = prob_weak0 
		param41 = prob_weak1
	elif arg4 == 'Strong' or arg4 == 'strong' or arg4 == 'STRONG'or arg4=='TRUE' or arg4=='True' or arg4 == 'true':
		param40= prob_strong0
		param41 = prob_strong1


	bestNo = prob_no*param10*param20*param30*param40
	bestYes = prob_yes*param11*param21*param31*param41
	print "\nConditional Probabilities for the attributes\n"
	print "\t\t%s\t\t%s\t\t%s\t\t%s\n" %(arg1,arg2,arg3,arg4)
	print "\tYES\t%.4f\t\t%.4f\t\t%.4f\t\t%.4f\n"%(param11,param21,param31,param41)
	print "\tNO\t%.4f\t\t%.4f\t\t%.4f\t\t%.4f\n\n"%(param10,param20,param30,param40)


	print "Best Case with YES for the attributes = %.4f" % bestYes
	print "Best Case with NO for the attributes = %.4f" % bestNo

	if bestNo>bestYes: print "\n\nPlayTennis is NO with probability %.4f" % bestNo
	elif bestNo<bestYes: print "\n\nPlayTennis is YES with probability %.4f" %bestYes



if len(sys.argv) < 5:
	print "ERROR: python [FILENAME] [ARG1] [ARG2] [ARG3] [ARG4]"
	sys.exit()



weather = csv.DictReader(open('weather.csv', 'rb'), delimiter=',', quotechar='"')

Outlook={'Sunny':1, 'Overcast':2, 'Rain':3}
PlayTennis={'Yes':1, 'No':0}
Temperature={'Cool':1, 'Mild':2, 'Hot':3}
Humidity={'Normal':1, 'High':2}
Wind={'Weak':1, 'Strong':2}


count_yes,count_no = 0, 0
weather_Outlook=[]
weather_PlayTennis=[]
weather_Temp=[]
weather_Humidity=[]
weather_Wind=[]
d={}
for row in weather:
	#print row.keys()
		for k in row.keys():
		#print k		
		#print row[k]
		
			if k=='Outlook':
				weather_Outlook.append(Outlook[row[k]])
			elif k=='PlayTennis':
				weather_PlayTennis.append(PlayTennis[row[k]])			
			elif k=='Temperature':
				weather_Temp.append(Temperature[row[k]])			
			elif k=='Humidity':
				weather_Humidity.append(Humidity[row[k]])			
			else:
				weather_Wind.append(Wind[row[k]])		









arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
arg4 = sys.argv[4]
print "---------------------------------------------------------------------------------"
print "Naive Bayes Classifier for Weather DataSet"
print "=============================================="
prior()
count_calc(weather_Outlook, weather_Temp, weather_Humidity, weather_Wind, weather_PlayTennis)
cond_prob()
bestCase(arg1,arg2,arg3,arg4)
 
print "---------------------------------------------------------------------------------"
