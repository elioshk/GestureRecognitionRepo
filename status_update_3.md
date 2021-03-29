This week we finished a basic version of the key input emulator, started brainstorming on a UI for the project, and achieved a basic level of transfer learning.

-- Expand on the emulator here --

-- Expand on the UI here --

With the last status update, we were made aware of a powerful lambda computer owned by the university which we can have unlimited access to.  This removes major obstacles we were formerly dealing with and has already enabled a much stronger work flow.  With this we were able to easily replicate a basic transfer learning tutorial from the official pytorch website, which uses the pretrained model ResNet18 as opposed to the one from the github repo we've been planning to use. We then added data for our first basic gesture, "fist", which was able to be recognized by our model with minimal tweaking.  We are now in pursuit of more basic gesture data to experiment further.

Setbacks and challenges:

Working with the pretrained model from the https://github.com/ahmetgunduz/Real-time-GesRec repo was proving to be a dead end as we are unfamiliar with the format of 3D-CNNs.  We decided to take a step back and make sure we understand how to make this work with a basic 2D-CNN.  While this could still be sufficient for our goals, we hope to move back to a 3D-CNN very soon.

Plan for the next 3 weeks:

We now believe we can progress to add more photos of more gestures and push the accuracy of our model up.  We would also like to start testing with live video feed in the near future.  As our understanding increases we hope to be able to switch back to the original pretrained model to transfer learn from there instead, but this is becoming a stretch goal.
