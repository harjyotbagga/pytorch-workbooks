import torch

"""
Tensor Indexing
"""

batch_size = 10
features = 32
x = torch.rand((batch_size, features))

print(x.shape)
print(x[0,:].shape)
print(x[0,0:9])
print(x[0:5, 0])

x = torch.arange(start=1, end=25, step=2)
print(x)
indices = [2,5,8]
print(x[indices])

# Advance indexing
print(x[(x<10) | (x>20)])
print(x[x.remainder(2)==0])
x = torch.arange(10)
print(x)
print(torch.where(x>5, x*2, x))
print(torch.tensor([0,0,1,2,2,3]).unique())
print(x.ndimension())
print(x.numel())