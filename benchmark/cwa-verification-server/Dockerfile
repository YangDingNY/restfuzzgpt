FROM ubuntu:22.04

# install git:2.34 java11 maven:3.6.3
RUN apt-get update && \
    apt-get install git -y && \
    apt-get install maven -y

# clone project
RUN git clone -b 1.5.0 --single-branch https://github.com/corona-warn-app/cwa-verification-server.git /root/cwa

# run project
WORKDIR /root/cwa
RUN mvn clean package
CMD ["java", "-jar", "target/cwa-verification-server-1.5.0-SNAPSHOT.jar"]


