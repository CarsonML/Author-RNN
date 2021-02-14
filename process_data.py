import os
import re
import random
import numpy as np
import tensorflow as tf
import pickle
directory = "./orig_data"
total_indiv = []
total_total = []
for filename in os.listdir(directory):
    with open(os.path.join(directory, filename)) as file:
        current_text = file.read()
    current_text = current_text.lower()
    current_text = current_text.replace("'", "")
    current_text = current_text.replace("_", " ")
    current_text = current_text.replace("’", "")
    current_text = current_text.replace("-", " ")
    current_text = current_text.replace("—", " ")
    lis = re.findall(r"[\w']+|[\]\[\(\).,!?;]", current_text)
    total_indiv.append(lis)
    total_total += lis
print("tokenizing")
tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='',lower=True, split=' ')
tokenizer.fit_on_texts(total_total)
print("transform")
data = tokenizer.texts_to_sequences(total_indiv)
def data_iteration():
    final = []
    for i in range(6):
        total = []
        for ii in range(len(data[i])-101):
            gi = ii + 0
            if (gi % 50000 == 0):
                print(gi)
            start_index = gi
            X = data[i][start_index:start_index+100]
            # y_gen = [0] * (len(tokenizer.word_index) + 1)
            y_gen = [data[i][start_index+100]]
            y_class = [0] * 6
            y_class[i] = 1
            total.append([X, y_class, y_gen])
        # random.shuffle(total)
        print(len(total))
        print(total[0:2])
        final.append(total)
    pickle.dump(final, open( "data3.pkl", "wb+" ) )
    pickle.dump(tokenizer, open("tokenizer3.pkl", "wb+"))
data_iteration()


