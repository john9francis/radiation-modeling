# Time spent on my thesis ( and finishing up )

Contents:
- [Notes](#notes)
- [Week 1](#week-1-17-113)
- [Week 2](#week-2-114-120)
- [Week 3](#week-3-121-127)
- [Week 4](#week-4-128-23)
- [Week 5](#week-5-24-210)
- [Week 6](#week-6-211-217)

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
- 2/16 9:48 pm developing radiation shielding app


**Notes:**
- 2/15 TO DO:
- 1. Create a geant4 app that records pdd with one energy of photon. should be pretty easy. Then check and make sure my pdd looks good.
  2. I can also test what is the best energy spectrum for a good pdd. 
