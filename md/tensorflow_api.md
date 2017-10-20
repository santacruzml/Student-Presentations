# TensorFlow API

+++?code=code/linear_regression.py&lang=python
@title[Example: Linear Regression]

@[9](Import Tensorflow)
@[13-18](Create inputs subgraph)
@[14-18](Define Placeholders)
@[20-26](Create model subgraph)
@[21-24](Define Variables)
@[26](Model prediction)
@[28-30](Define loss)
@[32-34](Define optimizer)
@[36](Define summary)
@[39-40](Training data)
@[42-44](Create Session)
@[45-46](Save graph)
@[48-52](Initialize Variables)
@[54-63](Training loop)
@[56-60](Evaluate nodes)
@[62-63](Save loss)
@[65-67](Get training results)

+++
# TensorBoard
```
tensorboard --logdir=logs
```

+++?image=imgs/tensorboard_graph.png&size=contain
@title[Graph Visualization]

+++?image=imgs/tensorboard_loss.png&size=auto 90%
@title[Loss Visualization]

