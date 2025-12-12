print(">>> HELLO FROM simple_CNN_for_MNIST.py <<<", flush=True)
from simple_CNN_model import Simple_CNN
import os
import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision import datasets, models, transforms
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import Subset
def evaluate(model, loader, device, criterion):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in loader:
            images = images.to(device, non_blocking=True)
            labels = labels.to(device, non_blocking=True)

            logits = model(images)
            loss = criterion(logits, labels)

            running_loss += loss.item() * images.size(0)   # sum over batch
            _, preds = torch.max(logits, dim=1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)

    avg_loss = running_loss / total
    accuracy = correct / total
    return avg_loss, accuracy

# for resnet only, because it expects 3-channel 224x224 images like ImageNet
# train_transform = transforms.Compose([
#     transforms.Resize(224),
#     transforms.Grayscale(num_output_channels=3),
#     transforms.ToTensor(),
#     transforms.Normalize(
#         mean=[0.485, 0.456, 0.406],
#         std=[0.229, 0.224, 0.225],
#     ),
# ])

# for simple_CNN model
train_transform = transforms.Compose([
    transforms.ToTensor(),                     # -> (1, 28, 28)
    # transforms.Normalize((0.1307,), (0.3081,)) # standard MNIST normalization (optional but nice)
])

# log_dir = "runs/mnist_resnet_v7"   
log_dir = "runs/simple_CNN_mnist_v1"   
writer = SummaryWriter(log_dir=log_dir)

ckpt_dir = "simple_CNN_mnist_v1/checkpoints"

os.makedirs(ckpt_dir, exist_ok=True)
# print(">>> TensorBoard log dir:", os.path.abspath(log_dir), flush=True)
# print(">>> Checkpoint dir:", os.path.abspath(ckpt_dir), flush=True)


mnist_train_full = datasets.MNIST(
    root="./data",
    train=True,
    download=False,           
    transform=train_transform,
)
mnist_test_full = datasets.MNIST(
    root="./data",
    train=False,
    download=False,
    transform=train_transform,
)

subset_size = 1000  # try 1k, 2k, 5k etc.
indices = list(range(subset_size))  # first 2000 samples

# mnist_train = Subset(mnist_train_full, indices)
mnist_test = Subset(mnist_test_full, indices)
train_loader = DataLoader(
    mnist_train_full,
    batch_size=32,
    shuffle=True,
    num_workers=4,
    pin_memory=True,
)
val_loader = DataLoader(
    mnist_test,
    batch_size=64,
    shuffle=False,
    num_workers=4,
    pin_memory=True,
)

# model = models.resnet50(weights=None)
model = Simple_CNN()
# only for resnet:
# num_features = model.fc.in_features
# model.fc = nn.Linear(num_features, 10)  # MNIST has 10 classes

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-4)


num_epochs = 10          
global_step = 0
print(">>> Train dataset size:", len(mnist_train_full), flush=True)
print(">>> Steps per epoch:", len(train_loader), flush=True)
# model.train()
print(">>> ABOUT TO START TRAINING LOOP", flush=True)
# not applicable for simple CNN:
# model.train(): use during training -> Dropout ON, BatchNorm uses batch stats & updates running stats
# model.eval(): use during eval/inference -> Dropout OFF, BatchNorm uses stored running stats (no updates)

for epoch in range(num_epochs):
    model.train()
    print(f">>> Starting epoch {epoch+1}/{num_epochs}", flush=True)
    running_loss = 0.0

    for images, labels in train_loader:
        images = images.to(device, non_blocking=True)
        labels = labels.to(device, non_blocking=True)

        optimizer.zero_grad()
        logits = model(images)
        loss = criterion(logits, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        global_step += 1

        writer.add_scalar("train/loss_batch", loss.item(), global_step)
        writer.flush()
    avg_loss = running_loss / len(train_loader)
    train_loss_epoch, train_acc = evaluate(model, train_loader, device, criterion)
    val_loss, val_acc = evaluate(model, val_loader, device, criterion)
    writer.add_scalar("train/loss_epoch", avg_loss, epoch + 1)
    writer.add_scalar("train/accuracy",   train_acc,        epoch + 1)
    writer.add_scalar("val/loss",         val_loss,         epoch + 1)
    writer.add_scalar("val/accuracy",     val_acc,          epoch + 1)
    writer.flush()
    ckpt_path = os.path.join(ckpt_dir, f"epoch_{epoch+1}.pt")
    print(f">>> Saving checkpoint for epoch {epoch+1}", flush=True)
    torch.save(
        {
            "epoch": epoch + 1,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "avg_loss": avg_loss,
            "val_loss": val_loss,
            "val_acc": val_acc,
        },
        ckpt_path,
    )
    print(f"Saved checkpoint: {ckpt_path}")

writer.close()
print("Training done, TensorBoard data written to", log_dir)
