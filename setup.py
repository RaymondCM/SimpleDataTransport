import setuptools

setuptools.setup(
    name='SimpleImageTransport',
    version='0.1',
    author="Raymond Kirk",
    author_email="ray.tunstill@live.co.uk",
    description="Simple python 3 library for transporting images to a remote machine, applying transformations and "
                "returning a response.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RaymondKirk/SimpleImageTransport",
    packages=["SimpleImageTransport"],
    install_requires=['opencv-python', 'Flask', 'numpy', 'requests', 'jsonpickle'],
)
