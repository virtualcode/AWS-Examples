#!/usr/bin/env python3

import boto3
import pprint

pp = pprint.PrettyPrinter(indent=2)

iam = boto3.client('iam')
result = iam.delete_user(UserName='botoTest')
pp.pprint(result)
