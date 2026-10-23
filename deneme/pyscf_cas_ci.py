# for my all calculation I will  utualize the GPU.....
from pyscf import gto, fci, mcscf
from mpi4pyscf import scf

import numpy as np

# h3 cation
mol= gto.M(
    atom = '''
    H          0.00000000   0.49074773   0.00000000 
    H         -0.42500000  -0.24537386   0.00000000
    H          0.42500000  -0.24537386   0.00000000
    ''',
    basis = 'sto-6g',
    charge = 1,
    spin = 0,
    output = "./deneme.txt  ",
    verbose = 5)

mhf= mol.RHF().run()
S_ij = mhf.get_ovlp()
C_ij = mhf.mo_coeff


print(mol.ao_labels())

#c0, c1, c2 = mci.cisdvec_to_amplitudes(mci.ci)

#np.savetxt("S_ij.txt", S_ij,fmt = '%.8f')
#np.savetxt("C_ij.txt", C_ij,fmt = '%.8f')

"""
orb_energy = mhf.mo_energy
orb_occ = mhf.mo_occ

def orb_occ_table(orb_energy,orb_occ):
    print ("orbital  energy   occ")
    for i in range (0,(len(orb_energy))):
        print(i ,"   ", orb_energy[i],"  ",orb_occ[i])
    return 0

orb_occ_table(orb_energy,orb_occ)
"""


#mci= mhf.CISD().run()