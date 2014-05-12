# Forest Fire Simulation

This amazing product enables pyromaniacs to satisfy their needs. This can be achieved through epic forest fire simulations made in python. _We are neither liable nor responsible for anything. Only burn a forest if it's your property._

## How to run

The main interface started by `python run_cl.py`, this requires an OpenCL GPU device and quite a few packages. In case you have access to the DTU HPC system, you can use this guide to get started:
https://gist.github.com/AndreasMadsen/45050d426e411e985703

The simulation can then be configured by selecting a picture with:

```python
forest = np.load('picture/forest2.npy')
```

and a simulation model with:

```python
model = Simulator("random_type", forest)
```

Look in the picture and kernels directory, to see which pictures and models are available.


##License

**The software is license under "MIT"**

> Copyright (c) 2013 Andreas Madsen
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.
