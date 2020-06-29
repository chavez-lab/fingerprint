# Use python2 as base image
FROM python:2

WORKDIR /home/

#COPY 

# Install required packages
RUN pip install --no-cache-dir pysam==0.7.8

# Add required files
COPY . /app

# Run 

