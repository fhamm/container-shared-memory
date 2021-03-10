# Docker + SharedMemory = <3
## Description
This is a simple example of how you can share memory blocks between containers using Docker and Python3 SharedMemory library.

## Usage

### Build with docker-compose
```docker-compose up```

Or alternatively (and with more work), build and run the transmitter and receiver individually:

### Build transmitter image
```docker build ./transmitter/ --tag "transmitter:shm"```

### Build receiver image 
```docker build ./receiver/ --tag "receiver:shm"```

### Run transmitter
```docker run --ipc="shareable" [TRANSMITTER_IMAGE_ID]```

### Run receiver
```docker run --ipc="container:[TRANSMITTER_CONTAINER_ID]" [RECEIVER_IMAGE_ID]```

## Author
This tutorial was written by Felipe Hamm and Rodrigo Faria.

## Useful links

https://docs.docker.com/engine/reference/commandline/build/

https://docs.docker.com/engine/reference/run/#ipc-settings---ipc

https://docs.python.org/3/library/multiprocessing.shared_memory.html
