FROM ubuntu

WORKDIR /app

COPY my-model.py /app

RUN apt update && apt install -y python3 python3-pip
RUN pip3 install umbridge

CMD python3 my-model.py
