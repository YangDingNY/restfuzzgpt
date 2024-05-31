#!/bin/bash


sudo rm -rf ./container-mysql
sudo docker stop warehouse
sudo docker stop mysql-warehouse
sudo docker rm warehouse
sudo docker rm mysql-warehouse
sudo docker rmi spring-boot-rest-api-warehouse-master-warehouse