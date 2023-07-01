# Installing and Compiling Geant4 with Qt visualization driver
6/29/2023
Note: this tutorial is for Windows 11 Geant4 v11.1.2 and Qt 5.15.14

This is a guide for installing Geant4 with the Qt visualization driver. If you want to install just Geant4 alone with no visualization, click [here.](Geant4-install-instructions.md)

Having a visualization driver for Geant4 is optional, but very helpful for beginners. Geant4 has many options for visualization, but a good beginnger-friendly tool is Qt. Qt is a software package that's used for making really nice GUIs. It uses OpenGL, (So make sure you have OpenGL libraries installed as well.) If you want to test and see if you have OpenGL installed, try installing [these examples](https://github.com/g-truc/ogl-samples) and running them. If you see some visualization, then you have OpenGL on your computer. 

There are four steps for installing Geant4 on windows:
* [Step 1: Install prerequisites](#step-1-install-all-the-prerequisites)
* [Step 2: Install and set up Qt](#step-2-install-and-set-up-qt)
* [Step 3: Build and install from source](#step-3-building-and-installing-from-source)
* [Step 4: Postinstall setup](#step-4-postinstall-setup)


## Step 1: Install all the prerequisites:

As explained in the Installation guide, we need to start by installing 3 prerequisites:
1. [Geant4 toolkit source code](#geant4-toolkit-source-code) 
2. [C++ compiler and library](#c-compiler-and-library)
3. [Cmake](#cmake)

### Geant4 toolkit source code

To download this, go to the [Geant4 main page](https://geant4.web.cern.ch), click on Download, and under the "Source code" header you want to download the .zip file.

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

CMake is an open-source, cross-platform family of tools designed to build, test and package software. Geant4 is designed to be installed with CMake, so we need to download it. To do so, go to the [CMake download website](https://cmake.org/download/), scroll down, and click the link to download the Windows x64 Installer. It should be an .msi file. Double click on the file, and follow the steps to install it. 

## Step 2: Install and set up Qt

Qt is a powerful GUI building program that costs $300 a month for professional use. Luckily, we can use it for free with an educational or open-source account. If you are working on research for a university, the educational account is a good option, but if you are using Geant4 for personal projects, you have to use the open-source account. 

To install Qt, first go to the [Qt website.](https://www.qt.io/) 

### Educational users:
If you are using Qt for educational purposes, you need to apply for an educational license. On the Qt homepage, go to the resources drop down menu, and under "Learn Qt tools" there is a link called, "[Get Qt Educational License.](https://www.qt.io/qt-educational-license)" Click on that, then scroll down and where it says "Qt Edu for Developers," click on "Get Qt now." That will bring you down to a form where you have to fill out your name, email, educational institution, etc. This is your Qt educational license application. Submit, and pretty soon you will get an email showing you your next steps. 

### Open source users:
If you aren't using Qt for educational purposes, you can still use Qt as an open source user. Click on the "[Download/try](https://www.qt.io/download)" link. There should be a little window that says, "[Open source user?](https://www.qt.io/download-open-source)" click on that. 

Make sure you read the terms and conditions. You can use the Qt for free as an open source user, but you have to contribute your project back to the Qt community. As long as you agree to the terms, you can go down to where it says, "Looking for binaries?" and then install the Qt installer for whatever operating system you are on.  

### The Qt installer
Either path you choose, you will end up with a Qt installer. Double click on it, and it will pop up a window. You are going to need a Qt account to use it, so enter your username and password.

The entire Qt package is HUGE... but luckily for Geant4 we only need one specific release of Qt. You want to choose the option, "custom installation" in the installer. Deselect everything, and only choose Qt version 5.15.14 specifically for visual studio 2019.

Before the installer installs Qt, it will tell you how many Gigabytes it will be. It should only be 1-2, maybe 3 Gigabytes. If it's way more, you did something wrong. Remember, you should only have one thing checked on the install page, Qt 5.15.14 for msvc2019.

Keep in mind, in the future Geant4 may work with Qt 6 or future versions, but for now it's just compatible with 5.

Most likely Qt will install in:
```
C://Qt
```

### Adding the Qt bin directory to Path
The last step we need to do for Qt before we compile Geant4 is add a certain bin directory to Path. Open up your environmental variables and on path add this directory:
```
C:\Qt\5.15.14\msvc2019_64\bin
```
IMPORTANT: If you have anything that uses a different version of Qt, (e.g. Anaconda), you NEED this new directory to be above that one on Path. The reason why is because when Geant4 compiles, it will look for the Qt binaries in the first instance of Qt. So if Anaconda is first on the list, Geant4 is going to try to compile with Qt6 instead of Qt5, and you'll get dll errors.

So make sure that the directory:
```
C:\Qt\5.15.14\msvc2019_64\bin
```
is near the beginning of Path.

## Step 3: Building and installing from source

The next step is installing and building Geant4 from the source files. The first thing I tried was using the [Instructions on the Geant4 website](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/installguide.html#buildandinstall). This method does everything from the command line using command prompt or powershell. Personally, I got a lot of bugs and issues with this approach, so I ended up going a different direction.

What ended up working for me was closely following Physino's YouTube tutorial, "[How to compile Geant4 on Windows](https://www.youtube.com/watch?v=GykiM1lPON4)." This approach uses the CMake GUI instead of the command line. 

### 1. Create the necessary folders.

Go to the directory where you saved the Geant4 source code .zip file.
```
C:\Users\my-user-name\Geant4
```
First, you want to un-zip the file, and you should end up with a folder called, "geant4-v11.1.1" or something similar. This is going to be your "source folder." Now we create a new folder which is going to be our "build folder". I named mine, "geant4-v11.1.1-build".

### 2. Use CMake GUI to build from source.

Open the CMake GUI application. At the top of the CMake GUI, there's a place to enter "Where is the source code" and right below it has a place for, "Where to build the binaries." Under "Where is the source code," enter the path to your geant4-v11.1.1 folder and under "Where to build the binaries," enter the path to the geant4-v11.1.1-build folder.

After choosing the correct folders, make sure you check the GEANT4_INSTALL_DATA option. It should be in one of the red-highlighted rows in the middle of the GUI with a check-box next to it.
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
There is an option in the GUI called, "CMAKE_CONFIGURATION_TYPES." This has several options such as Release, RelWithDebInfo, Debug, etc. Make sure you delete everything besides "Release" or "RelWithDebInfo" if you want to have the debug info included. I personally chose to delete everythin except "RelWithDebInfo."

### Qt setup:
There should be an option called GEANT4_USE_QT. Check that box.

### Finishing up the config and generation:

Finally, go to the bottom of the GUI and click "configure." 

You may see a new pop up called, "QT_DIR." if it says, "DIR-NOTFOUND," set the path to:

```
C:/Qt/5.15.14/msvc2019_64/lib/cmake/Qt5
```

Then press "configure" again.

More options will pop up, including Qt53DCore_DIR, Qt53DExtras_DIR, etc. Some of these will say, "DIR-NOTFOUND," That's fine. Just make sure the following options are not "DIR-NOTFOUND" and are in these directories:

```
QT_DIR: C:/Qt/5.15.14/msvc2019_64/lib/cmake/Qt5
Qt5_DIR: C:/Qt/5.15.14/msvc2019_64/lib/cmake/Qt5
Qt5Core_DIR: C:/Qt/5.15.14/msvc2019_64/lib/cmake/Qt5Core
Qt5Gui_DIR: C:/Qt/5.15.14/msvc2019_64/lib/cmake/Qt5Gui
Qt5OpenGL_DIR: C:/Qt/5.15.14/msvc2019_64/lib/cmake/Qt5OpenGL
Qt5PrintSupport_DIR: C:/Qt/5.15.14/msvc2019_64/lib/cmake/Qt5PrintSupport
Qt5Widgets_DIR: C:/Qt/5.15.14/msvc2019_64/lib/cmake/Qt5Widgets
```
As long as these are correct, everything should work just fine. Click configure again to see all the options turn white. 

then "generate," and finally "open project."

At this point, Visual Studio should open. 

Make sure you have the "ALL_BUILD" option selected in your solution explorer, then right click on ALL_BUILD and click on "Build."

After like an hour or more, it will finish building... But you're not quite done yet.

### 3. Don't forget to install the last little bit

For some reason, the Geant4 setup skips the "INSTALL" option which installs all the header files which are neccesary for the thing to run. So we need to find the "INSTALL" solution, and click build. Now the Geant4 is completely compiled.

## Step 4: Postinstall setup

[Geant4 postinstall setup instructions](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/postinstall.html)

To complete the installation of the Geant4 program, we need to set up 2 more things.

1. Add the Geant4 bin directory to PATH
2. Create a new environmental variable for the Geant4 datasets.

### You could use a .batch file, but...

On the Geant4 website installation instructions, they suggest using their experimental .batch file to add these variables automatically. Also, in Physino's YouTube tutorial, he offers his own batch file.

The main problem I found while examining both of these batch files is that they may not work properly, and are not very future-proof. For example, Physino's batch file was out of date and included a folder that the new version of Geant4 doesn't even include. I tried the Geant4 experimental batch file, but it just didn't do anything. Using a batch file is a nice idea, but in this tutorial, I will show how to manually add these variables. 

### 1. Add the bin directory to PATH

If you go into the folder where you have your program files, (where you set your INSTALL_PREFIX, for me it was in the "program_files" folder) you will find four folders: "bin," "include," "lib," and "share." We need to add this "bin" folder to the system PATH. 

To add this to PATH, click on the windows button and search, "environment variables." Click on the "edit system environment variables" link. This opens up a "System Properties" window. At the bottom there should be a button labelled, "Environment Variables." Click on this.

The "Environment Variables" window should now be displayed. There should be two sections, the top should be, "User variables," and the bottom should be, "System variables." In the User variables, there is one labelled, "Path." (If you don't have the path variable, click on "New" and create a variable named "Path" or "PATH". Path is used by many programs, so it's nice to have.)

Once you have clicked on the "Path" variable, a window called, "Edit environment variable" is displayed. Click "New," and add your bin directory here.
```
C:\Users\my-user-name\Geant4\program_files\bin
```

Once you add this variable, it is important that you click the "OK" button in all windows until everything is closed. Doing this will save the change.

Once you add the bin directory to path, Geant4 will know where to look to find the essential binary files to be able to run.

### Create a "Datasets" environmental variable.

Using the same environmental variables window, we need to create a new variable called, "GEANT4_DATA_DIR". 

Go ahead and open the environmental varaibles window again by clicking the windows button and searching for it. Then, under User variables, click "New..." It will ask for the variable name, and the variable value. For "Name", enter in:
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

Now, we are going to try and run one of the Geant4 examples to make sure Geant4 is installed correctly.

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

We will find several solutions to build. Right click on "exampleB1" in the solution explorer and click on, "Set as Startup Project." it will then become bold. Right click it again and click, "Build."

In the Output, it should tell you that the project was successfully built, and a .exe file has been generated. it will also tell you where the executable file is. Mine was generated in the path, 
```
C:\Users\my-user-name\Geant4\program_files\share\Geant4\examples\basic\B1\Release
```
In this directory, you will find a file called, exampleB1.exe. Double click it, and you should see it run!

At this point, you should see the Qt GUI, which is really nice. You can initialize a viewer by running vis.mac, and you should see the example B1 displayed beautifully. Congratulations, you have complied Geant4 with Qt. 

## References
### Geant4:
* [Geant4 website](https://geant4.web.cern.ch/)
* [Geant4 source code download](https://geant4.web.cern.ch/download/11.1.1.html)
* [Visual Studio download](https://visualstudio.microsoft.com/downloads/)
* [CMake download](https://cmake.org/download/)
* [Getting C++ support on Visual Studio YouTube tutorial](https://www.youtube.com/watch?v=OMa2xDjdXJw)
* [Geant4 Installation instructions](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/installguide.html#on-windows-platforms)
* [Geant4 Post-install setup](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/postinstall.html#required-environment-settings-on-windows)
* [How to compile Geant4 on windows Physino YouTube tutorial](https://www.youtube.com/watch?v=GykiM1lPON4)
* [How to compile a Geant4 example Physino YouTube tutorial](https://www.youtube.com/watch?v=nY-vO6yN65c&t=67s)
* [Geant4 forumn (for help!)](https://geant4-forum.web.cern.ch/)

### Qt:
* [Qt website](https://www.qt.io/)
* [Install Qt5 for Geant4 Physino YouTube tutorial](https://www.youtube.com/watch?v=p-MRo4LJNCQ)

### Other:
* [Dependency walker app (for broken DLLs)](https://www.dependencywalker.com/)
