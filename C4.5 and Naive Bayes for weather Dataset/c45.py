from __future__ import division
import csv
import math

def entropyS(variable_data): #occupancy is the target
	count0, count1 = 0, 0  # counter for the class0 and class1 in the occupancy column
	total = len(variable_data)
	for i in range(len(variable_data)):
		if variable_data[i] == 0: 
			count0 += 1
		else:  count1 += 1
	p0 = count0 / total 
	p1 = count1 / total
	v0 = math.log(p0, 2) if p0 != 0 else 0  # to avoid log(0)
	v1 = math.log(p1, 2) if p1 != 0 else 0  # to avoid log(0)	
	return -(p0*v0)-(p1*v1)
	


def entropyOut(outlook, PlayTennis):
	global GainRatio_Outlook, Gain_Outlook, SplitInfo_out
	countsunny0, countsunny1, countoc0, countoc1, countrain0, countrain1 = 0, 0, 0, 0, 0, 0
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
	
	sunnyp0 = countsunny0/totalsunny
	sunnyp1 = countsunny1/totalsunny
	sunnyv0=math.log(sunnyp0,2) if sunnyp0 != 0 else 0
	sunnyv1=math.log(sunnyp1,2) if sunnyp1 != 0 else 0
	entropysunny = -(sunnyp0*sunnyv0)-(sunnyp1*sunnyv1)		
		
	ocp0 = countoc0/totaloc
	ocp1 = countoc1/totaloc
	ocv0=math.log(ocp0,2) if ocp0 != 0 else 0
	ocv1=math.log(ocp1,2) if ocp1 != 0 else 0
	entropyoc = -(ocp0*ocv0)-(ocp1*ocv1)

		
		
	rainp0 = countrain0/totalrain
	rainp1 = countrain1/totalrain
	rainv0=math.log(rainp0,2) if rainp0 != 0 else 0
	rainv1=math.log(rainp1,2) if rainp1 != 0 else 0		
	entropyrain = -(rainp0*rainv0)-(rainp1*rainv1)
	TotalData = len(outlook)
	SplitInfo_out = -((totalsunny/TotalData)*(math.log((totalsunny/TotalData),2)))-((totaloc/TotalData)*(math.log((totaloc/TotalData),2)))-((totalrain/TotalData)*(math.log((totalrain/TotalData),2)))
	Gain_Outlook = entropyS(PlayTennis) - ((totalsunny/len(outlook))*entropysunny) - ((totaloc/len(outlook))*entropyoc) - ((totalrain/len(outlook))*entropyrain)		
	
	GainRatio_Outlook = Gain_Outlook/SplitInfo_out	
	return Gain_Outlook



def entropyTemp(temp, PlayTennis):
	global GainRatio_Temp, Gain_temp,SplitInfo_temp
	countcool0, countcool1, countmild0, countmild1, counthot0, counthot1 = 0, 0, 0, 0, 0, 0
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
	
	coolp0 = countcool0/totalcool
	coolp1 = countcool1/totalcool
	coolv0=math.log(coolp0,2) if coolp0 != 0 else 0
	coolv1=math.log(coolp1,2) if coolp1 != 0 else 0
	entropycool = -(coolp0*coolv0)-(coolp1*coolv1)		
		
	mildp0 = countmild0/totalmild
	mildp1 = countmild1/totalmild
	mildv0=math.log(mildp0,2) if mildp0 != 0 else 0
	mildv1=math.log(mildp1,2) if mildp1 != 0 else 0
	entropymild = -(mildp0*mildv0)-(mildp1*mildv1)

		
		
	hotp0 = counthot0/totalhot
	hotp1 = counthot1/totalhot
	hotv0=math.log(hotp0,2) if hotp0 != 0 else 0
	hotv1=math.log(hotp1,2) if hotp1 != 0 else 0		
	entropyhot = -(hotp0*hotv0)-(hotp1*hotv1)
	TotalData = len(temp)
	SplitInfo_temp = - ((totalcool/TotalData)*(math.log((totalcool/TotalData),2)))- ((totalmild/TotalData)*(math.log((totalmild/TotalData),2)))- ((totalhot/TotalData)*(math.log((totalhot/TotalData),2)))
	Gain_temp = entropyS(PlayTennis) - ((totalcool/len(temp))*entropycool) - ((totalmild/len(temp))*entropymild) - ((totalhot/len(temp))*entropyhot)		
	
	GainRatio_Temp = Gain_temp/SplitInfo_temp
		
	return Gain_temp


def entropyHum(hum, PlayTennis):
	global GainRatio_Hum, Gain_hum, SplitInfo_hum
	countnor0, countnor1, counthigh0, counthigh1 = 0, 0, 0, 0
	
	for i in range(len(hum)):
		if hum[i]==1 and PlayTennis[i]==0: countnor0 += 1  
		elif hum[i]==1 and PlayTennis[i]==1: countnor1 += 1
		if hum[i]==2 and PlayTennis[i] == 0: counthigh0+=1
		elif hum[i]==2 and PlayTennis[i] == 1: counthigh1+=1

	totalnor = countnor0 + countnor1
	totalhigh = counthigh0 + counthigh1
	
	norp0 = countnor0/totalnor
	norp1 = countnor1/totalnor
	norv0=math.log(norp0,2) if norp0 != 0 else 0
	norv1=math.log(norp1,2) if norp1 != 0 else 0
	entropynor = -(norp0*norv0)-(norp1*norv1)		
	
		
	
	highp0 = counthigh0/totalhigh
	highp1 = counthigh1/totalhigh
	highv0=math.log(highp0,2) if highp0 != 0 else 0
	highv1=math.log(highp1,2) if highp1 != 0 else 0	
	entropyhigh = -(highp0*highv0)-(highp1*highv1)
	TotalData = len(hum)
	SplitInfo_hum = - ((totalnor/TotalData)*(math.log((totalnor/TotalData),2)))- ((totalhigh/TotalData)*(math.log((totalhigh/TotalData),2)))
	Gain_hum = entropyS(PlayTennis) - ((totalnor/len(hum))*entropynor) - ((totalhigh/len(hum))*entropyhigh)	
	
	GainRatio_Hum = Gain_hum/SplitInfo_hum	
	return Gain_hum


