import msgpack, zlib, io, numpy as np, matplotlib.pyplot as plt

file_path = '/Users/macintosh/Downloads/HelmholtzEOSBackend(n-Propane[1.0000000000])/single_phase_logpT.bin.z'


with open(file_path, 'rb') as fp:
    values = msgpack.load(io.BytesIO(zlib.decompress(fp.read())))
    revision, matrices = values[0:2]
    # Now you can access arrays like temperature, enthalpy, pressure
    T, h, p, rho = np.array(matrices['T']), np.array(matrices['hmolar']), np.array(matrices['p']), np.array(matrices['rhomolar'])
    plt.plot(p, h, 'x')
    plt.show()
