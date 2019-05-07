"""
The following function will iterate all of the CloudFormation stacks
within a given region. It will then call the detect_stack_drift API
for each stack which will update the status within the CloudFormation
console.
"""

import json
import boto3
import logging
from botocore.exceptions import ClientError

"""Set up logging"""
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    cf = boto3.client('cloudformation')
    try:
        """Get a list of CloudFormation stacks"""
        logger.info('Getting a list of stacks')
        stacks = cf.list_stacks(
            StackStatusFilter=[
                'CREATE_COMPLETE', 'ROLLBACK_COMPLETE', 'UPDATE_COMPLETE',
                'UPDATE_ROLLBACK_COMPLETE'
            ]
        )
        logger.debug('Found the following stacks: {}'.format(stacks))
    except ClientError as error:
        logger.error('Problem getting stacks {}'.format(error))
    else:
        for stack in stacks['StackSummaries']:
            logger.info('Checking drift detection on {}'.format(stack['StackName']))
            try:
                """Update the status of drift detection on this stack"""
                response = cf.detect_stack_drift(
                    StackName=stack['StackName']
                )
            except ClientError as error:
                logger.error('Problem detecting drift {}'.format(error))
            else:
                logger.info('OK')
