FROM alpine:latest

# install python3, latest pip and django 
RUN apk add python3
RUN pip3 install --upgrade pip
RUN pip3 install Django
RUN mkdir /code

# set working directory to code inside container
WORKDIR /code

# copy project requirements.txt and download its packages
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# copy app files
COPY ./app_files ./app_files

#run web app
CMD ["python3", "./app_files/manage.py", "runserver", "0.0.0.0:8000"]