# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython




# %%
## load the libraries 
import sys
import warnings
import os
import glob
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import cv2
from sklearn.model_selection import train_test_split

from keras.layers import *
from keras.callbacks import EarlyStopping
from keras.utils.np_utils import to_categorical
from tensorflow.keras.models import Model
from keras.models import Sequential
from keras.metrics import *
from keras.optimizers import Adam, RMSprop
from scipy.stats import norm
from keras.preprocessing import image
from keras import datasets
import tensorflow as tf
from keras import backend as K

from imgaug import augmenters
import matplotlib.pyplot as plt
plt.gray()



# %%
# # !pwd

# !unzip ./21-MAI.zip


# %%
TRAIN_IMAGES = glob.glob('21-MAI/Train/*.jpg')
CLEAN_IMAGES = glob.glob('21-MAI/original/*.jpg')
TEST_IMAGES = glob.glob('21-MAI/test/*.*')


# %%
plt.figure(figsize=(20,8))
img = cv2.imread('21-MAI/Train/0.jpg', 0)
plt.imshow(img, cmap='gray')
print(img.shape)


# %%
plt.figure(figsize=(20,8))
img = cv2.imread('21-MAI/original/0.jpg', 0)
plt.imshow(img, cmap='gray')
print(img.shape)


# %%
def load_image(path):
    image_list = np.zeros((len(path), 768, 1024, 1))
    for i, fig in enumerate(path):
        img = image.load_img(fig, grayscale=True, target_size=(768, 1024))
        x = image.img_to_array(img).astype('float32')
        x = x / 255.0
        image_list[i] = x
    
    return image_list

x_train = load_image(TRAIN_IMAGES)
y_train = load_image(CLEAN_IMAGES)
x_test = load_image(TEST_IMAGES)

print(x_train.shape, x_test.shape,y_train.shape)


# %%
x_train.shape


# %%
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2)
print(x_train.shape, x_val.shape)


# %%
plt.imshow(x_train[10, :, :, 0])


# %%
plt.imshow(y_train[10, :, :, 0])


# %%
input_layer = Input(shape=(768, 1024, 1))
        
# # encoder
encoder = Conv2D(64, (3, 3), activation='relu', padding='same')(input_layer)
encoder = MaxPooling2D( (2, 2), padding='same')(encoder)
encoder = Conv2D(32, (3, 3), activation='relu', padding='same')(encoder)
encoder = MaxPooling2D( (2, 2), padding='same')(encoder)
# encoder = Conv2D(16, (3, 3), activation='relu', padding='same')(encoder)
# encoder = MaxPooling2D((2, 2), padding='same')(encoder)

# decoder
# decoder = Conv2D(16, (3, 3), activation='relu', padding='same')(encoder)
# decoder = UpSampling2D((2, 2))(decoder)
decoder = Conv2D(32, (3, 3), activation='relu', padding='same')(encoder)
decoder = UpSampling2D((2, 2))(decoder)
decoder = Conv2D(64, (3, 3), activation='relu',padding='same')(decoder)
decoder = UpSampling2D((2, 2))(decoder)
output_layer = Conv2D(1, (3, 3), activation='sigmoid',padding='same')(decoder)

ae = Model(input_layer, output_layer)


# %%
# input_layer = Input(shape=(788, 1024, 1))
        
# # encoder
# encoder = Conv2D(64, (3, 3), activation='relu', padding='same')(input_layer)
# encoder = MaxPooling2D((2, 2), padding='same')(encoder)

# # decoder
# decoder = Conv2D(64, (3, 3), activation='relu', padding='same')(encoder)
# decoder = UpSampling2D((2, 2))(decoder)
# output_layer = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(decoder)

# ae = Model(input_layer, output_layer)


# %%
ae.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.001))
# ae.compile(optimizer='adam',loss='mse')
ae.summary()


# %%
batch_size = 16
epochs = 500

