import random
import collections
import time

# Leaky Token Bucket class (representing the queue)
class LeakyTokenBucket:
    def __init__(self, capacity):
        self.capacity = capacity  # Max number of tokens in the bucket (waiting room)
        self.tokens = collections.deque()  # Tokens in the waiting room (queue)

    def add_token(self, token_number):
        """Add a token to the queue, respecting the capacity."""
        if len(self.tokens) < self.capacity:
            self.tokens.append(token_number)

    def call_token(self):
        """Call the next token in the queue (process a patient)."""
        if self.tokens:
            return self.tokens.popleft()
        return None

    def get_token_list(self):
        """Return the current list of tokens in the waiting room."""
        return list(self.tokens)

# Set parameters for the simulation
waiting_room_capacity = 50  # Max number of patients (tokens)
steps = 60  # Total time steps (simulating 60 rounds of staff calling patients)

# Create the token bucket (waiting room)
waiting_room = LeakyTokenBucket(waiting_room_capacity)

# Generate unique token numbers for the patients
token_numbers = [f"{i:05d}" for i in range(1, waiting_room_capacity + 1)]

# Add all the patients (tokens) to the waiting room
for token in token_numbers:
    waiting_room.add_token(token)

# Simulation loop (staff calling token numbers)
for step in range(steps):
    # Staff calls a token (process a patient)
    called_token = waiting_room.call_token()

    # If there is a token to call, process the patient
    if called_token:
        print(f"Step {step + 1}: Staff calls token {called_token}. The patient is processed through the ETC.")
    else:
        print(f"Step {step + 1}: No tokens left in the waiting room.")
    
    # Wait a bit before the next step (for simulation effect)
    time.sleep(1)
