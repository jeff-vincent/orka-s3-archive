FROM python:3.9-alpine
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN rm -rf /tmp/requirements.txt
COPY main.py .
CMD python main.py
