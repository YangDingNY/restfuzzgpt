FROM ubuntu:22.04
LABEL authors="YangDingNJU"

# install java8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y wget

# get evomaster.jar
RUN wget -P /root/evomaster https://github.com/EMResearch/EvoMaster/releases/download/v3.0.0/evomaster.jar

# WORKDIR
WORKDIR /root/evomaster