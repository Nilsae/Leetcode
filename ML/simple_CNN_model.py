import torch.nn as nn
class Simple_CNN(nn.Module):
    def __init__(self):
        super(Simple_CNN, self).__init__()
        self.conv_2d_1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.relu_1 = nn.ReLU()
        self.maxpool_1 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv_2d_2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.relu_2 = nn.ReLU()
        self.maxpool_2 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.flatten = nn.Flatten()
        self.linear_1 = nn.Linear(in_features=32*7*7, out_features=128)
        self.relu_3 = nn.ReLU()
        self.linear_2 = nn.Linear(in_features=128, out_features=10)
        # self.softmax = nn.Softmax(dim=1) 
    def forward(self, x):
        x = self.conv_2d_1(x) # shape = (N, 1, 28, 28) 
        x = self.relu_1(x)
        x = self.maxpool_1(x) # shape = (N, 16, 14, 14) 
        x = self.conv_2d_2(x) 
        x = self.relu_2(x)
        x = self.maxpool_2(x) # shape = (N, 32, 7, 7) (sample size, channels, height, width)
        x = self.flatten(x) # shape = (N, 32*7*7)
        x = self.linear_1(x)
        x = self.relu_3(x)
        x = self.linear_2(x)
        # x = self.softmax(x)
        return x