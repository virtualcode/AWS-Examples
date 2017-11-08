#!/usr/bin/env python3

import boto3
import pprint

pp = pprint.PrettyPrinter(indent=2)

iam = boto3.client('iam')

def main():
    try:
        response = iam.create_user(UserName='botoTest')
        pp.pprint(response)
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    main()
