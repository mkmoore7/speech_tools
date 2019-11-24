
"""
A Collection of functions to extract features from the audio
"""
import numpy as np
import librosa
import argparse
import os
import pickle as pkl

def make_melspectrograms(data_loc, save_loc, nfft, hop, win_len, fmax):

    data = []
    #iterate through the given data directory
    for filename in os.listdir(data_loc):

        #open the speech, and make the spectrogram
        y, sr = librosa.load(os.path.join(data_loc, filename))
        spect = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=nfft, hop_length=hop, win_length=win_len, fmax=fmax)

        #save the spectrogram... add to a list and save the list at the end.
        data.append([filename, spect])
        pkl.dump(open(os.path.join(save_loc, 'melspect.pkl'), 'wb'))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File to extract features from audio')
    parser.add_argument('--feature')
    parser.add_argument('--data_dir')
    parser.add_argument('--save_loc')
    parser.add_argument('--nfft')
    parser.add_argument('--hop')
    parser.add_argument('--win_len')
    parser.add_argument('--fmax')
    args = parser.parser_args()

    if args.feature == 'melspect':
        make_melspectrograms(args.data_dir, args.save_loc, args.nfft, args.hop, args.win_len, args.fmax)

