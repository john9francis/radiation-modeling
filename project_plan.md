# Project plan:

[home](README.md)

Started: 5/22/2023

Finished:

# Contents
- [Long term goals](#long-term-goals)
- [Project plan 1](#project-plan-1)
- [Summary of phase 1 upon finishing](#summary-of-phase-1-upon-finishing)
- [Records of time spent](#records-of-time-spent)

# Long term goals

- 400 total hours
- 30 weeks
- 12.5 hours a week

# Project plan 1
(planned 6/22)
### Phase 1 plan (10 weeks):
- Create a model of a stationary x-ray LINAC and the radiation activity at different distances, amounts of time, and voltages.
- Implement a method to convert that activity into exposure

### Phase 2 (10 weeks): 
- Create a model of a person (for now, just one circular cross-section) with a tumor in the center
- Modify the linac model to be able to rotate around the person 
- Record the exposure in each layer of the body

### Phase 3 (10 weeks):
- Add attenuation to the model. The beam will lose energy as it passes through layers.

### Further work (the rest of the time): 
- Add functionality for the tumor to be anywhere in the cross-section, not just the center.
- Make the person model a bit more realistic. Mark out the cross section with organs, bones, etc.
- Implement a method to convert the exposure into effective dose. Record the effective dose in each of the different organs.
- Repeat everything with proton therapy instead of x-ray therapy

# Summary of phase 1 upon finishing:
[Phase 1 summary](phase_1_completion_summary.md)

# Project Plan 2
(planned 7/17)

This is the plan now that I’m basically finished with Phase 1:

## Phase 2: Create 1D model of a radiation treatment (6 weeks)
- Have the model shoot one beam of the correct energy of photons into one detector
- Display the amount of dose the detector receives. 
- Create a graph of the dose profile, and the PDD. 
- Extra: flattening filter in the beam!

## Phase 3: Start work on a 3DCRT model (6 weeks)
Basic requirements:
- Model a realistic body part (pelvis, breast, etc) with multiple detectors
- Have multiple beams of photons in different locations with the correct energies
- Display data for how much dose each detector receives (tumor, important organs, etc)

# Phase 4: Make the model better (10 weeks)
Ideas:
- Allow for user to specify a prescription (e.g. 500 cGy) and have the model automatically stop when the prescription has been hit
- Have the model shut off a beam when it gives too much to a sensitive organ like the heart
- Allow to save the settings after a run including the beam locations and how much dose each beam distributes
- Optimize for speed
- Have the model do a couple of runs and keep the one that distributes the least dose to the sensitive organs
- Or have the model shoot test particles all around and start the beam in the locations where the particles do the least damage.
- Maybe do a run called, “calibration” that decides the best locations for beams, and saves the settings for future runs.
- Allow for the model to work on multiple body parts
- Maybe the user provides a certain file containing the information about the body part and the tumor, and then the program constructs it into a 3D model.  



# Records of time spent

- [Time spent on phase 1](timeSpentPhase1.md)
