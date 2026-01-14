"""
Data loading and preprocessing utilities for medical AI applications.
"""

import os
import numpy as np
from typing import Tuple, List, Optional, Dict, Any
from pathlib import Path

# Check if running in Colab
def is_colab() -> bool:
    """Check if code is running in Google Colab."""
    try:
        import google.colab
        return True
    except ImportError:
        return False


def get_device(force_cpu_for_3d=False):
    """
    Get the best available device (CUDA, MPS, or CPU).
    
    Args:
        force_cpu_for_3d: If True, returns CPU even if MPS is available.
                          Useful for 3D operations not yet supported on MPS.
    
    Returns:
        torch.device
    """
    import torch
    import os
    
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print(f"Using CUDA: {torch.cuda.get_device_name(0)}")
    elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
        if force_cpu_for_3d:
            device = torch.device("cpu")
            print("Using CPU (MPS available but 3D ops not fully supported)")
        else:
            # Enable MPS fallback for unsupported operations
            os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
            device = torch.device("mps")
            print("Using Apple Silicon MPS (with CPU fallback for unsupported ops)")
    else:
        device = torch.device("cpu")
        print("Using CPU")
    
    return device


def download_sample_data(data_dir: str = "data", dataset: str = "brats_sample") -> Path:
    """
    Download sample datasets for the notebooks.
    
    Args:
        data_dir: Directory to store data
        dataset: Which dataset to download:
            - 'brats_sample': Synthetic data for quick demos
            - 'decathlon': Real brain tumor MRI from Medical Segmentation Decathlon
            - 'synthetic': Empty synthetic data directory
    
    Returns:
        Path to the downloaded data
    """
    data_path = Path(data_dir)
    data_path.mkdir(parents=True, exist_ok=True)
    
    if dataset == "brats_sample":
        # For quick demos, use synthetic data
        sample_path = data_path / "brats_sample"
        if not sample_path.exists():
            print("Generating synthetic brain MRI-like data for demo...")
            print("For real data, use dataset='decathlon' or follow BraTS download instructions.")
            sample_path.mkdir(parents=True, exist_ok=True)
            _generate_synthetic_mri(sample_path, n_samples=5)
        return sample_path
    
    elif dataset == "decathlon":
        # Real brain tumor data from Medical Segmentation Decathlon
        return download_decathlon_brain_tumor(data_path)
    
    elif dataset == "synthetic":
        synthetic_path = data_path / "synthetic"
        synthetic_path.mkdir(parents=True, exist_ok=True)
        return synthetic_path
    
    else:
        raise ValueError(f"Unknown dataset: {dataset}")


def download_decathlon_brain_tumor(data_dir: Path, max_samples: int = None) -> Path:
    """
    Download real brain tumor MRI data from Medical Segmentation Decathlon.
    
    This dataset contains multiparametric MRI (FLAIR, T1w, T1gd, T2w) with
    expert segmentations of gliomas.
    
    Args:
        data_dir: Base directory for data storage
        max_samples: Limit number of samples (None = all ~484 training cases)
    
    Returns:
        Path to the dataset directory
    
    Note:
        - Download size: ~7.5 GB
        - Extracted size: ~16 GB
        - First run will take several minutes
    """
    decathlon_path = data_dir / "decathlon_brain"
    
    if (decathlon_path / "Task01_BrainTumour").exists():
        print(f"Decathlon brain tumor data already exists at {decathlon_path}")
        return decathlon_path / "Task01_BrainTumour"
    
    print("=" * 60)
    print("DOWNLOADING MEDICAL SEGMENTATION DECATHLON - BRAIN TUMOR")
    print("=" * 60)
    print("Dataset: Task01_BrainTumour")
    print("Size: ~7.5 GB download, ~16 GB extracted")
    print("Source: http://medicaldecathlon.com/")
    print("=" * 60)
    
    try:
        from monai.apps import DecathlonDataset
        
        decathlon_path.mkdir(parents=True, exist_ok=True)
        
        # This will download and extract the dataset
        print("\nDownloading (this may take 10-30 minutes)...")
        _ = DecathlonDataset(
            root_dir=str(decathlon_path),
            task="Task01_BrainTumour",
            section="training",
            download=True,
            cache_rate=0.0,  # Don't cache to save memory
        )
        
        print("\n✓ Download complete!")
        print(f"Data location: {decathlon_path / 'Task01_BrainTumour'}")
        
        return decathlon_path / "Task01_BrainTumour"
        
    except ImportError:
        print("\nMONAI not installed. Install with: pip install monai")
        print("Or download manually from: http://medicaldecathlon.com/")
        raise
    except Exception as e:
        print(f"\nDownload failed: {e}")
        print("\nManual download instructions:")
        print("1. Go to http://medicaldecathlon.com/")
        print("2. Download Task01_BrainTumour.tar")
        print(f"3. Extract to: {decathlon_path}/")
        raise


