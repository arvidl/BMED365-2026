"""
Neural network model architectures for medical AI applications.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Tuple, Optional


class ConvBlock(nn.Module):
    """Basic convolutional block with BatchNorm and ReLU."""
    
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int = 3):
        super().__init__()
        self.conv1 = nn.Conv3d(in_channels, out_channels, kernel_size, padding=kernel_size//2)
        self.bn1 = nn.BatchNorm3d(out_channels)
        self.conv2 = nn.Conv3d(out_channels, out_channels, kernel_size, padding=kernel_size//2)
        self.bn2 = nn.BatchNorm3d(out_channels)
        self.relu = nn.ReLU(inplace=True)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.relu(self.bn1(self.conv1(x)))
        x = self.relu(self.bn2(self.conv2(x)))
        return x


class UNet3D(nn.Module):
    """
    Simple 3D U-Net for medical image segmentation.
    
    Based on: Ronneberger et al., "U-Net: Convolutional Networks for 
    Biomedical Image Segmentation", MICCAI 2015.
    
    Args:
        in_channels: Number of input channels (e.g., 4 for T1, T1ce, T2, FLAIR)
        out_channels: Number of output channels (segmentation classes)
        base_features: Base number of features (doubled at each level)
        depth: Number of encoder/decoder levels
    """
    
    def __init__(
        self,
        in_channels: int = 4,
        out_channels: int = 3,
        base_features: int = 32,
        depth: int = 4
    ):
        super().__init__()
        
        self.depth = depth
        features = base_features
        
        # Encoder
        self.encoders = nn.ModuleList()
        self.pools = nn.ModuleList()
        
        in_ch = in_channels
        for i in range(depth):
            self.encoders.append(ConvBlock(in_ch, features))
            self.pools.append(nn.MaxPool3d(2))
            in_ch = features
            features *= 2
        
        # Bottleneck
        self.bottleneck = ConvBlock(in_ch, features)
        
        # Decoder
        self.upconvs = nn.ModuleList()
        self.decoders = nn.ModuleList()
        
        for i in range(depth):
            self.upconvs.append(nn.ConvTranspose3d(features, features // 2, kernel_size=2, stride=2))
            self.decoders.append(ConvBlock(features, features // 2))
            features //= 2
        
        # Final convolution
        self.final_conv = nn.Conv3d(features, out_channels, kernel_size=1)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Encoder path
        encoder_outputs = []
        for encoder, pool in zip(self.encoders, self.pools):
            x = encoder(x)
            encoder_outputs.append(x)
            x = pool(x)
        
        # Bottleneck
        x = self.bottleneck(x)
        
        # Decoder path
        for upconv, decoder, enc_output in zip(
            self.upconvs, self.decoders, reversed(encoder_outputs)
        ):
            x = upconv(x)
            # Handle size mismatch
            if x.shape != enc_output.shape:
                x = F.interpolate(x, size=enc_output.shape[2:], mode='trilinear', align_corners=True)
            x = torch.cat([x, enc_output], dim=1)
            x = decoder(x)
        
        return self.final_conv(x)


class UNet2D(nn.Module):
    """
    Simple 2D U-Net for slice-by-slice segmentation.
    
    Useful for faster training and inference on 2D slices.
    """
    
    def __init__(
        self,
        in_channels: int = 4,
        out_channels: int = 3,
        base_features: int = 64,
        depth: int = 4
    ):
        super().__init__()
        
        self.depth = depth
        features = base_features
        
        # Encoder
        self.encoders = nn.ModuleList()
        self.pools = nn.ModuleList()
        
        in_ch = in_channels
        for i in range(depth):
            self.encoders.append(self._conv_block_2d(in_ch, features))
            self.pools.append(nn.MaxPool2d(2))
            in_ch = features
            features *= 2
        
        # Bottleneck
        self.bottleneck = self._conv_block_2d(in_ch, features)
        
        # Decoder
        self.upconvs = nn.ModuleList()
        self.decoders = nn.ModuleList()
        
        for i in range(depth):
            self.upconvs.append(nn.ConvTranspose2d(features, features // 2, kernel_size=2, stride=2))
            self.decoders.append(self._conv_block_2d(features, features // 2))
            features //= 2
        
        # Final convolution
        self.final_conv = nn.Conv2d(features, out_channels, kernel_size=1)
    
    def _conv_block_2d(self, in_ch: int, out_ch: int) -> nn.Sequential:
        return nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True)
        )
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        encoder_outputs = []
        for encoder, pool in zip(self.encoders, self.pools):
            x = encoder(x)
            encoder_outputs.append(x)
            x = pool(x)
        
        x = self.bottleneck(x)
        
        for upconv, decoder, enc_output in zip(
            self.upconvs, self.decoders, reversed(encoder_outputs)
        ):
            x = upconv(x)
            if x.shape != enc_output.shape:
                x = F.interpolate(x, size=enc_output.shape[2:], mode='bilinear', align_corners=True)
            x = torch.cat([x, enc_output], dim=1)
            x = decoder(x)
        
        return self.final_conv(x)


class MultimodalFusionNet(nn.Module):
    """
    Neural network for multimodal data fusion (imaging + clinical).
    
    Combines imaging features and clinical features through learned
    attention-based fusion.
    """
    
    def __init__(
        self,
        imaging_dim: int = 50,
        clinical_dim: int = 10,
        hidden_dim: int = 128,
        output_dim: int = 2,
        dropout: float = 0.3
    ):
        super().__init__()
        
        # Imaging feature encoder
        self.imaging_encoder = nn.Sequential(
            nn.Linear(imaging_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        # Clinical feature encoder
        self.clinical_encoder = nn.Sequential(
            nn.Linear(clinical_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim // 2, hidden_dim)
        )
        
        # Attention for fusion
        self.attention = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, 2),
            nn.Softmax(dim=1)
        )
        
        # Classifier
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim // 2, output_dim)
        )
    
    def forward(
        self,
        imaging_features: torch.Tensor,
        clinical_features: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Forward pass.
        
        Returns:
            logits: Classification logits
            attention_weights: Attention weights for interpretability
        """
        # Encode modalities
        img_encoded = self.imaging_encoder(imaging_features)
        clin_encoded = self.clinical_encoder(clinical_features)
        
        # Compute attention weights
        combined = torch.cat([img_encoded, clin_encoded], dim=1)
        attention_weights = self.attention(combined)
        
        # Weighted fusion
        fused = (attention_weights[:, 0:1] * img_encoded + 
                 attention_weights[:, 1:2] * clin_encoded)
        
        # Classification
        logits = self.classifier(fused)
        
        return logits, attention_weights


