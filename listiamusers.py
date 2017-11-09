#!/usr/bin/env python3

"""
python example using boto paginator
"""

import pprint
import boto3

def main():
    """
    list AWS IAM users
    """
    try:
        pretty = pprint.PrettyPrinter(indent=2)
        iam = boto3.client('iam')
        page = iam.get_paginator('list_users')
        for response in page.paginate():
            pretty.pprint(response['Users'])
    except Exception as exception:
        print('Error:', exception)


if __name__ == '__main__':
    main()
