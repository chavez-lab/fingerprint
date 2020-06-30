# Use an official Python runtime as a parent image
FROM ubuntu:14.04
#FROM continuumio/miniconda

# Build in non-interactive mode for online continuous building
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /home/

# Install required packages
RUN apt-get update && apt-get install -y
RUN apt-get install apt-utils -y
RUN apt-get install python python-pip wget unzip build-essential python-dev -y
RUN apt-get install zlib1g-dev -y
RUN pip install Cython --install-option="--no-cython-compile"
#RUN conda install -c conda-forge gcc
RUN pip install pysam==0.7.8

# Add required files
COPY . /app

# Run 