early_stopping = EarlyStopping(monitor='val_loss',min_delta=0,patience=10,verbose=1, mode='auto')
history = ae.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(x_val, y_val), callbacks=[early_stopping])
# history = ae.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(x_val, y_val))


# %%
preds = ae.predict(x_test)


# %%
n = 17

headPath = "/content/drive/MyDrive/21-ManufactureAI/Result1/"
for n in range(12):
  preds_0 = preds[n] * 255.0
  preds_0 = preds_0.reshape(768, 1024)
  x_test_0 = x_test[n] * 255.0
  x_test_0 = x_test_0.reshape(768, 1024)
  plt.imshow(x_test_0, cmap='gray')
  plt.savefig(str(n)+"compare.png",dpi=300)
  plt.imshow(preds_0, cmap='gray')
  plt.savefig(str(n)+"result.png",dpi=300)


# %%


# %% [markdown]
# ## Part 4: Generating New Fashion using VAEs
# %% [markdown]
# ### Understanding VAEs
# %% [markdown]
# !["VAE"](http://www.cvc.uab.es/people/joans/slides_tensorflow/tensorflow_html/vae_files/ae.png)
# %% [markdown]
# ### Reset data

# %%
### read dataset 
train = pd.read_csv("fashion-mnist_train.csv")
train_x = train[list(train.columns)[1:]].values
train_x, val_x = train_test_split(train_x, test_size=0.2)

## create train and validation datasets
train_x, val_x = train_test_split(train_x, test_size=0.2)


# %%
## normalize and reshape
train_x = train_x/255.
val_x = val_x/255.

train_x = train_x.reshape(-1, 28, 28, 1)
val_x = val_x.reshape(-1, 28, 28, 1)

# %% [markdown]
# ### Setup Encoder Neural Network
# %% [markdown]
# Try different number of hidden layers, nodes?

# %%
import keras.backend as K


# %%
batch_size = 16
latent_dim = 2  # Number of latent dimension parameters

input_img = Input(shape=(784,), name="input")
x = Dense(512, activation='relu', name="intermediate_encoder")(input_img)
x = Dense(2, activation='relu', name="latent_encoder")(x)

z_mu = Dense(latent_dim)(x)
z_log_sigma = Dense(latent_dim)(x)


# %%
# sampling function
def sampling(args):
    z_mu, z_log_sigma = args
    epsilon = K.random_normal(shape=(K.shape(z_mu)[0], latent_dim),
                              mean=0., stddev=1.)
    return z_mu + K.exp(z_log_sigma) * epsilon

# sample vector from the latent distribution
z = Lambda(sampling)([z_mu, z_log_sigma])


# %%
# decoder takes the latent distribution sample as input
decoder_input = Input((2,), name="input_decoder")

x = Dense(512, activation='relu', name="intermediate_decoder", input_shape=(2,))(decoder_input)

# Expand to 784 total pixels
x = Dense(784, activation='sigmoid', name="original_decoder")(x)

# decoder model statement
decoder = Model(decoder_input, x)

# apply the decoder to the sample from the latent distribution
z_decoded = decoder(z)


# %%
decoder.summary()


# %%
# construct a custom layer to calculate the loss
class CustomVariationalLayer(Layer):

    def vae_loss(self, x, z_decoded):
        x = K.flatten(x)
        z_decoded = K.flatten(z_decoded)
        # Reconstruction loss
        xent_loss = binary_crossentropy(x, z_decoded)
        return xent_loss

    # adds the custom loss to the class
    def call(self, inputs):
        x = inputs[0]
        z_decoded = inputs[1]
        loss = self.vae_loss(x, z_decoded)
        self.add_loss(loss, inputs=inputs)
        return x

# apply the custom loss to the input images and the decoded latent distribution sample
y = CustomVariationalLayer()([input_img, z_decoded])


# %%
z_decoded


