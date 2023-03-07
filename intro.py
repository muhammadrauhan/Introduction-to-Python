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
#answers Fred Frequentist and Gertrude Cox
