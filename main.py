import structlog
import flask
import status
import functions_framework
from cloudevents.http import from_http


@functions_framework.http
def handler(request: flask.Request) -> flask.typing.ResponseReturnValue:
    logger = structlog.get_logger()
    try:
        event = from_http(request.headers, request.get_data())

        logger.debug("Function loaded")
        logger.debug(f"Received event with ID: {event['id']} and data {event.data}")
        logger.debug(f"Cloudevent: {event}")
        logger.info("OK")

        return "", status.HTTP_204_NO_CONTENT
    except Exception as err:
        logger.error(str(err))
