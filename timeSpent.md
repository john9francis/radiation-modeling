# Time Spent:

This file is a record of the time I have spent on this project. 

Started: 5/22/2023

## Contents:

* [Long term goals](#long-term-goals)
* [Project plan](#project-plan)
* [Week 0](#week-0-517)
* [Week 1](#week-1-522-528)
* [Week 2](#week-2-529-64)
* [Week 3](#week-3-65-611)
* [Week 4](#week-4-612-618)
* [Week 5](#week-5-619-625)
* [Week 6](#week-6-626-72)
* [Week 7](#week-7-73-79)
* [Week 8](#week-8-710-716)

# Long term goals:

- 400 total hours
- 16 weeks before school starts
- 14 weeks of the semester
- ~ 14 hours a week 
- or 20 hours a week until school starts and 6 hours a week when school is in session

# Project plan: 
### Phase 1 (6 weeks):
- Create a model of a stationary x-ray LINAC and the radiation activity at different distances, amounts of time, and voltages.
- Implement a method to convert that activity into exposure
### Phase 2 (6 weeks): 
- Create a model of a person (for now, just one circular cross-section) with a tumor in the center
- Modify the linac model to be able to rotate around the person 
- Record the exposure in each layer of the body
### Phase 3 (6 weeks):
- Add attenuation to the model. The beam will lose energy as it passes through layers.

### Further work (the rest of the time): 
- Add functionality for the tumor to be anywhere in the cross-section, not just the center.
- Make the person model a bit more realistic. Mark out the cross section with organs, bones, etc.
- Implement a method to convert the exposure into effective dose. Record the effective dose in each of the different organs.
- Repeat everything with proton therapy instead of x-ray therapy

# Week 0: 5/17
 - 5/17 8:45 am 8 hours shadowing Dr. Mghari, lead medical physicist at cape fear hospital. Learned about dosimetry and linac machines, as well as many different types of radiotherapy. 

# Week 1: 5/22-5/28

Goals: 20 hours

- [x] Come up with some research papers to read and learn more about medical radiation procedures
- [x] Set up GitHub repository
- [x] Make a Python virtual environment
- [x] Make a plan for the project

- 5/22 9:00 pm 2 hrs Working on setting up GitHub and coming up with time periods for the project, setting up virtual environment. 
- 5/23 5:50 pm 1 hr Research medical equipment websites to see which tools they use and researched how they work
- 5/24 7:15 pm 1.5 hrs Researched how the LINAC works (it's just a high energy x-ray beam) and looked into how proton therapy works. Also got about 4 research papers collected to read
- 5/25 3:45 pm 2 hrs Things I got done: 1. Learned about units: Grays are units of "dose" which is the damage done by the photon beam. 2. I compiled a bunch of graphs and papers about dose from an x-ray photon beam. 3. I wrote a short paper summarizing my goals for this project. 
- 5/26 9:30 am 1 hr looked through about 5 research papers. I have been seeing the PDD (percentage depth dose) vs. depth graph a lot. Next thing to do is really understand what this graph is saying. 

# Week 2: 5/29-6/4

- 5/29 9:25 pm 15 minutes working on a project plan and timeline
- (Memorial day vacation, didn't do much )

# Week 3: 6/5-6/11
- [x] Figure out how to measure the radiation damage to the body. What affects the area, is it time? area? voltage? 
- [x] Read a research paper about how an x-ray beam from a LINAC can affect the body
- [ ] Get a model of the activity per distance of a LINAC completed.

- 6/5 4:23 pm 1 hr Learned that "Dosimetry" is the field of measuring how much dose each part of the body recieves. Learned all about activity vs. exposure including the units of Bq, Gy, and Sv. Next step is learning the correlation between activity and distance and then coding something.
- 6/6 12:30 pm 2 hrs added some sources to my notes from yesterday. Also learned that activity follows the inverse square law for distance. Tried to write a simple program demonstrating the inverse square law, but I need to do more research on it because I'm not completely understanding it. 
- 6/7 9:00 am, 1:00 pm, 1 hr I have the unique opportunity to shadow an administrator at Landaur medical physics. He provides imaging and treatment machines to hospitals. This morning I completed the onboarding training to be considered to shadow him.
- 6/7 2:00 pm 1 hr worked on repo organization and learned more about the inverse square law
- 6/8 11:39 pm 2 hours researching LINAC's and how much activity they might have at a distance, I found out some info. First, it seems like they don't really measure activity of these beams, they skip right to measuring exposure aka dose. To end off today I'm going to look into Geant4, it seems like a super powerful C++ library we could use for modeling an x-ray beam. UPDATE: I did tons of research into Geant4... it might be an option although it seems pretty complex.
- 6/9 8:40 am 3 hrs. Looking into installing Geant4 and learning more about it. Also deciding which direction i want to take moving forward. 
- 6/9 2:07 pm 3 hrs installing Geant4 virtual machine. this is a super involved process. I couldn't even get it working yet
- 6/9 5:30 pm 30 min playing with linux and virtualBox to learn how it works. next step is **Downloading Geant4 using Linux command line in VirtualBox** just kidding, I can do it on windows turns out
- 6/9 9:30 pm 1.5 hrs Get Geant4 up and running or bust!
- 6/10 11:00 pm 2 hrs Installing Geant4... Got about 60-70 percent done with it. I GOT AN ERROR: "library limit of 65535 objects exceeded when I tried to build the "INSTALL" solution. My hypothesis is that since this is my third time trying to install this, I need to uninstall some of the old ones and then try again. I'll do more research to make sure.

# Week 4: 6/12-6/18

**Geant4**
- [x] Get Geant4 installed.
- [ ] Run one test Geant4 project
- [x] Run at least one Geant4 example from the website

**Research**
- [x] Read more about linacs to get comfortable with how they measure dose.

**Shadowing**
- [x] Turn in my onboarding info to cape fear hospital by email
- [x] Email David Fentner to let him know I'm ready to shadow and my schedule.

- 6/12 **Plan:** delete my Geant4 folder and try installing it again. This time install "ALL" and "INSTALL" at the same time.
- 6/12 6:20 pm 30 min Started with a clean slate to try and download Geant4 again. Installing both "ALL" and "INSTALL" at the same time isn't gonna work with my setup, because I'm using the visual studio GUI, so I'll just wait for "ALL" to finish and then i'll do the "INSTALL." I'm building this in the "RelWithDebInfo" configuration.
- 6/12 9:30 pm 45 min Did more research about LINACs. I think I'm going to go with the specific "Varian VitalBeam" linac. Found out that the photon energy configuration is ~6 to 10 MV. ALSO, successfully started the INSTALL build for Geant4.
- 6/13 9:00 am 1 hr Finishing the Geant4 install. Now I just need to test it and make sure it works.
- 6/13 10:30 am 45 min Succesfully running a Geant4 example... Only problem is I have no idea what's going on with it. Next step is to learn the Geant4 UI.
- 6/14 1:00 pm 30 min completely signed up for shadowing at Cape Fear hospital
- 6/14 2:00 pm 1 hr Working on my "geant4-installation-instructions" document
- 6/14 3:51 pm 1 hr Finishing up that document
- 6/14 5:15 pm 3 hrs Made YouTube video about how to install Geant4
- 6/15 1:50 pm 1 hr Learning more about how linacs measure dose. Found two articles I can use to check my work. Learned about PDD and dose profile. 

# Week 5: 6/19-6/25

**Geant4:**
- [ ] learn how to use the GUI
- [ ] run an example project
- [ ] figure out how to modify the code in an example

**Research**
- [ ] Nail down how a linac characterizes a beam and measures dose
- [x] make a presentation to make sure i understand it good
- [x] make a google sheet to make sure I'm on track on my goals

**Shadowing:**
- [x] come up with questions to ask mr. fentner
- [x] shadow david fentner once 

- 6/19 10:10 am 1 hr coming up with questions to ask mr. fentner, and starting my presentation of how linacs work
- 6/19 5:20 pm 2 hrs working on presentation 
- 6/20 10:00 am 4 hours shadowing mr. fentner, diagnostic medical physicist.
- 6/20 4:00 pm 1.5 hrs Working on a google sheet to plan my project, and writing down what I learned from mr. Fentner.
- 6/20 10:20 pm 1 hr working on the linac presentation. Next step is really classifying a linac. Like what dose exactly does a 6MV beam give? Then we recreate it using Geant4. Also, I need to get started on geant4 figuring out how to use it.
- 6/21 11:00 am 2 hrs trying to figure out how to use the Geant4 GUI, looking into visual options like Qt. PLAN: run every option in example b1 to see what they all do.
- 6/21 6:15 pm 1 hr messing with Geant4 GUI. found out i need get a visualization driver attached
- 6/22 11:00 am 45 mins researching OpenGL. Next step, download OpenGL with visual studio and then figure out how to attach it with Geant4. (putting it in the environment variables with priority=1. On the powerpoints it should have something to help with that.)
- 6/22 11:30 pm 45 min looking into installing openGL on visual studio. Also tried out all the macro files for B1... Nothing is displaying.
- 6/23 1:40 pm 1 hr did a TON of research in the Geant4 for app developers book, and I came to the conclusion to re-download Geant4 with the Qt driver.
- 6/23 3:30 30 min Trying to compile Geant4 again but this time with OGL selected.
- 6/23 6:25 15 min Compilation finished, now gonna finish building and test an example. Nothing displayed AGAIN. I really don't want to use Qt... but I probably have to. It just has all those weird licenses and stuff.
- 6/24 6:00 30 mins applying for Qt educators license and trying one more time without Qt
- 6/24 8:30 pm 4 hours compile Geant4 with Qt or bust! NOTE: if this works, I should make a tutorial for installing Geant4 with Qt. Also, I should summarize my Geant4 findings so far and put them in my paper. UPDATE: I got an error when compiling. I’m going to try again another day with a different version of Qt. Last thing for tonight is reading the GitHub Geant4 release notes to see if it says anything about Qt. None of the release notes for the last year mentioned anything about the Qt version. Maybe I'll try the lastest version and see if it works. Or maybe I'll ask the Geant4 forum. Found out that Qt specifically the Qt5OpenGL.dll file has a lot of dependency issues. The installation must have messed up. :( that makes this complicated.

# Week 6: 6/26-7/2

**Geant4:**
- [x] Get it compiled with Qt, or a different visualiztion driver.
- [x] Run an example with visualization

**Research**
- [ ] Learn how to convert MV to Grays.
- [ ] Make a small program to convert any units back to Grays
- [ ] Learn more about dose RATE as opposed to just dose

- 6/27 10:07 am 1.5 hrs gonna figure out this Qt dll error. UPDATE: I'm gonna try to uninstall and reinstall Qt and Geant4, and if it still doesn't work, I'll post something on the forum.
- 6/27 12:38 pm 2 hrs I'm gonna try and compile Geant4 again with Qt. UPDATE: it's currently compiling. Hoping for the best...
- 6/27 3:30 pm 1 hr trying an example with Qt. fingers crossed! Update: of course it didn't work. I realized I may have a conflicting Qt version because I have anaconda installed. Trying a new Geant4 build, this time with my path rearranged so that the Qt5 directory is before the anaconda one.
- 6/27 pm 15 min IT WORKED!!! Now I just need to figure out how to interact with example1.
- 6/29 10:06 pm 1 hr gonna try some commands with the geant4 gui UPDATE: I got example 1 ran with visualization. You just need to run the vis.mac file. Super excited. I also checked out the advanced example 'medical linac', but I coundn't get it to run.
- 6/30 9:00 pm 1 hr working on the Geant4 with Qt install directions. 
- 6/30 10:45 pm 45 min researching macro commands for the example files. Also brushing up on my C++. Getting ready to start next week on a Geant4 project.
- 7/1 9:30 pm 1 hr. preparing and learning as much as I can about the Geant4 structure before next week I start a simple Geant4 app of my own. 

# Week 7: 7/3-7/9

**Geant4**
- [x] Code at least half of my "photon shooter" application
- [x] Learn about detectors in Geant4
- [x] Make Geant4 with Qt tutorial 

**Research**
- [ ] Learn what it means to have a 6 MV beam, how many photons / second is that?

- 7/3 10:28 am 2 hrs researching photons/second in a 6 MV beam, and made half the geant4 with Qt tutorial video 
- 7/3 2:00 pm 3 hrs making Geant4 with Qt tutorial vid
- 7/4 STARTING GEANT4 2 WEEK PROJECT: I'm logging my time in a different file, so I will log chunks of time in here periodically.
- 7/8 6 hrs Geant4 project. So far I have it to it can run a Geant4 app in interactive or batch mode.

# Week 8: 7/10-7/16

**Geant4**
- [ ] study and learn about example B1
- [ ] finish "photon dose sim"

**Research**
- [ ] learn about ion chambers
- [ ] learn more about how photons turn into dose

**Shadowing**
- [x] ask questions to dr. mghari
- [x] possibly shadow mr. fentner

- ================================================================================

- 7/11 9:00 am 1.5 hr learning from dr. mghari medical physicist and diana the dosimetrist
- 7/12 10:00 am 3 hours shadowing david fentner diagnostic medical physicist 
- 7/12 3:45 pm 45 min writing down what i learned from shadowing this week

