from collections import namedtuple
from pathlib import Path

# Dataset root directory, relative to this file's location
_DATASET_ROOT = Path(__file__).parent.parent / 'Dataset'

Dataset = namedtuple('Dataset', ['name', 'src', 'bug_repo', 'features'])
# Source codes and bug repositories

aspectj = Dataset(
    'aspectj',
    _DATASET_ROOT / 'org.aspectj-bug433351',
    _DATASET_ROOT / 'bug reports' / 'AspectJ.txt',
    _DATASET_ROOT / 'features_aspectj.csv'
)

eclipse = Dataset(
    'eclipse',
    _DATASET_ROOT / 'eclipse.platform.ui-johna-402445',
    _DATASET_ROOT / 'bug reports' / 'Eclipse_Platform_UI.txt',
    _DATASET_ROOT / 'features_eclipse.csv'
)

swt = Dataset(
    'swt',
    _DATASET_ROOT / 'eclipse.platform.swt-xulrunner-31',
    _DATASET_ROOT / 'bug reports' / 'SWT.txt',
    _DATASET_ROOT / 'features_swt.csv'
)

tomcat = Dataset(
    'tomcat',
    _DATASET_ROOT / 'tomcat-7.0.51',
    _DATASET_ROOT / 'bug reports' / 'Tomcat.txt',
    _DATASET_ROOT / 'features_tomcat.csv'
)

birt = Dataset(
    'birt',
    _DATASET_ROOT / 'birt-20140211-1400',
    _DATASET_ROOT / 'bug reports' / 'Birt.txt',
    _DATASET_ROOT / 'features_birt.csv'
)

ALL_DATASETS = [aspectj, eclipse, swt, tomcat, birt]



### Current dataset in use. (change this name to change the dataset)
DATASET = eclipse

if __name__ == '__main__':
    print(DATASET.name, DATASET.src, DATASET.bug_repo)
