import pandas as pd
import numpy as np


monthly_value = 500
interest = 0.07

x = monthly_value * ((1 + (interest / 12)))
y = (x + monthly_value) * ((1 + (interest / 12)))
z = (y + monthly_value) * ((1 + (interest / 12)))

new_value = 500

empty_list = []
new_value = new_value * (1 + (interest / 12))
empty_list.append(new_value)
i = 0
while i < 24:
    i += 1
    new_value = (new_value + monthly_value) * ((1 + (interest / 12)))
    empty_list.append(new_value)
    

empty_list[-1]
