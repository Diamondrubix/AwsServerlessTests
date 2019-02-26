""" Lambda to launch ec2-instances """
import boto3
import json
import os

REGION = 'us-east-1' # region to launch instance.
#AMI = 'ami-24bd1b4b'
AMI = 'ami-66506c1c'
    # matching region/setup amazon linux ami, as per:
    # https://aws.amazon.com/amazon-linux-ami/
INSTANCE_TYPE = 't2.micro' # instance type to launch.

#EC2.describe_key_pairs('Virginia')
#EC2.KeyPairInfo('Virginia.pem')
def lambda_handler(event, context):
    """ Lambda handler taking [message] and creating a httpd instance with an echo. """
    #message = event['message']
    init_script = """#!/bin/bash
    echo "Hello World" >> /tmp/data.txt
    sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
    /etc/init.d/ssh restart
    sudo adduser aarato --gecos "First Last,RoomNumber,WorkPhone,HomePhone" --disabled-password
    echo "aarato:Password123" | sudo chpasswd
    sudo adduser aarato sudo
    apt update
    apt install gedit"""
    # bash script to run:
    #  - update and install httpd (a webserver)
    #  - start the webserver
    #  - create a webpage with the provided message.
    #  - set to shutdown the instance in 5 minutes.


    if(event == 1):
        EC2 = boto3.client('ec2', region_name='us-east-1')
        #return "i-0ddfeb428871dcdb1"
        instance = EC2.run_instances(
            ImageId=AMI,
            InstanceType=INSTANCE_TYPE,
            MinCount=1, # required by boto, even though it's kinda obvious.
            MaxCount=1,
            KeyName='dad',
            InstanceInitiatedShutdownBehavior='terminate', # make shutdown in script terminate ec2
        UserData=init_script # file to run on instance init.
        )
        print "New instance created."
        instance_id = instance['Instances'][0]['InstanceId']

        output = EC2.get_console_output(
        InstanceId=instance_id,
        DryRun=False
        )

        return instance_id
        #return output
    else:
        #return event
        #EC2 = boto3.client('ec2')
        ec2 = boto3.resource('ec2', region_name='us-east-1') # call ec2 recourse to perform further actions
        instances = ec2.instances.all()
        instance_id = event
        for instance in instances:
            if (instance.id == instance_id):
                return instance.public_ip_address
                #return instance.console_output(DryRun=False)['Output']#InstanceId
                #return os.system("ssh-keyscan arato.biz | ssh-keygen -lf /dev/stdin -E sha256 | grep ECDSA")
        #instances = EC2.describe_instances(InstanceIds=[instance_id])
        #ec2info = defaultdict()
        #public_ip = instances[0]['Reservations'][0]['Instances'][0]['PublicIpAddress']
        return "nope"