# %%
# VAE model statement
vae = Model(input_img, y)
vae.compile(optimizer='rmsprop', loss=None)


# %%
vae.summary()


# %%
train_x.shape


# %%
train_x = train_x.reshape(-1, 784)
val_x = val_x.reshape(-1, 784)


# %%
vae.fit(x=train_x, y=None,
        shuffle=True,
        epochs=20,
        batch_size=batch_size,
        validation_data=(val_x, None))


# %%
# Display a 2D manifold of the samples
n = 20  # figure with 20x20 samples
digit_size = 28
figure = np.zeros((digit_size * n, digit_size * n))

# Construct grid of latent variable values - can change values here to generate different things
grid_x = norm.ppf(np.linspace(0.05, 0.95, n))
grid_y = norm.ppf(np.linspace(0.05, 0.95, n))

# decode for each square in the grid
for i, yi in enumerate(grid_x):
    for j, xi in enumerate(grid_y):
        z_sample = np.array([[xi, yi]])
        z_sample = np.tile(z_sample, batch_size).reshape(batch_size, 2)
        
        x_decoded = decoder.predict(z_sample, batch_size=batch_size)
        
        digit = x_decoded[0].reshape(digit_size, digit_size)
        
        figure[i * digit_size: (i + 1) * digit_size,
               j * digit_size: (j + 1) * digit_size] = digit

plt.figure(figsize=(20, 20))
plt.imshow(figure)
plt.show()  


# %%
### read dataset 
train = pd.read_csv("fashion-mnist_train.csv")
train_x = train[list(train.columns)[1:]].values
train_y = train[list(train.columns)[0]].values

train_x = train_x/255.
# train_x = train_x.reshape(-1, 28, 28, 1)

# Translate into the latent space
encoder = Model(input_img, z_mu)
x_valid_noTest_encoded = encoder.predict(train_x, batch_size=batch_size)
plt.figure(figsize=(10, 10))
plt.scatter(x_valid_noTest_encoded[:, 0], x_valid_noTest_encoded[:, 1], c=train_y, cmap='brg')
plt.colorbar()
plt.show()

# %% [markdown]
# ## Part 5: Exercise: Generating New Fashion using VAEs: Adding CNNs and KL Divergence Loss

# %%
batch_size = 16
latent_dim = 2  # Number of latent dimension parameters

# Encoder architecture: Input -> Conv2D*4 -> Flatten -> Dense
input_img = Input(shape=(28, 28, 1))

x = Conv2D(32, 3,
                  padding='same', 
                  activation='relu')(input_img)
x = Conv2D(64, 3,
                  padding='same', 
                  activation='relu',
                  strides=(2, 2))(x)
x = Conv2D(64, 3,
                  padding='same', 
                  activation='relu')(x)
x = Conv2D(64, 3,
                  padding='same', 
                  activation='relu')(x)

# need to know the shape of the network here for the decoder
shape_before_flattening = K.int_shape(x)

x = Flatten()(x)
x = Dense(32, activation='relu')(x)

# Two outputs, latent mean and (log)variance
z_mu = Dense(latent_dim)(x)
z_log_sigma = Dense(latent_dim)(x)

# %% [markdown]
# ### Set up sampling function

# %%
# sampling function
def sampling(args):
    z_mu, z_log_sigma = args
    epsilon = K.random_normal(shape=(K.shape(z_mu)[0], latent_dim),
                              mean=0., stddev=1.)
    return z_mu + K.exp(z_log_sigma) * epsilon

# sample vector from the latent distribution
z = Lambda(sampling)([z_mu, z_log_sigma])

# %% [markdown]
# ### Setup Decoder Neural Network
# %% [markdown]
# Try different number of hidden layers, nodes?

# %%
# decoder takes the latent distribution sample as input
decoder_input = Input(K.int_shape(z)[1:])

# Expand to 784 total pixels
x = Dense(np.prod(shape_before_flattening[1:]),
                 activation='relu')(decoder_input)

