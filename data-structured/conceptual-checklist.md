# DSA Structured Checklist

## Arrays & Strings
- **Basic operations**
  - Traversal
  - Insertion
  - Deletion
- Two-pointer and Sliding Window techniques
- Prefix sums / cumulative array
- Subarray / Subsequence problems
- String manipulation, pattern matching

## Linked List
- Single & Doubly linked lists
- Reverse, detect cycles (Floyd's algorithm)
- Merge two sorted lists
- Linked list-based stack / queue problems

## Stacks & Queues
- Implementation using arrays / linked lists
- Monotonic stacks
- Sliding window maximum
- Circular queue / deque
- Priority queues (heaps)

## Hashing
- Hash Maps / Hash Sets
- Frequency counting
- Two-sum and similar problems
- Hash collisions & handling

## Trees & Graphs
- **Binary Trees / BST**
  - Traversals:
    - Preorder
    - Inorder
    - Postorder
  - Height, Diameter, LCA
- N-ary trees
- **Graph representations**
  - Adjacency list / matrix
- **Graph traversal**
  - BFS
  - DFS
- **Shortest path**
  - Dijkstra
  - Bellman-Ford
- **Minimum spanning trees**
  - Prim
  - Kruskal
- Topological sort
- Detect cycles, connected components

## Recursion & Backtracking
- Recursive problem solving
- Permutations, combinations, subsets
- N-Queens, Sudoku solver
- Word search / maze problem

## Dynamic Programming (DP)
- Classic problems:
  - Fibonacci
  - Knapsack
  - Coin change
  - Longest common subsequence / substring
  - Matrix chain multiplication
  - DP on trees / grids
- Memoization vs Tabulation
- State definition & transition

## Greedy Algorithms
- Interval scheduling
- Activity selection
- Minimum coins
- Optimal merges
- Huffman coding

## Sorting & Searching
- **Basic sorts**
  - Bubble
  - Insertion
  - Selection
- **Efficient sorts**
  - Merge sort
  - Quick sort
  - Heap sort
- Binary search and variations
- Search in rotated / sorted arrays

## Bit Manipulation
- AND
- OR
- XOR
- Shift operations
- Single number problem
- Subset problems
- Counting bits
- Power of two checks

## Advanced Data Structures
- Heaps / Priority Queues
- Tries
- Segment trees / Fenwick trees
- Disjoint set (Union-Find)
- Balanced BSTs (AVL, Red-Black tree)

# Data Structure Patterns

## Sliding Window
- **When to use:** Problems involving subarrays or substrings with a continuous window.
- **Common operations:**
  - Maximum / minimum sum
  - Longest substring without repeating characters
  - Subarray of size k
- **Examples**
  - Maximum sum subarray of size k
  - Longest substring with at most k distinct characters
- **Techniques**
  - Two pointers
  - Dynamic window size

## Two Pointers
- **When to use:** Problems involving arrays or linked lists where two indices move towards each other
- **Common operations:**
  - Searching
  - Sorting
  - Merging
- **Examples**
  - Two sum in a sorted array
  - Reverse a linked list in pairs
  - Remove duplicates from sorted array

## Fast & Slow Pointers
- **When to use:** Detecting cycles or middle elements in linked lists
- **Common operations:**
  - Cycle detection
  - Finding mid-points
- **Examples**
  - Detect cycle in a linked list
  - Find start of cycle
  - Find middle node

## Merge Intervals / Overlapping Interval
- **When to use:** Problems involving intervals or ranges
- **Common operations:**
  - Merge
  - Insert
  - Remove
  - Find overlaps
- **Examples**
  - Merge overlapping intervals
  - Insert intervals
  - Meeting rooms scheduling

## Top K / Heap Pattern
- **When to use:** Finding largest / smallest elements or streaming data
- **Data Structures:**
  - Min-heap
  - Max-heap
- **Examples**
  - Top K frequent elements
  - Kth largest / smallest element
  - Median of a data stream

## BFS / DFS Pattern
- **When to use:** Graph or tree traversal problems
- **Common operations:**
  - Shortest path
  - Connected components
  - Tree traversal
- **Examples**
  - Level order traversal (BFS)
  - Connected components in a graph
  - Detect cycle in graph (DFS)

## Backtracking / Recursion Pattern
- **When to use:** Problems with choices and constraints
- **Common operations:**
  - Generate combinations
  - Permutations
  - Subsets
- **Examples**
  - N-Queens
  - Sudoku solver
  - Word search

## Dynamic Programming / Memoization Pattern
- **When to use:** Overlapping subproblems and optimal substructure
- **Common operations:**
  - Count
  - Max / Min
  - Longest subsequence / subarray
- **Examples**
  - Fibonacci sequence
  - Longest Increasing Subsequence
  - 0/1 Knapsack

## Greedy Pattern
- **When to use:** Problems where local optimal choice leads to global optimum
- **Common operations:**
  - Interval scheduling
  - Selection
  - Optimization
- **Examples**
  - Activity selection problem
  - Minimum coins problem
  - Gas station / refueling problem

## Union-Find / Disjoint Set Pattern
- **When to use:** Problems involving connectivity, grouping, or cycles in graphs
- **Common operations:**
  - Connected components
  - Cycle detection
  - Kruskal's algorithm
- **Examples**
  - Number of islands
  - Detect cycle in undirected graph
  - Kruskal's MST algorithm

## Trie / Prefix Tree Pattern
- **When to use:** Problems with strings, prefixes, or dictionary matching
- **Examples**
  - Autocomplete system
  - Word search
  - Longest common prefix

## Bit Manipulation
- **When to use:** Problems involving integers and binary representation
- **Examples**
  - Single number problems
  - Count set bits
  - Subsets generation

# Trick to solve the problem 
- Understand the Problem
    - Read carefully: Ensure you understand exactly what's being asked
    - Identify input and output: Clarify the type, size and constraints of input
    - Ask clarifying question 
        - Are inputs sorted?
        - Can there be duplicates
        - Are negative number allowed
    - Example: Find the longest substring without repeating characters
        - Input : String s
        - Output: integer(length)
        - Constraints: ASCII characters, string length <= 10^5
- Identify Constraints & Edge Cases
    - Constraints often hint at time/space complexity requirements
        - Small N -> O(n2) may be fine
        - Large N -> O(NlogN) or O(N) expected
    - Edge cases to consider
        - Empty input
        - Single element
        - Maximum/Minimum values
    - Example: Empty string or string with all identical characters
- Spot the Pattern
    - Look for structural clues in the problemc:
        - Continuous elements - Sliding Window / Two pointer
        - Graph/ relationships - BFS / DFS/ Union-Find
        - Combinations/ Permutations - Backtracking / Recursion
        - Max/Min / Top-K - Heap/ Priority queue
        - Overlapping subproblems - Sliding window pattern
    - Example: Longest substring - Sliding window pattern
- Choose a suitable Data Structure/Algorithim
    - Based on the identified pattern, pick the right tools:
        - Arrays, Strings - Two pointer , sliding window
        - Trees - BFS/DFS
        - Graph - Adjacency list/ matrix, BFS/DFS
        - Frequent elements - HashMap + Heap
    - Always justify your choice in the interview
- Estimate Time & Space Complexity
    - Check if your approach fits within constraints 
    - Trade-offs: Sometimes a slightly slower but simpler solution is acceptable initially
    - Example: Sliding window - O(N) time 0(K) space
- Plan Before Coding
    - High-level steps: Explain your approach in 2-3 sentences
    - Example - I’ll use a sliding window with two pointers. Maintain a hashmap to track character frequency and expand/shrink the window to find the longest substring without repeats.
- Validate With Examples
    - Test small examples manually before coding
        - Normal case
        - Edge case
        - Large input case
- Summary
    - Understand input/output & ask clarifying questions
    - Identify constraints & edge cases
    - Spot the underlying pattern
    - Choose appropriate data structure / algorithm
    - Estimate complexity and check feasibility
    - Plan high-level approach
    - Validate with examples