def download_brats_subset_github(data_dir: Path) -> Path:
    """
    Download the 50-sample BRATS subset from GitHub Releases.
    
    This provides the same 50 cases (BRATS_001-BRATS_050) as the full
    Decathlon dataset but downloads only ~1.5 GB instead of ~7.5 GB.
    
    The subset is hosted as a GitHub Release asset for reliable access
    from Google Colab and other environments.
    
    The directory structure matches Decathlon format for compatibility:
        brats_subset/Task01_BrainTumour/
            imagesTr/BRATS_001.nii.gz, ..., BRATS_050.nii.gz
            labelsTr/BRATS_001.nii.gz, ..., BRATS_050.nii.gz
    
    Args:
        data_dir: Base directory for data storage (e.g., Path("data"))
        
    Returns:
        Path to the subset directory (contains imagesTr/ and labelsTr/)
        
    Note:
        - Download size: ~1.5 GB
        - Cases: BRATS_001 through BRATS_050 (50 total)
        - Identical to first 50 cases from full Decathlon dataset
    """
    import urllib.request
    import zipfile
    
    # Convert to Path if string
    data_dir = Path(data_dir)
    
    # The subset mimics Decathlon structure for compatibility
    subset_path = data_dir / "brats_subset" / "Task01_BrainTumour"
    
    if (subset_path / "imagesTr").exists():
        n_files = len([f for f in (subset_path / "imagesTr").glob("BRATS_*.nii.gz") 
                       if not f.name.startswith("._")])
        print(f"BRATS subset already exists at {subset_path} ({n_files} cases)")
        return subset_path
    
    # GitHub Release URL
    # The release is hosted on the public BMED365-2026 repo for universal access
    RELEASE_TAG = "v1.0-data"
    REPO = "arvidl/BMED365-2026"
    FILENAME = "brats_subset_50.zip"
    release_url = f"https://github.com/{REPO}/releases/download/{RELEASE_TAG}/{FILENAME}"
    
    print("=" * 60)
    print("DOWNLOADING BRATS SUBSET FROM GITHUB")
    print("=" * 60)
    print(f"Cases: BRATS_001 to BRATS_050 (50 cases)")
    print(f"Size: ~1.5 GB (vs 7.5 GB for full Decathlon)")
    print(f"Source: GitHub Release ({RELEASE_TAG})")
    print("=" * 60)
    
    data_dir.mkdir(parents=True, exist_ok=True)
    zip_path = data_dir / "brats_subset_50.zip"
    
    # Download with progress indicator
    print("\nDownloading (this may take 2-5 minutes)...")
    
    def download_progress(block_num, block_size, total_size):
        downloaded = block_num * block_size
        if total_size > 0:
            percent = min(100, downloaded * 100 / total_size)
            mb_downloaded = downloaded / (1024 * 1024)
            mb_total = total_size / (1024 * 1024)
            print(f"\r  {percent:.1f}% ({mb_downloaded:.1f}/{mb_total:.1f} MB)", end="", flush=True)
    
    try:
        urllib.request.urlretrieve(release_url, zip_path, download_progress)
        print()  # New line after progress
    except Exception as e:
        print(f"\n\nDownload failed: {e}")
        print("\nPossible solutions:")
        print("1. Check your internet connection")
        print("2. The GitHub Release may not exist yet - use DATA_SOURCE='decathlon_full'")
        print(f"3. Try downloading manually from: {release_url}")
        print(f"   Extract to: {data_dir}/brats_subset/")
        raise
    
    # Extract
    print("Extracting...")
    subset_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zf:
        zf.extractall(subset_path.parent)
    
    # Clean up zip file
    zip_path.unlink()
    
    # Verify extraction
    images_dir = subset_path / "imagesTr"
    labels_dir = subset_path / "labelsTr"
    
    if images_dir.exists() and labels_dir.exists():
        n_images = len([f for f in images_dir.glob("*.nii.gz") if not f.name.startswith("._")])
        n_labels = len([f for f in labels_dir.glob("*.nii.gz") if not f.name.startswith("._")])
        
        print(f"\n✓ Download complete!")
        print(f"  Images: {n_images} files")
        print(f"  Labels: {n_labels} files")
        print(f"  Location: {subset_path}")
    else:
        print(f"\n⚠ Warning: Expected directory structure not found")
        print(f"  Looking for: {subset_path}/imagesTr/ and labelsTr/")
    
    return subset_path


