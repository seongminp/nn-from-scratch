class NN:
    """Class representing a neural network.

    Attributes:
        layers (list): Layers :)
        layer_props (list): 
            List of tuples containing layer size and activation info.
            Must contain at least two elements (input and output layer).
    """

    def __init__(self, layer_props):
        """Initialize NN class with supplied layer properties."""
        # Number of layers.
        self.num_layers = props['layers']
        self.layers = []

        # Validate layer properties. 
        # Specific to this implementation of NN, nothing really to learn here.
        # Will raise error if layer_props is invalid.
        self.validate_layer_props(layer_props)
        self.layer_props = []

        # Initialize layers from input props.
        self.init_layers()

    def validate_layer_props(self, layer_props):
        """Check if layers are valid. 
        Args:
            layer_props (list): List of tuples containing 
                layer size and activation info.

        Returns:
            bool: Whether supplied layer properties are valid.
        """
        
        if len(layer_props) < 2:
            raise ValueError('layer_props must have length of at least 2.')

        for i, (size, act) in enumerate(layer_props):
            if dim <= 0:
                raise ValueError(
                        f'layer {i}: layer dimention must have size > 0')

    def init_layers(self):
        """Initialize weights and biases"""


