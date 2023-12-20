from uuid import uuid4
import structlog
import flask
import status
import functions_framework
from cloudevents.http import from_http, CloudEvent
from cloudevents.conversion import to_structured


@functions_framework.http
def handler(request: flask.Request) -> flask.typing.ResponseReturnValue:
    logger = structlog.get_logger()
    try:
        event = from_http(request.headers, request.get_data())

        logger.debug("Function loaded")
        logger.debug(f"Received event with ID: {event['id']} and data {event.data}")
        logger.debug(f"Cloudevent: {event}")
        logger.info("OK")

        attributes = {
            "id": str(uuid4()),
            "type": "dev.knative.staging.helloworld-cloudevent-function",
            "source": "dev.knative.staging/helloworld-cloudevent-function",
        }
        data = {"message": "Hello World!"}
        event = CloudEvent(attributes, data)
        headers, body = to_structured(event)

        return flask.Response(
            response=body,
            headers={**headers, **{"Prefer": "reply"}},
            status=status.HTTP_200_OK,
        )
    except Exception as err:
        logger.error(str(err))