def entropyWind(Wind, PlayTennis):
	global GainRatio_Wind, SplitInfo_wind, Gain_wind
	countweak0, countweak1, countstrong0, countstrong1 = 0, 0, 0, 0
	
	for i in range(len(Wind)):
		if Wind[i]==1 and PlayTennis[i]==0: countweak0 += 1  
		elif Wind[i]==1 and PlayTennis[i]==1: countweak1 += 1
		if Wind[i]==2 and PlayTennis[i] == 0: countstrong0+=1
		elif Wind[i]==2 and PlayTennis[i] == 1: countstrong1+=1

	totalweak = countweak0 + countweak1
	totalstrong = countstrong0 + countstrong1
	
	weakp0 = countweak0/totalweak
	weakp1 = countweak1/totalweak
	weakv0=math.log(weakp0,2) if weakp0 != 0 else 0
	weakv1=math.log(weakp1,2) if weakp1 != 0 else 0
	entropyweak = -(weakp0*weakv0)-(weakp1*weakv1)		
	
		
	
	strongp0 = countstrong0/totalstrong
	strongp1 = countstrong1/totalstrong
	strongv0=math.log(strongp0,2) if strongp0 != 0 else 0
	strongv1=math.log(strongp1,2) if strongp1 != 0 else 0	
	entropystrong = -(strongp0*strongv0)-(strongp1*strongv1)
	TotalData = len(Wind)
	SplitInfo_wind = - ((totalweak/TotalData)*(math.log((totalweak/TotalData),2)))- ((totalstrong/TotalData)*(math.log((totalstrong/TotalData),2)))
	Gain_wind = entropyS(PlayTennis) - ((totalweak/len(Wind))*entropyweak) - ((totalstrong/len(Wind))*entropystrong)	
	
	GainRatio_Wind = Gain_wind/SplitInfo_wind
	return Gain_wind








weather = csv.DictReader(open('weather.csv', 'rb'), delimiter=',', quotechar='"')

Outlook={'Sunny':1, 'Overcast':2, 'Rain':3}
PlayTennis={'Yes':1, 'No':0}
Temperature={'Cool':1, 'Mild':2, 'Hot':3}
Humidity={'Normal':1, 'High':2}
Wind={'Weak':1, 'Strong':2}



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


'''
for i in xrange(len(weather_Outlook)):
	print str(weather_Outlook[i]) +' \t\t '+ str(weather_PlayTennis[i]) +' \t\t '+ str(weather_Temp[i]) +' \t\t '+str(weather_Humidity[i])+' \t\t '+str(weather_Wind[i])
	#S[i] = weather['PlayTennis']	



'''






entropyOut(weather_Outlook, weather_PlayTennis)
entropyS(weather_PlayTennis)
entropyTemp(weather_Temp, weather_PlayTennis)
entropyHum(weather_Humidity, weather_PlayTennis)
entropyWind(weather_Wind, weather_PlayTennis)

print "----------------------------------------------------------------------------"
print "Best Split using C4.5 Algorithm"
print"================================\n"
print "\t\tOUTLOOK\t\tTEMPERATURE\tHUMIDITY\tWIND"
print "Gain\t\t%.4f\t\t%.4f\t\t%.4f\t\t%.4f"%(Gain_Outlook, Gain_temp, Gain_hum, Gain_wind)
print "Split Info\t%.4f\t\t%.4f\t\t%.4f\t\t%.4f"%(SplitInfo_out, SplitInfo_temp, SplitInfo_hum, SplitInfo_wind)
print "Gain Ratio\t%.4f\t\t%.4f\t\t%.4f\t\t%.4f"%(GainRatio_Outlook, GainRatio_Temp, GainRatio_Hum, GainRatio_Wind)
print "\n\n"
print "Gain Ratio for OUTLOOK:%.4f"%GainRatio_Outlook
print "Gain Ratio for TEMPERATURE:%.4f"%GainRatio_Temp
print "Gain Ratio for WIND:%.4f"%GainRatio_Wind
print "Gain Ratio for HUMIDITY:%.4f"%GainRatio_Hum

print "\n"
if GainRatio_Outlook > GainRatio_Temp and GainRatio_Outlook > GainRatio_Wind and GainRatio_Outlook > GainRatio_Hum:print "The first best split for Decision Tree is OUTLOOK with GainRatio=%.4f"%GainRatio_Outlook
elif GainRatio_Temp > GainRatio_Outlook and GainRatio_Temp > GainRatio_Wind and GainRatio_Temp > GainRatio_Hum:print "The first best split for Decision Tree is TEMPERATURE with GainRatio=%.4f"%GainRatio_Temp
elif GainRatio_Wind > GainRatio_Outlook and GainRatio_Wind > GainRatio_Temp and GainRatio_Wind > GainRatio_Hum:print "The first best split for Decision Tree is WIND with GainRatio=%.4f"%GainRatio_Wind
elif GainRatio_Hum > GainRatio_Outlook and GainRatio_Hum > GainRatio_Temp and GainRatio_Hum > GainRatio_Wind:print "The first best split for Decision Tree is HUMIDITY with GainRatio=%.4f"%GainRatio_Hum
print "-----------------------------------------------------------------------------"

