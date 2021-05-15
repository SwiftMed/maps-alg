
#random patients
from faker import Faker 
fake = Faker()
import random


from faker import Faker

#Format 

# [Hospital name, patients, address, Doctor Available]


class Data:

    def data(self):
        random_num_hospitals = random.randint(1, 20)
        #address_counter = random_num_hospitals
        

        hospitals = []

        for i in range(random_num_hospitals):
            doctor = fake.name()
            patients = random.randint(1, 500)
            lat = random.uniform(-50, 70)
            longitude = random.uniform(-50, 70)
            hospital_name = 'Hospital ' + str(i)
            elm = [hospital_name, patients, fake.address(), doctor, longitude, lat]
            hospitals.append(elm)
        
        return hospitals 

        


test = Data()

test2 = test.data()

