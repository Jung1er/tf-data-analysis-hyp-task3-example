import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp


chat_id = 392609262 # Ваш chat ID, не меняйте название переменной

def solution(arr) -> bool: 
    m = 500
    t_stat, p_val = ttest_1samp(arr, m)
    a = 0.02
    if p_val/2 < a and t_stat < 0:
        return True
    else:
        return False
