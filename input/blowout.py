# Initial conditions for sending vertical line of electrons through blowout regime of Quasi3D simulation
# All conditions are normalized to c/w_p units

simulation_name = 'QUASI3D'
shape = 'vline'
fill = False
density = 20
iterations = 1000000

# Probe centered at the following initial coordinates:
x_c = -2.4 # Start within region of field
y_c = 0
xi_c = -18.3

# Initial momentum
px_0 = 100 # Make sure it goes towards the screen!
py_0 = 0
pz_0 = 1000 # Large p_z0 needed so electron travels with wakefield in z

# Screen Parameters (Assume infinite in y and z)
x_s = 10

# Shape Parameters (Radius or Side Length)
s1 = 0.25 # In y
s2 = 0.01 # In xi
