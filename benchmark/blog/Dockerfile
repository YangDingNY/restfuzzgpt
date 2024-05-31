FROM ubuntu:22.04
LABEL authors="YangDingNJU"

# install git:2.34 java11 maven:3.6.3
RUN apt-get update && \
    apt-get install git -y && \
    apt-get install maven -y

# prepare project
RUN git clone https://github.com/YangDingNY/blog.git /root/blog
COPY ./start.sh /root/blog/start.sh

# build project
WORKDIR /root/blog
RUN mkdir ./data
RUN mvn clean package -DskipTests
EXPOSE 8080
RUN chmod +x ./start.sh

# run project when creating container
ENTRYPOINT ["./start.sh"]