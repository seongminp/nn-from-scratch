from .activations import str2act

class Layer():
    """Class representing a single layer.

    Attributes:
        size (int): Size of layer (number of neurons). 
        activation (str): Name of activation function.
        W (2D np.ndarray): Weight matrix, including bias.
    """

    def __init__(self, size, activation):
        """Initialize layer with supplied layer properties."""

        if size <= 0:
            raise Exception('Layer size must be > 0.')

        if activation not in str2act:
            raise Exception('Invalid activation function supplied.')
                        
        self.size = size
        self.activation = activation
        self.W = None


    def init(self, input_size, output_size):
        """Randomly initialize weights and biases."""
        self.W = np.random.randn(output_size, input_size+1)

    def forward(self, X):
        """Forward propagation step for layer.

        Args:
            X (2D np.ndarray): Input to the layer.

        Returns:
            2D np.ndarray: Output from layer.
        """
        Z = np.dot(self.W, X)
        f = str2act[self.activation]
        return f(Z)

        

    

