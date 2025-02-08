import tensorflow as tf

# tf.random.uniform (维度，minval = 最小值，maxval = 最大值)
f = tf.random.uniform([2, 2], minval=0, maxval=1)
print("f:", f)
