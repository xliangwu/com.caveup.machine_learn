import tensorflow as tf

print("Tensorflow intro")
hello = tf.constant('Hello, Tensorflow')
session = tf.Session()
print(session.run(hello))
