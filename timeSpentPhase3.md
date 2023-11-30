# Time spent phase 3

Goal:
- Create a 1D Linac beam model, with graphs of PDD
- Discuss accuracy with other people's research

Contents
- [Week 1](#week-1-1030-115)
- [Week 2](#week-2-116-1112)
- [Week 3](#week-3-1113-1119)
- [Week 4](#week-4-1120-1126)
- [Week 5](#week-5-1127-123)

# Week 1: 10/30-11/5
Goals:
- [ ] Put out G4 Brems v060 vid
- [ ] Prove the accuracy of G4-Brems using the claimed bremsstrahlung process in the g4 documentation, for the cross sections. Basically I need to analytically make the graph using mathematica or something
- [x] Make the g4-linac beam video
- [ ] Make documentation for g4-brems

- 10/30 1:00 pm .25 hr running a test on G4-Brems, and emailing professors
- 10/30 5:20 pm 1.25 hr planning phase 3 and looking at the geant4 claimed bremsstrahlung spectrum, trying to graph their analytical data.
- 10/31 9:16 am .5 hr looking at the g4-app video I started, and prepping for g4-medical-linac
- 10/31 10:40 am 1.25 hr recording the beginnings of g4-medical-linac
- 10/31 3:00 pm 1.5 hr prepping and talking to brother kelley about next steps, also messing with g4-brems more
- 11/2 4:50 pm 2.25 hr working on g4 med linac and learning about geant4 with python. UPDATE: I almost got g4 med linac going but there's a bug with the visualization
- 11/2 9:39 pm 2 hr trying to see if I can get geant4 with python. UPDATE: I'm almost done with the whole basic program in python
- 11/4 9:59 am .5 hr working on g4 python, I can't get it to work, I think it might be an issue with the docker image. 
- 11/4 1:01 pm 1.5 hr working on g4 python docker image
- 11/4 3:45 pm .75 hr pushing my first g4 python image to docker hub
- 11/4 5:47 pm 1 hr trying again to push my image to docker, and testing it
- 11/4 10:50 pm 1 hr finishing up g4-brems. UPDATE: It's basically done for now, I got the absolute and relative energies being recorded.


# Week 2: 11/6-11/12
Goals:
- [x] Put out G4 Brems vid
- [ ] G4Brems documentation
- [x] Get the basic functionality of med linac done
- [x] record videos
- [x] Put out first med linac video

- 11/6 5:36 pm .75 hr working on g4 med linac. Note: I'm going to start where I left off on G4-Brems
- 11/6 8:29 pm 1 hr working on med linac
- 11/8 12:35 pm .25 hr setting up first detector in med linac
- 11/10 11:05 am 1 hr working on the g4-brems release UPDATE: Finished release 0.6.1, time to make the video
- 11/10 12:05 pm .25 hr working on med linac
- 11/10 8:35 pm 1 hr working on med linac. UPDATE: I got the gun all contained in one volume, now just to get the primarygeneratoraction to start shooting particles from there. Also I need to allow for rotation in the med linac head.
- 11/10 10:44 pm 2 hrs getting the medical linac beam head movable. UPDATE: Now the head can move and rotate, and the beam moves and rotates accordingly. I also created the release notes for medical linac v0.1.0 and tomorrow I will make the video.
- 11/11 12:25 pm 1 hr recording g4-brems video
- 11/11 2:11 pm 1 hr recording med-linac video
- 11/11 3:24 pm 1.75 hr editing g4 brems video
- 11/11 5:35 pm 1 Posting g4-brems video

# Week 3: 11/13-11/19
- [ ] Get that G4 Brems graph from b. Oliphant's book, and return it!
- [x] Edit and post g4 med linac video
- [ ] Edit and post g4 med linac pt 2 video
- [ ] Get a PDD graph
- [ ] Get a beam profile
- [x] Get a lead box around linac head
- [ ] and a flattening filter

- 11/14 9:07 am 1.75 hr editing med linac and researching beam profile and pdd articles UPDATE: Got 3 articles read and their graphs saved, I just need to analyze them. Also edited the entire part 1 of my med linac videos.
- 11/14 7:53 pm 2.5 hr going over b. oliphant's article one last time to see if I can get relative energies. Then editing med linac. UPDATE: I posted med linac v010 video, (Just the demo not the code) and then I coded in a lead protector around my linac head.
- 11/15 5:15 pm 1 hr reading more about PDD and trying to quickly create a pdd graph. UPDATE: Got the phantom to be a sensitiveDetector, and started registering hits.
- 11/15 7:20 pm .5 hr Making a big hitsCollection For the entire run on med linac UPDATE: I decided to not do that, instead using analysis and skipping the hitscollecting. But at least I have a hitsCollection for each event.
- 11/16 12:47 am .75 hr getting that H3 made in med linac. update: it's made, but doesn't display anything.
- 11/16 8:40 am 2 hrs seeing if I can figure out the histogram, or maybe just create a H2
- 11/16 1:53 pm .5 hr looking at the presentation I have to do for the conference, and talking to b. kelley about it.
- 11/17 10:45 pm .25 hr signing up for RCW conference
- 11/18 7:54 pm 1.5 hrs working on the med linac PDD graph and visualization

# Week 4: 11/20-11/26
- [ ] Get pdd graph
- [ ] beam profile
- [ ] heat map
- [ ] flattening filter

- 11/21 9:03 am 2 hrs working on pdd graph. update: I changed the whole thing around so it's using steppingAction and runAction instead of SD, but the only issue now is getting the depth relative to the detector instead of absolute position in the world
- 11/24 10:30 am 1.75 hrs researching geant4 some more and how to have a universal geant4 app, also messing around with the PDD graph in med linac

# Week 5: 11/27-12/3
- [ ] Get to a point where I can present for the RCW conference
- [ ] Get a heat map at the end of the run

- 11/27 9:27 am .5 hr planning how to get a heat map
- 11/29 5:20 pm .75 hr making a heat map, it's not that great but it's there
