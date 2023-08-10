# Time Spent phase 2:

[home](README.md)

This is my record of time spent on phase 2 of my project. 

# Goal
Create an accurate and computationally efficient model of one single linac x-ray beam, and record the dose in a detector with numerical data as well as graphs. 

started: 7/30/2023

# Contents
- [Week 11](#week-11-731-86)
- [Week 12](#week-12-87-813)


# Week 11 7/31-8/6

**Geant4**
- [x] Finish the pointers tutorial (I finished the beginners tutorial but there's a lot more to learn)

**Research**
- [x] Find out the photon energy distribution of linac beams (Got some photos and data saved)
- [x] Decide which project to pursue moving forward. (Going to develop G4Brems and compare it to the data I found)

- 7/31 7:15 am 45 min making plan and studying about the photon energy distribution
- 7/31 2:05 pm 1 hr researching photon energy distribution
- 8/3 8:03 am 2 hrs tryin to find relative photon energies. UPDATE: I found some graphs to go off of, but I would still like to create my own data using G4-Brems. I created a target volume in G4-Brems, and tried to figure out how to do Bremsstrahlung in Geant4. I was looking over example "GammaTherapy," which uses Brems.., but I couldn't really make sense of it. It will be a good resource though. I am going to try and do what the Geant4 documentation suggests and do brems. in macro commands.
- 8/3 10:15 am 1.5 hrs going to look over the Geant4 documentation for brems. UPDATE: I successfully implemented my G4-Brems physics list. It is a basic EM list but including Bremsstrahlung using the G4eBremsstrahlung Geant4 class. Fingers crossed that it works!
- 8/3 5:41 pm 30 min working on pointers
- 8/4 1:00 pm 1 hr Let's try and figure out primarygenerator action with G4-Brems. UPDATE: I create the primarygeneratoraction class, but I need to figure out how to impliment it.
- 8/4 5:45 pm 45 min working on pointers
- 8/4 7:10 pm 1.5 Finishing up pointers essay
- 8/4 9:00 pm 30 min Testing for pointers and filming video


- ========================================

# Week 12 8/7-8/13

**C++**
- [ ] Put out 2 "pointers" videos 

**Geant4**
- [x] Finish implementing primary generator action
- [x] Get G4Brems working
- [ ] Display some graphs and data from the brems.

- 8/7 7:45 am 2 hrs making a weekly plan and working on pointers
- 8/7 10:00 am 1 hr switching gears and working on implimenting primary generator action in G4-Brems. UPDATE: 10:45 I think I have successfully implemented the primary generator action. Now I just need to get the thing working. I'm gonna try and just make the particles visible using mac files, but I suspect I'm gonna need to implement the event class somehow. UPDATE 2: 11:00 It's working! one thing I noticed is that the more the MeV, the more beams end up on the other side of the target. I want to add some macro commands to adjust the MeV possibly, so the user can do it from the GUI. This may not be the most important priority right now... I'm going to think for a little while and see what the next steps are.
- 8/7 2:48 pm 1 hr set up a collimator and a detector, and tried to set up scoreing but it's not working yet.
- 8/8 8:25 am 1 hr trying to get scoring to work on G4Brems. UPDATE: I'm trying out the G4VHit class. Also I did some progress on pointers, specifically learning about references.
- 8/8 11:15 am 1.25 hr continuing learning about hits in Geant4
- 8/8 2:20 pm 1 hr working on pointers
- 8/8 6:00 pm 30 min learning more about references and testing out some Geant4 examples with no luck.
- 8/9 9:00 am 1 hr Going to try and initialize all the classes in action initialization, and see what happens when I don't register bremsstrahlung as a physics process. UPDATE: I didn't need to add in bremsstrahlung specifically, because the basic em physics list already had it. (makes sense, it's a pretty basic process) Now I'm in the thick of implementing a sensitivedetector in G4_BREMS.
- 8/9 11:00 am 15 mins learning about multithreading
- 8/9 4:50 pm 45 min researching pointers
- 8/9 5:55 pm 1 hr trying to create my first release of G4-Brems... next steps: test stuff in another user to see what binaries will work on another machine.
- 8/9 7:10 pm 45 creating the first release of G4-Brems UPDATE: I could not figure it out... it's super hard to run a Geant4 app on a different computer.
- 8/9 8:00 pm 1 hr working on compiling Geant4 on other user UPDATE: it didn't work. Geant4 is SO FINIKY!!! NEXT STEPS: I am considering using [physino's](https://physino.xyz/gears) batch file to download all the geant4 datasets and set them as environment variables. This makes me nervous, but I guess I can also manually set them all...... Or I can manually set the ones that the app wants. I think I'll do that. And let's cross our fingers that this works! UPDATE: it didn't work. Upon running as an administrator, I could run the example because I have the datasets in my admin environment variables... However it ran without Qt which was interesting. It still (sort of ) worked too. I wish there was a way I could have an .exe file with ZERO dependencies. 
