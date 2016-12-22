path = '/Users/rantidevsharma/personal/dcgan/keras-dcgan-master/genres/jazz/'
import numpy as np
import os
import librosa
smcam = np.zeros((100,400,400),dtype=np.float32)

# Reads wav file and produces spectrum
# Fourier phases are ignored
N_FFT = 798
def read_audio_spectum(filename):
    x, fs = librosa.load(filename)
    S = librosa.stft(x, N_FFT)
    p = np.angle(S)
    return np.log1p(np.abs(S[np.newaxis,:,:400])), fs
i=0
for filename in os.listdir(path):
	pf = path+filename
	print pf
	aa=read_audio_spectum(pf)
	smcam[i]=aa.reshape(400,400)
	i=i+1


np.savez('simple_data_test.npz',imgs=smcam)


