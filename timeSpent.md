# Time Spent:

This file is a record of the time I have spent on this project. 

Started: 5/22/2023

## Contents:

* [Long term goals](#long-term-goals)
* [Project plan](#project-plan)
* [Week 1](#week-1-522-528)
* [Week 2](#week-2-529-64)
* [Week 3](#week-3-65-611)

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

# Week 2: 5/29 - 6/4

- 5/29 9:25 pm 15 minutes working on a project plan and timeline
- (Memorial day vacation, didn't do much )

# Week 3: 6/5 - 6/11
- [x] Figure out how to measure the radiation damage to the body. What affects the area, is it time? area? voltage? 
- [ ] Read a research paper about how an x-ray beam from a LINAC can affect the body
- [ ] Get a model of the activity per distance of a LINAC completed.

- 6/5 4:23 pm 1 hr Learned that "Dosimetry" is the field of measuring how much dose each part of the body recieves. Learned all about activity vs. exposure including the units of Bq, Gy, and Sv. Next step is learning the correlation between activity and distance and then coding something.
- ================
- 6/6 12:30 pm 2 hrs added some sources to my notes from yesterday. Also learned that activity follows the inverse square law for distance. Tried to write a simple program demonstrating the inverse square law, but I need to do more research on it because I'm not completely understanding it. 
- 6/7 9:00 am, 1:00 pm, 1 hr I have the unique opportunity to shadow an administrator at Landaur medical physics. He provides imaging and treatment machines to hospitals. This morning I completed the onboarding training to be considered to shadow him.
- 6/7 2:00 pm worked on repo organization and learned more about the inverse square law