# reshape
x = Reshape(shape_before_flattening[1:])(x)

# use Conv2DTranspose to reverse the conv layers from the encoder
x = Conv2DTranspose(32, 3,
                           padding='same', 
                           activation='relu',
                           strides=(2, 2))(x)
x = Conv2D(1, 3,
                  padding='same', 
                  activation='sigmoid')(x)

# decoder model statement
decoder = Model(decoder_input, x)

# apply the decoder to the sample from the latent distribution
z_decoded = decoder(z)

# %% [markdown]
# ### Set up loss functions

# %%
# construct a custom layer to calculate the loss
class CustomVariationalLayer(Layer):

    def vae_loss(self, x, z_decoded):
        x = K.flatten(x)
        z_decoded = K.flatten(z_decoded)
        # Reconstruction loss
        xent_loss = binary_crossentropy(x, z_decoded)
        # KL divergence
        kl_loss = -5e-4 * K.mean(1 + z_log_sigma - K.square(z_mu) - K.exp(z_log_sigma), axis=-1)
        return K.mean(xent_loss + kl_loss)

    # adds the custom loss to the class
    def call(self, inputs):
        x = inputs[0]
        z_decoded = inputs[1]
        loss = self.vae_loss(x, z_decoded)
        self.add_loss(loss, inputs=inputs)
        return x

# apply the custom loss to the input images and the decoded latent distribution sample
y = CustomVariationalLayer()([input_img, z_decoded])

# %% [markdown]
# ### Train VAE

# %%
# VAE model statement
vae = Model(input_img, y)
vae.compile(optimizer='rmsprop', loss=None)


# %%
vae.summary()


# %%
train_x = train_x.reshape(-1, 28, 28, 1)
val_x = val_x.reshape(-1, 28, 28, 1)


# %%
vae.fit(x=train_x, y=None,
        shuffle=True,
        epochs=20,
        batch_size=batch_size,validation_data=(val_x, None))

# %% [markdown]
# ### Visualize Samples reconstructed by VAE

# %%
# Display a 2D manifold of the samples
n = 20  # figure with 20x20 samples
digit_size = 28
figure = np.zeros((digit_size * n, digit_size * n))

# Construct grid of latent variable values - can change values here to generate different things
grid_x = norm.ppf(np.linspace(0.05, 0.95, n))
grid_y = norm.ppf(np.linspace(0.05, 0.95, n))

# decode for each square in the grid
for i, yi in enumerate(grid_x):
    for j, xi in enumerate(grid_y):
        z_sample = np.array([[xi, yi]])
        z_sample = np.tile(z_sample, batch_size).reshape(batch_size, 2)
        x_decoded = decoder.predict(z_sample, batch_size=batch_size)
        digit = x_decoded[0].reshape(digit_size, digit_size)
        figure[i * digit_size: (i + 1) * digit_size,
               j * digit_size: (j + 1) * digit_size] = digit

plt.figure(figsize=(20, 20))
plt.imshow(figure)
plt.show()  

# %% [markdown]
# ## TODO:
# #### VAE: Visualize latent space

# %%
train = pd.read_csv("fashion-mnist_train.csv")


# %%
### read dataset 
train = pd.read_csv("fashion-mnist_train.csv")
train_x = train[list(train.columns)[1:]].values
train_y = train[list(train.columns)[0]].values

train_x = train_x/255.
train_x = train_x.reshape(-1, 28, 28, 1)


# %%
# Translate into the latent space
encoder = Model(input_img, z_mu)
x_valid_noTest_encoded = encoder.predict(train_x, batch_size=batch_size)
plt.figure(figsize=(10, 10))
plt.scatter(x_valid_noTest_encoded[:, 0], x_valid_noTest_encoded[:, 1], c=train_y, cmap='brg')
plt.colorbar()
plt.show()


