"""
Visualization utilities for medical AI applications.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Optional, List, Tuple, Dict
from pathlib import Path


def plot_mri_slice(
    volume: np.ndarray,
    slice_idx: Optional[int] = None,
    axis: int = 2,
    title: str = "",
    cmap: str = "gray",
    figsize: Tuple[int, int] = (6, 6),
    ax: Optional[plt.Axes] = None,
    radiological: bool = True
) -> plt.Axes:
    """
    Plot a single slice from a 3D MRI volume in radiological orientation.
    
    Args:
        volume: 3D numpy array (assumed RAS orientation)
        slice_idx: Slice index (default: middle slice)
        axis: Axis for slicing (0=sagittal, 1=coronal, 2=axial)
        title: Plot title
        cmap: Colormap
        figsize: Figure size
        ax: Existing axes to plot on
        radiological: If True, display in radiological convention (R on left)
    
    Returns:
        matplotlib Axes object
    """
    if slice_idx is None:
        slice_idx = volume.shape[axis] // 2
    
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    
    # Extract slice based on axis
    # For data with shape (D, H, W) after Decathlon loading:
    # axis=0: Axial slices (most common clinical view)
    # axis=1: Coronal slices
    # axis=2: Sagittal slices
    if axis == 0:  # Axial (slicing along D dimension)
        img = volume[slice_idx, :, :]
    elif axis == 1:  # Coronal
        img = volume[:, slice_idx, :]
    else:  # Sagittal
        img = volume[:, :, slice_idx]
    
    # Apply radiological convention transformations for axial view
    # Transpose to correct orientation, then flip for R on left, A on top
    if radiological:
        # Rotate 90 degrees counter-clockwise and flip for radiological convention
        img = np.rot90(img, k=1)  # Rotate 90° CCW
        img = np.fliplr(img)      # R on left
        ax.imshow(img, cmap=cmap, origin='upper')
    else:
        ax.imshow(img, cmap=cmap, origin='lower')
    ax.set_title(title)
    ax.axis('off')
    
    return ax


def plot_mri_modalities(
    data: Dict[str, np.ndarray],
    slice_idx: Optional[int] = None,
    axis: int = 2,
    figsize: Tuple[int, int] = (16, 4),
    save_path: Optional[Path] = None
) -> plt.Figure:
    """
    Plot all MRI modalities side by side.
    
    Args:
        data: Dictionary with modality names as keys and 3D volumes as values
        slice_idx: Slice index
        axis: Slicing axis
        figsize: Figure size
        save_path: Optional path to save figure
    
    Returns:
        matplotlib Figure object
    """
    modalities = [k for k in ['t1', 't1ce', 't2', 'flair'] if k in data]
    n_mods = len(modalities)
    
    fig, axes = plt.subplots(1, n_mods, figsize=figsize)
    if n_mods == 1:
        axes = [axes]
    
    for ax, mod in zip(axes, modalities):
        volume = data[mod]
        if slice_idx is None:
            idx = volume.shape[axis] // 2
        else:
            idx = slice_idx
        
        plot_mri_slice(volume, idx, axis, title=mod.upper(), ax=ax)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    
    return fig


def plot_segmentation_overlay(
    image: np.ndarray,
    segmentation: np.ndarray,
    slice_idx: Optional[int] = None,
    axis: int = 2,
    alpha: float = 0.5,
    title: str = "",
    figsize: Tuple[int, int] = (12, 4),
    save_path: Optional[Path] = None,
    radiological: bool = True
) -> plt.Figure:
    """
    Plot MRI with segmentation overlay in radiological orientation.
    
    Args:
        image: 3D MRI volume (assumed RAS orientation)
        segmentation: 3D segmentation mask
        slice_idx: Slice index
        axis: Slicing axis (0=sagittal, 1=coronal, 2=axial)
        alpha: Overlay transparency
        title: Plot title
        figsize: Figure size
        save_path: Optional path to save figure
        radiological: If True, display in radiological convention
    
    Returns:
        matplotlib Figure object
    """
    if slice_idx is None:
        slice_idx = image.shape[axis] // 2
    
    # Extract slices
    # For data with shape (D, H, W) after Decathlon loading:
    # axis=0: Axial slices (most common clinical view)
    # axis=1: Coronal slices
    # axis=2: Sagittal slices
    if axis == 0:  # Axial
        img_slice = image[slice_idx, :, :]
        seg_slice = segmentation[slice_idx, :, :]
    elif axis == 1:  # Coronal
        img_slice = image[:, slice_idx, :]
        seg_slice = segmentation[:, slice_idx, :]
    else:  # Sagittal
        img_slice = image[:, :, slice_idx]
        seg_slice = segmentation[:, :, slice_idx]
    
    # Apply radiological orientation (R on left, A on top)
    if radiological:
        # Rotate 90° CCW and flip for radiological convention
        img_slice = np.fliplr(np.rot90(img_slice, k=1))
        seg_slice = np.fliplr(np.rot90(seg_slice, k=1))
        img_origin = 'upper'
    else:
        img_origin = 'lower'
    
    fig, axes = plt.subplots(1, 3, figsize=figsize)
    
    # Original image
    axes[0].imshow(img_slice, cmap='gray', origin=img_origin)
    axes[0].set_title('MRI')
    axes[0].axis('off')
    
    # Segmentation
    axes[1].imshow(seg_slice, cmap='tab10', origin=img_origin, vmin=0, vmax=3)
    axes[1].set_title('Segmentation')
    axes[1].axis('off')
    
    # Overlay
    axes[2].imshow(img_slice, cmap='gray', origin=img_origin)
    masked_seg = np.ma.masked_where(seg_slice == 0, seg_slice)
    axes[2].imshow(masked_seg, cmap='hot', alpha=alpha, origin=img_origin)
    axes[2].set_title('Overlay')
    axes[2].axis('off')
    
    plt.suptitle(title)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    
    return fig


def plot_training_history(
    history: Dict[str, List[float]],
    figsize: Tuple[int, int] = (12, 4),
    save_path: Optional[Path] = None
) -> plt.Figure:
    """
    Plot training history curves.
    
    Args:
        history: Dictionary with 'train_loss', 'val_loss', 'train_dice', 'val_dice'
        figsize: Figure size
        save_path: Optional path to save figure
    
    Returns:
        matplotlib Figure object
    """
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    
    # Loss
    if 'train_loss' in history:
        axes[0].plot(history['train_loss'], label='Train Loss')
    if 'val_loss' in history:
        axes[0].plot(history['val_loss'], label='Val Loss')
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('Loss')
    axes[0].set_title('Training and Validation Loss')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Dice score
    if 'train_dice' in history:
        axes[1].plot(history['train_dice'], label='Train Dice')
    if 'val_dice' in history:
        axes[1].plot(history['val_dice'], label='Val Dice')
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('Dice Score')
    axes[1].set_title('Dice Score')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    
    return fig


def plot_patient_similarity_network(
    similarity_matrix: np.ndarray,
    labels: np.ndarray,
    threshold: float = 0.5,
    figsize: Tuple[int, int] = (10, 10),
    max_nodes: int = 100,
    save_path: Optional[Path] = None
) -> plt.Figure:
    """
    Plot patient similarity network.
    
    Args:
        similarity_matrix: N x N similarity matrix
        labels: Patient labels for coloring
        threshold: Similarity threshold for edges
        figsize: Figure size
        max_nodes: Maximum nodes to display
        save_path: Optional path to save figure
    
    Returns:
        matplotlib Figure object
    """
    try:
        import networkx as nx
    except ImportError:
        print("NetworkX not installed. Showing heatmap instead.")
        fig, ax = plt.subplots(figsize=figsize)
        im = ax.imshow(similarity_matrix[:max_nodes, :max_nodes], cmap='viridis')
        plt.colorbar(im, ax=ax, label='Similarity')
        ax.set_title('Patient Similarity Matrix')
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
        return fig
    
    n = min(len(similarity_matrix), max_nodes)
    sim = similarity_matrix[:n, :n]
    lab = labels[:n]
    
    # Create graph
    G = nx.Graph()
    for i in range(n):
        G.add_node(i, label=lab[i])
    
    for i in range(n):
        for j in range(i+1, n):
            if sim[i, j] > threshold:
                G.add_edge(i, j, weight=sim[i, j])
    
    fig, ax = plt.subplots(figsize=figsize)
    
    pos = nx.spring_layout(G, k=1/np.sqrt(n), iterations=50)
    colors = ['#1f77b4' if lab[i] == 0 else '#ff7f0e' for i in range(n)]
    
    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=50, alpha=0.7, ax=ax)
    nx.draw_networkx_edges(G, pos, alpha=0.2, ax=ax)
    
    ax.set_title(f'Patient Similarity Network (n={n}, threshold={threshold})')
    ax.axis('off')
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    
    return fig


def plot_confusion_matrix(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    class_names: Optional[List[str]] = None,
    figsize: Tuple[int, int] = (8, 6),
    save_path: Optional[Path] = None
) -> plt.Figure:
    """
    Plot confusion matrix.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
        class_names: Optional class names
        figsize: Figure size
        save_path: Optional path to save figure
    
    Returns:
        matplotlib Figure object
    """
    from sklearn.metrics import confusion_matrix
    
    cm = confusion_matrix(y_true, y_pred)
    
    fig, ax = plt.subplots(figsize=figsize)
    im = ax.imshow(cm, cmap='Blues')
    
    n_classes = cm.shape[0]
    if class_names is None:
        class_names = [str(i) for i in range(n_classes)]
    
    ax.set_xticks(range(n_classes))
    ax.set_yticks(range(n_classes))
    ax.set_xticklabels(class_names)
    ax.set_yticklabels(class_names)
    
    # Add text annotations
    for i in range(n_classes):
        for j in range(n_classes):
            text = ax.text(j, i, cm[i, j], ha="center", va="center",
                          color="white" if cm[i, j] > cm.max()/2 else "black")
    
    ax.set_xlabel('Predicted')
    ax.set_ylabel('True')
    ax.set_title('Confusion Matrix')
    
    plt.colorbar(im, ax=ax)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    
    return fig
