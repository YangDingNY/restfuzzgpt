#!/bin/bash

sudo docker stop evomaster
sudo docker rm evomaster
sudo docker rmi evomaster
rm -rf ./src