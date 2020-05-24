class NN:
    """Class representing a neural network.

    Attributes:
        layers (list): List of Layer instances.
    """

    def __init__(self, layers):
        """Initialize NN class with supplied layer instances."""

        if len(layers) < 1:
            raise Exception('NN must have at least one layer.')

        self.layers = layers
        self.num_layers = len(layers)

        # Initialize layers from input props.
        self.init_layers()

    def init_layers(self):
        """Initialize weights and biases"""
        prev_s = self.layers[0].size
        for l in self.layers:
            l.init(prev_s, l.size)
            prev_s = l.size

    def forward(self, X):
        """Forward pass through all layers.

        Args:
            X (2D np.ndarray): Input to the neural network.

        Returns:
            2D np.ndarray: Output of forward pass.
        """
        for l in self.layers:
            layer_activation = l.forward(X)





