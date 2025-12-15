 We will be using multiparametric magnetic resonance images (mp-MRI) recordings from previous BraTS challenges openly available in the Medical Segmentation Decathlon (MSD) repository (http://medicaldecathlon.com) as `Task01_BrainTumor.tar` (see also https://decathlon-10.grand-challenge.org).



Some technicalities for downloading data on colab:
```
import gdown
import shutil
import os
import sys
```

```
# This is a quick check of whether the notebook is currently 
# running on Google Colaboratory or on Kaggle, 
# as that makes some difference for the code below.

try:
    import colab
    colab=True
except:
    colab=False

import os
kaggle = os.environ.get('KAGGLE_KERNEL_RUN_TYPE', '')

#Install `fastMONAI` if notebook is running on Google Colab or on Kaggle
if (colab or kaggle):
    %pip install fastMONAI
    if colab:
        from fastMONAI.utils import print_colab_gpu_info
        print_colab_gpu_info()
else:
    print('Running locally')
```

Download `assets.zip` file if ./assets does not exist (as when running in Colab)


```
if os.path.isdir('./assets') == False:
    
    ## Download assets.zip from Google Drive (My Drive -> ELMED219 -> Lab1-mpMRI-glioblastoma -> assets.zip)
    # OLD: https://drive.google.com/file/d/1yYoQZR8jSyL1_23wimkMDHQv3cGC8TWN/view?usp=share_link
    # https://drive.google.com/file/d/1uF32YcNp1DveTqmEg4ao6INTJWv0WkXA/view?usp=sharing
    
    file_id = '1uF32YcNp1DveTqmEg4ao6INTJWv0WkXA'
    url = 'https://drive.google.com/uc?id=%s' % file_id
    output = './assets.zip'
    #gdown.download(url, output, quiet=False)
    !gdown "1uF32YcNp1DveTqmEg4ao6INTJWv0WkXA&confirm=t"
    
    ## Unzip the assets.zip file into `./assets`
    shutil.unpack_archive(output, '.')
    
    ## Delete the `assets.zip` file
    os.remove(output)
else:
    print(f'./assets  exists already and will not be overwritten!')
```
Download data.zip file if ./data does not exist (as when running in Colab)
```
if os.path.isdir('./data') == False:
    
    ## Download data.zip from Google Drive  (My Drive -> ELMED219 -> Lab1-mpMRI-glioblastoma -> data.zip)
    # https://drive.google.com/file/d/1y3OvRNthpDdllo--L3WHYXTsjb6H87FT/view?usp=sharing
    # OLD: https://drive.google.com/file/d/1mKbERWG09Ni5UpnYhLlcebKfxeVu_Y2c/view?usp=share_link
    
    file_id = '1y3OvRNthpDdllo--L3WHYXTsjb6H87FT'
    url = 'https://drive.google.com/uc?id=%s' % file_id
    output = './data.zip'
    #gdown.download(url, output, quiet=False)
    !gdown "1y3OvRNthpDdllo--L3WHYXTsjb6H87FT&confirm=t"
    
    ## Unzip the data.zip file into `./data`
    shutil.unpack_archive(output, '.')
    
    ## Delete the `data.zip` file
    os.remove(output)
else:
    print(f'./data  exists already and will not be overwritten!')
```
