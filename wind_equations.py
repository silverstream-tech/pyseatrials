import numpy as np
import pandas as pd

#    This is a devleopment version of appendix E of ITTC Preparation, Conduct and Analysis of Speed-Power Trials

def corrected_relative_wind_velocity_v1(true_wind_velocity, speed_over_ground, true_wind_direction, ships_heading):
    '''
    Equation E-6
    
    true_wind_velocity = V_WT
    speed_over_groun = V_G
    true_wind_direction = PSI_WT
    ships_heading = psi
    
    This equation is the law of cosines
    
    Can produce significant rounding errors for small values of V_WT. This may not be a problem as it would mean relative wind speed is either,
    0 or close to full windspeed. Should be checked
    '''
    
    relative_wind_velocity = np.sqrt(true_wind_velocity**2 + speed_over_ground**2 + 
                                     2*true_wind_velocity*speed_over_ground*np.cos(true_wind_direction- ships_heading))
    
    return relative_wind_velocity

def corrected_relative_wind_direction_v1(true_wind_velocity, speed_over_ground, true_wind_direction, ships_heading):
    
    '''
    Equation E-7
    
    true_wind_velocity = V_WT
    speed_over_groun = V_G
    true_wind_direction = PSI_WT
    ships_heading = psi
    
    '''
    
    opposite = true_wind_velocity * np.sin(true_wind_direction - ships_heading)
    adjacent_plus_sog = speed_over_ground + true_wind_velocity * np.cos(true_wind_direction - ships_heading)
    
    relative_wind_direction  = np.arctan2(opposite, adjacent_plus_sog)
    #relative_wind_direction  = np.arctan(opposite/adjacent_plus_sog)
    
    #adds 180 aka pi degrees on if the adjacent_plus_sog is smaller than 0
    #the below approach avoids an if statement to make vectorisation easier
    #relative_wind_direction  = relative_wind_direction + np.pi * (adjacent_plus_sog <0)
    
    return relative_wind_direction

def relative_vector_opposite(true_variable_magnitude, angle):
    
    '''
    This is one of the consitutent parts of the law of cosines, it works out the relative magnitude of the variable
    perpendicular to the ship
    '''
    x = - true_variable_magnitude * np.sin(angle)
    
    return x

def relative_vector_adjacent(true_variable_magnitude, angle, speed_over_ground ):
    
    '''
    This is one of the consitutent parts of the law of cosines, it works out the relative magnitude of the variable
    perpendicular to the ship
    '''
    
    x = speed_over_ground - true_variable_magnitude * np.cos(angle)
    
    return x


def corrected_relative_wind_velocity(true_wind_velocity, speed_over_ground, true_wind_direction, ships_heading):
    '''
    Equation E-6 & E-9
    
    true_wind_velocity = V_WT
    speed_over_groun = V_G
    true_wind_direction = PSI_WT
    ships_heading = psi
    
    This equation is the law of cosines
    
    Can produce significant rounding errors for small values of V_WT. This may not be a problem as it would mean relative wind speed is either,
    0 or close to full windspeed. Should be checked
    '''
    
    adjacent = relative_vector_adjacent(-true_wind_velocity, true_wind_direction - ships_heading, speed_over_ground )**2 
    opposite = relative_vector_opposite(-true_wind_velocity, true_wind_direction - ships_heading )**2
    
    return np.sqrt(adjacent + opposite)


def corrected_relative_wind_direction(true_wind_velocity, speed_over_ground, true_wind_direction, ships_heading, constrain_to_positive = True):
    
    '''
    Equation E-7 & E-10
    
    true_wind_velocity = V_WT
    speed_over_groun = V_G
    true_wind_direction = PSI_WT
    ships_heading = psi
    
    '''
    
    opposite = relative_vector_opposite(-true_wind_velocity, true_wind_direction - ships_heading )
    adjacent_plus_sog =  relative_vector_adjacent(-true_wind_velocity, true_wind_direction - ships_heading, speed_over_ground ) 
    
    relative_wind_direction = np.arctan2(opposite, adjacent_plus_sog)
    
    #prevents negative angles if constrain to positive is true
    relative_wind_direction = relative_wind_direction + 2*np.pi*(relative_wind_direction<0)*constrain_to_positive
       
    return relative_wind_direction

def true_wind_velocity(relative_wind_velocity, speed_over_ground, relative_wind_direction):
    
    '''
    E-2
    
        very similar to "relative_vector_adjacent" and corrected_relative_wind_velocity. only differences are uses a single angle
        and wind direction is positive
    
    '''
    
    adjacent = relative_vector_adjacent(relative_wind_velocity, relative_wind_direction, speed_over_ground )**2 
    opposite = relative_vector_opposite(relative_wind_velocity, relative_wind_direction )**2
    
    return np.sqrt(adjacent + opposite)


def relative_to_true_wind_direction_fn(relative_wind_velocity, speed_over_ground, relative_wind_direction, ships_heading, constrain_to_positive = True):
    
    
    '''
    E-3
    '''
    
    sin_ship_speed = speed_over_ground * np.sin(ships_heading)
    sin_wind_speed = relative_wind_velocity * np.sin(relative_wind_direction + ships_heading )
    cos_wind_speed = relative_wind_velocity * np.cos(relative_wind_direction + ships_heading) 
    cos_ship_speed = speed_over_ground * np.cos(ships_heading) 
    
    true_wind_direction = np.arctan2(sin_wind_speed - sin_ship_speed,  cos_wind_speed - cos_ship_speed  )
    #SHOULD THE CONSTRAIN TO POSITIVE SHOULD BE ITS OWN FUNCTION
    true_wind_direction = true_wind_direction + 2 * np.pi * (true_wind_direction<0) * constrain_to_positive
    
    return true_wind_direction

def vertical_position_anemometer(wind_velocity, ref_height, measured_height ):
    '''
    Equation E-8
    
    '''
    
    return wind_velocity * (ref_height/measured_height)^(1/9)
    
    
    
