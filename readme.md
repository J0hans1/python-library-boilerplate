# Build your library

Make sure your present working directory is /path/to/library (so the root folder of your project). In your command prompt, run:
> python setup.py bdist_wheel

Your wheel file is stored in the “dist” folder that is now created. You can install your library by using:
> pip install /path/to/wheelfile.whl

Once you have installed your Python library, you can import it using:

```import mypythonlib```
````from mypythonlib import myfunctions```
