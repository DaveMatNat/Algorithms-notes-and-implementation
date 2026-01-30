def min_additional_implications(n, m, implications):
    # Create a directed graph to represent the implications
    graph = {i: set() for i in range(1, n + 1)}
    in_degree = {i: 0 for i in range(1, n + 1)}

    for s1, s2 in implications:
        graph[s1].add(s2)
        in_degree[s2] += 1

    # Function to perform topological sort
    def topological_sort():
        result = []
        queue = [node for node in in_degree if in_degree[node] == 0]

        while queue:
            current_node = queue.pop(0)
            result.append(current_node)

            for neighbor in graph[current_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result

    # Perform topological sort
    top_order = topological_sort()

    # Check if there is a valid topological order
    if len(top_order) != n:
        return "impossible"

    # The minimum number of additional implications is equal to the number of nodes not covered in the topological sort
    return 0

# Read the number of test cases
num_test_cases = int(input().strip())

# Process each test case
for _ in range(num_test_cases):
    n, m = map(int, input().strip().split())
    implications = [tuple(map(int, input().strip().split())) for _ in range(m)]

    # Output the minimum number of additional implications needed for each test case
    result = min_additional_implications(n, m, implications)
    print(result)
