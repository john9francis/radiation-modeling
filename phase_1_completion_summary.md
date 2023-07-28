# Phase 1 Summary
Author: John Francis, written 7/24/2023

Phase one of my project consisted of learning about radiation therapy and learning how to use my simulation tools. I achieved a considerable amount of progress during these ten weeks, and now I have a solid foundation to start creating models. I also produced several helpful videos, infographics, and presentations to help learn the concepts that my project explores. 
LINAC machines
I started my project learning all about linear accelerators, or LINACs, which are machines that distribute the radiation to the patient. I learned that most LINACs use x-ray photon beams to deliver the radiation. There are other particles used in radiation therapy; protons, electrons, etc., but I decided that for my project I would focus on the most commonly used particle, photons. 

I learned the detailed process of how a LINAC works, from producing electrons, accelerating them, converting them into photons, and aiming the photons into a beam. I condensed my research into a presentation about how LINACs work (Francis 1). This presentation was greatly influenced by Elekta’s video on YouTube (Elekta 1).

Learning about how LINACs work was useful to give me some basic knowledge, but I won’t be using many specific parts of a LINAC in my model. Instead, I plan to start the model at the photon beam. I plan on possibly including a flattening filter (FF) which is a part of the linac, that way I will have a more realistic model, but I won’t be worrying about the electron gun, the wave guide, etc. 

# Geant4
At the beginning of my project, I planned on creating a python program to model the radiation treatment. I stumbled upon a research article summarizing a similar project, where the authors simulated an entire LINAC machine using a simulation toolkit called Geant4 (Sardari 1). This inspired me to look into Geant4 as an alternative tool.

I decided to go with Geant4 because of its credibility, accuracy, and popularity. Geant4 was developed by CERN for the modeling of several high energy physics situations. It has been around for several years and still receives regular updates. (Geant4) Many hospitals use Geant4 based modeling for their radiation treatment plans (Gate 1). 

Going with Geant4 instead of python forced me to change my modeling strategy. With python, I was planning on creating an integral-based approximation to model the radiation treatment. Geant4 uses an entirely different approach. According to the Geant4 creators, “Geant4 provides an atomistic, rather than an integral approach to physics” (Novak 1). This means that Geant4 models the effect of each individual atom. This is entirely different than I was planning, but it has the benefit of accuracy, and taking into account particle scattering and other imperfections.

During phase one, I installed Geant4 and created one application called “Photon Dose Sim.” The goals of photon dose sim were to become comfortable with creating Geant4 applications, and hopefully to create a one-dimensional version of my final project. I succeeded in creating a working Geant4 application, but it wasn’t usable for my final project. Photon dose sim uses the wrong physics list and the wrong particle type. 

During my journey learning Geant4, I created several documentations to help others on the way. I created some video tutorials on how to install Geant4, (Francis 2, Francis 3) I created a few videos showing off photon dose sim, (Francis 4, Francis 5) and I created 2 helpful infographics to understand the organization of Geant4. (Francis 6, Francis 7). 

# 3DCRT
During phase one, I was privileged to shadow some medical physicists and dosimetrists at Cape Fear Valley Medical Center. There, I learned that there are many different types of radiation treatments. To name a few, there are, “3D-CRT, IMRT, IORT, SRS,” etc. Learning about each type helped me to decide on which method I wanted to model. I decided to model a 3D-CRT radiation treatment. 

A 3D-CRT or “Three dimensional conformal radiation therapy,” (khan 1) is one of the many methods of radiotherapy. This method interested me because its benefits include reduced radiation exposure to the healthy tissue and increased beam accuracy. (khan)

# Further work
The next phase of my project will be to create an accurate “1d-crt” program in Geant4. This project will consist of generating a beam of radiation and one detector that registers accurate PDD and beam profile. This will not be trivial, as there are a lot of things to take into account. 

# Understanding Pointers
The first step for me in phase two will be understanding pointers in C++ better. Geant4 utilizes pointers extensively, and pointers are something I haven’t used very much in the past. To learn more about pointers, I have researched and started writing a short paper. I will also be dissecting a Geant4 example and writing notes on how the use of pointers improved performance. 

# Taking Bremsstrahlung into account
Medical linacs work by accelerating electrons and colliding them with a target to produce photons. The electrons more-or-less have the same kinetic energy as they hit the target, but the photons generated have a wide range of energies. (Wikipedia, Clover learning) This gives me a difficult decision. Should I model the electrons and the tungsten target, and then model a collimator to focus all the x-rays into a beam? Or do I model the photons, making sure to give them each a different energy and conforming them to the correct energy distribution? I will have to continue to research and decide which course is better. 

# Conclusion
I have finished the preparation phase of my project. I have become relatively comfortable with Geant4, and comfortable with the process of producing medical radiation. I am now much more educated and understand where my project will go. In this next phase, I will undertake the challenge of creating a realistic radiation beam and log realistic data. 

# Works cited:
- Clover learning, “Understanding Bremsstrahlung Radiation” https://www.youtube.com/watch?v=pghykOzTVPw 
- Elekta, “How a Linear Accelerator Works” https://www.youtube.com/watch?v=jSgnWfbEx1A
- Francis, John. “Medical LINACs” https://prezi.com/view/LCqqiqkJdII7mVcUly4L/
- Francis, John. “Complete Geant4 Installation Tutorial 2023” https://www.youtube.com/watch?v=w7k9PK1Ipv8&list=PL1AYUn8GT4HkL09iElGRk8NRIfR3tUywQ&index=1
- Francis, John. “Geant4 Installation with Qt 2023” https://www.youtube.com/watch?v=rtCsfDD45Bc&list=PL1AYUn8GT4HkL09iElGRk8NRIfR3tUywQ&index=2&t=14s
- Francis, John. “‘Photon Dose Sim’ Geant4 application demo and code walkthrough” https://www.youtube.com/watch?v=mqMxX8hLwwU&list=PL1AYUn8GT4HkL09iElGRk8NRIfR3tUywQ&index=3&t=1s
- Francis, John. (TBD)
- Francis, John. “Geant4 App Basic Structure” https://prezi.com/i/gp3kiz0ubh3e/geant4-basic-structure/
- Francis, John. “Photon Dose Sim Organization” https://prezi.com/i/o7edcdeqyjh3/photon-dose-sim-organization/
- Gate. “Gate” http://www.opengatecollaboration.org/
- Geant4 https://geant4.web.cern.ch/
- Khan, Faiz M. PhD “Khan’s the Physics of Radiation Therapy” 
- Novak, Mihaly. “Physics Lists” https://indico.cern.ch/event/776050/contributions/3237925/attachments/1789252/2914238/PhysLists.pdf
- Sardari, D. “Measurement of depth-dose of linear accelerator and simulation by use of Geant4 computer code” https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3863189/ 
- Wikipedia, “Bremsstrahlung” https://en.wikipedia.org/wiki/Bremsstrahlung
