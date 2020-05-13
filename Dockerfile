FROM ubuntu:16.04

MAINTAINER  san "me@gmail.com"

RUN apt-get update -y && \
    apt-get install  -y python3-pip python3-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

#RUN pip3 install random-cat
RUN pip3 install -r requirements.txt
COPY templates/index.html /usr/src/app/templates/
COPY . /

ENTRYPOINT [ "python3" ]

CMD ["app/app.py"]