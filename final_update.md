# Final update for team Gesture Recognition

Over the past few weeks we have finished our integration with the model, webcam, and input mapping. Now the final product works as intended.

# Model tweaking/training -

Kyle spent a lot of time tweaking to get slightly more accurate models. We now have a few different models to choose from, with multiple over 90% accurate. These use various different architectures, with our main testing model being resnext with depth 50.

# Dataset collection/sorting -

Eli finalized the data into a folder, and our last group member Ryan submitted his images, now completing our dataset that has 8500+ images.

# Input mapping - 

Ryan and Kyle worked on this, using different libraries to finish it. Our final script uses pynput to map the inputs to keypresses.

# Main script -

Eli and Kyle worked on and successfully implemented model integration between opencv and pytorch, allowing us to process webcam frames as they come in. This took a lot of troubleshooting, as simply running a single image through a model was tricker than we originally thought. Currently the script processes multiple images per second and upon reaching a threshold of the same predicted gesture in a row, will input a keypress.

# Setbacks and Challenges -

Communication has been difficult as always. We also wanted to implement a GUI originally to change things but had to scrap that idea due to lack of time.

# Plan going forward -

Presentation time!
