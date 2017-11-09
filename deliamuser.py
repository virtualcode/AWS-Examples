#!/usr/bin/env python3

import boto3
import pprint

def main():
    pp = pprint.PrettyPrinter(indent=2)

    iam = boto3.client('iam')
    try:
        result = iam.delete_user(UserName='botoTest')
        pp.pprint(result)
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    main()
