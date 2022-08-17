from django.conf import settings
from typing import Dict, Any, List, Union
from botocore import exceptions
import boto3
import json


class SQSService(object):
    """
    AWS SQS service
    """

    def __init__(self) -> None:
        self._client = boto3.client(
            service_name="sqs",
            endpoint_url=settings.CONSTANTS["sqs_endpoint"],
        )
        self._queue_url = f'{settings.CONSTANTS["sqs_endpoint"]}/{settings.CONSTANTS["sqs_default_queue"]}'
        self._delay_seconds = 10
        self._wait_seconds = 20

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(SQSService, cls).__new__(cls)
        return cls.instance

    async def send(
        self, payload: Dict[str, Any], attrs: Dict[str, Any] = {}
    ) -> Union[str, None]:
        try:
            res = self._client.send_message(
                QueueUrl=self._queue_url,
                DelaySeconds=self._delay_seconds,
                MessageAttributes=attrs,
                MessageBody=json.dumps(payload),
            )
            return res.get("MessageId")
        except exceptions.ConnectionError as e:
            print(e)
        return None

    async def receive(self) -> List[Dict[str, Any]]:
        try:
            res = self._client.receive_message(
                QueueUrl=self._queue_url,
                WaitTimeSeconds=self._wait_seconds,
                MessageAttributeNames=["All"],
                VisibilityTimeout=0,
            )
            return res.get("Messages")
        except exceptions.ConnectionError as e:
            print(e)
        return []
