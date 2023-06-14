# Geant4 Installation for Windows 11 
6/9/2023

[Video](insert-link-here)

This is a very simple tutorial on how I installed Geant4 (from the source code) on my Windows 11 laptop. I recommend watching [my YouTube tutorial](insert-link-here) where I walk through each of these steps on my own computer.

There are three steps for installing Geant4 on windows:
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
C:\Users\my-user-name\Geant4
```
In the next steps, we're going to create a bunch more files and it's nice to keep them all in this folder.

### C++ compiler and library

To get the correct C++ environment, use Visual Studio. I used Visual Studio 2022. If you don't have Visual Studio, you can download it [Here](https://visualstudio.microsoft.com/downloads/).

The best tutorial I found to install the correct C++ workload is this [YouTube video](https://www.youtube.com/watch?v=OMa2xDjdXJw). Basically it just has you open Visual Studio installer and install the "Desktop development with C++" workload. You also need to go under the "Individual components" tab and make sure you check the MSBuild component.

- [x] Desktop Development with C++
- [x] MSBuild

### CMake

CMake is an open-source, cross-platform family of tools designed to build, test and package software. Geant4 is designed to be installed with CMake, so we need to download it. To do so, go to the [CMake download website](https://cmake.org/download/), scroll down, and click the link to download the Windows x64 Installer. It should be an .msi file.

## Step 2: Building and installing from source

The next step is installing and building Geant4 from the source files. The first thing I tried was using the [Instructions on the Geant4 website](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/installguide.html#buildandinstall). This method does everything from the command line using command prompt or powershell. Personally, I got a lot of bugs and issues with this approach, so I ended up going a different direction.

What ended up working for me was closely following Physino's YouTube tutorial, "[How to compile Geant4 on Windows](https://www.youtube.com/watch?v=GykiM1lPON4)." This approach uses the CMake GUI instead of the command line. 

### 1. Create the neccesary folders.

Go to the directory where you saved the Geant4 source code .zip file.
```
C:\Users\my-user-name\Geant4
```
First, you want to un-zip the file, and you should end up with a folder called, "geant4-v11.1.1" or something similar. This is going to be your "source folder." Now we create a "build folder. I called mine, "geant4-v11.1.1-build". It's convenient if you put both the source and build folders in the same folder "Geant4".

### 2. Use CMake GUI to build from source.

Physino walks through how to use CMake's GUI to build Geant4 from the source in his video, but I'll quickly summarize. In the CMake GUI, at the top there's a place to enter "Where is the source code" and right below it has a place for, "Where to build the binaries." Under "Where is the source code," enter the path to your geant4-v11.1.1 folder and under "Where to build the binaries," enter the path to the geant4-v11.1.1-build folder.

After choosing the correct folders, make sure you check the GEANT4_INSTALL_DATA option. It should be in one of the red-highlighted things in the middle of the GUI with a check-box next to it.
- [x] GEANT4_INSTALL_DATA

### Setting INSTALL_PREFIX

In the CMake GUI, there is an option called, "CMAKE_INSTALL_PREFIX" with a certain directory. The directory is most likely in:
```
C:/Program Files (x84)
```
 Once we compile Geant4, it will create a folder in this directory with some important files. I reccommend changing this directory to be in the same folder you have been working in this whole time, keeping everything consistent. I put mine in a folder called "program_files" in my Geant4 folder (where I'm keeping everything organized)
 ```
