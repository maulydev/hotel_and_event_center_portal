import requests

def send_otp_sms(phone_number, otp):
    # url = 'https://api.msg91.com/api/sendhttp.php'
    api_key = 'VUJnZXF5ZnRnV1pOZHdGeVRibmU'
    sender_id = 'ercodr(TM)'
    message = f'Your Verfication code is: {otp}'
    recipient = phone_number
    url = f'https://sms.arkesel.com/sms/api?action=send-sms&api_key={api_key}&to={recipient}&from={sender_id}&sms={message}'
    response = requests.get(url)
    return response.json()
    