#include <stdio.h>

#define MAX_PROCESSES 10

#define MAX_RESOURCES 10



int available[MAX_RESOURCES];

int max[MAX_PROCESSES][MAX_RESOURCES];

int allocation[MAX_PROCESSES][MAX_RESOURCES];

int need[MAX_PROCESSES][MAX_RESOURCES];



int num_processes, num_resources;



void initialize() {

    printf("Enter the number of processes: ");

    scanf("%d", &num_processes);



    printf("Enter the number of resources: ");

    scanf("%d", &num_resources);



    printf("Enter the available resources for each type: ");

    for (int j = 0; j < num_resources; j++) {

        scanf("%d", &available[j]);

    }



    printf("Enter the maximum demand of each process: \n");

    for (int i = 0; i < num_processes; i++) {

        printf("Process %d: ", i);

        for (int j = 0; j < num_resources; j++) {

            scanf("%d", &max[i][j]);

        }

    }



    printf("Enter the current allocation for each process: \n");

    for (int i = 0; i < num_processes; i++) {

        printf("Process %d: ", i);

        for (int j = 0; j < num_resources; j++) {

            scanf("%d", &allocation[i][j]);

            need[i][j] = max[i][j] - allocation[i][j];

        }

    }

}



int request_resources(int process_id, int request[]) {

    for (int j = 0; j < num_resources; j++) {

        if (request[j] > need[process_id][j] || request[j] > available[j]) {

            return 0; // Request exceeds maximum allowed or available resources

        }

    }



    // Try to allocate resources temporarily

    for (int j = 0; j < num_resources; j++) {

        available[j] -= request[j];

        allocation[process_id][j] += request[j];

        need[process_id][j] -= request[j];

    }



    // Check for safety

    if (is_safe()) {

        return 1; // Resources allocated successfully

    } else {

        // Rollback changes if not safe

        for (int j = 0; j < num_resources; j++) {

            available[j] += request[j];

            allocation[process_id][j] -= request[j];

            need[process_id][j] += request[j];

        }

        return 0; // Resources cannot be allocated safely

    }

}



int release_resources(int process_id, int release[]) {

    for (int j = 0; j < num_resources; j++) {

        if (release[j] > allocation[process_id][j]) {

            return 0; // Trying to release more resources than allocated

        }

    }



    // Release resources

    for (int j = 0; j < num_resources; j++) {

        available[j] += release[j];

        allocation[process_id][j] -= release[j];

        need[process_id][j] += release[j];

    }



    return 1; // Resources released successfully

}



int is_safe() {

    int work[MAX_RESOURCES];

    int finish[MAX_PROCESSES] = {0};



    // Initialize work array

    for (int j = 0; j < num_resources; j++) {

        work[j] = available[j];

    }



    // Find an index i such that both finish[i] is false and need[i] is less than or equal to work

    int i, j;

    for (i = 0; i < num_processes; i++) {

        if (!finish[i]) {

            for (j = 0; j < num_resources; j++) {

                if (need[i][j] > work[j]) {

                    break;

                }

            }

            if (j == num_resources) {

                break; // Found a process that can complete

            }

        }

    }



    if (i == num_processes) {

        return 1; // All processes can complete safely

    } else {

        return 0; // Deadlock detected

    }

}



int main() {

    initialize();



    int process_id;

    printf("Enter the process id making the request: ");

    scanf("%d", &process_id);



    int request[MAX_RESOURCES];

    printf("Enter the request for resources: ");

    for (int j = 0; j < num_resources; j++) {

        scanf("%d", &request[j]);

    }



    if (request_resources(process_id, request)) {

        printf("Resources allocated successfully.\n");

    } else {

        printf("Request denied. Resources cannot be allocated safely.\n");

    }



    return 0;

}


