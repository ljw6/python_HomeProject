from Data_get import get_audio
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import pandas as pd
import librosa
import librosa.display
#调试
# import logging as log
# # log.basicConfig(level=log.INFO,
# # format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
#get_audio()
y,x = librosa.load("out.wav",sr=None)

#显示波形图
# plt.figure()
# librosa.display.waveplot(y, x)
# plt.title('Beat wavform')
# plt.show()