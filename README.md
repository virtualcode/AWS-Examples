# Python examples using boto3

[aws-shell](https://github.com/awslabs/aws-shell) Example of a python text based program.

## Requirements:
 * A valid Amazon Web Services (AWS) account
 * Python
 * boto
 * Keys configured

Useful but not required:  AWS CLI

[Setting Up Credentials](http://boto3.readthedocs.io/en/latest/guide/configuration.html)


### There are three types of python SDK/API access to AWS:
 * Botocore: Boto 3 is built atop of a library called Botocore, which is shared by the AWS CLI. Botocore provides the low level clients, session, and credential & configuration data. Boto 3 builds on top of Botocore by providing its own session, resources and collections.

 * Clients: low level service connections

 * Resources: a high level, object oriented interface

[More detail here](http://boto3.readthedocs.io/en/latest/guide/new.html)
