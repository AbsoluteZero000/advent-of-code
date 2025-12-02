import sys

def mathematical_solution(filename):
    """Simplified mathematical approach"""
    current = 50
    zero_counter = 0

    with open(filename) as file:
        for line in file:
            direction = line[0]
            distance = int(line[1:])
            start = current

            if direction == "R":
                current += distance
                # Count zeros during right rotation
                zeros_during = (start + distance) // 100
                zero_counter += zeros_during
            else:
                current -= distance
                # Count zeros during left rotation
                if start > 0 and current < 0:
                    zero_counter += 1  # Cross zero once
                    zero_counter += (-current - 1) // 100  # Additional cycles
                elif current < 0:
                    zero_counter += (-current + 99) // 100  # Only full cycles

            # Normalize current to 0-99 range
            current = current % 100

            # Check if ends at 0 (avoid double-counting)
            if current == 0:
                # Don't count if we already counted this zero during rotation
                if not ((direction == "R" and (start + distance) % 100 == 0) or
                        (direction == "L" and start > 0 and start - distance < 0)):
                    zero_counter += 1

    return zero_counter

if "__main__" == __name__:
    if len(sys.argv) < 2:
        print("Please enter the file name as in python3 main.py 'file_name'")
        exit()

    try:
        file = open(sys.argv[1])

    except Exception as e:
        print(e)
        exit()

    current = 50

    zero_counter = 0

    for line in file:
        direction = line[0]
        distance = int(line[1:])
        
        for step in range(distance):
            if direction == "R":
                current = (current + 1) % 100
            else:
                current = (current - 1) % 100
            
            if current == 0:
                zero_counter += 1

    print("the count of zeros is ", zero_counter)
    
    # Optional: Compare with mathematical approach
    math_result = mathematical_solution(sys.argv[1])
    print(f"Mathematical approach result: {math_result}")

