class BankersAlgorithm:
    def __init__(self, total_resources, allocated, max_claims):
        """
        Initialize the Banker's Algorithm with:
        - total_resources: Total available resources.
        - allocated: Resources already allocated to each process.
        - max_claims: Maximum resource requirements of each process.
        """
        self.total_resources = total_resources
        self.allocated = allocated  # Allocated resources to each process
        self.max_claims = max_claims  # Maximum resource needs of each process
        self.n = len(allocated)  # Number of processes
        self.m = len(total_resources)  # Number of resource types

        # Calculate the available resources by subtracting allocated resources from the total resources
        self.available = [total_resources[i] - sum(self.allocated[j][i] for j in range(self.n)) for i in range(self.m)]
        
        # Debugging: Output the available resources
        print(f"Available resources: {self.available}")

    def is_safe(self):
        """
        Check if the current system state is safe.
        """
        work = self.available[:]  # Work starts as available resources
        finish = [False] * self.n  # Keeps track of whether processes have finished
        safe_sequence = []  # To store the safe sequence of processes

        # Try to find a safe sequence
        while len(safe_sequence) < self.n:
            progress = False  # Flag to check if we made progress in finding a process that can finish
            for i in range(self.n):
                if not finish[i]:
                    # Calculate the remaining needs of the process
                    needs = [self.max_claims[i][j] - self.allocated[i][j] for j in range(self.m)]
                    
                    # Check if the process can finish with the current available resources
                    if all(needs[j] <= work[j] for j in range(self.m)):
                        # If so, simulate the process finishing and release its resources
                        work = [work[j] + self.allocated[i][j] for j in range(self.m)]  # Add allocated resources to available
                        finish[i] = True  # Mark process as finished
                        safe_sequence.append(i)  # Add process to safe sequence
                        progress = True
                        break
            
            # If no process could finish, the system is unsafe
            if not progress:
                print("System is in an unsafe state!")
                return False, []

        # If we have found a safe sequence, the system is in a safe state
        print(f"System is in a safe state. Safe sequence: {safe_sequence}")
        return True, safe_sequence

    def request_resources(self, process_id, request):
        """
        Simulate resource request from a process and check if it is granted.
        """
        print(f"Process {process_id} is requesting resources: {request}")

        # Check if the request is less than or equal to the needed resources
        needs = [self.max_claims[process_id][j] - self.allocated[process_id][j] for j in range(self.m)]
        if any(request[j] > needs[j] for j in range(self.m)):
            print("Request exceeds maximum claim")
            return False
        
        # Check if the request is less than or equal to available resources
        if any(request[j] > self.available[j] for j in range(self.m)):
            print("Not enough resources available")
            return False
        
        # Temporarily allocate the resources (pretend we grant the request)
        original_allocated = [self.allocated[i][:] for i in range(self.n)]
        original_available = self.available[:]
        
        # Allocate the resources
        self.allocated[process_id] = [self.allocated[process_id][j] + request[j] for j in range(self.m)]
        self.available = [self.available[j] - request[j] for j in range(self.m)]
        
        # Check if the system is in a safe state after allocation
        safe, _ = self.is_safe()
        
        if safe:
            print(f"Resources granted to Process {process_id}")
            return True
        else:
            # Rollback the allocation if it leads to an unsafe state
            self.allocated = original_allocated
            self.available = original_available
            print(f"Request denied for Process {process_id}")
            return False
    
    def release_resources(self, process_id, release):
        """
        Simulate the release of resources by a process.
        """
        print(f"Process {process_id} is releasing resources: {release}")
        self.allocated[process_id] = [self.allocated[process_id][j] - release[j] for j in range(self.m)]
        self.available = [self.available[j] + release[j] for j in range(self.m)]
        print(f"Process {process_id} released resources")

# Example Usage
total_resources = [10, 5, 7]  # Total resources available of type 0, 1, 2
allocated = [
    [3, 2, 2],  # Resources allocated to Process 0
    [2, 1, 3],  # Resources allocated to Process 1
    [3, 3, 2]   # Resources allocated to Process 2
]
max_claims = [
    [7, 5, 3],  # Max claims by Process 0
    [3, 2, 2],  # Max claims by Process 1
    [9, 0, 2]   # Max claims by Process 2
]

bankers = BankersAlgorithm(total_resources, allocated, max_claims)

# Check if the initial state is safe
safe, sequence = bankers.is_safe()
if safe:
    print(f"System is in a safe state. Safe sequence: {sequence}")
else:
    print("System is in an unsafe state.")
