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

The next step is installing and building Geant4 from the source files. The first thing I tried was using the [Instructions on the Geant4 website](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/installguide.html#buildandinstall). This method does everything from the command line using command prompt or powershell. Personally, I got a lot of bugs and issues with this approach, and ended up giving up on it.

An easier way for me personally was closely following Physino's YouTube tutorial, "[How to compile Geant4 on Windows](https://www.youtube.com/watch?v=GykiM1lPON4)." This approach uses the CMake GUI instead of the command line. 

I would reccomend following the YouTube tutorial, but here's a basic overview of how to build and compile Geant4 from the source.

### 1. Create the neccisary folders.

Go to the directory where you saved the Geant4 source code .zip file, 
```
C:\Users\Your-User-Name\Geant4
```
First, you want to un-zip the file, and you should end up with a folder called, `geant4-v11.1.1` or something similar. This is going to be your "source folder." Now we create a "build folder. I called mine, `geant4-v11.1.1-build`. It's convenient if the source and build folders are both found in the same folder `Geant4`.

### 2. Use CMake to build from source.

There are two ways to build the binaries. First, the command line. This is more complicated, but here's a quick example of how to do it.

```powershell
C:Users/Your-User-Name/Geant4 cmake -S geant4-v11.1.1 -B geant4-v11.1.1-build
```


## Step 3: Postinstall setup


