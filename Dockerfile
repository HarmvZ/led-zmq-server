FROM python:3.7.4-buster

COPY requirements /home/docker/requirements/
RUN pip3 install -r /home/docker/requirements/local.txt

COPY . /home/docker/code/

EXPOSE 5555

CMD ["python", "/home/docker/code/app/zmq_server.py"]