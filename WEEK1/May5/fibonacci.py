#!/usr/bin/env python3

def generate_fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    
    # Start with the first two numbers
    sequence = [0, 1]
    
    # Generate the rest of the sequence
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence[:n]  # Ensure we return exactly n terms

def print_sequence(sequence):
    """Nicely print the sequence with indices"""
    print("\nFibonacci Sequence:")
    print("-----------------")
    for i, num in enumerate(sequence):
        print(f"F({i}): {num}")

def main():
    print("Fibonacci Sequence Generator")
    print("---------------------------")
    
    while True:
        try:
            n = input("\nEnter the number of terms to generate (or 'q' to quit): ")
            
            if n.lower() == 'q':
                print("Goodbye!")
                break
                
            n = int(n)
            
            if n <= 0:
                print("Please enter a positive number!")
                continue
                
            sequence = generate_fibonacci(n)
            print_sequence(sequence)
            
            print(f"\nSum of the sequence: {sum(sequence)}")
            
            if n > 1:
                # Calculate the ratio of consecutive terms (Golden Ratio approximation)
                ratio = sequence[-1] / sequence[-2] if sequence[-2] != 0 else "undefined"
                print(f"Ratio of the last two terms (Golden Ratio approximation): {ratio}")
            
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()