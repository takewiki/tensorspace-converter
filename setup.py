import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

CONSOLE_SCRIPTS = [
    "tensorspace_converter = tensorspacejs.converters.hello_world:main"
]

setuptools.setup(
    name="tensorspacejs",
    version="0.0.2",
    author="Chenhua Zhu",
    author_email="zchholmes@gmail.com",
    description="TensorSpace.js Python tool package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tensorspace-team/tensorspace-converter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: JavaScript",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],

    entry_points={
        "console_scripts": CONSOLE_SCRIPTS
    },
    license="Apache 2.0",
    keywords="tensorspace javascript neural network 3d visualization converter"
)