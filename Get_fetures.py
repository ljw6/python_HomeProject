"""
音频特征提取及处理
"""
from Data_get import get_audio
from Data_process import reduce_noise
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import pandas as pd
import wave
import librosa
import librosa.display as ld
import logging as log
log.basicConfig(level=log.INFO,
format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
#载入wav文件
y,sr=librosa.load("en_outfile.wav")#处理过后音频
#y1,sr1=librosa.load("out.wav")#未降噪处理音频
#提取特征 提取Log-Mel Spectrogram 特征（梅尔频谱）
#提取得到的梅尔频谱特征melspec为二维数组(矩阵)
melspec = librosa.feature.melspectrogram(y, sr, n_fft=1024, hop_length=512, n_mels=128)#分帧，加权，增窗
#对数转换
log_mel = librosa.power_to_db(melspec)
log.info(log_mel)
#绘制频谱图
# plt.figure()
# plt.subplot(2,1,1)
# ld.waveplot(y,sr)
# plt.title("已处理频谱")
# plt.subplot(2,1,2)
# ld.waveplot(y1,sr1)
# plt.title("未处理")
# plt.show()