C:/Users/my-user-name/Geant4/program_files
 ```

### Configuration types
There is an option in the GUI called, "CMAKE_CONFIGURATION_TYPES." This has several options such as Release, RelWithDebInfo, Debug, etc. Make sure you delete everything besides "Release" or "RelWithDebInfo" if you want to have the debug info included

### Finishing up the config and generation:

Finally, go to the bottom of the GUI and click "configure," then "generate," and finally "open project."

At this point, Visual Studio should open. 

Make sure you have the "ALL_BUILD" option selected in your solution explorer, then go to the top bar and click on Build, and Build solution.

After like an hour or more, it will finish building... But you're not quite done yet.

### 3. Don't forget to install the last little bit

For some reason, the Geant4 setup skips the "INSTALL" option which installs all the header files which are neccesary for the thing to run. So we need to find the "INSTALL" solution, and click build. Now the Geant4 is completely compiled.

## Step 3: Postinstall setup

[Geant4 postinstall setup instructions](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/postinstall.html)

To complete the installation of the Geant4 program, we need to set up 2 more things.

1. Add the bin directory to PATH
2. Create a new environmental variable for the Geant4 datasets.

### You could use a .batch file, but...

On the Geant4 website installation instructions, they suggest using their experimental .batch file to add these variables automatically. Also, in the YouTube tutorial, Physino offers his own batch file to do it automatically.

The main problem I found while examining both of these batch files is that they may not work properly, and are not very future-proof. For example, Physino's batch file was out of date and included a folder that the new version of Geant4 doesn't even include. I tried the Geant4 experimental batch file, but it just didn't do anything. Using a batch file is a nice idea, but in this tutorial, I will show how to manually add these variables. 

### 1. Add the bin directory to PATH

If you go into the folder where you have your program files, (where you set your INSTALL_PREFIX, for me it was in the "program_files" folder) you will find four folders: "bin," "include," "lib," and "share." We need to add this "bin" folder to the system PATH. 

To add this to PATH, click on the windows button and search, "environment variables." Click on the link to, "edit system environment variables." This opens up a "System Properties" window. At the bottom there should be a button labelled, "Environment Variables." Click on this.

The "Environment Variables" window should now be displayed. There should be two sections, the top should be, "User variables," and the bottom should be, "System variables." In the User variables, there is one labelled, "Path." (If you don't have the path variable, click on "New" and create a variable named "Path" or "PATH". Path is used by many programs, so it's nice to have.)

Once you have clicked on the "Path" variable, a window called, "Edit environment variable" is displayed. Click "New," and add the path to your bin directory.
```
C:\Users\my-user-name\Geant4\program_files\bin
```

Once you add this variable, it is important you click the "OK" button in all windows until everything is closed. Doing this will save the change.

Once you add the bin directory to path, Geant4 will no where to look to find the essential binary files to be able to run.

### Create a "Datasets" environmental variable.

Using the same environmental variables window, we need to create a new variable called, "GEANT4_DATA_DIR". 

Go ahead and open the environmental varaibles window again by clicking the windows button and searching for it. Then, under User variables, click "New..." It will ask for the variable name, and the variable value. For name, you want to enter in:
```
GEANT4_DATA_DIR
```
and for value, you want to enter the directory to the program_files/share/Geant4/data folder. In my case, this was found here:
```
C:\Users\my-user-name\Geant4\program_files\share\Geant4\data
```

Again, remember to click "OK" in each of the window to save the changes. 

## Step 4: See if Geant4 opens by running an example project

[How to compile a Geant4 example](https://www.youtube.com/watch?v=nY-vO6yN65c&t=67s)

Now, we are going to try and run one of the Geant4 examples to make sure Geant4 is installed correctly. To do this, we are going to run one of the examples that was installed along with Geant4.

First, locate the examples folder. This is in the program_files/share folder. Navigate to:

```
C:\Users\my-user-name\Geant4\program_files\share\Geant4\examples\basic
```
This directory contains the basic examples. We are going to run B1 as a test, so go to the B1 folder. In the B1 folder there will be a file called CMakeLists.txt:
```
...\basic\B1\CMakeLists.txt
```
Open CMake GUI and drag this text file into the window. This will automatically populate the window with data. It will put the path to the source AND the build as:
```
C:/Users/my-user-name/Geant4/program_files/share/Geant4/examples/basic/B1
```
It's a good idea to change the "build" path to it's own folder, namely:
```
C:/Users/my-user-name/Geant4/program_files/share/Geant4/examples/basic/B1/build
```
(this will just keep it more organized.) For CMAKE_CONFIGURATION_TYPES, just delete everything except "Release."

Finally, we are ready to build this example. Click on configure, generate, and open project. This should open Visual Studio.

We will find several solutions to build. Right click on "exampleB1" in the solution explorer and click on, "Set as Startup Project." it will then become bolded. Right click it again and click, "Build."

In the Output, it should tell you that the project was successfully built, and a .exe file has been generated. Mine was generated in the path, 
```
C:\Users\my-user-name\Geant4\program_files\share\Geant4\examples\basic\B1\Release
```
In this directory, you will find a file called, exampleB1.exe. Double click it, and you should see it run!

It won't be anything fancy, but if you at least get a window opening, that's a good sign that Geant4 has been successfully downloaded. Congratulations!
