from multiprocessing import shared_memory

SHM_NAME = "TEST_BLOCK"
SHM_SIZE = 5

shm = shared_memory.SharedMemory(create=False, name=SHM_NAME, size=SHM_SIZE)
buffer = shm.buf

for n in range(SHM_SIZE):
    print("Reading", buffer[n], "at", n)

buffer[0] = 1;
shm.close()
