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

# Week 4: 6/12 - 6/18

**Geant4**
- [ ] Get Geant4 installed.
- [ ] Run one test Geant4 project
- [ ] Run at least one Geant4 example from the website

**Research**
- [ ] Read more about linacs to get comfortable with how they measure dose.

**Shadowing**
- [ ] Turn in my onboarding info to cape fear hospital by email
- [ ] Email David Fentner to let him know I'm ready to shadow and my schedule.

- =================================================================================
- 6/12 **Plan:** delete my Geant4 folder and try installing it again. This time install "ALL" and "INSTALL" at the same time.
- 6/12 6:20 pm 30 min Starting with a clean slate to try and download Geant4 again. Installing both "ALL" and "INSTALL" at the same time isn't gonna work with my setup, because I'm using the visual studio GUI, so I'll just wait for "ALL" to finish and then i'll do the "INSTALL." I'm building this in the "RelWithDebInfo" configuration.
