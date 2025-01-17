from setuptools import setup, find_packages
cuda_deps = ['cupy-cuda112',
	'torch@https://download.pytorch.org/whl/cu111/torch-1.8.1%2Bcu111-cp38-cp38-linux_x86_64.whl',
'torchvision@https://download.pytorch.org/whl/cu111/torchvision-0.9.1%2Bcu111-cp38-cp38-linux_x86_64.whl',
'torchaudio@https://download.pytorch.org/whl/torchaudio-0.8.1-cp38-cp38-linux_x86_64.whl']

setup(
    name='oyLabImaging',
    version='0.2.2',
    description='data processing code for the Oyler-Yaniv lab @HMS',
    author='Alon Oyler-Yaniv',
    url='https://github.com/alonyan/oyLabImaging',
    packages=find_packages(include=['oyLabImaging', 'oyLabImaging.*']),
    python_requires='>=3.8, <3.9',
    dependency_links=[
        "https://download.pytorch.org/whl/torch_stable.html",
    ],
    extras_require = {'cuda': cuda_deps,
    },
    install_requires=[
        'PyYAML',	
	'PyQt5',
	'opencv-python',
	'cellpose==0.7.2',
	'cloudpickle==1.6.0',
	'dill>=0.3.4',
	'ipython>=7.27.0',
	'ipywidgets>=7.6.3',
	'lap==0.4.0',
	'matplotlib>=3.3.4',
	'napari==0.4.11',
	'nd2reader==3.3.0',
	'numba>=0.53.1',
	'numpy>=1.20.1',
	'pandas>=1.2.4',
	'Pillow>=8.3.1',
	'poppy>=1.0.1',
	'pyfftw>=0.12.0',
	'scikit_image<0.19',
	'scikit_learn>=0.24.2',
	'scipy>=1.6.2',
	'setuptools>=52.0.0',
	'cmake',
	'tqdm>=4.59.0',
	'zernike>=0.0.32',
	'multiprocess>=0.70'		
    ]
)
