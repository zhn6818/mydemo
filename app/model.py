import torch
import torchvision.models as models
import time

def train_resnet():
    # Example of ResNet training function (simplified)
    # model = models.resnet18(pretrained=False)
    
    # Dummy training process (replace with actual training logic)
    for epoch in range(10):
        yield f"Epoch {epoch+1}: Training started..."
        time.sleep(2)  # Simulate some training time
        yield f"Epoch {epoch+1}: Training completed"
        time.sleep(1)  # Simulate delay between epochs