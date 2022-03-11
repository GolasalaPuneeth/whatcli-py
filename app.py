from twilio.rest import*
import time
data=('hello 😊','hope you are good 🙌',"today our deals cooking oil @100 😍😍", "grab the deal soon 👌😎")
account_sid = 'AC12eed5ea4c9f3755883bcb1d11b2d6fe' 
auth_token = 'ba1de6a58e9be3db005724a941cc447d'
client = Client(account_sid, auth_token)
def example():
    for i in data:
        message = client.messages.create( 
        from_='whatsapp:+14155238886',  
        body=i,      
        to='whatsapp:+918096226158') 
        print(message.sid)
        time.sleep(1)
