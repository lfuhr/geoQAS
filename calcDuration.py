"""
Used to estimate durations based the beeline and ratios
"""
v_pedestrian = 5#km/h
v_car = 18#km/h
blratio_car = 1.5
blratio_pedestrian = 1.4

def minutes_it_takes(distance, vehicle):
    if vehicle == "car": return distance * blratio_car * 60 / v_car
    elif vehicle == "pedestrian": return distance * blratio_pedestrian * 60 / v_pedestrian
    else: raise Exception("Unknown vehicle", vehicle)

def minutes_it_takes_string(vehicle) :
    if vehicle == "car": return str(blratio_car) + " / " + str(v_car)
    elif vehicle == "pedestrian": return str(blratio_pedestrian) + " / " + str(v_pedestrian)
    else: raise Exception("Unknown vehicle", vehicle)
