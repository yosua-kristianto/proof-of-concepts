# Smol POC of me learning TensorlayerX

May, 4th 2024.
With the x-times I learned to make some DNN with TensorlayerX, I kind of trying to reassure what is going on within the TensorlayerX. Why can't I ever justify what's going on within the TensorlayerX, even though I'm doing a simple Artificial Neural Network. So here we go, another part of my pilmirage of learning TensorlayerX, begin.

## [May, 4th 2024]()
My goal today is to justify whether I really can do simple ANN with this API.

> What I'm really consider is, there is no "Linear" activation. Only "None" activation. Is it okay?
> 
> I just found out the default activation function settings in TensolayerX is Truncated Normal.
>
> And all this time, I just found out that all "uniform" activation functions may provides minus logits.

## [May, 5th 2024]()
My goal today is getting accuracy above 90% for the validation phase.

> I'm little worried since the accuracy and the loss results are more constant than Tensorflow that gives some more fuzzy result. But I'm using Tensorflow's Backend no?
>
> I found that softmax_cross_entropy_with_logits's label implemnetation is not a One-Hot Encoded data. Also, when using this loss function, I have to let go the activation function on the output layer.
>
> I found that SGD's Learning rate in here for some reason is 1e-3 instead of 1e-1. 
>
> I found that for some reason, initializer other than Truncated Normal is not really work for classification case. I also found this on SRGAN and CIFAR-10.
>
> Tensorlayerx didn't return the loss and acc directly from train function. So if you want to make a plot of the accuracy, you need to copy the output from training function. Unless you're using TrainOneStep. Which what I will do the next day.