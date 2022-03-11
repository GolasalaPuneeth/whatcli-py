from twilio.rest import*
import time
data=('hello 😊','hope you are good 🙌',"today our deals cooking oil @100 😍😍", "grab the deal soon 👌😎")
account_sid = 'AC12eed5ea4c9f3755883bcb1d11b2d6fe' 
auth_token = '0751edadc7c7e4a9603dcb214abf7e36'
client = Client(account_sid, auth_token)
def example():
    for i in data:
        message = client.messages.create( 
        from_='whatsapp:+14155238886',  
        body=i,      
        to='whatsapp:+918096226158') 
        print(message.sid)
        time.sleep(1)
#AC12eed5ea4c9f3755883bcb1d11b2d6fe
#0751edadc7c7e4a9603dcb214abf7e36