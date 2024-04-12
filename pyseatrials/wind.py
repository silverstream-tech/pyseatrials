# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_wind.ipynb.

# %% auto 0
__all__ = ['rel2true_speed', 'rel2true_dir', 'true2rel_speed', 'true2rel_dir', 'double_run_average',
           'vertical_position_anemometer']

# %% ../nbs/02_wind.ipynb 5
import numpy as np
import pandas as pd
from fastcore.test import *
from .trig import *


# %% ../nbs/02_wind.ipynb 8
def rel2true_speed(relative_windspeed:float, #speed of wind relative to ship
                            sog:float, #speed over ground
                           relative_wind_direction:float #wind direction relative to ship
                           ) ->float: # True windspeed
    "converts a relative wind speed and direction to a true wind speed"
    return law_of_cosines(relative_windspeed, sog, relative_wind_direction)

# %% ../nbs/02_wind.ipynb 18
def rel2true_dir(
    relative_wind_speed:float, #Speed of the wind relative to the ship
    sog:float, #Speed of the ship overground
    relative_wind_direction:float, #direction of wind in radians relative to the ship
    vessel_heading:float, #The direction of the ship through the water
    constrain_to_positive:bool = True #Should the function return a value between 0 and 2 pi
)-> float: # the true wind directionangle relative to north in radians.
    "converts relative wind direction to true wind direction"
    #This function should probably be abstracted to a more trignonometric form
    numerator = opposite_magnitude_fn(relative_wind_speed, relative_wind_direction + vessel_heading) - opposite_magnitude_fn(sog, vessel_heading) 
    denominator = adjacent_magnitude_fn(relative_wind_speed, relative_wind_direction + vessel_heading) - adjacent_magnitude_fn(sog, vessel_heading) 
    
    gamma = np.arctan2(numerator, denominator)
        
    #prevents negative angles if constrain to positive is true
    #using this method instead of an if statement means the function can perform vectorised operations
    gamma = gamma + 2*np.pi*(gamma<0)*constrain_to_positive
    
    return gamma 
    

# %% ../nbs/02_wind.ipynb 27
def true2rel_speed(true_wind_speed:float, #The windspeed over ground
                            sog:float, #Speed over ground of the vessel
                            true_wind_direction:float, #Direction of wind relative to north
                            vessel_heading:float, #Direction of vessel in water relative to north
)-> float: #returns relative windspeed using the same units entered
    
    "converts true windspeed to relative"
    
    return np.sqrt(true_wind_speed**2 +sog**2 +2*true_wind_speed*sog*np.cos( true_wind_direction - vessel_heading))
           

# %% ../nbs/02_wind.ipynb 34
def true2rel_dir(
                            true_wind_speed:float, #The windspeed over ground
                            sog:float, #Speed over ground of the vessel
                            true_wind_direction:float, #Direction of wind relative to north
                            vessel_heading:float, #Direction of vessel in water relative to north
                            constrain_to_positive:bool = True #Should the function return a value between 0 and 2 pi
)-> float: #relative wind direction
    
    "converts true direction speed to relative"
    
    gamma  = find_gamma_fn(true_wind_speed, sog, true_wind_direction - vessel_heading)

    return gamma + 2*np.pi*(gamma<0)*constrain_to_positive

# %% ../nbs/02_wind.ipynb 43
def double_run_average(a, b, alpha, beta):
    #it makes no difference if a/2, b/2 is used or average_velocity/2 the result is the same
    average_velocity, average_direction = combine_vectors(a, b, alpha, beta)

    return average_velocity/2, average_direction

# %% ../nbs/02_wind.ipynb 47
def vertical_position_anemometer(true_wind_speed:float, #True windspeed [m/s]
                                 reference_height:float, #reference height [m]
                                 measured_height:float,  # measured height [m]
                                 exponent:float = 1/9 #exponent for height adjustment. Defaults to 1/9
                                )-> float: #The true windspeed corrected for measurement height
    
    "Adjusts the windspeed taking into account the height of the anemometer on the ship relative to the reference height for windspeed"

    
    return true_wind_speed * (reference_height/measured_height)**(exponent)
