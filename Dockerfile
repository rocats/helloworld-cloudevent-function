#                      _       
#   _ __ ___   ___ __ _| |_ ___ 
#  | '__/ _ \ / __/ _` | __/ __|
#  | | | (_) | (_| (_| | |_\__ \
#  |_|  \___/ \___\__,_|\__|___/
#
#  https://github.com/rocats/apigateway-interceptor
#
#  Copyright (C) 2023 @rocats
#
#  This is a self-hosted software, liscensed under the Apache License. 
#  See /License for more information.

ARG PYTHON_VERSION
ARG APP_DIR="/app"

FROM python:${PYTHON_VERSION}-slim-bullseye as builder

ARG APP_DIR

ADD requirements.txt ${APP_DIR}/requirements.txt

WORKDIR ${APP_DIR}
RUN pip install -r requirements.txt

COPY main.py ./

EXPOSE 8080

ENTRYPOINT [ "/usr/local/bin/functions-framework", "--signature-type=http", "--debug" ]
CMD [ "--target=handler" ]
