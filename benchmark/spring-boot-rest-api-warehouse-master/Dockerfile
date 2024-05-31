FROM ubuntu:22.04
LABEL authors="YangDingNJU"

# install git:2.34 java11 maven:3.6.3
RUN apt-get update && \
    apt-get install git -y && \
    apt-get install maven -y


# add the project to the container
RUN git clone https://github.com/elenamountz/spring-boot-rest-api-warehouse.git /root/warehouse
COPY ./start.sh /root/warehouse/start.sh

# replace maven settings.xml
# COPY ../settings.xml /usr/share/maven/conf/settings.xml

# package
WORKDIR /root/warehouse
RUN mkdir ./data
RUN mvn clean package -DskipTests

EXPOSE 8080
RUN chmod +x ./start.sh

# run project when creating container
ENTRYPOINT ["./start.sh"]