class DiceLoss(nn.Module):
    """
    Dice loss for segmentation tasks.
    
    Based on: Milletari et al., "V-Net: Fully Convolutional Neural Networks
    for Volumetric Medical Image Segmentation", 3DV 2016.
    """
    
    def __init__(self, smooth: float = 1e-5, include_background: bool = False):
        super().__init__()
        self.smooth = smooth
        self.include_background = include_background
    
    def forward(self, pred: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
        """
        Compute Dice loss.
        
        Args:
            pred: Predicted logits (B, C, ...)
            target: Ground truth one-hot or class indices (B, ...)
        
        Returns:
            Dice loss value
        """
        pred = F.softmax(pred, dim=1)
        
        # Convert target to one-hot if needed
        if target.dim() == pred.dim() - 1:
            target = F.one_hot(target.long(), num_classes=pred.shape[1])
            target = target.permute(0, -1, *range(1, target.dim() - 1)).float()
        
        start_channel = 0 if self.include_background else 1
        
        dice_scores = []
        for c in range(start_channel, pred.shape[1]):
            pred_c = pred[:, c].flatten(1)
            target_c = target[:, c].flatten(1)
            
            intersection = (pred_c * target_c).sum(1)
            union = pred_c.sum(1) + target_c.sum(1)
            
            dice = (2 * intersection + self.smooth) / (union + self.smooth)
            dice_scores.append(dice)
        
        if not dice_scores:
            return torch.tensor(0.0, device=pred.device)
        
        mean_dice = torch.stack(dice_scores).mean()
        return 1 - mean_dice


def compute_dice_score(
    pred: torch.Tensor,
    target: torch.Tensor,
    smooth: float = 1e-5
) -> float:
    """
    Compute Dice score for evaluation.
    
    Args:
        pred: Predicted segmentation (B, ...)
        target: Ground truth segmentation (B, ...)
        smooth: Smoothing factor
    
    Returns:
        Mean Dice score
    """
    pred = pred.flatten()
    target = target.flatten()
    
    intersection = (pred == target).float().sum()
    dice = (2 * intersection + smooth) / (pred.numel() + target.numel() + smooth)
    
    return dice.item()
