from torch.utils.tensorboard import SummaryWriter
import time

# new log dir so we don't confuse things
writer = SummaryWriter("runs/tb_test")

for step in range(10):
    value = 1.0 / (step + 1)
    writer.add_scalar("test/loss", value, step)
    writer.flush()
    time.sleep(0.1)

writer.close()
print("Wrote 10 scalar points to runs/tb_test")
