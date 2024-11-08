import msgpack, zlib, io, numpy as np, matplotlib.pyplot as plt

file_path = '/Users/macintosh/Downloads/HelmholtzEOSBackend(n-Propane[1.0000000000])/phase_envelope.bin.z'

with open(file_path, 'rb') as fp:
    values = msgpack.load(io.BytesIO(zlib.decompress(fp.read())))
    revision, matrices = values[0:2]

    # Print available keys in matrices
    print(matrices.keys())

    # Extract parameters
    T = np.array(matrices['T'])
    p = np.array(matrices['p'])
    rhomolar_liq = np.array(matrices['rhomolar_liq'])
    rhomolar_vap = np.array(matrices['rhomolar_vap'])
    hmolar_liq = np.array(matrices['hmolar_liq'])
    hmolar_vap = np.array(matrices['hmolar_vap'])
    cpmolar_liq = np.array(matrices['cpmolar_liq'])
    cpmolar_vap = np.array(matrices['cpmolar_vap'])
    cvmolar_liq = np.array(matrices['cvmolar_liq'])
    cvmolar_vap = np.array(matrices['cvmolar_vap'])
    viscosity_liq = np.array(matrices['viscosity_liq'])
    viscosity_vap = np.array(matrices['viscosity_vap'])
    speed_sound_vap = np.array(matrices['speed_sound_vap'])
    conductivity_liq = np.array(matrices['conductivity_liq'])
    conductivity_vap = np.array(matrices['conductivity_vap'])

    # Example plot for pressure vs. enthalpy of the liquid phase
    plt.plot(p, hmolar_liq, 'x', label='Liquid Enthalpy')
    plt.xlabel('Pressure (Pa)')
    plt.ylabel('Enthalpy (J/mol)')
    plt.title('Pressure vs Enthalpy for n-Propane')
    plt.legend()
    plt.grid()
    plt.show()
