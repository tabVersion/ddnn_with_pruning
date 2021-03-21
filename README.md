# ddnn_with_pruning

This project is a practice of deploying [DDNN](https://github.com/kunglab/ddnn) as a service on edge devices (Raspberry Pi).

In this repo an image classification service will be deployed, where the end device (smart phone) will upload images to four edge nodes, each of which will process a quarter of the images (16\*16 resolution for cifar 10 dataset). These results are then collected and the classification results are returned directly if they are sufficiently confident, otherwise these feature maps are uploaded to the cloud for further computing.

## Design

The whole inference process is described as below:

1. (end device) upload an image
2. (edge device) receive the image and process the corresponding parts of each device
3. (edge device) all results from all edge devices are collected. If they are sufficiently confident, the service will return the label and the session will be closed. Otherwise, all edge devices' feature maps are handed to the cloud.
4. (cloud) compute the rest of NN and returnd a label
