# Time spent on my thesis ( and finishing up )

Contents:
- [Notes](#notes)
- [Week 1](#week-1-17-113)
- [Week 2](#week-2-114-120)
- [Week 3](#week-3-121-127)
- [Week 4](#week-4-128-23)

# Notes
Writing order: 
1. Outline ☑️
2. Methods
3. Results
4. Discussion
5. Introduction
6. Conclusion

# Week 1: 1/7-1/13

- 2 hrs planning and outlining
- 1/12 .5 hr recruiting thesis committee members 

# Week 2: 1/14-1/20

Goals:
- [x] Clean up med linac repo
- [x] make mac file for PDD
- [x] make mac file for beam profile
- [x] make mac file for heat map
- [x] finish up
- [ ] compile static
- [x] Get 5 references of why my project is worth spending money on
- [x] Get 5 references of what work people have already done on the subject
- [ ] Make a thesis repo

- 1/15 10:15 am 1 hr working on the 1 pg. version of my thesis
- UPDATE: I cloned g4-medical-linac main branch in a separate folder. in my original g4-medical-linac folder I have the branch that works. I CANT DO GIT PULL because the remote branch is messed up. I just need to work on cleaning my main branch and making it look like my local copy.
- 1/15 5:11 pm .5 hr cleaning up main branch UPDATE: It's cleaned up. now I just have to figure out how to do PDD from the ui commands in a mac file.
- 1/15 6:41 pm .5 hr making the release and adding a radiation shield on the med linac
- 1/15 7:28 pm 1.25 hr trying to make an analysis mac file. UPDATE: I got the pdd file done and it's pretty good!
- 1/16 12:45 pm 1.5 hr in thesis class
- 1/16 6:57 pm 1.25 hr working on the heat map. UPDATE: Got results for the heat map, beam profile, and pdd, although it's a little weird. I suspect mess ups with the x y and z direction in phantomSD.cc file. 
- 1/16 9:06 pm 1.75 hrs working on methods section of my thesis
- 1/20 12:00 pm .25 hr collecting resources
- 1/20 9:45 pm 1.5 hr implementing the rotate method into medical linac

# Week 3: 1/21-1/27

Goals:
- [ ] Finish procedure section
- [ ] Dockerize med-linac
- [x] Make thesis repo for backups
- [ ] Get colorful code in thesis
- [x] Make singleton to enable and disable analysis NOTE: there's an easier way to do this

- 1/23 9:00 am .5 hrs getting the rest of my sources
- 1/23 12:45 pm 1 hr thesis class
- 1/23 4:22 pm .75 hr working on thesis methods section, and emailed brother kelley with methods section to see what he thinks.
- NEXT: analyze my results
- 1/24 10:50 am 1.25 hrs making an analysis singleton
- NEXT: Take advantage of the analysis manager's activation stuff instead of the singleton :( my singleton is a bit buggy. messenger is good though.
- 1/25 11:22 .5 hrs switching over to geant4 analysis methods
- 1/26 11:00 1 hr. working on thesis
- 1/27 12:51 pm 1.25 hr working on thesis, moved all of procedure to background information
- 1/27 6:48 pm 1.25 hr working on thesis procedure, got as far as how bremsstrahlung is handled in geant4


# Week 4: 1/28-2/3

**Goals:**
- [ ] Finish procedure
- [ ] Analyze data

- 1/29 9:18 pm 1.25 hr working on procedure section
- 1/30 12:50 pm 2 hrs thesis class and working on pdd graph
- 1/30 6:11 pm 1.25 hr seeing if I can normalize the PDD graph
- 2/1 11:15 pm 1.5 hr trying to make the pdd graph an H2 instead of H1
- Notes: First of all, the H2 didn't work. but I got the h1 working. I have some suuuuuper good results attained by adding a FF and testing out some copper and AL filters. I have a lot of results to talk about. The last thing I have to do is figure out how to do a really good PDD graph. I am thinking in run action creating a hitsCollection or at least a few variables that keep track of max dose, min depth, and max depth. Then scaling the graph accordingly. Just because for now the PDD graph measures position vs. energy, not depth vs. percent energy. NOTE: it's fine to keep it as energy instead of grays because it's a percent. But yeah, figuring out how to convert it to percent instead of absolute values is going to be tricky. 
- Notes continued: I want to do runs with the copper, FF, and AL for my results. and I think I'll ask b. kelley about how to get the pdd to be normalized. right now I'm fixing my OGL error where it says error, can't find referenced memory 0x00000000000. A YouTube video showed me that running: `sfc /scannow` on an admin command prompt finds the issue and fixes it. Well, actually that didn't help. however here is a website for more help. https://www.partitionwizard.com/clone-disk/the-instruction-at-referenced-memory.html Luckily the batch mode still works which is a relief, especially since I am just getting results right now. Eventually I gotta figure this out though.
- TODO: Scan for malware

- 2/3 12:00 pm Switching from using a SD to using stepping action. This is simply because the SD couldn't access the run manager class. I should write about this in my thesis, the use for each one. Also, that 0x00000000000 error fixed somehow which is a relief. 
