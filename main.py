import structlog
import functions_framework
from cloudevents.http.event import CloudEvent


@functions_framework.cloud_event
def handler(event: CloudEvent) -> None:
    logger = structlog.get_logger()
    try:
        logger.debug("Function loaded")
        logger.debug(f"Received event with ID: {event['id']} and data {event.data}")
        logger.debug(f"Cloudevent: {event}")
        logger.info("OK")
    except Exception as err:
        logger.error(str(err))

    return
