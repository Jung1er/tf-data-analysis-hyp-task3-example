import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest


chat_id = 392609262 # Ваш chat ID, не меняйте название переменной

def solution(arr) -> bool:
    a = 0.02
    stat, p_val  = ztest(arr, value=500, alternative='larger')
    return p_val < a
