import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

long_description = ""
setuptools.setup(
    name="vietocr",
    version="0.3.11",
    author="pbcquoc",
    author_email="pbcquoc@gmail.com",
    description="Transformer base text detection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/buiducthanh22/VietOCR_Fix",
    packages=setuptools.find_packages(),
    install_requires=[
        'einops==0.2.0',
        'scikit-image>=0.21.0',
        'prefetch_generator==1.0.1',
        'lmdb>=1.0.0',
        'imgaug==0.4.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