def load_decathlon_sample(sample_path: Path) -> Dict[str, np.ndarray]:
    """
    Load a sample from the Medical Segmentation Decathlon brain tumor dataset.
    
    The dataset provides 4-channel images (FLAIR, T1w, T1gd, T2w) in a single file.
    
    Args:
        sample_path: Path to the image NIfTI file
        
    Returns:
        Dictionary with 'image' (4, D, H, W), 'seg' (D, H, W), and modality keys
    """
    try:
        import nibabel as nib
    except ImportError:
        raise ImportError("nibabel required: pip install nibabel")
    
    # Load 4D image (4 modalities stacked)
    img = nib.load(sample_path)
    image_data = img.get_fdata()
    
    # Load segmentation (same name but in labelsTr folder)
    seg_path = str(sample_path).replace("imagesTr", "labelsTr")
    if Path(seg_path).exists():
        seg = nib.load(seg_path)
        seg_data = seg.get_fdata().astype(np.uint8)
        
        # BraTS/Decathlon uses non-consecutive labels: 0, 1, 2, 4
        # Remap to consecutive: 0->0, 1->1, 2->2, 4->3
        # Label meanings: 0=background, 1=necrotic/non-enhancing, 2=edema, 4->3=enhancing
        seg_data = np.where(seg_data == 4, 3, seg_data)
    else:
        seg_data = np.zeros(image_data.shape[:3], dtype=np.uint8)
    
    # Decathlon brain tumor has 4 channels: FLAIR, T1w, T1gd (T1ce), T2w
    # Transpose from (H, W, D, C) to (C, D, H, W) for PyTorch
    if image_data.ndim == 4:
        image_data = np.transpose(image_data, (3, 2, 0, 1))
        seg_data = np.transpose(seg_data, (2, 0, 1))
        
        return {
            'image': image_data.astype(np.float32),  # (4, D, H, W)
            'flair': image_data[0],
            't1': image_data[1],
            't1ce': image_data[2],  # T1 with gadolinium
            't2': image_data[3],
            'seg': seg_data,
        }
    else:
        raise ValueError(f"Unexpected image shape: {image_data.shape}")


def get_decathlon_file_list(data_dir: Path, max_samples: int = None) -> List[Path]:
    """
    Get list of sample paths from Decathlon dataset.
    
    Args:
        data_dir: Path to Task01_BrainTumour directory
        max_samples: Limit number of samples
        
    Returns:
        List of paths to image files
    """
    images_dir = data_dir / "imagesTr"
    if not images_dir.exists():
        raise FileNotFoundError(f"Images directory not found: {images_dir}")
    
    # Get all NIfTI files, excluding macOS metadata files (._*)
    samples = sorted([
        f for f in images_dir.glob("*.nii.gz") 
        if not f.name.startswith("._")
    ])
    
    if max_samples:
        samples = samples[:max_samples]
    
    print(f"Found {len(samples)} samples in {images_dir}")
    return samples


def _generate_synthetic_mri(output_dir: Path, n_samples: int = 5):
    """Generate synthetic brain MRI-like data for demonstration."""
    import numpy as np
    
    for i in range(n_samples):
        sample_dir = output_dir / f"sample_{i:03d}"
        sample_dir.mkdir(exist_ok=True)
        
        # Generate 3D volumes (simplified 64x64x64)
        shape = (64, 64, 64)
        
        # Create synthetic modalities with different intensity distributions
        t1 = _create_synthetic_brain(shape, modality='t1')
        t1ce = _create_synthetic_brain(shape, modality='t1ce')
        t2 = _create_synthetic_brain(shape, modality='t2')
        flair = _create_synthetic_brain(shape, modality='flair')
        seg = _create_synthetic_segmentation(shape)
        
        # Save as numpy arrays (in practice, would be NIfTI)
        np.save(sample_dir / "t1.npy", t1)
        np.save(sample_dir / "t1ce.npy", t1ce)
        np.save(sample_dir / "t2.npy", t2)
        np.save(sample_dir / "flair.npy", flair)
        np.save(sample_dir / "seg.npy", seg)
    
    print(f"Generated {n_samples} synthetic MRI samples in {output_dir}")


