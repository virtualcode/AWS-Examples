#!/usr/bin/env python3

# example using boto paginator

import boto3
import pprint

pp = pprint.PrettyPrinter(indent=2)

iam = boto3.client('iam')

def main():
    try:
        page = iam.get_paginator('list_users')
        for response in page.paginate():
            pp.pprint(response['Users'])
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    main()
