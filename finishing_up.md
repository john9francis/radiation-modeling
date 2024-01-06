# Time spent finishing up:

# Contents
- [Week 1](#week-1-1224-1230)
- [Week 2](#week-2-1231-16)

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
