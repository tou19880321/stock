FROM centos
#RUN apt-get update
#RUN apt-get install python3-pip
WORKDIR /app

RUN dnf install python3 -y

RUN python3 --version

RUN pip3 install websockets

RUN pip3 --default-timeout=100 install -U lxml
RUN pip3 install requests
RUN pip3 install lxml

EXPOSE 80
#CMD python3 server.py
#RUN pip3 install pipenv
#RUN pipenv install --dev
