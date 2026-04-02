import settings

def height_perct(percentage): # define a function to calculate a percentage of screen height
    return (settings.height/100)*percentage # Return  the calculated height percentage based on settings.height

def width_perct(percentage):  # define a function to calculate a percentage of screen width
    return (settings.width/100)*percentage # Return  the calculated width percentage based on settings.width

