from sdr_availability import *

print("################################################################################################################## \n" + 
    "Welcome to Ena Vu's SDR availability meeting search app \n" +
    "You will search from a list of Meeting Offices and also length of minutes \n" +
    "You have 3 tries each in the Office Location and the minutes section to select the right options \n" +
    "If none of the locations/minutes match - the program will shut down \n" +
    "Once appropriate selections are made, a tabular view will show the schedules for each SDR in your location \n" +
    "################################################################################################################## \n \n \n" +
    "### Please start by selecting your Office Location ###")

office = prompt_office()

print(f"### Please then by select your Meeting minutes for Office location: {office} ### \n")
minutes = prompt_minutes()

print(f"### Please then by select your time for Office location: {office} and interval of {minutes}: ### \n")
time_selected = prompt_time(minutes)

print(f"### Finding list of availabilities for Office location: {office} and time of {minutes} minutes ### \n \n")
sdr = get_sdr_list(minutes, office, time_selected)

l = len(sdr[0])
l_1= len(sdr[1])

###This function needs to be updated such that - the time needs to be handled correctly
###Input of 1 - 7 hour are in AM currently and we need to handle it such that its converted to business hours
###Since I ran out of time, I have listed all availibilities for the office overall
print(f"There are {l} available SDRs in the Twilio {office} Office for {minutes} minutes interval meetings with time of {time_selected[0]} - {time_selected[1]}: \n")
for ind, row in sdr[0].iterrows():
    print('--------------------------------------------------------------------------------------------')
    print('{} {} {} \n \n \n'.format(ind, row['Email'], row['combined_slots']))

print(f"Overall There are {l_1} available SDRs in the Twilio {office} Office for {minutes} minutes: \n")
for ind, row in sdr[1].iterrows():
    print('--------------------------------------------------------------------------------------------')
    print('{} {} {}'.format(ind, row['Email'], row['combined_slots']))
