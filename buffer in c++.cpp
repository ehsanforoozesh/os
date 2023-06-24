#include <iostream>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>

#define BUFFER_SIZE 10

using namespace std;

typedef struct {
    int value;
} item;

int main() {
    int shmid;
    item *buffer;
    int in = 0, out = 0;

    // Create shared memory segment
    if ((shmid = shmget(IPC_PRIVATE, BUFFER_SIZE * sizeof(item), IPC_CREAT | 0666)) < 0) {
        perror("shmget");
        exit(1);
    }

    // Attach shared memory segment
    if ((buffer = (item *) shmat(shmid, NULL, 0)) == (item *) -1) {
        perror("shmat");
        exit(1);
    }

    // Producer
    if (fork() == 0) {
        int next_produced = 1;
        while (true) {
            sleep(1); // Simulate production time
            item produced_item;
            produced_item.value = next_produced++;

            // Wait for empty slot
            while (((in + 1) % BUFFER_SIZE) == out);

            // Add item to buffer
            buffer[in] = produced_item;
            in = (in + 1) % BUFFER_SIZE;

            cout << "Produced item with value " << produced_item.value << endl;
        }
    }

    // Consumer
    if (fork() == 0) {
        while (true) {
            sleep(1); // Simulate consumption time

            // Wait for item to consume
            while (in == out);

            // Remove item from buffer
            item consumed_item = buffer[out];
            out = (out + 1) % BUFFER_SIZE;

            cout << "Consumed item with value " << consumed_item.value << endl;
        }
    }

    // Wait for child processes to finish
    wait(0);
    wait(0);

    // Detach and remove shared memory segment
    shmdt(buffer);
    shmctl(shmid, IPC_RMID, NULL);

    return 0;
}