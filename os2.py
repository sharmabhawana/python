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

