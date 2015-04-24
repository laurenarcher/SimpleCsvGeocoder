import csv
import time
from pygeocoder import Geocoder

#A super simple python .csv geocoder
#You can geocode up to 2500 properties a day (per IP Address)
#Upload the resulting newfile.csv to Google Fusion Tables for an instant google map.

input_file = open('file.csv', 'r') #Open your .csv file
output_file = open('newfile.csv', 'w') #Make an empty .csv This is where your geocodes will end up.
data = csv.reader(input_file)

def csvGeocoder(data):
    for line in data:
        [StreetNumber,Street,City,Province,Country,FullAddress,OtherField,OtherField2,Whatever] = line #Make sure the number of columns matches/aligns with the number of fields listed here.
        if City == "City": #This skips the header. Don't geocode the header :D
            Latitude = ["Latitude"]
            Longitude = ["Longitude"] 
            new_line = line + Latitude + Longitude #This adds two new columns to your .csv, Latitude and Longitude.
            csv.writer(output_file).writerow(new_line)
            print new_line # This isn't required. I just like to watch.
        else:
            #I use a column with the Full Address (Street Number, Street, City, Provice/State, Country) But you could concatenate from multiple fields too.
            results = Geocoder.geocode(FullAddress)
            Latitude = [results.coordinates[0]] 
            Longitude = [results.coordinates[1]]
            new_line = line + Latitude + Longitude
            csv.writer(output_file).writerow(new_line)
            time.sleep(.21) #This throttles your requests. The GoogleAPI doesn't like too many requests per second.
            print new_line #Printing to the console makes the process a lot longer. Omit for speed.
    
    del url,City,Address,Ward,Status,ListDate,IntentionDate,ByLaw,PartIVDate,PartVDate,HeritageDistrict,DistrictStatus,HeritageEasement,RegistrationDate,BuildingType,ArchitectBuilder,ConstructionYear,Province,Country,FullAddress,Details,DemoDate,PrimaryAddress, line
    del data

    input_file.close()
    output_file.close()
