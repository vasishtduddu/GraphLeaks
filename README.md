# Quantifying Privacy Leakage in Graph Embedding (MobiQuitous'20 and NeurIPS PPML '20)

Preprint: https://arxiv.org/pdf/2010.00906.pdf

The code is as follows:

1) AIA: Attribute inference attacks. The embeddings are already generated using code form their original repos.

2) MIA: Membership Inference attacks. The code is divided into blackbox (includes confidence score attacks and shadow model attack) and whitebox. MIA in blackbox setting is performed on inductive training of GraphSage model. 

3) Reconstruction: Graph Reconstruction using graph encoder decoder.

Data: The facebook and LastFM dataset for attribute inference attacks is available from Stanford Large Network Datasete Collection. The data for graph reconstruction requires to load the train and test graphs seperately unlike what most libraries provider. The data can be obtained from https://github.com/DaehanKim/vgae_pytorch.


### Credits:

- Node2Vec and DeepWalk embeddings algorithms from their original repositories (https://github.com/phanein/deepwalk) (https://github.com/aditya-grover/node2vec)

- Graph Encoder Decoder: https://github.com/DaehanKim/vgae_pytorch

- BlackBox MIA: https://github.com/inspire-group/privacy-vs-robustness


### Citation

@inproceedings{duddu2020graphleaks,
author = {Duddu, Vasisht and Boutet, Antoine and Shejwalkar, Virat},
title = {Quantifying Privacy Leakage in Graph Embedding},
year = {2020},
isbn = {9781450388405},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3448891.3448939},
doi = {10.1145/3448891.3448939},
booktitle = {MobiQuitous 2020 - 17th EAI International Conference on Mobile and Ubiquitous Systems: Computing, Networking and Services},
pages = {76–85},
numpages = {10},
keywords = {Graph Embeddings., Inference Attacks, Privacy Leakage, Graph Neural Networks},
location = {Darmstadt, Germany},
series = {MobiQuitous '20}
}

  

