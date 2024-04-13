FROM ubuntu:22.04
LABEL authors="YangDingNJU"

# install git:2.34 java11 maven:3.6.3
RUN apt-get update && \
    apt-get install git -y && \
    apt-get install maven -y

# replace maven settings.xml
COPY ../settings.xml /usr/share/maven/conf/settings.xml

# clone project version:1.5.0
RUN git clone -b 1.5.0 --single-branch https://github.com/corona-warn-app/cwa-verification-server.git /root/cwa

# build project
WORKDIR /root/cwa
RUN mvn clean package -DskipTests
EXPOSE 8080

# run project when creating container
ENTRYPOINT ["java", "-jar", "target/cwa-verification-server-1.5.0-SNAPSHOT.jar"]