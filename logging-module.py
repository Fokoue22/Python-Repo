import logging

#logging.warning("this is a debuge messages")
#logging.critical("this is a debuge messages")
#logging.error("this is a debuge messages")


#import boto3

#call boto client 
#ec2_client = boto3.client('ec2')

#retrieves all region/endpoint
#response = ec2_client.describe_regions()
#print(response['Region'][0]['RegionName'])

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger()
logger.error("this is a debuge messages")