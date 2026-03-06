#import libraries and packages 
import mne # might need to pip install mne
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

mne.set_log_level("WARNING")

# load dataset and all subjects 
# load all data file paths into eeg_files
data_path = Path("ds004504-download")
eeg_files = sorted(list(data_path.glob("sub-*/eeg/*.set")))

# each subject load as a MNR raw object
file = eeg_files[0]
raw = mne.io.read_raw_eeglab(file, preload=True)