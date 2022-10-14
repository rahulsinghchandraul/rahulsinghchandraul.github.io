---
title: Signed Graph Neural Networks
layout: page
tags: GNN, Signed Graphs
permalink: /research/GNN.html
---

Graph convolutional networks (GCNs) and its variants are designed for unsigned graphs containing only positive links. 
Many existing GCNs have been derived from the spectral domain analysis of signals lying over (unsigned) graphs and in each convolution layer 
they perform low-pass filtering of the input features followed by a learnable linear transformation. 
Their extension to signed graphs with positive as well as negative links imposes multiple issues including computational irregularities and
ambiguous frequency interpretation, making the design of computationally efficient low pass filters challenging. 
In this paper, we address these issues via spectral analysis of signed graphs and propose two different signed graph neural networks, 
one keeps only low-frequency information and one also retains high-frequency information. 
We further introduce magnetic signed Laplacian and use its eigendecomposition for spectral analysis of directed signed graphs.
We test our methods for node classification and link sign prediction tasks on signed graphs and achieve state-of-the-art performances.

#### List of Publications: ####


1. [Signed Graph Neural Networks: A Frequency Perspective](https://arxiv.org/pdf/2208.07323.pdf){:target="_blank"} \\
**Rahul Singh** and Yongxin Chen 
