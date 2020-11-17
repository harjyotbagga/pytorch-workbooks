import torch

"""
Tensor math and comparison operations
"""

x = torch.tensor([1,2,3])
y = torch.tensor([4,5,6])
print(x)
print(y)

# Addition
z = torch.add(x,y)
z = x + y
print(z)

# Subtraction
z = x - y
print(z)

# Multiplication (element-wise)
z = torch.mul(x,y)
print(z)

# Division (element-wise)
z = torch.div(x, y)
print(z)

# Inplace operations (computationally faster, as a copy isnt created)
t = torch.zeros(3)
t.add_(x)
print(t)
t += x  # t = t + x; is not an inplace operation
print(t)

# Exponential operations
z = x.pow(2)
z = x**2
print(z)

# Comparison operations
z = x > 0
z = x < 0

# Matrix Multiplications
x1 = torch.rand((2,5))
x2 = torch.rand((5,3))
x3 = torch.mm(x1,x2)
x3 = x1.mm(x2)
print(x3)

# Matrix Exponentiation
x = torch.tensor([1.0,2.0,3.0])
x = torch.diag(x)
x = x.matrix_power(3)
print(x)

# Dot product
x = torch.rand(3)
y = torch.rand(3)
z = torch.dot(x,y)
print(z)

# Batch Matrix Multiplication
batch = 32
n = 10
m = 20
p = 30
x = torch.rand(batch,m,n)
y = torch.rand(batch,n,p)
z = torch.bmm(x,y)
print(z)

# Tensor Broadcasting
x1 = torch.rand((5,5))
x2 = torch.rand((5,1))
x3 = torch.mm(x1,x2)
x3 = x1 ** x2

# Useful Mathematical Tensor Operations
x = torch.rand(5)
print(x)
print(torch.sum(x, dim=0))              
values, indices = torch.max(x, dim=0)       # x.max(dim=0)
print(values, indices)
values, indices = torch.min(x, dim=0)   
print(values, indices)
x = torch.abs(x)
print(torch.argmax(x, dim=0))               # x.argmax(dim=0)
z = torch.argmin(x, dim=0)
print(torch.mean(x.float(), dim=0))
y = torch.rand(5)
print(torch.eq(x,y))
z, indices = torch.sort(x, dim=0,descending=False)
print(z, indices)
print(torch.clamp(x, min=0))

k = torch.tensor([1,1,1,0,1], dtype=torch.bool)
print(k)
print(torch.any(k))
print(torch.all(k))

