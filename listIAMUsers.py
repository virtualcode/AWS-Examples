#!/usr/bin/env python3

# example using boto paginator

import boto3
import pprint

pp = pprint.PrettyPrinter(indent=2)

iam = boto3.client('iam')
paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
  pp.pprint(response['Users'])
