#Use an import statement to import statsmodels
import statsmodels

#MYSTERY OF BAYES' KIDNAPPING!
#Filing a missing puppy report, which name is Bayes

bayes_age = 4.0 #Define a variable called bayes_age
print(bayes_age) #Display the variable bayes_age

favorite_toy = "Mr. Squeaky" #His favorite toy

import pandas as pd #Import pandas
r = pd.read_csv('ransom.csv') #Load the 'ransom.csv' into a DataFrame
print(r)
#variable plate represents the observed license plate: the first three letters were FRQ, 
#but the witness couldn't see the final 4 letters
plate = 'FRQ****' #Use * to represent the missing four letters
lookup_plate(plate)
      #result 
      #Fred Frequentist
      #John W. Tukey
      #Ronald Aylmer Fisher
      #Karl Pearson
      #Gertrude Cox
      #Kirstine Smith
#use color of the car to get smaller list      
lookup_plate(plate, color='Green') #it also accepts a keyword arguments
      #result Fred Frequentist
            #Ronald Aylmer Fisher
            #Gertrude Cox
            #Kirstine Smith
#LOADING DATA IN PANDAS            
#some of them made suspicious purchases before the kidnapping!
credit_records = pd.read_csv("credit_records.csv") #creditcard records are in csv
credit_records.head()
print(credit_records.head()) #display first five rows

print(credit_records.info()) #to see how many rows are in this Dataframe
#There are 104 rows in the Dataframe

items = credit_records['item'] #selecting items from credit_records
#OR
items = credit_records.item #selecting item using dot notation

print(mpr.info()) #Inspect the Dataframe mpr using info

print(height_inches > 70) #height_inches represents the height of a suspect
print(plate1 == "FRQ123") #plate1 represents a license plate number of a suspect
print(fur_color != "brown") #fur_color represents the color of Bayes' fur

#anyone of them recently purchased dog treats in kidnapping
purchase = credit_records[credit_records.location == 'Pet Paradise'] #those who visited 'Pet Paradise'
#Fred Frequentist and Gertrude Cox

#PLOTTING DATA WITH MATPLOTLIB
from matplotlib import pyplot as plt
#Officer Deshaun has created DataFrames called "deshaun" to track amount of time he spent working on this case.
#this DataFrame has two columns: day_of_week, hours_worked

plt.plot(deshaun.day_of_week, deshaun.hours_worked) #officer's working hours
plt.show() #diplay plot

#Two other officers have been working with Deshaun, help to find "Bayes(a dog)"
#names are Officer Mengfei and Officer Aditya
plt.plot(aditya.day_of_week, aditya.hours_worked)
plt.plot(mengfei.day_of_week, mengfei.hours_worked)
plt.show()

#Add Labels
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')
plt.legend()  #command to make the legend display
plt.show

#DataFrames which are "suspect1" contains the letter frequencies for the sample from Fred Frequentist,
#"suspect2" contains the letter frequencies for the sample from Gertrude Cox.
plt.plot(suspect1.letter, suspect1.frequency, label='Fred Frequentist')
plt.plot(suspect2.letter, suspect2.frequency, label='Gertrude Cox')
plt.xlabel("Letter")
plt.ylabel("Frequency")
plt.legend()
plt.show()

#DIFFERENT TYPES OF PLOTS
#BAR CHART
print(hours) #DataFrame "hours"
plt.bar(hours.officer, hours.avg_hours_worked,
        #Add error bars
        yerr=hours.std_hours_worked)
plt.show()
#split out the average hours worked per week into desk_work and field_work
plt.bar(hours.officer, hours.desk_work, label = 'Desk Work')
plt.show()

#Comparing two bars!
plt.bar(hours.officer, hours.desk_work, label = 'Desk Work')
plt.bar(hours.officer, hours.field_work, bottom = hours.desk_work, label='Field Work')
plt.legend()
plt.show()

#HISTOGRAM
plt.hist(puppies.weight)
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')
plt.show()

plt.hist(puppies.weight, bins=50) #add bins
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')
plt.show()

plt.hist(puppies.weight, range=(5, 35)) #add range
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')
plt.show()

#A shoe print at the crime scene contains a specific type of gravel
#The radii of individual gravel pieces has been loaded into the DataFrame gravel
plt.hist(gravel.radius) #Dataframe "gravel"
plt.show()
#Modify Histogram
plt.hist(gravel.radius, bins=40, range=(2, 8))
plt.show() #display histogram

#Normalizing Histogram
#so that the sum of the bins adds to 1.
plt.hist(gravel.radius,
         bins=40,
         range=(2, 8),
         density=True)
plt.show()
#add labels
plt.xlabel('Gravel Radius (mm)')
plt.ylabel('Frequency')
plt.title('Sample from Shoeprint')

#KIDDNAPER WAS FREDDY FREQUENTIST!
