/**
 * Simple demo program for MPI: a master/worker program that searches for prime numbers in a range of numbers.
 */

#include <stdio.h>
#include <mpi.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

#define SIZE_N 23000
#define BLOCK_SIZE 100
#define R_MULTIPLIER 130

int matrix[SIZE_N][SIZE_N];
int vector[SIZE_N];

/**
 * Given a value 'n', return {\code true} iff the value is prime.
 *
 * @param n The value to examine.
 * @return {\code true} iff the value is prime.
 */
void execute_work(long int n, int *results) {
    for (int offset = 0; offset < BLOCK_SIZE; offset++) {
        int baseNumber = vector[n + offset];
        int *row = matrix[n + offset];

        int result = 0;
        for (int i = 0; i < SIZE_N; i++) {
            result += baseNumber * row[i] * R_MULTIPLIER; 
        }
        results[offset] = result;
    }
}

/**
 * Given a value to send and a worker to send the value to, send
 * a message ordering the worker to compute whether the given value
 * is prime. The special value '0' means that the worker should quit.
 * The worker will send a message to the master with the verdict.
 *
 * @param worker  The worker to send the message to.
 * @param val The value to examine.
 */
void send_work_command(int worker, long int val) {
    // printf("send_work_command: worker=%d val=%lu\n", worker, val);
    MPI_Send(&val, 1, MPI_LONG, worker, 0, MPI_COMM_WORLD);
}


/**
 * Given a result to send, send a message telling the master that
 * the value it sent is prime or not. Note that the value for which the
 * result has been computed is not sent, since nobody cares about it.
 *
 * @param result The result.
 */
void send_result(int result) {
    MPI_Send(&result, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
}


/**
 * Wait for the next value to compute. The value zero means that the worker should quit.
 *
 * @param val A pointer to the value to fill with the received value.
 */
void await_command(long int *val) {
    MPI_Recv(val, 1, MPI_LONG, 0, MPI_ANY_TAG, MPI_COMM_WORLD,
             MPI_STATUS_IGNORE);
}


/**
 * Wait for the next result from a worker.
 *
 * @param worker A pointer to the variable that will hold the worker that sent the result.
 * @param result A pointer to the variable that will hold the result.
 */
void await_result(int *worker, int *result) {
    MPI_Status status;
    MPI_Recv(result, 1, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD,
             &status);
    *worker = status.MPI_SOURCE;
}


/**
 * The code to run as master: send jobs to the workers, and await their replies.
 * There are `worker_count` workers, numbered from 1 up to and including `worker_count`.
 *
 * @param worker_count The number of workers
 * @param startval  The first value to examine.
 * @param nval The number of values to examine.
 * @return The number of values in the specified range.
 */
void run_as_master(int worker_count) {
    int active_workers = 0;
    long int val = 0;

    for (int worker = 1; worker < worker_count && worker < SIZE_N; worker++) {
        send_work_command(worker, val);
        val += BLOCK_SIZE;
        active_workers++;
    }
    int round = 0;
    int lastResultPosition = 0;
    while (active_workers > 0) {
        int worker;
        int result[BLOCK_SIZE];
        await_result(&worker, &result);
        for (int i = 0; i < BLOCK_SIZE; i++) {
            vector[lastResultPosition] = result[i];
            lastResultPosition++;
        }
        
        // vectorResult
        if (val > SIZE_N) {
            if (round > R_MULTIPLIER) {
                send_work_command(worker, 0);
                active_workers--;
            } else {
                round++;
                val = 0;
                lastResultPosition = 0;
            }
        } else {
            send_work_command(worker, val);
            val += BLOCK_SIZE;
        }
    }
}

/**
 * The code to run as worker: receive jobs, execute them, and terminate when told to.
 */
void run_as_worker(void) {
    while(true) {
        long int val;

        await_command(&val);
        if (val == 0) {
            break;  // The master told us to stop.
        }
        int result[BLOCK_SIZE];
        execute_work(val, result);
        send_result(result);
    }
}

int main(int argc, char *argv[]) {
    int rank;
    int size;


    /* Start up MPI */
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    const bool am_master = 0 == rank;

    if (am_master) {
        for (int i = 0; i < SIZE_N; i++) {
            vector[i] = i;
            for (int j = 0; j < SIZE_N; j++) {
                matrix[i][j] = i * j;
            }
        }

        printf("Running as master\n");
        const double start = MPI_Wtime();
        run_as_master(size - 1);
        const double finish = MPI_Wtime();
        printf("Master has finished. This took %.10f seconds\n", finish-start);
    } else {
        printf("Running as worker %d\n", rank);
        run_as_worker();
        printf("Worker %d has finished\n", rank);
    }

    MPI_Finalize();

    return 0;
}
