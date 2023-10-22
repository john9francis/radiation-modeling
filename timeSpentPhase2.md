# Time Spent phase 2:

[home](README.md)

This is my record of time spent on phase 2 of my project. 

# Goal
Create an accurate and computationally efficient model of one single linac x-ray beam, and record the dose in a detector with numerical data as well as graphs. 

started: 7/30/2023

# Contents
- [Week 11](#week-11-731-86)
- [Week 12](#week-12-87-813)
- [Week 13](#week-13-814-820)
- [Week 14](#week-14-821-827)
- [Week 15](#week-15-828-93)
- [Week 16](#week-16-94-910)
- [Week 17](#week-17-911-917)
- [Week 18](#week-18-918-924)
- [Week 19](#week-19-925-101)
- [Week 20](#week-20-102-108)
- [Week 21](#week-21-109-1015)
- [Week 22](#week-22-1016-1022)
- [Week 23](#week-23-1023-1029)


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


# Week 12 8/7-8/13

**C++**
- [ ] Put out 2 "pointers" videos
- [x] I ended up putting out 1 video :)

**Geant4**
- [x] Finish implementing primary generator action
- [x] Get G4Brems working
- [ ] Display some graphs and data from the brems.
- [x] I ended up displaying the hits on the console!

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
- 8/9 10:45 pm 1 hr 20 min working on pointers and references.
- 8/10 TODO: put out the pointers and references tutorials!
- 8/10 9:09 am 35 min making pointers and references videos
- 8/10 10:13 am 1.25 hr Let's try and figure out how to register hits in G4-Brems.
- 8/10 3:30 pm 1 hr recording pointers video.
- 8/10 5:55 pm 1.25 hr editing pointers video
- 8/11 12:27 pm 1.25 hr working on project plan and implementing stepping action (slow and steady)...
- 8/11 3:30 pm 35 min Working on references tutorial
- 8/11 4:27 pm 1 hr Working on stepping action, and created HitsCollection class.
- 8/11 6:44 pm 30 min Let's get some hits printing!!! UPDATE: it's still not quite printing, I think I need to look into the PrintAll() function from HitsCollection.
- 8/11 9:50 pm 1 hr Finally got hits printing out to the console!!! this is great news. There are many kinks to be worked out but it's something for sure! It prints the energy and position. Super great stuff.

# Week 13 8/14-8/20

**G4 Brems**
- [x] Get accurate hits displaying in console
- [ ] Possibly get some graphs started for the hits

**C++**
- [ ] Put out a references C++ vid
- [ ] Put out a constructors and destructors vid

**G4 Brems v1.0.0**
- [ ] Make a docker for G4Brems v1.0.0
- [x] Put out a G4Brems v1.0.0 vid


- 8/14 9:45 am 35 min Working on making a docker for G4Brems v1.0.0 UPDATE: 10:18 am got the branch release-v1.0.0 all ready, now I'm going to look at docker.
- 8/14 11:18 am 1.25 hrs Looking into getting started with docker. It's gonna be complex to get a geant4 app into docker... Maybe I try with a simpler app first, and then go into Geant4. My plan moving forward is to play around with ubuntu and figure out how to download Geant4 using it. Then, I will be able to create a dockerfile with the same commands. **PS. we can use the vscode WSL extension to help us out with this!**
- 8/14 1:27 pm 2 hrs Let's keep working on G4-Brems and see what is going on with the Hit.print() function. 
- 8/14 5:05 pm 35 min Implimenting eventaction class so we can keep track of how much energy deposited in each step 5:20 switching gears and learning about docker with openGL.
- 8/15 10:08 1.25 hr Let's do a simple docker project. UPDATE: spent the time messing with WSL to see if I could get Geant4 downloaded, succeeded in downloading conda and that's it. I still need to add it to path before using it. 
- 8/15 8:00 pm 1 hr working on G4-Brems getting those hits registered. Update: I went with a different method, using event action instead! it seems to work great!
- 8/15 9:50 pm 35 min Let's work on the releases of G4-Brems. I gotta write some notes on Release 1.0.0 and come up with release 1.1.0 as well. UPDATE: I had semantic versioning all wrong lol but I did create release notes for the first release of Geant4, release 0.1.0-alpha1
- 8/16 9:50 am 1 hr Working on G4-Brems release v0.1.0-alpha1 recording
- 8/16 11:11 am 1 hr editing video
- 8/16 12:30 pm 3 hrs finished video editing and learning more about radiotherapy
- 8/17 8:00 am 2 hrs working on installing Geant4 in wsl and docker. UPDATE: I got all the prereqs installed in WSL, so now I just have to run a Geant4 project.
- 8/17 11:15 am 45 min Continuing to figure out how to run a Geant4 project
- 8/18 9:20 am 1 hr Cleaning up G4-Brems code UPDATE: 20 minutes in we got all the unnecessary classes deleted, and now we're working on getting units on that energy. UPDATE: 40 mins in we created a new branch for release v0.2.0-alpha1 where the energy is displaying on the console with units. Now I'm going to try and find the correct dimensions of the tungsten target, collimator, etc. FINAL UPDATE: I am getting some good info on the dimensions of all the little parts, the target, collimator, etc. But I need more. If I want this to be super accurate, I need some concrete data.
- 8/18 12:55 1.5 hrs Looking more into measurements, and cleaning up more G4-Brems. Now we can display the energy and the position, but it's still weird with multithreading... We need a way to keep one specific particle with all of it's OWN attributes.
- 8/18 2:40 pm 35 min Let's switch gears and try and find a CMakeLists file that works for Linux with the conda Geant4 environment. UPDATE: it's currently installing dependencies, it's gonna take awhile.
- 8/18 5:53 pm 25 min Let's try and run that Geant4 app in Linux now. UPDATE: Still workin' on it
- 8/18 6:55 pm still trying to build Geant4 on Linux
- 8/18 11:30 pm 1 hr making slow and steady progress building geant4 on linux
- 8/19 11:00 am 1 hr trying to get Geant4 Hello World to work and it still ain't workin.

# Week 14 8/21-8/27

**G4 Brems**
- [ ] Power through and finish!!!
- [x] Put out 0.2.0 vid!
- [ ] now put out 0.3.0 vid!

**Docker**
- [x] Get Geant4 running on WSL
- [ ] geant4 on linux vid

**Other**
- [x] Email prof. Kelley my progress
- [x] G4-Hello-World debugging


- 8/21 11:11 am 1 hr planning week and emailing bro kelley, and researching accumulables in Geant4
- 8/21 12:45 pm 1.5 hrs Working on getting hits into runaction. UPDATE: I used G4VHit and G4THitsCollection to create a hit in the eventaction class and then save it to the hitscollection in the runaction class. It works!
- 8/21 2:30 pm .5 hr Gotta create release notes for 0.2.0 and 0.3.0! UPDATE: I ran into a bug. The 0.2.0 branch won't configure with cmake...?
- 8/21 7:41 pm 1.5 Let's debug why cmake isn't working and also finish getting geant4 WSL. UPDATE: found out that the cmake bug was about path-length limit! I had a really really long path to get to the source code. UPDATE 2: We got Geant4 running on WSL!!! I have all the notes recorded in g4-docker repo. I have some debugging to do with G4-Hello-World
- 8/22 10:27 am 1 hr Working on geant4 on linux tutorial
- 8/22 1:12 pm 2 hrs making G4-Brems v0.2.0 video
- 8/22 7:00 pm 2 hrs finishing up editing v0.2.0 video
- 8/23 8:00 am 1 hr Posting video and responding to question from another person working on Geant4
- 8/23 9:00 am 1 hr deciding what to do next, and debugging G4-Hello-World
- 8/23 11:40 am .5 hr debugging G4-Hello-World and making it work on linux and mac UPDATE: I got it configured for mac and linux, now just need to finish the geant4 installation with linux instructions.
- 8/23 12:15 am .75 hr Trying to impliment an average function with RunAction to average the energies (G4-Brems)
- 8/23 5:48 pm .25 hr Working on G4-Brems v0.3.0 release. I decided to adjust the organization a little bit and try and merge with main branch. We will see what happens.
- 8/23 8:04 pm 1.75 hrs Working on v0.3.0 and getting it ready UPDATE: Not only is v0.3.0 (basically) ready (besides some useless "print" code in EventAction) v0.3.0 is pretty much ready! also, I completely finished G4-Hello-World debugging! Next step: migrate all the G4-Hello-World cmake settings into G4-Brems. Also my next video to get out will be how to install Geant4 on Linux, featuring G4-Hello-World.
- 8/24 7:27 am 2 hrs Finished g4 Linux install instructions
- 8/24 10:15 am 1.5 hrs Working on Geant4 dockerfile
- 8/24 12:00 pm .5 hr building my new dockerfile
- 8/25 8:15 am 2 hrs working on my dockerfile
- 8/25 1:07 pm 1.5 hrs Working on dockerfile

# Week 15 8/28-9/3

**G4 Brems**
- [x] Put out 0.3.0 video
- [x] Work on analysis

**Geant4**
- [ ] ~Geant4 on Linux video~
- [ ] Finish up G4-Docker

**Research**
- [ ] Solve the math behind bremsstrahlung
- [ ] Get some really good photon spectrum data

- 8/28 8:18 am .5 hr planning the week
- 8/28 10:08 am 1 hr struggling with G4-docker and putting the geant4 on linux installation tutorial on Radiation Modeling repo
- 8/28 11:28 am 1.75 hr Making Geant4 on Linux vid
- 8/29 8:17 am 1 hr studying analysis and learning more commands
- 8/29 10:00 am 1 hr failing to make Geant4 installation on Linux vid, at this point I give up.
- 8/29 2:54 pm 1 hr trying to figure out analysis for G4-Brems, ended up building CERN's ROOT from source.
- 8/29 4:08 pm .25 hr I'm going to try and install the root executable instead. UPDATE it works and root works. tomorrow I'm gonna learn how to use it.
- 8/30 10:45 am .75 hr recording g4-brems v0.3.0 video
- 8/30 6:32 pm .75 hr Editing g4-brems v0.3.0 video
- 8/30 7:50 2 hrs Editing video and posting it!
- 8/31 11:34 am 1.5 hr learning how to use ROOT! Update: I learned the basics, and i found out that Geant4 produces .root files that display your graphs on a browser.
- 8/31 4:52 pm .25 hr Learning more about root
- 8/31 9:28 pm .5 hr Planning the next projects and messing around more with Root
- 9/1 8:43 am 1 hr going through more root tutorials UPDATE: figured out how to make plots in Root! Next step is I am REALLY itching to get Geant4 docker up and running, AND a geant4 root docker as well. Because I am just building up the dependencies right now.
- 9/1 10:16 am 1 hr working on saving all the particle data as a CSV G4-Brems. I almost have it, but I need to populate the file I think.
- 9/1 11:20 am 1.25 hr Trying to get my data to save to a file. I feel like I'm making progress but it's still not working.
- 9/2 10:33 am 1 hr debugging why the analysis won't save a file?
- 
# Week 16 9/4-9/10

**G4 Brems v040**
- [x] Finish up analysis!
- [x] Look into other options to make the code simpler: saving the ntuples in eventaction, or even using the 'RecordEvent' function in runaction instead of a Hit class
- [ ] cross reference data with other articles to prove accuracy 

**G4 Brems v050**
- [ ] Decide on what histograms I want to make, and make them.
- [ ] Migrate the new CMakeLists.txt file from G4-Hello-World over

**Other**
- [ ] Finish G4 Docker

- 9/4 8:04 am 1.25 hr Planning the week and getting the csv file saving on G4-Brems. UPDATE: I got analysis working!!! thanks to some help from B4a. Next steps are: learning how to use the root viewer, and possibly switching it up so I get the histograms booked from eventaction instead of the hitscollection.
- 9/4 10:02 am 1.5 hr Simplifying code a bit
- 9/4 2:03 pm .5 hr learning about root and learning more about geant4 on linux 
- 9/4 8:17 pm .5 hr Writing up the release notes for 0.4.0 G4-Brems
- 9/4 9:00 pm .5 hr Finishing up 0.4.0 release notes
- 9/5 2:52 pm 1.75 hr Seeing if I can get G4-Brems running on docker? UPDATE: WSL broken
- 9/5 4:45 pm 1 hr testing G4 Brems with the dockerfile and fixing WSL UPDATE: Wsl is fixed, but G4 Brems doesn't really work with docker... yet. I have 2 options now. Either build it with cmake with docker, OR, build it in WSL and give THOSE binaries to the dockerfile.
- 9/6 8:39 am 1.5 hr working on the dockerfile for G4-Brems UPDATE: It built with cmake and everything (FINALLY) and it runs but exits super fast. The 2 workaround are: 1. do more research about running a qt gui in docker, or 2. just build the executable in WSL and then try to run THAT with docker??? that might work?
- 9/6 11:32 am .5 hr prepping for g4-brems v040 vid
- 9/6 12:20 pm 1 hr recording g4-brems v0.4.0 vid
- 9/6 2:45 pm 1.25 hr editing G4-Brems v0.4.0 vid
- 9/7 9:10 am 1 hr editing vid
- 9/7 10:37 am 1 hr making thumbnail and uploading vid
- 9/7 2:41 pm .5 hr finding references for g4_brems and running accurate_run. UPDATE: reading research articles is soul sucking
- 9/7 3:17 pm .25 hr reading another article
- 9/8 9:20 am 1.25 hr deciding what to do next, and fixing some issues with g4 brems

# Week 17 9/11-9/17

**G4 Brems**
- [x] Make it so the file doesn't close upon ending the run. That way, I can simulate a lot more particles and keep adding them to the same file
- [ ] Create really good documentation about G4-Brems including sources
- [x] Create a project proposal (figure out where I want to take this project)
- [ ] Finish up phase 2 and write a summary
- [ ] Post a video about G4 Brems accuracy release

**Other**
- [x] Meet with brother kelley about my project

- 9/11 10:37 am .75 hr Working on testing randomness of G4-Brems
- 9/11 8:02 pm 1.75 hrs Working on randomizing simulations and testing mac files. UPDATE: I randomized the simulations, and wrote the first 2 sections of my G4-Brems research paper.
- 9/13 9:20 am 1.25 hrs working on testing mac files and how long each one takes
- 9/13 11:03 am .25 hr testing how it works to run multiple mac files at once
- 9/13 8:00 pm 1.5 hrs giving electron energies a gaussian distribution, and giving specific commands to open and close file so I can run multiple simulations before closing the file. UPDATE: it's ready for an accurate run. I'm gonna do it tonight.
- 9/14 8:15 am 1.25 hr creating accurate data, comparing that data to reality, and coming up with project proposal
- 9/14 2:00 pm .25 hr meeting with bro kelley and discussing my project
- 9/14 9:00 pm 2 hrs working on project proposal for research class UPDATE: finished rough draft
- 9/15 9:12 pm 1.5 hrs revising project proposal
- 9/15 8:57 pm 1 hr release notes for G4-Brems 0.5.0
- 9/16 9:00 am 1.25 hr writing release notes for G4-Brems 050 and planning for next week

# Week 18 9/18-9/24

**G4 Brems**
- [ ] Finish up! what does that mean exactly?:
- [x] Make a video of the accuracy update
- [ ] 1. Make sure I have all the histograms I want
- [ ] 2. Write a paper talking about G4 Brems
- [x] 3. Make sure cmakelists.txt is right and hopefully get set up on docker!
- [ ] Make a video of the release 1.0.0!

**Other**
- [ ] Start on Geant4 1DCRT? maybe come up with catchy name

- 9/18 7:30 1.5 hr Working on dockerizing and cmakeizing G4-Brems. UPDATE: cmakeized it, but it's gonna be really hard to dockerize. I did about 1 hr of research into connecting docker to my systems graphics, it's gonna be really really hard. I think i'll just focus on generating data, or making it into just an executable.
- 9/19 8:45 am 1.75 hrs planning and working on the extra histograms I want in Geant4. UPDATE: I got some more sources about the analytical spectrum of bremsstrahlung. I am almost done understanding it. I think I'm going to start next on comparing g4 brems to the data from these articles.
- 9/19 9:46 pm .75 hr analyzing more research articles and comparing them to G4-Brems. update: for now I can't seem to get any bremsstrahlung data!!! and there are other processes going into this than just bremsstrahlung I think.
- 9/20 9:30 am 2 hrs Learning more about how clinical linac's work. UPDATE: They should just work with simple bremsstrahlung... so why is my data wrong? I've been running some tests, and I founds something weird... the higher the energy, the weirder the photon distribution gets. I'm going to do an experiment tonight where I run simulations from like 1 to 100 MeV  or something and compare the results.
- 9/22 7:40 am 3 hrs doing my experiment to see what happens the higher we get in energy UPDATE: i came up with graphs from 5-40 MeV, I need to talk to brother Kelley about them. Now I'm gonna work on dockerizing G4_Brems UPDATE2: I pushed my first tag to docker hub! I also put instructions in the github repo for how to use the docker image.
- 9/22 7:55 pm 2.5 hrs making video of G4 brems v050, testing g4-brems on docker, and planning the next step, G41dcrt.
- 9/23 9:20 am 1 hr researching why energy spectrum skews at higher energies. UPDATE: I didn't figure it out, but I did add a new executable to g4-brems called G4_Brems_terminal that runs interactive mode. It works super good in docker.
- 9/23 10:35 am .25 hr planning my 'dockerizing geant4' video
- 9/23 3:00 pm .25 hr submitting progress and emailing bro. kelley


# Week 19 9/25-10/1

**G4 Brems**
- [ ] Figure out if my model is accurate? Maybe compare it to similar Geant4 examples
- [ ] Make some more histograms (finally)

**G4 1DCRT**
- [ ] Figure out how to include g4 brems in the new g41dcrt project? modularly hopefully
- [ ] Start with G4 1DCRT

**Docker/Cmake**
- [ ] Get visualization working in docker either with HepRapp or something else
- [x] Get cmake to build both "g4 brems" and "g4 brems terminal" at the same time
- [x] Get rid of "install" prefix, I don't need it
- [ ] Figure out how to cmake from command line on windows

- 9/25 12:50 pm 1 hr Testing if g4-brems takes into account relativistic contributions. the answer is yes. Also looked into several different options for physics lists.
- 9/25 11:05 pm 1.5 hr Testing all the different em standard physics lists
- 9/26 8:19 am 1.25 hrs testing physics lists and researching different visualization
- 9/27 3:00 pm 1 hr talking to bro Oliphant about bremsstrahlung and reading from the textbook he let me borrow
- 9/28 8:33 am 1 hr coming up with analytical bremsstrahlung UPDATE: investigated kulenkampff's law, and got halfway through kramers
- 9/28 10:37 pm 1 hr continuing the testing of kramers law, confirmed accuracy for 5-10 mev... actually, that's all I need for now!!!

To do tomorrow:
- [x] Shift the detector in g4-brems to right next to the target
- [ ] test angle dependence just for fun
- [ ] Write a paper to finish off g4-brems!

- 9/29 7:52 am 1.25 hr checking units of intensity, and overhauling cmakelists
- 9/30 9:03 am .25 hr readjusting g4 brems detector
- 9/30 10:23 am 1.5 hr creating more data with the new setup
- 9/30 7:35 pm 3 hrs writing the g4-brems essay, then messing with g4-brems. I tried filtering the particles and saving only the gammas or only the electrons. It turns out that I think that energy graph I was seeing was mostly electrons. But when I did only the gammas, it looked like characteristic x-rays. In other words, only very specific energies were shown. It was super interesting, it looked like a quantum effect was going on. Then I tried to impliment where the program creates both graphs at once, and it didn't quite work.


# Week 20 10/2-10/8
- [x] Make the detector catch ALL the bremsstrahlung
- [x] Filter the particles by type
- [x] Get some energy distributions
- [ ] Get an accurate photon energy distribution
- [ ] Test my calorimeter detector
- [ ] Re-impliment hits into g4-brems! so that each photon will create it's own hit. (this is gonna be hard...)
- [x] Study physics lists, and look into creating my own or getting a high-accuracy bremsstrahlung one
- [ ] Impliment my own version of G4eBremsstrahlung that only uses the RelModel.

- 10/3 1:44 pm 2.5 hrs working on a new detector that catches ALL the bremsstrahlung. Also testing out different physics lists and running simulations to compare. Also made sure that each one is relativistic, and found out that yes they are. Next step is to run simulations filtering out particles like only displaying the electrons or only the photons.
- 10/4 7:05 pm 2.5 hrs testing the following simulations: em_Standard with all particles, only electrons, only photons, and only positrons. Got some graphs of all those interactions from 4-9 MeV.
- 10/5 2:00 pm .75 hrs discussing with Br. Kelley about my data, and making plans going forward how to debug.
- 10/5 11:37 pm 1 hr testing the different physics lists with filtering out everything except gammas. UPDATE: I need to figure out a much more accurate physics list with more bins for bremsstrahlung.
- 10/6 10:32 pm 2 hrs learning about the nitty gritty of how physics lists work in Geant4
- 10/7 9:09 pm 3 hrs making a test calorimeter geant4 project. UPDATE: Running into an issue where it can't find the particle in the particle table, so it's trying to give the gun a nullptr.

# Week 21 10/9-10/15
- [x] Test G4-Brems in docker
- [x] Figure out that weird thing with the datasets: It's not the datasets issue, in fact they do the best job in modeling.
- [x] Finish TestCalorimeter
- [ ] dockerize g4 brems?

- 10/9 10:00 am .25 hr learning about x-servers and geant4
- 10/10 9:09 am 2 hr testing g4-brems in docker and working on TC. Update: Got TC working and created an automated script to build, which is a game changer. Next step is getting TC done to make sure the calorimeter works fine.
- 10/11 9:02 am .75 hr consulting the geant4 forum about my eBremsstrahlung issue. Created an issue for it.
- 10/11 8:41 pm 1 hr Researched bremsstrahlung and got some dope resources
- 10/11 11:15 pm 1.25 hrs working on instructions to dockerize geant4 UPDATE: I got as far as I have personally tried... Next step will be experimenting with visualization as well as root data analysis.
- 10/12 9:30 am 1.25 hr researching more about physics lists to see if I can create my own. UPDATE: I found out that in EmTest18 example I can create a good looking bremsstrahlung graph... So I just need to modify G4-Brems to be similar to this one. 
- 10/13 6:57 am 1.5 hr looking at how testEm18 works. Update: it was a really good study session of TestEM18. I learned a lot, and next on my list is to finish up TestCalorimeter with a sensitive detector.
- 10/13 7:37 pm 2.25 hrs working on Test Calorimeter. Update: I got the energy to print to the console!

# Week 22 10/16-10/22
- [x] Finish TC v010
- [ ] make TC video
- [ ] Track secondary particles in G4-Brems like TestEM 18
- [x] Get visualization working in docker: I figured out HepRep, but it's still a little buggy 
- [x] Put out first tutorial for dockerized geant4

- 10/16 10:20 pm 1 hr Working on Docker geant4 instructions
- 10/17 5:38 pm 1.5 hr making the g4docker video recording
- 10/17 7:45 pm 3 hrs editing and publishing g4docker video
- 10/18 8:31 pm .5 hrs starting to track the secondary particles in g4 brems. UPDATE: got what I wanted from testem18, basically the track object has the particle's kinetic energy!
- 10/19 10:50 pm 2.5 hrs logging total kinetic energy in TC. UPDATE: I polished up TC pretty well. it's ready for the first release and detects particles perfectly. Next step is to apply this knowledge to G4-Brems, and also figure out analysis and better visualization
- 10/20 10:23 .75 hr am working on G4-Brems and displaying with HepRep.
- 10/20 2:00 .25 hr trying to get g4Brems detecting only the first secondary to be produced.
- 10/21 5:00 .75 hr trying to track only the first secondary in g4brems
- 10/21 11:03 pm 1 hr working on g4-brems trying to get those secondaries tracked update: It works!!!

# Week 23 10/23-10/29
- [ ] Make TC video
- [ ] Prove that G4-Brems is accurate using analytical data
- [ ] Clean up G4-Brems code
- [ ] Create documentation for G4-Brems
- [ ] Release G4-Brems on GitHub
- [ ] Release G4-Brems on Docker
- [ ] Start on LinacBeam
