This week we finished a basic version of the key input emulator, started brainstorming on a UI for the project, and achieved a basic level of transfer learning.

-- Expand on the emulator here --

-- Expand on the UI here --

With the last status update, we were made aware of a powerful lambda computer owned by the university which we can have unlimited access to.  This removes major obstacles we were formerly dealing with and has already enabled a much stronger work flow.  With this we were able to easily achieve basic transfer learning in our jupyter notebook using pytorch.  We are currently using the basic pretrained model ResNet18 and plan to do testing with others. We then started adding data for our first basic gestures, "point left", "point right", "palm flat", and "not a gesture" using the webcam we purchased with requested funding.  After transfer learning the model was able to recognize our custom gestures with up to 84% accuracy.  We are now in pursuit of more hand data from each teammate to help drive thise number up and prevent overfitting.

Setbacks and challenges:

Working with the pretrained model from the https://github.com/ahmetgunduz/Real-time-GesRec repo was proving to be a dead end as we are unfamiliar with the format of 3D-CNNs.  We decided to take a step back and make sure we understand how to make this work with a basic 2D-CNN.  Since this will likely be proficient for our goals, we will now be using this project as a reference for how to handle problems we encounter.  Additionally, the massive pre-labeled video data-sets didn't control for background or angle, so we will be keeping these particularly in mind as we take our pictures.

Plan for the next 3 weeks:

We now believe we can progress to add more photos of more gestures and push the accuracy of our model up.  We would also like to start testing with live video feed in the very near future. 
