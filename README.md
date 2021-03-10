# Build transmitter image
docker build ./transmitter/ --tag "transmitter:shm"

# Build receiver image 
docker build ./receiver/ --tag "receiver:shm"

# Run transmitter
docker run --ipc="shareable" [TRANSMITTER_IMAGE_ID]

# Run receiver
docker run --ipc="container:[TRANSMITTER_CONTAINER_ID]" [RECEIVER_IMAGE_ID]
