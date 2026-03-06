#import libraries and packages 
import mne
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

mne.set_log_level("WARNING")

# load dataset and all subjects 
# load all data file paths into eeg_files
data_path = Path("ds004504-download")
eeg_files = sorted(list(data_path.glob("sub-*/eeg/*.set")))