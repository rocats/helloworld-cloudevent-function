import structlog
from cloudevents.http.event import CloudEvent


def handler(event: CloudEvent):
    logger = structlog.get_logger()
    try:
        logger.debug("Function loaded")
        logger.debug(f"Received event with ID: {event['id']} and data {event.data}")
        logger.debug(f"Cloudevent: {event}")
        logger.info("OK")

        return "OK", 200
    except Exception as err:
        logger.error(str(err))
        return "Internal Server Error", 500
