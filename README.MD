1. Install dependencies:

'''
pip install -r requirements.txt
'''

2. Run docker process:

'''
docker run -d -p 5672:5672 rabbitmq
'''

3. Put values to environment variables:

'''
export TWILIO_ACCOUNT_SID="foo"

export TWILIO_ACCOUNT_SID="foo"

for Windows use:

set TWILIO_ACCOUNT_SID="foo"

set TWILIO_ACCOUNT_SID="foo"
'''

4. Run worker process

'''
celery -A send_sms worker -l INFO 
'''

5. Run Django webserver 

'''
python manage.py runserver
'''