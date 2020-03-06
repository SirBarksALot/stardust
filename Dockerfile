FROM alpine:latest

# install python3, latest pip and django 
RUN apk add python3==3.8.1-r0
RUN pip3 install --upgrade pip

# install postgres dependencies
RUN apk add postgresql-dev gcc python3-dev musl-dev

# copy project requirements.txt and download its packages
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

# copy app files
COPY ./app_files /app/app_files

# run web app
WORKDIR /app/app_files
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
