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
- [ ] Finish the pointers tutorial

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
- [ ] Finish implementing primary generator action
- [ ] Get G4Brems working
- [ ] Display some graphs and data from the brems.

- 8/7 7:20 making a weekly plan and working on pointers 