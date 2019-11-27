import pickle
import os
import numpy as np
import argparse

def split_data(source_in, target_in):

    #load source and target from pickle
    source_file = open(source_in, 'rb')
    target_file = open(target_in, 'rb')

    print('loading from pickle')
    source = pickle.load(source_file)
    print('Source loaded')
    target = pickle.load(target_file)
    print('Target loaded.')
    #shuffle target

    print('Shuffling target.')
    np.random.shuffle(target)

    print('Creating source dictionary')
    source_dict = make_dict(source)
    #target_dict = make_dict(target)

    #split 60 / 20 / 20     train / test / val,
    #for each split, save as 'source filename', 'source melspect' , 'target_melspect'
    train = []
    test = []
    val = []

    #TODO: We also need to sort these via length to avoid having to pad a lot. We can maybe use len(melspect[1])

    print('Building training data')
    for target_filename, target_melspect in target[0:26442]:
        #fill train
        filename_parts = target_filename.split('_')
        #target filename is t_pXXX_YYY.wav, convert to pXXX_YYY
        source_filename = filename_parts[1] + '_' + filename_parts[2]
        print(source_filename)
        source_melspect = source_dict[source_filename]
        source_len = len(source_melspect[1])
        train.append([source_len, source_filename, source_melspect, target_melspect])
        train.sort()

    print('Building testing data')
    for target_filename, target_melspect in target[26442:35256]:
        #fill test
        filename_parts = target_filename.split('_')
        #target filename is t_pXXX_YYY.wav, convert to pXXX_YYY
        source_filename = filename_parts[1] + '_' + filename_parts[2]
        print(source_filename)
        source_melspect = source_dict[source_filename]
        source_len = len(source_melspect[1])
        test.append([source_len, source_filename, source_melspect, target_melspect])
        test.sort()

    print('Building validation data')
    for target_filename, target_melspect in target[35256:]:
        #fill val
        filename_parts = target_filename.split('_')
        #target filename is t_pXXX_YYY.wav, convert to pXXX_YYY
        source_filename = filename_parts[1] + '_' + filename_parts[2]
        print(source_filename)
        source_melspect = source_dict[source_filename]
        source_len = len(source_melspect[1])
        val.append([source_len, source_filename, source_melspect, target_melspect])
        val.sort()

    #save train, test, and val
    pickle.dump(train, open('/data/mer/VCTK/train.p', 'wb'))
    pickle.dump(test, open('/data/mer/VCTK/test.p', 'wb'))
    pickle.dump(val, open('/data/mer/VCTK/val.p', 'wb'))



def make_dict(list):
    dict = {'filename' : 'melspect'}
    for element in list:
        #add a new key-value pair in dictionary
        dict.update({element[0]: element[1]})
    return dict






if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source')
    parser.add_argument('--target')
    args = parser.parse_args()
    split_data(args.source, args.target)