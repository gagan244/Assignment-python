def total_length(A, B, C):
    return A + B + C

# User inputs
A = int(input("Enter the distance by which Amit beats Suman (in meters): "))
B = int(input("Enter the distance by which Amit beats Ravi (in meters): "))
C = int(input("Enter the distance by which Suman beats Ravi (in meters): "))

# Calculate total length of the track
total_track_length = total_length(A, B, C)
print(f"Total length of the Track= {total_track_length} m")
