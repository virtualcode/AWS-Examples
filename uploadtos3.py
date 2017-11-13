#!/usr/bin/env python3

"""
Upload a file to an AWS S3 bucket
"""

import argparse
import boto3

def main():
    """
    Connect to s3.  Requires a valid bucket name and file name
    Converts the filename to all lower case
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("bucketname", help="A valid AWS S3 bucket name")
    parser.add_argument("filename", help="A valid file to upload")
    args = parser.parse_args()

    try:
        s3bucket = boto3.resource('s3')
        s3bucket.meta.client.upload_file(args.filename,
                                         args.bucketname,
                                         str.lower(args.filename))

    except Exception as exception:
        print(exception)

if __name__ == '__main__':
    main()
