FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y aptitude
RUN apt-get install -y binutils libproj-dev gdal-bin
RUN aptitude install -y libgdal-dev
RUN aptitude install -y python3-gdal
RUN aptitude install -y binutils
RUN pip install -r requirements.txt
COPY . /code/
