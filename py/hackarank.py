def find(arr):
    unique_score = set(arr)  # Convert to set to remove duplicates
    unique_score.remove(max(unique_score))  # Remove the maximum score
    runner_up = max(unique_score)  # Find the new maximum (runner-up)
    return runner_up

if __name__ == '__main__':
    n = int(input())  # Input for the size of the array
    score = list(map(int, input().split()))  # Input the array elements
    result = find(score)  # Call the function
    print(result)  # Print the result
