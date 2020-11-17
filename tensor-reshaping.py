import torch

"""
Tensor Reshaping
"""

x = torch.arange(9)
print(x.view(3,3))
x3 = x.reshape(3,3)
print(x3)
print(x3.t())
batch = 32
x = torch.rand(batch, 5, 2)
x = x.permute(0,2,1)            # Transpose is a special case of permute
print(x)

x1 = torch.rand((2,2))
x2 = torch.rand((2,2))
print(torch.cat((x1,x2), dim=0).shape)
print(torch.cat((x1,x2), dim=1).shape)

print(x1.view(-1))
batch = 32
x = torch.rand(batch, 5, 2)
print(x.view(batch, -1).shape)


x = torch.arange(10)
print(x.shape)
print(x.unsqueeze(0))
print(x.unsqueeze(1))