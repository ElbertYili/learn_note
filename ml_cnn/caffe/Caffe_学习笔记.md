## Denny的学习专栏

### 一、数据层及参数

```Python
layer {
  name: "cifar"
  type: "Data"
  top: "data"
  top: "label"
  include {
    phase: TRAIN
  }
  transform_param {
    mean_file: "examples/cifar10/mean.binaryproto"
  }
  data_param {
    source: "examples/cifar10/cifar10_train_lmdb"
    batch_size: 100
    backend: LMDB
  }
}
```

* name:表示该层的名字，随意
* type:层类型，*Data*表示数据来源LMDB或LevelDB；*Input*
* top或bottom:每一层用bottom来输入数据，用top来输出数据，都是指定name。如果有多个 top或多个bottom，表示有多个blobs数据的输入和输出
  * *data 与 label*: 在数据层中，至少有一个命名为data的top。如果有第二个top，一般命名为label。 这种(data,label)配对是分类模型所必需的。
* include: 一般训练的时候和测试的时候，模型的层是不一样的。该层（layer）是属于训练阶段的层，还是属于测试阶段的层，需要用include来指定。如果没有include参数，则表示该层既在训练模型中，又在测试模型中。
* Transformations: 数据的预处理，可以将数据变换到定义的范围内



### 二、模块

* Blob：相当于tensor，是数据
* Layer：不仅可以表示神经网络层，也可以表示数据输入输出层。Blob在Layer上流动(forward & backward)
* Net：神经网络结构，将Layer关联和层叠起来
* Solver：协调神经网络的训练和测试、保存和恢复训练状态以及存储网络参数

*Note: prototxt描述文件大部分字段都非常好理解。对于不好理解的字段，或者是不知道有哪些参数的话，可以参考src/caffe/proto/caffe.proto. 这个文件里面每个字段都有比较详细说明。*



#### 2.1 Blob

四维数组，float32，(n, c, h, w)，

- n: number. 一次传播的输入数据量，比如进行sgd时候的mini-batch大小。
- c: channel. 如果是图像数据的话可以认为是通道数量。
- h,w: height, width. 如果是图像数据的话可以认为是图片的高度和宽度。



#### 2.2 Layer

[内置layer](http://caffe.berkeleyvision.org/tutorial/layers.html)

[完整Layer]([http://caffe.berkeleyvision.org/tutorial/layers.html](http://caffe.berkeleyvision.org/tutorial/layers.html))



#### 2.3 Net

Layer组成的DAG(邮箱无循环图)

使用文本格式来描述(protocol-buffers TextFormat)

```
name: "LogReg"
layers {
  name: "mnist"
  type: DATA
  top: "data"
  top: "label"
  data_param {
    source: "input_leveldb"
    batch_size: 64
  }
}
layers {
  name: "ip"
  type: INNER_PRODUCT
  bottom: "data"
  top: "ip"
  inner_product_param {
    num_output: 2
  }
}
layers {
  name: "loss"
  type: SOFTMAX_LOSS
  bottom: "ip"
  bottom: "label"
  top: "loss"
}
```

![](https://dirtysalt.github.io/images/caffe-net-logreg.jpg)

Net有很多函数，包括Init(), forward(), backward()等等



#### 2.4 Solver

优化、迭代、训练网络

工作：

- calls network forward to compute the output and loss
- calls network backward to compute the gradients
  - Stochastic Gradient Descent (SGD),
  - Adaptive Gradient (ADAGRAD),
  - Nesterov’s Accelerated Gradient (NESTEROV).
  - 如何选择和设置参数可以看 [这里](http://caffe.berkeleyvision.org/tutorial/solver.html)
- incorporates the gradients into parameter updates according to the solver method
- updates the solver state according to learning rate, history, and method




#### 2.5 配置文件

prototxt：solver、train_net、test_net（后两个可以用一个net的配置文件）