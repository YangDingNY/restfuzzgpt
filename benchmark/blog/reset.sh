#!/bin/bash


sudo rm -rf ./container-mysql
sudo docker stop blog
sudo docker stop mysql-blog
sudo docker rm blog
sudo docker rm mysql-blog
sudo docker rmi blog-blog