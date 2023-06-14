# Geant4 Installation for Windows 11 
6/9/2023

This is a very simple tutorial on how I installed Geant4 (from the source code) on my Windows 11 laptop.

There are the three steps for installing Geant4 on windows:
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

Make sure you put this .zip file somewhere safe on your computer. I put mine in a folder with the following path
```
C:\Users\Your-User-Name\Geant4
```
In the next steps, we're going to create a bunch more files and it's nice to keep them all in one folder.

### C++ compiler and library

To get the correct C++ environment, use Visual Studio. I used Visual Studio 2022. If you don't have Visual Studio downloaded, click [Here](https://visualstudio.microsoft.com/downloads/).

The best tutorial I found to install the correct thing is this [YouTube video](https://www.youtube.com/watch?v=OMa2xDjdXJw). Basically it just has you open Visual Studio installer and install the "Desktop development with C++" workload. You also need to go under the "Individual components" tab and make sure you check the MSBuild component.

- [x] Desktop Development with C++
- [x] MSBuild

### CMake

CMake is an open-source, cross-platform family of tools designed to build, test and package software. Geant4 is designed to be installed with CMake, so we need to download it. To do so, go to the [CMake download website](https://cmake.org/download/) and go down and click the link to download the Windows x64 Installer. It should be an .msi file.

## Step 2: Building and installing from source

The next step is installing and building Geant4 from the source files. The first thing I tried was using the [Instructions on the Geant4 website](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/installguide.html#buildandinstall). This method does everything from the command line using command prompt or powershell. Personally, I got a lot of bugs and issues with this approach, and ended up giving up on it.

What ended up working for me was closely following Physino's YouTube tutorial, "[How to compile Geant4 on Windows](https://www.youtube.com/watch?v=GykiM1lPON4)." This approach uses the CMake GUI instead of the command line. 

I would reccomend following the YouTube tutorial. The following is basically a summary of Physino's video:

### 1. Create the neccesary folders.

Go to the directory where you saved the Geant4 source code .zip file, 
```
C:\Users\Your-User-Name\Geant4
```
First, you want to un-zip the file, and you should end up with a folder called, "geant4-v11.1.1" or something similar. This is going to be your "source folder." Now we create a "build folder. I called mine, "geant4-v11.1.1-build". It's convenient if you put both the source and build folders in the same folder "Geant4".

### 2. Use CMake GUI to build from source.

Physino walks through how to use CMake's GUI to build Geant4 from the source in his video, but I'll quickly summarize. In the CMake GUI, at the top there's a place to enter "Where is the source code" and right below it has a place for, "Where to build the binaries." Under "Where is the source code," enter the path to your geant4-v11.1.1 folder and under "Where to build the binaries," enter the path to the geant4-v11.1.1-build folder.

After choosing the correct folders, make sure you check the GEANT4_INSTALL_DATA option. It should be in one of the red-highlighted things in the middle of the GUI with a check-box next to it.
- [x] GEANT4_INSTALL_DATA

Finally, go to the bottom of the GUI and click "configure," then "generate," and finally "open project."

At this point, Visual Studio should open. 

Make sure you have the "ALL_BUILD" option selected in your solution explorer, then go to the top bar and click on Build, and Build solution.

After like an hour or more, it will finish building... But you're not quite done yet.

### 3. Don't forget to install the last little bit

(See the video at around 08:00) For some reason, the Geant4 setup files don't install all the header files which are neccesary for the thing to run. So we need to find the "Install" solution, and build that manually.

## Step 3: Postinstall setup

[Geant4 postinstall setup instructions](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/postinstall.html)

To complete the installation of the Geant4 program, we need to set up a 2 more things.

1. Add the bin directory to PATH
2. Create a new environmental variable for the Geant4 datasets.

### About .batch files...

On the Geant4 website installation instructions, they suggest using their experimental .batch file to add these variables automatically. Also, in the YouTube tutorial, Physino offers his own batch file to do it automatically.

The main problem I found while examining both of these batch files is that they may not work properly, and are not very future-proof. For example, Physino's batch file was out of date and included a folder that the new version of Geant4 doesn't even include. I tried the Geant4 experimental batch file, but it just didn't do anything. Using a batch file is a nice idea, but in this tutorial, I will show how to manually add these variables. 

### Add the bin directory to PATH

If you go into the folder where you have your program files, (where you set your INSTALL_PREFIX) you will find four folders. "bin," "include," "lib," and "share." We need to add this "bin" folder to the system PATH. 

To add this to PATH, click on the windows button and search, "environment variables." Click on the link to, "edit system environment variables." This opens up a "System Properties" window. At the bottom there should be a button labelled, "Environment Variables." Click on this.

The "Environment Variables" window should now be displayed. There should be two sections, the top should be, "User variables," and the bottom should be, "System variables." In the User variables, (hopefully) there is one labelled, "Path." (If you don't have the path variable, click on "New" and create a variable named "Path" or "PATH". PATH is used by many programs, so it's nice to have.)

Once you have clicked on the "Path" variable, a window called, "Edit environment variable" is displayed. Click "New," and add the path to your bin directory. For example, my bin directory is:
```
C:\Users\my-user-name\Geant4\program_files\bin
```
But it could also be:
```
C:\Program files (x84)\Geant4\bin
```

Once you add this variable, it is important you click the "OK" button in all windows until everything is closed. Doing this will save the change.

Once you add the bin directory to path, Geant4 will no where to look to find the essential binary files to be able to run.

### Create a "Datasets" environmental variable.

Using the same environmental variables window, we need to create a new one called, "GEANT4_DATA_DIR". 

Go ahead and open the environmental varaibles window again by clicking the windows button and searching for it. Then, under User variables, click "New..." It will ask for the variable name, and the variable value. For name, you want to enter in:
```
GEANT4_DATA_DIR
```
and for value, you want to enter the directory to the program_files, share, Geant4, data folder. In my case, this was found here:
```
C:\Users\my-user-name\Geant4\program_files\share\Geant4\data
```
For you, everything from "share" and on will be the same, but the path before that will be wherever you have placed the bin, include, lib, and share folders.

Again, remember to click "OK" in each of the window to save the changes. 

## Step 4: See if Geant4 opens by running an example project

[How to compile a Geant4 example](https://www.youtube.com/watch?v=nY-vO6yN65c&t=67s)

Now, we are going to try and run one of the Geant4 examples to make sure Geant4 is installed correctly. To do this, we are going to try and run one of the examples that was installed along with Geant4.

First, locate the examples 
