# Computation Graphs 101
+++
# What is a Computation Graph?
A graph formed by nodes which represent mathematical operations.
+++
# Why use this paradigm?
It allows a complex computation to be decomposed into a finite set of
primitives. The derivatives of these primitives can then be computed
automatically.

+++?image=imgs/huh_meme.jpg&size=contain
@title[Huh meme]

+++
# Example: Linear Regression
$$y = Wx + b$$

+++?image=imgs/graph_empty.jpg&size=contain
@title[Computation Graph]

+++?image=imgs/graph_forward.jpg&size=contain
@title[Forward Pass]

+++?image=imgs/graph_backward.jpg&size=contain
@title[Backward Pass]
