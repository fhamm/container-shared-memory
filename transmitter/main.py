from multiprocessing import shared_memory

SHM_NAME = "TEST_BLOCK"
SHM_SIZE = 5

shm = shared_memory.SharedMemory(create=True, name=SHM_NAME, size=SHM_SIZE)
buffer = shm.buf

for n in range(SHM_SIZE):
    print("Writing", n, "at", n)
    buffer[n] = n

while (True):
    if (buffer[0] != 0):
        print("Signal confirmation received. Breaking...")
        shm.close()
        shm.unlink()
        break;
    else:
        continue
