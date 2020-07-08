from firebase import firebase
import os 
from twilio.rest import Client


firebase = firebase.FirebaseApplication('https://password-management-syst-60298.firebaseio.com/', None)

result = firebase.get('/password-management-syst-60298/Person', '')

tempText = '/password-management-syst-60298/Person/'

def inputPasswordData():
    data = {'Name': '', 'Email': '', 'Password': ''}

    for i in range(3):
        if i == 0: 
            values = input('Name: ')
            data['Name'] = values
        elif i == 1:
            values = input('Email: ')
            data['Email'] = values
        elif i == 2: 
            values = input('Password: ')
            data['Password'] = values

    print(data, '\n')
    result = firebase.post('/password-management-syst-60298/Person',data)

def updateData():
    clear = lambda: os.system('cls')

    temp = result.keys()

    dataList = list(temp)

    name = input('Name of person you want to update: ')

    # print(result[dataList[0]]['Name'] == 'kiel quitian')

    for i in range(len(temp)):
        if result[dataList[i]]['Name'] == name:
            foundData = dataList[i]
            tempText += foundData
            field = int(input('What field do you want to update: \n[1] Email \n[2] Name \n[3] Password \n'))
            
            if field == 1:
                newEmail = input('New Email: ')
                updateEmail = firebase.put(tempText, 'Email', newEmail);
                print('Email Updated')
                clear()

            elif field == 2:
                newName = input('New Name: ')
                updateName = firebase.put(tempText, 'Name', newName);
                print('Email Updated')
                clear()

            elif field == 3:
                newPass = input('New Password')
                updatePassword = firebase.put(tempText, 'Password', newPass)
                print('Password Updated')
                clear()
                sleep(5)
            else:
                print('Invalid input!')
            print(result[dataList[i]])

def deletePassword():
    result = firebase.get('/password-management-syst-60298/Person', '')

    temp = result.keys()

    dataList = list(temp)

    name = input('Name of person you want to delete: ')

    for i in range(len(temp)):
        if result[dataList[i]]['Name'] == name:
           firebase.delete(tempText, dataList[i])
           print('Item Deleted')
           break
        else:
            print('no item found')
            break

def sendSMS():
    result = firebase.get('/password-management-syst-60298/Person', '')
    # Your Account SID from twilio.com/console
    account_sid = ""
    # Your Auth Token from twilio.com/console
    auth_token  = ""

    client = Client(account_sid, auth_token)

    name = input('Name: ')

    temp = result.keys()

    dataList = list(temp)   

    for i in range(len(temp)):
        if result[dataList[i]]['Name'] == name:
            text = str(result[dataList[i]]['Password'])
            client.messages.create(
                to="insert_phone_num", 
                from_="+12057758507",
                body= "Password is: " + text)
        else:
            print('Name not found in FireStore database')



if __name__ == '__main__':
    temp = True
    while(temp):
        choices = int(input('\nFirebase Password Management Program\n----------------------------'
        '\n[1] Add Password Data\n[2] Update Password Data\n[3] Delete Password Data'
        '\n[4] End Program\n[5] Send an SMS to retrieve passwords\n----------------------------\n'))

        if choices == 1:
            inputPasswordData()
        elif choices == 2:
            updateData()
        elif choices == 3:
            deletePassword()
        elif choices == 4:
            temp = False
        elif choices == 5:
            sendSMS()
        else:
            print('Incorrect Input!')
        

        
