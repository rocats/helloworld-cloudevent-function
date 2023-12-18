import pytest
from cloudevents.http import CloudEvent
from cloudevents.conversion import to_structured
from httpx import AsyncClient, _status_codes


@pytest.mark.asyncio
async def test_post_request():
    url = "http://localhost:8080"
    attributes = {
        "Content-Type": "application/cloudevents+json",
        "specversion": "1.0",
        "type": "dev.knative.staging.helloworld-function",
        "source": "dev.knative.staging/localhost-dev",
        "subject": "helloworld",
        "time": "2018-04-05T17:31:00Z",
    }
    payload = {
        "data": "Hello world!",
    }

    event = CloudEvent(attributes, payload)
    headers, data = to_structured(event)

    async with AsyncClient() as client:
        response = await client.post(url, headers=headers, content=data)
        print(response.content)

    assert response.status_code == _status_codes.codes.OK
