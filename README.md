# SharkBinary

SharkBinary is a Python package that provides a simple interface for saving and loading data to and from custom binary files using a fixed format. With SharkBinary, you can easily convert Python objects to binary data and vice versa, making it easy to store and retrieve data from your Python programs.

## Installation

You can install SharkBinary using pip:

    pip install SharkBinary
    
Or alternativly:
  
   git clone https://github.com/Miskoking800/SharkBinary.git
   cd SharkBinary
   pip install .

## Usage

Here's an example of how to use SharkBinary to save and load data to and from a binary file:

```python
import sharkbinary

# Create some data to save
data = [1, 2, 3, 4, 5]

# Save the data to a binary file
sharkbinary.save_data(data, 'data.bin')

# Load the data from the binary file
loaded_data = sharkbinary.load_data('data.bin')

# Print the loaded data
print(loaded_data)

This will output:

[1, 2, 3, 4, 5]

#Contributing
Contributions are welcome! If you have a bug fix or feature you would like to contribute, please open an issue or pull request on GitHub.

#License

SharkBinary is released under the MIT License. See the LICENSE file for details.
