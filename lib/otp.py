import os
import requests
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/hotel_and_event_center_portal')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

# load_dotenv()

API_KEY = os.getenv('API_KEY')
SENDER_ID = os.getenv('SENDER_ID')


def send_otp_sms(phone_number, otp):
    # url = 'https://api.msg91.com/api/sendhttp.php'
    api_key = API_KEY
    sender_id = SENDER_ID
    message = f'Your Verfication code is: {otp}'
    recipient = phone_number
    url = f'https://sms.arkesel.com/sms/api?action=send-sms&api_key={api_key}&to={recipient}&from={sender_id}&sms={message}'
    response = requests.get(url)
    return response.json()
    