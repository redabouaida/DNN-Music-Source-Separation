from preprocessing import *
from keras.layers import Dense, Flatten, Input, concatenate, Reshape
from keras.models import Model
from keras.layers.advanced_activations import LeakyReLU

def amplitude_model():
    amplitude_input = Input(shape=(NB_BINS, NB_CHANNELS, 2*CONTEXT_SIZE+1))
    amplitude_output = Flatten()(amplitude_input)
    amplitude_output = Dense(500, activation=LeakyReLU())(amplitude_output)
    amplitude_output = Dense(500, activation=LeakyReLU())(amplitude_output)
    return amplitude_input, amplitude_output

def phase_model():
    phase_input = Input(shape=(NB_BINS, 2*NB_CHANNELS, 2*CONTEXT_SIZE+1))
    phase_output = Flatten()(phase_input)
    phase_output = Dense(500, activation=LeakyReLU())(phase_output)
    phase_output = Dense(500, activation=LeakyReLU())(phase_output)
    return phase_input, phase_output

def full_model(target_name, optimizer='adam'):
    amplitude_input, amplitude_output = amplitude_model()
    phase_input, phase_output = phase_model()

    output = concatenate([amplitude_output, phase_output])
    output = Dense(2*NB_BINS, activation=LeakyReLU())(output)
    output = Reshape((NB_BINS, 2))(output)
    
    model = Model(input=[amplitude_input, phase_input], output=output, name=target_name)
    model.compile(loss='mean_squared_error', optimizer=optimizer)

    return model

