# Gesture Recognition Status Update 1
The most important thing that we have accomplished in the past three weeks
was finding a dataset to train our model on. We went through various data sets
for hours, trying to find something easy and well-built specifically for 
something like our project.

We ended up landing on the twentybn jester dataset. It's a dataset created by a company that's offered for free for educational purposes.

Available at this link: 

https://20bn.com/datasets/jester

It offers clean, neatly sorted videos of humans performing a variety of different gestures in front of a webcam. Compared to the previous datasets we had found, this is nearly perfect. 

There are some small drawbacks to consider though. We first had planned to use a dataset of still images, so these short videos are a deviation from the plan. This shouldn't be that significant of a change though, but it is worth mentioning. The second is that the license for educational purposes is fairly specific, so we'll have to look into how to license our final project so that it can't be used for commercial purposes.

Other than the dataset, we also collected information on the various projects out there already looking at gesture recognition. The most useful one for us (that we found) appears to be a project by some graduate students at Cornell who had a similar idea, and even used the same dataset.

We will most likely heavily reference their project, linked here:

https://github.com/ahmetgunduz/Real-time-GesRec

Although we planned to train our own model, we aren't yet certain if we've secured funding for the compute time needed to conduct training.  As such we are considering simply using the pre-trained model from the link above, then adding in some of our own pictures/videos to add a custom gesture with transfer learning. This is an option which would allow us to reintroduce handicap applications and solutions into our project goals.
