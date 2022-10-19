# Python Library Boilerplate

This is a boilerplate code that can be used to create python libraries!

## Build your library

Make sure your present working directory is /path/to/library (so the root folder of your project). In your command prompt, run:
> python setup.py bdist_wheel

Your wheel file is stored in the “dist” folder that is now created. You can install your library by using:
> pip install /path/to/wheelfile.whl

Once you have installed your Python library, you can import it using:

1. ```import mypythonlib```
2. ```from mypythonlib import myfunctions```

## Credits

Credit is given where credit is due!
- The boilplate was written by following the tutorial at: https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f
- The tutorial was written by Kai Eisinga
