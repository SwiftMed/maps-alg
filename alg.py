
from test_data import test2

#import gps 
import os
import webbrowser
import gmplot 
import geocoder 
import test_data


coordinates = []
def linear_search(lst, target):
    matches = []
    for i in test2:
        if target in i:
            matches.append(i)
    matches_real = matches
    if len(matches) > 0:
        for j in matches:
            name = j[0]
            patients = j[1]
            address = j[3]
            lat = j[-2]
            longitude = j[-1]
            coordinate = [lat, longitude]
            coordinates.append(coordinate)
            print("""
            Hospital: {name} 
            Patients: {patients}
            Address: {address}
            Coordinates: {lat}, {long}
            """.format(name=name, patients=patients, address=address, lat=lat, long=longitude))     




# Calling all the existing stuffs

def initializer():
    numbers = []
    hospitals = test2
    for i in hospitals:
        for j in i:
            if type(j) == int:
                numbers.append(j)
    return numbers


def radix_sort(lst):
    max_value = max(lst)
    max_exponent = len(str(lst))
    being_sorted = lst[:]

    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position 
        digits = [ [] for i in range(10)]

        for number in being_sorted:
            string_number = str(number)
            try:
                digit = string_number[index]
            except IndexError:
                digit = 0 
            
            digit = int(digit)
            digits[digit].append(number)
            being_sorted = []
            for numeral in digits:
                being_sorted.extend(numeral)
            
    
    return being_sorted[0]

        



                

def test(lst):
    target = radix_sort(initializer())
    linear_search(lst, target)



def user_interaction():
    prompt = input("Would you like to see a clinic or a hospital? ")
    playing = True 
    while playing:
        if prompt == "clinic":
            print('Hello there! We are finding the nearest hospital/clinic to you...')
            final_output = test(initializer())
            print(final_output)
            get_map()
            
            
            break
        
        elif prompt == "hospital":
            final_output = test(initializer())
            print(final_output)
            get_map()
            
            break

        elif prompt == "/quit":
            break

        else:
            print("That request is unavailable! ")


def get_map():
    ipadress=geocoder.ip('me')
    #print(ipadress.latlng)
    lst = ipadress.latlng

    personal_lat = lst[0]
    personal_long = lst[-1]
    lat = [personal_lat]
    lang = [personal_long]
    
    
    for i in coordinates:
        for j in range(len(i)):
            if j == 0:
                hospital_lat = i[j]
                lat.append(hospital_lat)
            elif j == 1:
                hospital_long = i[j]
                lang.append(hospital_long) 


    gmapOne = gmplot.GoogleMapPlotter(lat[0], lang[0], 15)

    gmapOne.scatter(lat, lang, '#ff000', size=50, marker=False)
    gmapOne.plot(lat,lang,'blue', edge_width=2.5)
    gmapOne.draw("map.html")



#test = get_map()





user_interaction()




