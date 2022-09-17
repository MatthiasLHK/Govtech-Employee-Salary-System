FROM python:3.8-alpine

COPY ./requirements.txt /backend/requirements.txt

WORKDIR /backend

RUN pip install -r requirements.txt

COPY . /backend

ENTRYPOINT [ "python" ]

CMD ["view.py" ]