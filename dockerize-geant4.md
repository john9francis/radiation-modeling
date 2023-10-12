# Dockerizing Geant4
- [home](README.md)
- Author: John Francis
- Date: 10/11/2023
- Development environment: Windows 11, docker 24.0.5, VSCode

Contents:
- [Intro](#intro)
- [Basic Geant4 environment](#basic-geant4-environment)
- [Datasets](#datasets)
- [Visualization](#visualization)
- [Docker compose](#docker-compose)

# Intro

Docker is an incredibly useful tool for cross-platform application development. It can be used to develop using Geant4 without installing Geant4 locally on your machine. It can also be used to standardize your Geant4 application so that anyone with docker can run it on their machine. These two benefits can greatly improve Geant4 application development and distribution.

In this article, I will be going over how I dockerize my personal Geant4 applications. I am coming from a Windows 11 environment, but the principles should apply to any operating system. 

# Basic Geant4 environment

First, we can run Geant4 in a container without needing to install it locally. If you have seen my [Geant4 installation tutorial](g4-install-instructions-windows.md), you can already see the benefit of this. We're talking about minutes of setup instead of hours, not to mention saved memory on your computer. 

To use Geant4 in docker, VSCode makes it super simple. Let's say we have a simple Geant4 cmake project created. For this tutorial, I will be using my own [G4-Hello-World](https://github.com/john9francis/G4-Hello-World). To dockerize, we can use the official Geant4 docker image. 

Let's create a dockerfile in our geant4 project, and add the following line in it:

```
# dockerfile
FROM geant4/geant4
```

Now, if we open our directory inside this container, we will have Geant4 all linked up and ready to go. 

To open a directory inside a docker container in VSCode, we can do the following:\
1. Download the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension for VSCode
2. Make sure docker desktop is running in the background
3. Open our Geant4 project directory in VSCode
4. Click on the green arrows button in the bottom left hand corner:

![Picture of the green arrows button in VSCode]()


# Datasets

# Visualization

# Docker compose
