from matplotlib import pyplot as plt


ACTIVITY = float(100) # Bq

def get_activity_at_distance(source_activity:float, distance:float):
    '''Takes in activity at source and distance from source, and
    returns the activity at that distance using the inverse square law.'''

    def inverse_square_law(I1, X1, X2):
        I2 = I1 * (X1**2 /X2**2)
        return I2
    
    return inverse_square_law(source_activity, 0, distance)
        

def get_activity_at_location(source_activity:float, location:tuple):
    '''takes in activity at the source and
    the location of interest and uses the inverse 
    square law to return activity at the location.'''
    pass


# testing out different activities at different distances:
print(get_activity_at_distance(ACTIVITY, 1))
print(get_activity_at_distance(ACTIVITY, 10))
print(get_activity_at_distance(ACTIVITY, 30))