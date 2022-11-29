import tensorflow as tf
import os
import zipfile
import absl
from tensorflow.keras.preprocessing.image import ImageDataGenerator


zip = 'autistic.zip'
ref = zipfile.ZipFile(zip, 'r')
ref.extractall('/autis')
ref.close()


base_dir = '/autis'
train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'valid')

train_datagen = ImageDataGenerator(
    rescale = 1/255,
    rotation_range = 20,
    horizontal_flip = True,
    shear_range = 0.2,
    fill_mode = 'nearest'
)

test_datagen = ImageDataGenerator(
    rescale = 1/255
)

train_generator = train_datagen.flow_from_directory(
    train_dir, # direktori data latih
    target_size = (150, 150), # mengubah resolusi seluruh gambar menjadi 150x150 piksel
    # karena ini merupakan masalah klasifikasi 2 kelas, gunakan class_mode = 'binary'
    class_mode = 'binary'
)

val_generator = test_datagen.flow_from_directory(
    val_dir, # direktori data validasi
    target_size = (150, 150), # mengubah resolusi seluruh gambar menjadi 150x150 piksel
    batch_size = 4, # karena ini merupakan masalah klasifikasi 2 kelas gunakan class_mode = 'binary'
    class_mode = 'binary'
)

model = tf.keras.models.Sequential([
      tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
      tf.keras.layers.MaxPooling2D(2, 2),
      tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
      tf.keras.layers.MaxPooling2D(2,2),
      tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
      tf.keras.layers.MaxPooling2D(2,2),
      tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
      tf.keras.layers.MaxPooling2D(2,2),
      tf.keras.layers.Conv2D(512, (3,3), activation='relu'),
      tf.keras.layers.MaxPooling2D(2,2),
      tf.keras.layers.Flatten(),
      tf.keras.layers.Dense(512, activation='relu'),
      tf.keras.layers.Dense(1, activation='sigmoid')
])

model.summary()

# compile model dengan 'adam' optimizer loss function 'binary_crossentropy' 
model.compile(
    loss='binary_crossentropy',
    optimizer=tf.optimizers.Adam(),
    metrics=['accuracy']
)

# latih model dengan model.fit 
model.fit(
    train_generator,
    steps_per_epoch=12,
    epochs=35, 
    validation_data=val_generator, 
    validation_steps=5, 
    verbose=2
)

# save model
export_path = 'autistic_model'

tf.keras.models.save_model(
    model,
    export_path,
    overwrite=True,
    include_optimizer=True,
    save_format=None,
    signatures=None,
    options=None
)