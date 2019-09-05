# En commentaire c'est une fonction classique pour un GET hello venant d' une fonction lambda#
##############################################################################################


#import json
#

#def hello(event, context):
#    body = {
#        "message": "Go Serverless v1.0! Your function executed successfully!",
#        "input": event
#    }
#
#    response = {
#        "statusCode": 200,
#        "body": json.dumps(body)
#    }
#
#    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
#    
#    return {
#        "message": "Go Serverless v1.0! Your function executed successfully!",
#        "event": event
#    }
#    """
#

import json
import boto3
import os
region_name = os.environ['REGION_NAME']
aws_access_key_id = os.environ['ACCESS_KEY']
aws_secret_access_key = os.environ['SECRET_KEY']
def sendEmail(event, context):
    data = event['body']
    name = data ['name']    
    source = data['source']    
    subject = data['subject']
    message = data['message']    
    destination = data['destination']
    _message = "Message from: " + name + "\nEmail: " + source + "\nMessage content: " + message    
    
    client = boto3.client('ses' )    
        
    response = client.send_email(
        Destination={
            'ToAddresses': [destination]
            },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': _message,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': subject,
            },
        },
        Source=source,
)
    return _message + str(region_name)
