import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import optimize
import numpy as np
import sys
from numpy import mean as m
import os
import os.path
import sys
import statistics
import glob

########## Checking for Kinetic Compensation Effect ##########

#Iron
Fe_lnA_1GPa = 24.3016302720162
Fe_lnA_2GPa = 24.374419557613916
Fe_lnA_3GPa = 24.526941857681038
Fe_lnA_4GPa = 25.160268070121646
Fe_lnA_5GPa = 25.5239527718916

#Iron Oxide
Fe3O4_lnA_1GPa = 21.79264339783764
Fe3O4_lnA_2GPa = 21.85211425402552
Fe3O4_lnA_3GPa = 22.41112004417647
Fe3O4_lnA_4GPa = 23.0280743411055
Fe3O4_lnA_5GPa = 23.401381188933993

#Iron Carbide
FeC_lnA_1GPa = 24.43413240437313
FeC_lnA_2GPa = 23.786240682970515
FeC_lnA_3GPa = 23.79734749640708
FeC_lnA_4GPa = 24.689514217898317
FeC_lnA_5GPa = 24.867591816063513

############### Activation Energies #############

#Iron
Fe_Ea_1GPa = 16.221897212869344
Fe_Ea_2GPa = 16.53328982064729
Fe_Ea_3GPa = 17.300175412597014
Fe_Ea_4GPa = 21.09926926367782
Fe_Ea_5GPa = 21.663127230883852

#IronOxide
Fe3O4_Ea_1GPa = 9.008936573231207
Fe3O4_Ea_2GPa = 9.151919159307191
Fe3O4_Ea_3GPa = 11.123221282135109
Fe3O4_Ea_4GPa = 14.175484841506531
Fe3O4_Ea_5GPa = 16.484262942495057

#IronCarbide
FeC_Ea_1GPa = 17.06896481782376
FeC_Ea_2GPa = 13.719781424444344
FeC_Ea_3GPa = 14.289895092394426
FeC_Ea_4GPa = 17.731927738355253
FeC_Ea_5GPa = 17.731927738355253

FeCEa = [FeC_Ea_1GPa, FeC_Ea_2GPa, FeC_Ea_3GPa, FeC_Ea_4GPa, FeC_Ea_5GPa]
FeClnA = [FeC_lnA_1GPa, FeC_lnA_2GPa, FeC_lnA_3GPa, FeC_lnA_4GPa, FeC_lnA_5GPa]

FeEa = [Fe_Ea_1GPa, Fe_Ea_2GPa, Fe_Ea_3GPa, Fe_Ea_4GPa, Fe_Ea_5GPa]
FelnA = [Fe_lnA_1GPa, Fe_lnA_2GPa, Fe_lnA_3GPa, Fe_lnA_4GPa, Fe_lnA_5GPa]

Fe3O4Ea = [Fe3O4_Ea_1GPa, Fe3O4_Ea_2GPa, Fe3O4_Ea_3GPa, Fe3O4_Ea_4GPa, Fe3O4_Ea_5GPa]
Fe3O4lnA = [Fe3O4_lnA_1GPa, Fe3O4_lnA_2GPa, Fe3O4_lnA_3GPa, Fe3O4_lnA_4GPa, Fe3O4_lnA_5GPa]

KineticCompeEffectPlot, EavsLnA = plt.subplots()
EavsLnA.set_title('Activation Energy vs Prefactor')
EavsLnA.set_xlabel('Ea')
EavsLnA.set_ylabel('ln A')
EavsLnA.scatter(FeEa, FelnA, label='Fe')
EavsLnA.scatter(FeCEa, FeClnA, label='FeC')
EavsLnA.scatter(Fe3O4Ea, Fe3O4lnA, label='Fe3O4')
EavsLnA.legend(loc='lower right')
#EavsLnA.set_ylim(24, 26)
plt.show()