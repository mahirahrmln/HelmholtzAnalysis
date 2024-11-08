import msgpack, zlib, io, numpy as np, matplotlib.pyplot as plt

file_path = '/Users/macintosh/Downloads/HelmholtzEOSBackend(n-Propane[1.0000000000])/pure_saturation.bin.z'

with open(file_path, 'rb') as fp:
    values = msgpack.load(io.BytesIO(zlib.decompress(fp.read())))
    revision, matrices = values[0:2]

    # Print available keys in matrices
    print(matrices.keys())

    # Extract parameters using the specified keys
    TL = np.array(matrices['TL'])
    TV = np.array(matrices['TV'])
    condL = np.array(matrices['condL'])
    condV = np.array(matrices['condV'])
    cpmolarL = np.array(matrices['cpmolarL'])
    cpmolarV = np.array(matrices['cpmolarV'])
    cvmolarL = np.array(matrices['cvmolarL'])
    cvmolarV = np.array(matrices['cvmolarV'])
    hmolarL = np.array(matrices['hmolarL'])
    hmolarV = np.array(matrices['hmolarV'])
    logpL = np.array(matrices['logpL'])
    logpV = np.array(matrices['logpV'])
    logrhomolarL = np.array(matrices['logrhomolarL'])
    logrhomolarV = np.array(matrices['logrhomolarV'])
    logviscL = np.array(matrices['logviscL'])
    logviscV = np.array(matrices['logviscV'])
    pL = np.array(matrices['pL'])
    pV = np.array(matrices['pV'])
    rhomolarL = np.array(matrices['rhomolarL'])
    rhomolarV = np.array(matrices['rhomolarV'])
    smolarL = np.array(matrices['smolarL'])
    smolarV = np.array(matrices['smolarV'])
    speed_soundL = np.array(matrices['speed_soundL'])
    speed_soundV = np.array(matrices['speed_soundV'])
    umolarL = np.array(matrices['umolarL'])
    umolarV = np.array(matrices['umolarV'])
    viscL = np.array(matrices['viscL'])
    viscV = np.array(matrices['viscV'])

    # Example plot for liquid and vapor enthalpy against temperature
    plt.plot(TL, hmolarL, 'o', label='Liquid Enthalpy')
    plt.plot(TV, hmolarV, 'x', label='Vapor Enthalpy')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Enthalpy (J/mol)')
    plt.title('Temperature vs Enthalpy for n-Propane')
    plt.legend()
    plt.grid()
    plt.show()
