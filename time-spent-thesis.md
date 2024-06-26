# Time spent on my thesis ( and finishing up )

Contents:
- [Notes](#notes)
- [Week 1](#week-1-17-113)
- [Week 2](#week-2-114-120)
- [Week 3](#week-3-121-127)
- [Week 4](#week-4-128-23)
- [Week 5](#week-5-24-210)
- [Week 6](#week-6-211-217)
- [Week 7](#week-7-218-224)
- [Week 8](#week-8-225-32)
- [Week 9](#week-9-33-39)
- [Week 10](#week-10-310-316)
- [Week 11](#week-11-317-323)

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

- 1/29 9:18 pm **1.25** hr working on procedure section
- 1/30 12:50 pm **2 hrs** thesis class and working on pdd graph
- 1/30 6:11 pm **1.25 hr** seeing if I can normalize the PDD graph
- 2/1 11:15 pm **1.5 hr** trying to make the pdd graph an H2 instead of H1
- Notes: First of all, the H2 didn't work. but I got the h1 working. I have some suuuuuper good results attained by adding a FF and testing out some copper and AL filters. I have a lot of results to talk about. The last thing I have to do is figure out how to do a really good PDD graph. I am thinking in run action creating a hitsCollection or at least a few variables that keep track of max dose, min depth, and max depth. Then scaling the graph accordingly. Just because for now the PDD graph measures position vs. energy, not depth vs. percent energy. NOTE: it's fine to keep it as energy instead of grays because it's a percent. But yeah, figuring out how to convert it to percent instead of absolute values is going to be tricky. 
- Notes continued: I want to do runs with the copper, FF, and AL for my results. and I think I'll ask b. kelley about how to get the pdd to be normalized. right now I'm fixing my OGL error where it says error, can't find referenced memory 0x00000000000. A YouTube video showed me that running: `sfc /scannow` on an admin command prompt finds the issue and fixes it. Well, actually that didn't help. however here is a website for more help. https://www.partitionwizard.com/clone-disk/the-instruction-at-referenced-memory.html Luckily the batch mode still works which is a relief, especially since I am just getting results right now. Eventually I gotta figure this out though.
- TODO: Scan for malware

- 2/3 12:00 pm **2 hrs** Switching from using a SD to using stepping action. This is simply because the SD couldn't access the run manager class. I should write about this in my thesis, the use for each one. Also, that 0x00000000000 error fixed somehow which is a relief. UPDATE: I have a new branch now tht only uses stepping action no SD. might merge.
- NOTES: 2 ideas moving forward.
1. deal with using CSV files instead
2. make my own analysis manager singleton... that might be the move honestly. could be fun too. would it take a super long time? yes it would.
- This analysis manager class could plot to python or the geant4 root plotting. either way.
3. Inherit from the g4 analysis manager and make my own method called "normalize" that would access some private member variables and just divide each bin by the height of the tallest bin.
- 2/3 2:20 pm **1 hr** looking into my analysis options. NOTE: I'm thinking of going with making my own analysis manager singleton and inheriting from G4ThreadLocalSingleton. here is the recommended implementation:

```cpp
class G4Class
  {
    friend class G4ThreadLocalSingleton<G4Class>;
    private:
      G4Class() { ... }
    public:
      static G4Class* GetInstance()
      {
        static G4ThreadLocalSingleton<G4Class> instance;
        return instance.Instance();
      }
};
```
- Question is though....... will this mess up everything like activating the H1's and stuff? I will have to be super careful to only add to the histogram if the histogram is active.
- This could be fun as well integrating it with python and everything. Getting some reeeeally good analysis.
- The problem is it's a time suck and I need to keep working on my thesis.
- Maybe for now I just accept the graphs I have and analyze them.
- It's just hard to analyze them if I can't put them on top of graphs that actually exist.......
- Yeah, I think this analysis thing would be a waste of time, but after thesis I want to make my own geant4 analysis tool that integrates with python. Could be a really fun project!

NEXT STEPS:
1. merge with main
2. clean up code, delete SD
3. be happy with my data



# Week 5: 2/4-2/10

**Goals:**
- [ ] Clean up med linac repo
- [ ] Add Bremsstrahlung data in there.
- [ ] Create some official runs
- [ ] Create a release
- [ ] Start on data section
- [ ] Continue procedure section

**TIME:**
- 2/5 6:00 pm .25 hr merging github repo and cleaning up
- 2/5 9:00 pm 1.5 hrs cleaning code and getting ready
- 2/5 10:58 pm 2 hrs officially cleaning the repo and getting ready for outputs. NOTE: I'm running all outputs overnight.
- 2/6 12:45 pm 1.25 hrs compiling results and writing results section
- 2/6 10:00 pm .5 hr finishing up compiling those graphs
- 2/7 10:06 am .75 hr rewriting procedure
- 2/7 1:06 pm .25 hr working on procedure
- 2/7 5:30 pm .25 hr working on procedure
- 2/8 4:52 pm .5 hr re-making the official data
- 2/10 7:30 pm 1 hr working on results section
- 2/10 9:41 pm 2.5 hrs working on results section

**NOTES:**

2/5:
- TO DO TONIGHT: GET THE OFFICIAL RUNS DONE
- Decision time. Do I made linac head commands to change the material of the phantom? I think so. Then I will have mac files to do all the tests.
- ANOTHER decision: delete the hitscollection? and phantom hits? nah I'll just leave them. for now. IDK though because they are messy. 
- so todo = make all positions absolute and not relative,
- ~~and make a function to change the material of the phantom~~
- Clean up code 100%
- Make official thesis release
- Make official runs!

2/7:
- Added secondary collimator. NOTE: out of every 500 particles about 1 actually hits the phantom.
- Now I have runs with and without the secondary collimator. The heat map looks a lot better with the collimator, but PDD graph looks better without. I guess I could discuss that stuff, or just choose one. I think I'll check the accurate collimator heatMap runs and then decide. 



# Week 6: 2/11-2/17

**Goals:**
- [ ] Rewrite procedure

**Time:**
- 2/12 9:48 pm 1 hr working on procedure section
- 2/13 12:45 pm 1 hr in thesis class
- 2/13 3:44 pm .25 hr working on background
- 2/15 10:00 am 3 hrs meeting with b. Oliphant to discuss my results and trying different filters
- 2/15 2:00 pm .5 hr getting started on a new project, radiation-shielding. This will help me understand what brems spectrum I need for med linac.
- 2/16 9:48 pm .5 hr developing radiation shielding app
- 2/16 4:18 pm 1 hr developing radiation shielding app, got basic structure set up
- 2/16 10:29 pm 1 hr getting a pdd graph integrated in my radiation shielding app
- 2/17 12:00 am .5 hr made radiation shielding be able to generate an energy spectrum instead of just one value of energy.
- 2/17 8:50 am .25 hr testing my hypothesis that the spreading out of the beam is what's contributing to the weird pdd graph. So I'm making the beam spread out in radiation shielding. UPDATE: The PDD graph looks perfect with radiation shielding.
- 2/17 10:00 am 1.5 hrs adjusting med linac so we record energy spectrum of different particles. Also fit the spectrum curves
- 2/17 1:51 pm 1.5 hrs testing out radiation shielding with the photons and electrons


**Notes:**
- 2/15 TO DO:
- 1. Create a geant4 app that records pdd with one energy of photon. should be pretty easy. Then check and make sure my pdd looks good.
  2. I can also test what is the best energy spectrum for a good pdd.
 
- 2/16 To do:
- 1. Now I just need to curve fit the bremsstrahlung spectrum from med linac and add that distribution to radiation shielding app.
  2. Also add messengers to change how the energy is fired and a messenger to insert a radiation shield in the path.
  3. Also it would be nice to only draw the trajectories that make it to the phantom (for med linac)
  4. It would also be nice to have a distribution of how many particles per energy level. just record if the particle energy is from 0 to .1 mev or .1 to .2 mev etc. and record the number.
 
- 2/16 Next steps;
- 1. To explore what's going on with med linac, I can do the following graphs:
  - 1. energy distribution of various different particles
    2. or a pdd graph per particle
    3. Basically separate the graphs I have per particle.
    4. NOTE: This will be SUPER useful info for my thesis. If I find that the electrons are what make the weirdness on the pdd graph, that will be super good to note on my thesis.
    5. Finally, curve fit my pdd data so I can get a better one for the radiation shielding app.
   
- 2/17 Next steps:
- 1. test different things that can block electrons but not photons
 



# Week 7: 2/18-2/24

**Goals:**
- [ ] Finish first draft of thesis
- [X] ALMOST DONE with first draft!

**Time:**
- 2/19 9:39 .5 hrs working on finishing up rad shield NOTE: Started the pga messenger
- 2/19 11:20 1 hr working on pga messenger
- 2/19 4:41 pm 2 hrs working on pga messenger
- 2/19 8:08 pm 2.75 hrs working on thesis until I got too tired
- 2/22 2:54 pm .5 hr grinding out results section
- 2/23 8:30 pm 1.75 hrs working on procedure section
- 2/24 10:22 pm 2.5 hr working on results UPDATE: Got the FFF graphs input, and made significant work on the discussion section.

**Notes:**
- 2/23 : TODO:
- Get an official thesis release 2 on my github
- Same with radiation shielding!!!
- Put a lead shield right after the secondary collimator. Perhaps the low energy particles we're seeing are coming out of the edges, and not out of the hole where the beam is supposed to come out?


# Week 8: 2/25-3/2

**Goals:**
- [x] Finish first draft
- [x] Give it to some people to read over

**Time:**
- 2/26 8:50 am 1.75 hrs working on procedure and background. Edited quite a bit and added some good stuff into background.
- 2/26 10:06 pm .25 hr Writing introduction
- 2/27 12:52 pm 3.25 hrs thesis class and finishing up thesis first draft.
- 2/27 5:16 pm 1 hr putting code in thesis and printing it off!

**Notes:**


# Week 9: 3/3-3/9
**Goals:**
- [ ] Implement datwyler's changes
- [ ] implement keaton's changes
- [ ] implement oliphant's changes
- [ ] implement kelley's changes
- [ ] meet with hansen and talk about it

**Time:**
- 3/4 3:00 pm .5 hr talking with datwyler about changes
- 3/5 8:25 am .25 hr working on introduction a little more
- 3/5 12:54 pm 1 hr thesis class and working on the intro
- 3/6 7:04 pm 2.25 hr making the code look good in my thesis and revising intro and procedure.
- 3/7 2:00 pm .75 hr revising intro
- 3/9 4:30 pm .25 hr revising a bit and sending it to my dad and Abram to look over
- 3/9 9:24 pm 2 hrs revising thesis, looking into combining graphs


# Week 10: 3/10-3/16
**Goals:**
- [ ] Finish second draft
- [ ] Rewrite discussion to include stuff about pure photon beam
- [ ] Fix figures with word instead of paint
- [ ] Make longer captions in the figures
- [ ] Implement people's changes

**Time:**
- 3/13 9:40 pm 1.5 hrs working on results section, made significant progress.
- 3/14 8:13 pm 1.5 hrs working on grammer and stuff. UPDATE: finished results and added license to source code. 

**To do:**
- [x] Figures
- [x] Captions
- [x] Discussion
- [ ] Grammar


# Week 11: 3/17-3/23

- 3/18 1:35 pm 1.5 hr working w/ hansen about thesis
- 3/19 10:00 am 3 hrs making a pure photon beam straight from med linac. Time to revise thesis
- 3/19 10:00 pm 2 hrs working on procedure and introduction
- 3/21 9:00 am 5.5 hrs meeting w. thesis advisor and working on results. next step is discussion, and then fix all the pictures!
- 3/21 10:32 pm 1.75 hrs working on figures. I made one of my own figures and MAN is it a lot of work.
- 3/22 9:35 am 1.5 hrs working on refurbishing all the figures
- 3/22 1:24 pm 3 hrs working on figures
- 3/23 7:23 pm 3.5 working on discussion

# Week 12: 3/24-3/30

- 3/25 6:50 pm .75 hr working on figure captions
- 3/26 9:18 am 1.75 hrs working on figure captions
- 3/26 12:45 pm 2 hrs thesis class, scheduling defense, and talking with professors
- 3/26 3:56 pm 2 hrs working on grammer and sentence structure
- 3/28 2:35 pm .5 hr reading over for grammar
- 3/29 12:00 am 1.25 hr revising
- 3/30 1:15 pm 2 hrs revising
- 3/30 8:07 pm .5 hr working on presentation

# Week 13: 3/31-4/6

- 4/1 9:30 am .5 hr working on presentation
