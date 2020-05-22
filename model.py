import numpy as np
import pickle
import cv2, os
from glob import glob
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D, AveragePooling2D
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
from keras import backend as K
K.image_data_format()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def get_image_size():
	img = cv2.imread('new_gest/1/30.jpg', 0)
	return img.shape

def get_num_of_classes():
	return len(glob('new_gest/*'))

image_x, image_y = get_image_size()

def cnn_model():
	num_of_classes = get_num_of_classes()
	#Instantiate an empty model
	model = Sequential()

	# C1 Convolutional Layer
	model.add(Conv2D(6, kernel_size=(5, 5), strides=(1, 1), activation='tanh', input_shape=(image_x,image_y,1), padding='same'))

	# S2 Pooling Layer
	model.add(AveragePooling2D(pool_size=(2, 2), strides=(1, 1), padding='valid'))

	# C3 Convolutional Layer
	model.add(Conv2D(16, kernel_size=(5, 5), strides=(1, 1), activation='tanh', padding='valid'))

	# S4 Pooling Layer
	model.add(AveragePooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))

	# C5 Fully Connected Convolutional Layer
	model.add(Conv2D(120, kernel_size=(5, 5), strides=(1, 1), activation='tanh', padding='valid'))
	#Flatten the CNN output so that we can connect it with fully connected layers
	model.add(Flatten())

	# FC6 Fully Connected Layer
	model.add(Dense(84, activation='tanh'))

	#Output Layer with softmax activation
	model.add(Dense(num_of_classes, activation='softmax')) 
	sgd = optimizers.SGD(lr=1e-2)
	model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
	filepath="cnn_model_keras2.h5"
	checkpoint1 = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
	callbacks_list = [checkpoint1]
	#from keras.utils import plot_model
	#plot_model(model, to_file='model.png', show_shapes=True)
	return model, callbacks_list

def train():	
	with open("train_images", "rb") as f:
		train_images = np.array(pickle.load(f))
	with open("train_labels", "rb") as f:
		train_labels = np.array(pickle.load(f), dtype=np.int32)

	with open("val_images", "rb") as f:
		val_images = np.array(pickle.load(f))
	with open("val_labels", "rb") as f:
		val_labels = np.array(pickle.load(f), dtype=np.int32)

	#print(val_labels.shape)

	
	train_images = np.reshape(train_images, (train_images.shape[0], image_x, image_y, 1))
	val_images = np.reshape(val_images, (val_images.shape[0], image_x, image_y, 1))

	print(train_labels)
	train_labels = np_utils.to_categorical(train_labels)
	val_labels = np_utils.to_categorical(val_labels)



	print(train_labels)


	model, callbacks_list = cnn_model()
	model.summary()
	model.fit(train_images, train_labels, validation_data=(val_images, val_labels), epochs=15, batch_size=500, callbacks=callbacks_list)
	scores = model.evaluate(val_images, val_labels, verbose=0)
	print("CNN Error: %.2f%%" % (100-scores[1]*100))
	model.save('cnn_model_keras2.h5')

def debug():
	num_of_classes = get_num_of_classes()
	print("no of classes")
	print(num_of_classes)


debug()
train()
K.clear_session()