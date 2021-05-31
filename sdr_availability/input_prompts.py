import pandas as pd

def prompt_office():

    path = "sdr_availability/data/"
    file = "hr.csv"
    hr_list = pd.read_csv(path + file)

    offices = pd.DataFrame(hr_list['Office'].unique())
    offices.columns = ['Office']

    tries = 3
    officeOptions = ""
    officeIndex = list(offices.index)
    selectedOffice = ""

    for index, row in offices.iterrows():
        officeOptions += "[{}]: {}".format(index, row['Office']) + "\n"

    while tries > 0:
        print("Select a number below from list, to select your Office meeting availibility search: \n")
        print(officeOptions) 
        idx = input()

        if str(idx) not in str(officeIndex):
            tries -= 1
            print(f"####### You did not select a number from the list, you have {tries} tries left ######")

        else:
            selectedOffice = list(offices['Office'].iloc[[idx]])
            print("You have selected the Office: " + selectedOffice[0]+ "\n")
            tries = 0
            return selectedOffice[0]

        if tries == 0:
            print("Game Over, Try again")
            exit(0)
        


def prompt_minutes():

    meetingMins = pd.DataFrame(['15','30'])
    meetingMins.columns = ['Minutes']

    tries = 3
    minutesOptions = ""
    selectedMinutes = []
    minutesIndex = list(meetingMins.index)

    for index, row in meetingMins.iterrows():
        minutesOptions += "[{}]: {}".format(index, row['Minutes']) + "\n"
    
    while tries > 0:
        print("Select a number from list below, to select your meeting minutes availability search: \n")
        print(minutesOptions) 
        idx = input()

        if str(idx) not in str(minutesIndex):
            tries -= 1
            print(f"####### You did not select a number from the list, you have {tries} tries left ######")
        else:
            selectedMinutes = list(meetingMins['Minutes'].iloc[[idx]])
            print("You have selected meeting minutes of: " + selectedMinutes[0] + "\n")
            tries = 0
            return selectedMinutes[0]

        if tries == 0:
            print("####### Game Over, Try again #########")
            exit(0)
        
