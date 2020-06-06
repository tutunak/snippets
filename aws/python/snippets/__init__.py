import boto3    # pip3 install boto3


def boto_init(aws_id, aws_secret):
    """
    :param aws_id: aws key id
    :param aws_secret:  aws secret id
    :return: bot3 session object
    """
    session = boto3.Session(
        aws_access_key_id=aws_id,
        aws_secret_access_key=aws_secret
    )
    return session


def regions_ec2(session):
    """
    :param session: boto3 session object (example in boto_init())
    :return: regions
    """
    regions = session.get_available_regions('ec2')
    return regions


def get_ec2(session, region):
    """
    :param session: boto3 session object (example in boto_init())
    :param region: ec2 region
    :return: all ec2 instances in this region
    """
    ec2 = session.resource('ec2', region_name=region)
    return ec2
