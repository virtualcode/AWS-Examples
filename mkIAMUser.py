#!/usr/bin/env python3

import boto3
import pprint

pp = pprint.PrettyPrinter(indent=2)

iam = boto3.client('iam')
response = iam.create_user(UserName='botoTest')
pp.pprint(response)
