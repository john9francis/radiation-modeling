from matplotlib import pyplot as plt

def brems_photon_energy_graph():
    '''Displays a graph of the photon energy spectrum from the bremsstrahlung
    interaction in a 8 MeV linac, thanks to: https://aapm.onlinelibrary.wiley.com/doi/abs/10.1118/1.594221'''
    
    # Data
    energy_cutoff = 0.4
    measured_max_photon_energy = 8 * 1.06  # 6% greater than 8 MeV (nominal energy)
    weighted_mean_energy_measured = 2.3
    weighted_mean_energy_calculated = 2.4
    calculated_max_photon_energy = 1.8

    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.axvline(x=energy_cutoff, color='red', linestyle='--', label='Low Energy Cutoff')
    plt.axvline(x=measured_max_photon_energy, color='green', linestyle='--', label='Measured Max Photon Energy')
    plt.axvline(x=weighted_mean_energy_measured, color='blue', linestyle='--', label='Weighted Mean Energy (Measured)')
    plt.axvline(x=weighted_mean_energy_calculated, color='purple', linestyle='--', label='Weighted Mean Energy (Calculated)')
    plt.axvline(x=calculated_max_photon_energy, color='orange', linestyle='--', label='Calculated Max Photon Energy')
    plt.axhline(y=0, color='black', linewidth=0.5)
    plt.legend()
    plt.xlabel('Energy (MeV)')
    plt.title('Bremsstrahlung Spectrum from an 8 MeV Linear Accelerator')
    plt.grid(True)
    plt.show()


brems_photon_energy_graph()