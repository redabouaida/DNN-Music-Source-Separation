SAMPLE_RATE = 44100
N_FFT = 4096
HOP_SIZE = 1024
N_OVERLAP = N_FFT - HOP_SIZE
NB_CHANNELS = 2
CONTEXT_SIZE = 5
NB_BINS = 2049
PATH_DATA = 'DSD100/'
PATH_DATA_SUBSET = 'DSD100subset/'
TARGET_NAMES = {'bass', 'drum', 'other', 'vocals'}