FROM debian:buster-slim

ENV PATH /usr/local/bin:$PATH
ENV LANG C.UTF-8

RUN apt-get update -y
RUN apt-get install sudo -y
RUN sudo apt-get upgrade -y

# RUN sudo apt-get install python-pip -y
# RUN sudo apt-get install gcc -y
RUN sudo apt-get install curl -y
# python-dev python-pip
RUN sudo apt-get install python -y
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py

RUN python --version

# Fixed matplotlib issue
RUN sudo apt-get install python-subprocess32 -y

WORKDIR /app/DeepFloorplan-master

COPY ./DeepFloorplan-master/requirements.txt /app/DeepFloorplan-master

RUN pip install -r requirements.txt

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]