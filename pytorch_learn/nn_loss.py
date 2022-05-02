import torch
from torch.nn import L1Loss
from torch import nn

inputs = torch.tensor([1, 2, 3], dtype=torch.float32)
targets = torch.tensor([1, 2, 5], dtype=torch.float32)

inputs = torch.reshape(inputs, (1, 1, 1, 3))
targets = torch.reshape(targets, (1, 1, 1, 3))

loss = L1Loss(reduction="sum")
result = loss(inputs, targets)
print(result)

loss_mse = nn.MSELoss()
result2 = loss_mse(inputs, targets)
print(result2)


# 交叉熵
x = torch.tensor([0.1, 0.2, 0.3])
print(x.shape)
y = torch.tensor([1])
x = torch.reshape(x, (1, 3))
print(x.shape)
loss_cross = nn.CrossEntropyLoss()
result3 = loss_cross(x, y)
print(result3)
