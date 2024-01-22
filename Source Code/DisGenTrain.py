{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "99ce5d58",
   "metadata": {},
   "outputs": [],
   "source": [
    "from os import listdir\n",
    "from numpy import asarray\n",
    "from numpy import vstack\n",
    "#from keras.preprocessing.image import img_to_array\n",
    "from keras.utils.image_utils import img_to_array\n",
    "#from keras.preprocessing.image import load_img\n",
    "from keras.utils.image_utils import load_img \n",
    "from matplotlib import pyplot as plt\n",
    "import numpy as np\n",
    "import PIL\n",
    "from pathlib import Path\n",
    "from PIL import UnidentifiedImageError\n",
    "\n",
    "# load all images in a directory into memory\n",
    "def load_images(path, size=(256,256)):\n",
    "\tdata_list = list()\n",
    "\t\n",
    "\tfor filename in listdir(path):\n",
    "\t\t\n",
    "\t\tpixels = load_img(path + filename, target_size=size)\n",
    "\t\t\n",
    "\t\tpixels = img_to_array(pixels)\n",
    "\t\t\n",
    "\t\tdata_list.append(pixels)\n",
    "\treturn asarray(data_list)\n",
    "\n",
    "\n",
    "\n",
    "path = 'monet2photo/'\n",
    "\n",
    "# load dataset A - Monet paintings\n",
    "dataA_all = load_images(path + 'trainA/')\n",
    "print('Loaded dataA: ', dataA_all.shape)\n",
    "\n",
    "from sklearn.utils import resample\n",
    "#To get a subset of all images, for faster training during demonstration\n",
    "dataA = resample(dataA_all, \n",
    "                 replace=False,     \n",
    "                 n_samples=500,    \n",
    "                 random_state=42) \n",
    "\n",
    "# load dataset B - Photos \n",
    "dataB_all = load_images(path + 'trainB/')\n",
    "print('Loaded dataB: ', dataB_all.shape)\n",
    "#Get a subset of all images, for faster training during demonstration\n",
    "dataB = resample(dataB_all, \n",
    "                 replace=False,     \n",
    "                 n_samples=500,    \n",
    "                 random_state=42) \n",
    "\n",
    "# plot source images\n",
    "n_samples = 3\n",
    "for i in range(n_samples):\n",
    "\tplt.subplot(2, n_samples, 1 + i)\n",
    "\tplt.axis('off')\n",
    "\tplt.imshow(dataA[i].astype('uint8'))\n",
    "# plot target image\n",
    "for i in range(n_samples):\n",
    "\tplt.subplot(2, n_samples, 1 + n_samples + i)\n",
    "\tplt.axis('off')\n",
    "\tplt.imshow(dataB[i].astype('uint8'))\n",
    "plt.show()\n",
    "\n",
    "\n",
    "\n",
    "# load image data\n",
    "data = [dataA, dataB]\n",
    "\n",
    "print('Loaded', data[0].shape, data[1].shape)\n",
    "\n",
    "def preprocess_data(data):\n",
    "\t# load compressed arrays\n",
    "\t# unpack arrays\n",
    "\tX1, X2 = data[0], data[1]\n",
    "\t# scale from [0,255] to [-1,1]\n",
    "\tX1 = (X1 - 127.5) / 127.5\n",
    "\tX2 = (X2 - 127.5) / 127.5\n",
    "\treturn [X1, X2]\n",
    "\n",
    "dataset = preprocess_data(data)\n",
    "\n",
    "#from cycleGAN_model import define_generator, define_discriminator, define_composite_model, train\n",
    "# define input shape based on the loaded dataset\n",
    "image_shape = dataset[0].shape[1:]\n",
    "# generator: A -> B\n",
    "g_model_AtoB = define_generator(image_shape)\n",
    "# generator: B -> A\n",
    "g_model_BtoA = define_generator(image_shape)\n",
    "# discriminator: A -> [real/fake]\n",
    "d_model_A = define_discriminator(image_shape)\n",
    "# discriminator: B -> [real/fake]\n",
    "d_model_B = define_discriminator(image_shape)\n",
    "# composite: A -> B -> [real/fake, A]\n",
    "c_model_AtoB = define_composite_model(g_model_AtoB, d_model_B, g_model_BtoA, image_shape)\n",
    "# composite: B -> A -> [real/fake, B]\n",
    "c_model_BtoA = define_composite_model(g_model_BtoA, d_model_A, g_model_AtoB, image_shape)\n",
    "\n",
    "from datetime import datetime \n",
    "start1 = datetime.now() \n",
    "# train models\n",
    "train(d_model_A, d_model_B, g_model_AtoB, g_model_BtoA, c_model_AtoB, c_model_BtoA, dataset, epochs=5)\n",
    "\n",
    "stop1 = datetime.now()\n",
    "#Execution time of the model \n",
    "execution_time = stop1-start1\n",
    "print(\"Execution time is: \", execution_time)\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}