#!/bin/bash
set -e


REGISTRY=registry.inventec
echo "building nginx image.."
docker build -t nginximage . 

echo "hopefully nginx image build succesfully"
