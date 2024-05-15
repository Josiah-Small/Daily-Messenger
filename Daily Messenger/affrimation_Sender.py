import requests
from twilio.rest import Client
import schedule
import time

#Credentials of Twilio
account_sid = ''#Twilio account ID
auth_token = ''#Authentication Token 
twilio_phone_number = '' #Twilio Phone Number 
client_phone_number = ''#Client Phone Number

#Initialize Twilio Client

client = Client(account_sid, auth_token)

def get_affirmation():
    response = requests.get('https://www.affirmations.dev')
    if response.status_code == 200:
        data = response.json()
        if data:
            affirmations = data.get('affirmation', 'No affirmation available')
            return affirmations
        else:
            return 'No data returned from the API'
    else:
        return f'Error fetching data: {response.status_code}'
    data = response.json()
    affirmations = data[0]['q'] + " - " + data[0]['a']
    return affirmations



#Function to send Message

def send_message():
    affirmations = get_affirmation()
    text = f'Here is your daily affirmation: {affirmations}'
    message = client.messages.create(
        body=text,
        from_= twilio_phone_number,
        to= client_phone_number
    )
    
    print('Message sent:', message.sid)
   
schedule.every().day.at("13:10").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)