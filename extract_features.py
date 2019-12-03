
"""
A Collection of functions to extract features from the audio
"""
import numpy as np
import librosa
import argparse
import os
import pickle as pkl

def make_melspectrograms(data_loc, save_loc):

    data = []
    #iterate through the given data directory
    for filename in os.listdir(data_loc):
        print(filename)
        if filename.split('.')[-1] in ['wav', 'mp3']:
            #open the speech, and make the spectrogram
            y, sr = librosa.load(os.path.join(data_loc, filename))

            #TODO: attach arguments, right now it's hard coded the Google way, also for some reason win_length won't work
            y = librosa.core.resample(y, sr, 16000)
            spect = librosa.feature.melspectrogram(y=y, sr=16000, n_fft=1024, hop_length=200, fmax=7600, n_mels=80)

            #convert to log-scale (dbs)
            ps_db = librosa.power_to_db(spect, ref=np.max)

            #save the spectrogram... add to a list and save the list at the end.
            data.append([filename, ps_db])

    pkl.dump(data, open(os.path.join(save_loc, 'all_melspect.pkl'), 'wb'))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File to extract features from audio')
    parser.add_argument('--feature')
    parser.add_argument('--data_dir')
    parser.add_argument('--save_dir')
    args = parser.parse_args()

    if args.feature == 'melspect':
        make_melspectrograms(args.data_dir, args.save_dir)


