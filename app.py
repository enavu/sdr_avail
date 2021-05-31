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

print(f"### Finding list of availabilities for Office location: {office} and time of {minutes} minutes ### \n \n")
sdr = get_sdr_list(minutes, office)
l = len(sdr)

print(f"There are {l} available SDRs in the Twilio {office} Office for {minutes} minutes interval meetings: \n")
for a, b in enumerate(sdr, 1):
    print('--------------------------------------------------------------------------------------------')
    print('{} {}'.format(a, b))
