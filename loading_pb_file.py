# # load & inference the model ==================
import tensorflow as tf

from tensorflow.python.platform import gfile
with tf.Session() as sess:
    # load model from pb file
    with gfile.FastGFile('./sign_lang_tf.pb','rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        sess.graph.as_default()
        g_in = tf.import_graph_def(graph_def)
    # write to tensorboard (check tensorboard for each op names)
    writer = tf.compat.v1.summary.FileWriter('./log')
    writer.add_graph(sess.graph)
    writer.flush()
    writer.close()

    