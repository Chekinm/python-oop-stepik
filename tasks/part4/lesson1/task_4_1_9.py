class Layer:
    def __init__(self):
        self.name = 'Layer'
        self.next_layer = None

    def __call__(self, next_layer):
        self.next_layer = next_layer
        return self.next_layer


class Dense(Layer):
    def __init__(self, number_of_inputs, number_of_outputs, activation):
        super().__init__()
        self.name = 'Dense'
        self.inputs = number_of_inputs
        self.outputs = number_of_outputs
        self.activation = activation


class Input(Layer):
    def __init__(self, number_of_inputs):
        super().__init__()
        self.name = 'Input'
        self.inputs = number_of_inputs


class NetworkIterator:

    def __init__(self, network):
        self.current_layer = network
        self._next_layer = self.current_layer.next_layer

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_layer is None:
            raise StopIteration
        else:
            current_layer = self.current_layer
            self.current_layer = self.current_layer.next_layer
            return current_layer


nt = Input(12)
layer = nt(Dense(nt.inputs, 1024, 'relu'))
layer = layer(Dense(layer.inputs, 2048, 'relu'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

n = 0
for x in NetworkIterator(nt):
    assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
    n += 1
    
assert n == 4, "итератор перебрал неверное число слоев"