#!/usr/bin/env python3

# Start and stop an instance

import boto3
import json

ls = boto3.client('lightsail')
instance_name = input('Lightsail Instance Name: ')

try: 
    r = ls.get_instance_state(instanceName = instance_name)
except:
    print('instance not found')
    exit()
    
print(json.dumps(r['state']['name'], indent=2))
if r['state']['name'] == "running":
   print("stopping instance")
   r2 = ls.stop_instance(instanceName='digsserver')
   print(json.dumps(r2['ResponseMetadata'], indent=2))

if r['state']['name'] == "stopped":
    print("starting instance")
    r2 = ls.start_instance(instanceName = instance_name)
    print(json.dumps(r2['ResponseMetadata'], indent=2))

