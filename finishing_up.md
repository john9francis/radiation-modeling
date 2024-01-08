# Time spent finishing up:

# Contents
- [Week 1](#week-1-1224-1230)
- [Week 2](#week-2-1231-16)
- [Week 3](#week-3-17-113)

# Week 1: 12/24-12/30

**Goals:**
- [ ] Fix the bug for theta pi - 2pi

- 12/27 9:16 pm .25 hr seeing if I can get the particle gun to be a child in the detector construction
- 12/28 2:17 pm .5 hr trying again to see if I can make the particle gun a child of the detector construction. also trying to decide the organization. Where are things going to start? in the singleton? I'm thinking to create the geometry in construct() and then register the pointers to the singleton to move around. UPDATE: It's just not gonna work that way. I have to keep track of the position and rotation of the linac head to apply it to the particle gun. Much like what i have been doing just debug it.
- 12/28 2:58 pm 1 hr researching moveable geometry in geant4 and trying to track down the issue. 

# Week 2: 12/31-1/6

**Goals:**
- [x] Research memory allocation
- [ ] Make the C++ memory allocation article
- [ ] Make the C++ memory allocation video

- 1/4 10:27 am 1 hr researching memory allocation in C++ and working on the pointers website
- 1/5 8:17 pm 1.5 hr cleaning up med-linac UPDATE: Severely improved the singleton with memory safe stuff. Also got the detector construction to start the particle gun in the correct spot.
- 1/6 9:33 am 2 hrs looking into using a messenger without a singleton. UPDATE: I made a new branch for messenger without singleton. detector construction handles the moving around. it seems to work super good! I might push it to main.
- 1/6 8:31 pm 2 hrs working on moving the linac head all around. update: got it working! next step is to allow small shifts with commands, then I can start simulations of it rotating around. I also need to fix up the github repo... it's a mess.

- ===================================================================================

# Week 3: 1/7-1/13

**Goals:**
- [ ] Get the small movements done in med linac detector messenger
- [ ] Put out first med linac code video
- [ ] Put out video for release 2 of med linac
- [ ] put out that code video
- [ ] clean up the github repo
- [ ] After all that the next step would be to set up some analysis runs with ui commands.

- 1/8 6:23 am 1 hr trying to find and post the first med linac code video UPDATE: Edited about half of the med_linac v010 video, and optimized this new release of med_linac so that it sends vectors and matrices to the primaryGenAction instead of physical volumes.
