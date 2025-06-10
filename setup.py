from setuptools import setup, find_packages

setup(
    name="yolov5_baseline",
    version="0.0.1",
    python_requires=">=3.8",
    packages=find_packages(
        exclude=(
            "data*",        # exclude sample images / labels
            "segment*",     # segmentation helpers unused here
            "classify*", 
            "track*", 
            "runs*", 
            "weights*",
        )
    ),
    install_requires=[
        "torch>=1.10",          # use whatever CUDA wheel you already installed
        "numpy",
        "opencv-python",
        "tqdm",
        # add any extras the repo needs
    ],
)
