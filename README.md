# Overview

This project provides an easy-to-use command-line interface for encrypting and decrypting files using the Advanced Encryption Standard (AES) algorithm and the SHA256 hash function. The encryption and decryption processes are implemented using the PyCryptodome library, which is a self-contained Python package of low-level cryptographic primitives that supports both Python 2 and 3.

With this tool, you can securely encrypt any type of file, including videos, images, and documents, and protect them against unauthorized access. The tool also allows you to decrypt the encrypted files and restore them to their original form.

## Features

- Uses AES algorithm in the CBC mode with a 256-bit key and PKCS7 padding
- Use SHA256 for key derivation
- Support for both encryption and decryption
- Easy-to-use command-line interface
- Works with any type of file

## Getting Started

To use this tool, you'll need to have Python 3 and PyCryptodome installed on your machine.
You can install PyCryptodome using pip:

```python
pip install pycryptodome
```

Once you have the dependencies installed, you can clone this repository and use the script to encrypt or decrypt files.



For example, to encrypt a file called myfile.txt, you can use the following command:
```python
python encryption.py myfile.txt -p mypassword
```



This will create an encrypted version of the file called myfile.txt. 
To decrypt the file, you can use the following command:
```python
python decryption.py myfile.txt -p mypassword
```

## Contributing

We welcome contributions to this project. If you have any ideas for new features or find any bugs, please open an issue or submit a pull request.
