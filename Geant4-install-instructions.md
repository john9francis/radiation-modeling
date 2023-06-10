# Geant4 Installation for Windows 11 
6/9/2023

This is a very simple tutorial on how I installed Geant4 on my Windows 11 laptop.

To install Geant4, I started on the [Geant4 installation guide](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/index.html). I chose the option "Build and install Geant4 from source." 

Here are the three steps for installing Geant4 on windows:
* [Step 1: Install prerequisites](#step-1-install-all-the-prerequisites)
* [Step 2: Build and install from source](#step-2-building-and-installing-from-source)
* [Step 3: Postinstall setup](#step-3-postinstall-setup)


## Step 1: Install all the prerequisites:

As explained in the Installation guide, we need to start by installing 3 prerequisites:
1. [Geant4 toolkit source code](#geant4-toolkit-source-code) 
2. [C++ compiler and library](#c-compiler-and-library)
3. [Cmake](#cmake)

### Geant4 toolkit source code

To download this, go to the [Geant4 main page](https://geant4.web.cern.ch), click on [Download](https://geant4.web.cern.ch/download/11.1.1.html), and under the "Source code" header you want to download the .zip file.

You're going to want to place this .zip file into a folder with the following path:
```
C:\Users\Your-User-Name\Geant4
```
This just makes the next steps a lot easier.

### C++ compiler and library

To get the correct C++ environment, use Visual Studio. I used Visual Studio 2022. If you don't have Visual Studio downloaded, click [Here](https://visualstudio.microsoft.com/downloads/).

The best tutorial I found to install the correct thing is this [YouTube video](https://www.youtube.com/watch?v=OMa2xDjdXJw). Basically it just has you open Visual Studio installer and install the "Desktop development with C++" workload. 

### CMake

CMake is an open-source, cross-platform family of tools designed to build, test and package software. Geant4 is designed to be installed with CMake, so we need to download it. To do so, go to the [CMake download website](https://cmake.org/download/) and go down and click the link to download the Windows x64 Installer. It should be an .msi file.

## Step 2: Building and installing from source

## Step 3: Postinstall setup




[Build and install from source instructions](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/installguide.html#buildandinstall)
