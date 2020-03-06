FROM alpine:latest

# install python3, latest pip
RUN apk add python3==3.8.2-r0
RUN pip3 install --upgrade pip

# install postgres dependencies
RUN apk add postgresql-dev gcc python3-dev musl-dev

# copy project requirements.txt and download its packages
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

# copy app files
COPY ./stardust /app/stardust

# run web app
WORKDIR /app/stardust
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
