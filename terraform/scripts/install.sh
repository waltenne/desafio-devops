#!/bin/bash -xe
hostnamectl set-hostname terraform-apache-t2-micro

yes|sudo apt update
yes|sudo apt install git
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run

sudo wget https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb -o /tmp/amazon-cloudwatch-agent.deb
sudo dpkg -i -E /tmp/amazon-cloudwatch-agent.deb
sudo apt-get install -y -f
sudo service amazon-cloudwatch-agent start
sudo rm /tmp/amazon-cloudwatch-agent.deb

git clone https://github.com/waltenne/desafio-devops.git