def _create_synthetic_brain(shape: Tuple[int, int, int], modality: str = 't1') -> np.ndarray:
    """Create a synthetic brain-like 3D volume."""
    # Create ellipsoid brain shape
    z, y, x = np.ogrid[:shape[0], :shape[1], :shape[2]]
    center = np.array(shape) / 2
    
    # Brain ellipsoid
    brain_mask = ((z - center[0])**2 / (center[0]*0.8)**2 +
                  (y - center[1])**2 / (center[1]*0.9)**2 +
                  (x - center[2])**2 / (center[2]*0.85)**2) < 1
    
    # Base intensity based on modality
    base_intensities = {'t1': 0.6, 't1ce': 0.65, 't2': 0.5, 'flair': 0.55}
    base = base_intensities.get(modality, 0.5)
    
    volume = np.zeros(shape, dtype=np.float32)
    volume[brain_mask] = base + np.random.normal(0, 0.1, brain_mask.sum())
    volume = np.clip(volume, 0, 1)
    
    return volume


def _create_synthetic_segmentation(shape: Tuple[int, int, int]) -> np.ndarray:
    """Create a synthetic tumor segmentation mask."""
    seg = np.zeros(shape, dtype=np.uint8)
    
    # Random tumor location within brain
    center = np.array(shape) / 2
    tumor_center = center + np.random.randint(-10, 10, 3)
    tumor_radius = np.random.randint(5, 12)
    
    z, y, x = np.ogrid[:shape[0], :shape[1], :shape[2]]
    tumor_mask = ((z - tumor_center[0])**2 +
                  (y - tumor_center[1])**2 +
                  (x - tumor_center[2])**2) < tumor_radius**2
    
    seg[tumor_mask] = 1  # Tumor class
    
    return seg


def load_mri_sample(sample_dir: Path) -> Dict[str, np.ndarray]:
    """Load a single MRI sample with all modalities."""
    modalities = ['t1', 't1ce', 't2', 'flair', 'seg']
    data = {}
    
    for mod in modalities:
        filepath = sample_dir / f"{mod}.npy"
        if filepath.exists():
            data[mod] = np.load(filepath)
    
    return data


def normalize_volume(volume: np.ndarray, method: str = 'zscore') -> np.ndarray:
    """
    Normalize a 3D volume.
    
    Args:
        volume: Input volume
        method: 'zscore' or 'minmax'
    
    Returns:
        Normalized volume
    """
    if method == 'zscore':
        mask = volume > 0
        mean = volume[mask].mean()
        std = volume[mask].std()
        normalized = np.where(mask, (volume - mean) / (std + 1e-8), 0)
    elif method == 'minmax':
        vmin, vmax = volume.min(), volume.max()
        normalized = (volume - vmin) / (vmax - vmin + 1e-8)
    else:
        raise ValueError(f"Unknown normalization method: {method}")
    
    return normalized.astype(np.float32)


def create_multimodal_dataset(
    n_patients: int = 500,
    n_imaging_features: int = 50,
    n_clinical_features: int = 10,
    random_state: int = 42
) -> Dict[str, np.ndarray]:
    """
    Create a synthetic multimodal dataset combining imaging and clinical features.
    
    Args:
        n_patients: Number of patients
        n_imaging_features: Number of imaging-derived features
        n_clinical_features: Number of clinical features
        random_state: Random seed for reproducibility
    
    Returns:
        Dictionary with 'imaging', 'clinical', 'labels', 'patient_ids'
    """
    np.random.seed(random_state)
    
    # Generate imaging features (e.g., radiomics)
    imaging_features = np.random.randn(n_patients, n_imaging_features).astype(np.float32)
    
    # Generate clinical features
    clinical_features = np.zeros((n_patients, n_clinical_features), dtype=np.float32)
    clinical_features[:, 0] = np.random.randint(20, 80, n_patients)  # Age
    clinical_features[:, 1] = np.random.randint(0, 2, n_patients)    # Sex
    clinical_features[:, 2:] = np.random.randn(n_patients, n_clinical_features - 2)
    
    # Generate labels based on features (survival: 0=poor, 1=good)
    # Create some correlation with features
    risk_score = (0.3 * imaging_features[:, :5].mean(axis=1) + 
                  0.02 * clinical_features[:, 0] +  # Age effect
                  0.2 * clinical_features[:, 2])
    labels = (risk_score > np.median(risk_score)).astype(int)
    
    patient_ids = [f"PAT_{i:04d}" for i in range(n_patients)]
    
    return {
        'imaging': imaging_features,
        'clinical': clinical_features,
        'labels': labels,
        'patient_ids': patient_ids,
        'feature_names': {
            'imaging': [f"img_feat_{i}" for i in range(n_imaging_features)],
            'clinical': ['age', 'sex'] + [f"clin_feat_{i}" for i in range(n_clinical_features - 2)]
        }
    }
