# Quantifying Privacy Leakage in Graph Embedding (MobiQuitous'20 and NeurIPS PPML '20)

Preprint: https://arxiv.org/pdf/2010.00906.pdf

The code is as follows:

1) AIA: Attribute inference attacks. The embeddings are already generated using code form their original repos.

2) MIA: Membership Inference attacks. The code is divided into blackbox (includes confidence score attacks and shadow model attack) and whitebox. MIA in blackbox setting is performed on inductive training of GraphSage model. 

3) Reconstruction: Graph Reconstruction using graph encoder decoder.

4) /data: Includes the facebook and LastFM dataset for attribute inference attacks. The data for graph reconstruction requires to load the train and test graphs seperately unlike what most libraries provider. The data can be obtained from https://github.com/DaehanKim/vgae_pytorch.


Credits:

- Node2Vec and DeepWalk embeddings algorithms from their original reposiroties

- Graph Encoder Decoder: https://github.com/DaehanKim/vgae_pytorch
