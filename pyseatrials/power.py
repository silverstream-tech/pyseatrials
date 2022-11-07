# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/04_power.ipynb.

# %% auto 0
__all__ = ['correction_delivered_power', 'propulsive_efficiency_corr', 'full_scale_wake_fraction', 'self_propulsion_factors']

# %% ../nbs/04_power.ipynb 2
import numpy as np
from fastcore.test import *

# %% ../nbs/04_power.ipynb 4
def correction_delivered_power(
    p_dms:float, #delivered power [W]
    resistance_increase:float, #Resistance increase derived from data measured in seatrial
    stw:float, #speed through water [m/s]
    eta_id:float, #propulsive efficiency in the ideal conditions
    eta_ms:float, # propulsive efficiency in the seattrial

)-> float:
    
    "calculates the corrected delivered power, used as part of the direct power analysis"
    
    return resistance_increase * stw /eta_id + p_dms * (1- eta_ms/eta_id)
    

# %% ../nbs/04_power.ipynb 8
def propulsive_efficiency_corr(n_o:float, #open water efficiency
                          n_r:float, #relative rotative efficiency
                          t:float, #thrust deduction factor
                         w_s:float, #full-scale wake fraction
                         ):
    "Calculates propeller efficiency adjusting for additional resistances"
    return n_o*n_r*(1-t)/(1-w_s)
    

# %% ../nbs/04_power.ipynb 12
def full_scale_wake_fraction(wake_fraction_model:float,
                            scale_correlation_factor:float
                            )-> float:
    
    "used to scale from model results to full-scale vessel"
    
    return 1- (1- wake_fraction_model) * scale_correlation_factor

# %% ../nbs/04_power.ipynb 17
def self_propulsion_factors(
    x_ideal:float, #The variable in ideal conditions. It is acceptable to use this value without adjustments
    delta_x:float = 0, #The change per unit of the resistance ratios. Default is 0
    delta_r:float = 1, #increase in resistance from ideal conditions
    delta_r_ideal:float = 1 #Resistance in ideal conditions
) -> float:
    
    "Adjusting the self propulsion factors is only possible if the required model tests have been performed. By default this function returns the ideal value"
    
    return x_ideal + delta_x * (delta_r/delta_r_ideal)
