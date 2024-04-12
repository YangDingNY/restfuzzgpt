FROM maven:3.8.6-openjdk-8

# add the project to the container
ADD ./src /app/spring-boot-rest-api-warehouse-master/src
ADD ./pom.xml /app/spring-boot-rest-api-warehouse-master/pom.xml

# replace maven settings.xml
COPY ./settings.xml /usr/share/maven/conf/settings.xml

# package
WORKDIR /app/spring-boot-rest-api-warehouse-master
RUN mvn clean package -DskipTests

EXPOSE 8080