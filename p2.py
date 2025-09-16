# Banker's Algorithm for Deadlock Avoidance
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
        self.available = [total - allocated_sum for total, allocated_sum in zip(total_resources, map(sum, zip(*allocated)))]
        self.n = len(allocated)  # Number of processes
        self.m = len(total_resources)  # Number of resource types

    def is_safe(self):
        """
        Check if the current system state is safe.
        """
        work = self.available[:]
        finish = [False] * self.n
        safe_sequence = []
        
        while len(safe_sequence) < self.n:
            progress = False
            for i in range(self.n):
                if not finish[i]:
                    # Calculate the remaining needs of the process
                    needs = [self.max_claims[i][j] - self.allocated[i][j] for j in range(self.m)]
                    
                    # Check if the process can finish with the available resources
                    if all(needs[j] <= work[j] for j in range(self.m)):
                        # If so, simulate process completion
                        work = [work[j] + self.allocated[i][j] for j in range(self.m)]
                        finish[i] = True
                        safe_sequence.append(i)
                        progress = True
                        break
            
            if not progress:
                return False, []  # No progress, system is in an unsafe state
        return True, safe_sequence  # The system is in a safe state

    def request_resources(self, process_id, request):
        """
        Simulate resource request from a process and check if it is granted.
        """
        # Check if the request is less than or equal to the needed resources
        needs = [self.max_claims[process_id][j] - self.allocated[process_id][j] for j in range(self.m)]
        if any(request[j] > needs[j] for j in range(self.m)):
            print("Request exceeds maximum claim")
            return False
        
        # Check if the request is less than or equal to available resources
        if any(request[j] > self.available[j] for j in range(self.m)):
            print("Not enough resources available")
            return False
        
        # Temporarily allocate the resources
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
            # Rollback if not safe
            self.allocated = original_allocated
            self.available = original_available
            print(f"Request denied for Process {process_id}")
            return False
    
    def release_resources(self, process_id, release):
        """
        Simulate the release of resources by a process.
        """
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
    print("System is in a safe state. Safe sequence: {sequence}")
else:
    print("System is in an unsafe state.")

# Simulate resource request by Process 1
request = [1, 0, 2]  # Process 1 requests 1 unit of resource 0, 0 unit of resource 1, and 2 units of resource 2
bankers.request_resources(1, request)

# Simulate resource release by Process 0
release = [2, 1, 1]  # Process 0 releases 2 units of resource 0, 1 unit of resource 1, and 1 unit of resource 2
bankers.release_resources(0, release)

# Check again if the system is in a safe state
safe, sequence = bankers.is_safe()
if safe:
    print("System is in a safe state. Safe sequence: {sequence}")
else:
    print("System is in an unsafe state.")

