import torch
import numpy as np

"""
An introduction to Pytorch Tensors
"""

# Basic Tensor Operations
device = "cuda" if torch.cuda.is_available() else "cpu"
my_tensor = torch.tensor([[1,2,3], [4,5,6]], dtype=torch.float32, device=device, requires_grad=True)
print(my_tensor)
print(my_tensor.dtype)
print(my_tensor.shape)
print(my_tensor.requires_grad)
print(my_tensor.device)

# Types of Tensors
empty_tensor = torch.empty(size=(3,3))
zero_tensor = torch.zeros((3,3))
rand_tensor = torch.rand((3,3))
one_tensor = torch.ones((3,3))
eye_tensor = torch.eye(5,5)
print(eye_tensor)
arranged_tensor = torch.arange(start=0, end=5, step=1)
print(arranged_tensor)
linspace_tensor = torch.linspace(start=0.1, end=1, steps=10)
print(linspace_tensor)
empty_normalized_tensor = torch.empty(size=(1,5)).normal_(mean=0, std=1)
print(empty_normalized_tensor)
empty_uniform_tensor = torch.empty(size=(1,5)).uniform_(0,1)
print(empty_uniform_tensor)
diag_tensor = torch.diag(torch.ones(3))
print(diag_tensor)

# Convert Tensors post initialization
tensor = torch.arange(4)
print(tensor, tensor.dtype)
print(tensor.bool())
print(tensor.short())
print(tensor.long())
print(tensor.float())
print(tensor.double())

# Convert numpy to tensors
np_array = np.zeros((5,5))
tensor = torch.from_numpy(np_array)
np_array = tensor.numpy()
