FROM ubuntu:22.04
LABEL authors="YangDingNJU"

# install git:2.34 java11 maven:3.6.3
RUN apt-get update && \
    apt-get install git -y && \
    apt-get install maven -y

# clone project version:1.5.0
RUN git clone https://github.com/JavierMF/features-service.git /root/features

# build project
WORKDIR /root/features
RUN mvn clean package -DskipTests
EXPOSE 8081

# run project when creating container
ENTRYPOINT ["java", "-jar", "target/features-service-1.0.0-SNAPSHOT.jar"]