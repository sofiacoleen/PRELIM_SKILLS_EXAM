class Temperature:
    def __init__(self, kelvin=None, celsius=None, fahrenheit=None):
        values = [x for x in [kelvin, celsius, fahrenheit] if x]
        if len(values) < 1: 
            raise ValueError('Need argument