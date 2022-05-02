import torch
import torchvision
from torch import nn
from torch.nn import Linear
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10(
    "./dataset2",
    transform=torchvision.transforms.ToTensor(),
    train=False,
    download=True
)

dataloader = DataLoader(
    dataset,
    batch_size=64
)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.linear1 = Linear(196608, 10)

    def forward(self, input):
        output = self.linear1(input)
        return output


net = Net()

for data in dataloader:
    imgs, targets = data
    print(imgs.shape)
    # output = torch.reshape(imgs, (1, 1, 1, -1))
    output=torch.flatten(imgs)
    print(output.shape)
    output = net(output)
    print(output.shape)
