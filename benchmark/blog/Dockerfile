FROM ubuntu:22.04
LABEL authors="YangDingNJU"

# install git:2.34 java11 maven:3.6.3
RUN apt-get update && \
    apt-get install git -y && \
    apt-get install maven -y

# clone project
RUN git clone https://github.com/YangDingNY/blog.git /root/blog

# build project
WORKDIR /root/blog
RUN mvn clean package -DskipTests
EXPOSE 8081

# run project when creating container
ENTRYPOINT ["java", "-jar", "target/springboot-trail-0.0.1-SNAPSHOT.jar"]