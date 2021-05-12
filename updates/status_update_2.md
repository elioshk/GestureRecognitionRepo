We've split our project into two groups, one working on training the AI for gesture recognition and one to configure the output given to us by the AI into a usable form on a windows device. Emily, Eli and Kyle will be in the AI group, while Ryan and Devin will focus on windows implementation.

For the output configuration, we've identified a python library that will allow us to manipulate keypresses and mouse movement
https://pypi.org/project/pynput/

We will be using python for this implementation because it will integrate more easily with the AI, which is also in python.

We also plan to have a simple game or demonstration which these inputs will be used on.

Using cloud computing like Lambda Labs is new to all of us, so recently we had to figure out the basics with windows subsystem linux (WSL) and homogenize our team's setups so that we can work together (Lambda labs doesnt currently support multiuser access so we have to make sure we do things in the same way). We then played around with the instance, spending precious billing time learning about this new environment. In an effort to be efficient with this limited resource, we typed out a simple procedure detailing how to setup  our space quickly.

Setbacks and challenges:

We have had progress working with lambda labs and figuring out how it will function with our project, but the process has been complex
Mid-terms have presented a significant obstacle as far as time management goes for our team to coordinate, but this should rectify itself as exams finish up.

Our plan going forward:

Plans going forward are to continue working through the repo for the existing model, learning and preparing the model for the transfer learning step.  We have also ordered a basic camera for the data gathering phase which we are closing in on. Additionally, we plan on finishing a preliminary version of a python script which will take the data we get from our AI and configure it to register as key presses and/or mouse movement to begin testing.
