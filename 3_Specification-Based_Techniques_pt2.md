# Unit 3: Specification-Based Techniques - Part 2
### Learning Objectives+
1. Apply combinatorial test coverage to assess test quality
2. Apply design of experiments to develop tests
3. Understand mutation testing
4. Understand fuzz testing
5. Understand metamorphic testing
6. Apply defect-based testing techniques
7. Describe the role of exploratory testing

## Combinatorial Testing Techniques as an Aspect of Test Quality
1. Test Assessment Methods
    1. combinatorial coverage
    2. code coverage
    3. mutation testing
2. Combinatorial Testing Example
    1. parameter: variable A, B, and C. Each variable has value 0 and 1.
    2. 2 way coverage
        1. all the possible combinations of any two parameters (total of 12).
            1. (A, B): (0, 0), (0, 1), (1, 0), (1, 1)
            2. (A, C): (0, 0), (0, 1), (1, 0), (1, 1)
            3. (B, C): (0, 0), (0, 1), (1, 0), (1, 1)
        2. test case: (A, B, C): (0, 0, 0), (1, 1, 1), (1, 0, 0)
        3. coverage: 8 out of 12
            1. case (0, 0, 0)
                1. (A, B): (0, 0)
                2. (A, C): (0, 0)
                3. (B, C): (0, 0)
            2. case (1, 1, 1)
                1. (A, B): (1, 1)
                2. (A, C): (1, 1)
                3. (B, C): (1, 1)
            3. case (1, 0, 0)
                1. (A, B): (1, 0)
                2. (A, C): (1, 0)
                3. (B, C): (0, 0)
    3. 3 way coverage
        1. all the possible combinations of any two parameters (total of 8).
            1. (A, B, C): (0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1)...
        2. test case: (A, B, C): (0, 0, 0), (1, 1, 1), (1, 0, 0)
        3. coverage: 3 out of 8

### Design of Experiments
1. Many factors can impact the results of an experiment. The goal of Design of Experiments is improve efficiency and reduce costs.
2. Types of Experimental Design
    1. Full Factorial Design: Test for every factor value combinations
        1. similar to "complete decision table"
    2. Fractional Factorial Design: Only a subset of combinations are address.
        2. e.g., Pairwise test
3. Example: Cooking Pizza
    1. P1: Cooking time(10, 15, 20)
    2. P2: Rack position(low, hight)
    3. P3: Temperature(350, 400)
    4. Full Factorial: total of 3x3x2=18
    5. Pairwise Test:
        1. combination of P1 and P2: (10, low), (10, hight), (15, low), (15, hight), (20, low), (20, hight)
        2. add P3: (10, low, 350), (10, hight, 400), (15, low, 400), (15, hight, 350), (20, low, 350), (20, hight, 400)


### The review of the paper: Combinatorial Coverage as an Aspect of Test Quality
1. Combinatorial Coverage: Assesses test quality through parameter combinations analysis, no test execution needed.
2. Testing a few key parameter combinations can catch most errors
3. 2-3 parameter combinations can detect up to 99% of faults.


## Mutation Testing
1. Even if all tests pass, poor-quality tests might miss defects.
2. Mutation Testing: testing test case by inject errors (mutants) to the program.
3. Mutation Testing Process:
    1. Introduce Mutants
        1. Modify Boolean expressions, variables, arithmetic operations, etc.
        2. Ensure the mutated program can still run without compile errors.
    2. Run Tests
    3. If test cases detect mutants, they’re considered effective.
4. Assumptions:
    1. Competent Programmer Hypothesis: Programmers generally write code close to correct
    2. Coupling Effect: Tests that catch small errors may also detect complex defects.

### The review of the paper: Mutation Testing
1. Equivalent Mutants: mutants that do not affect functionality.
2. Challenges
    1. High time and computational cost
    2. Managing equivalent mutants
2. Guidelines for Effective Mutation Testing
    1. Use tools with cost reduction techniques and relevant mutation operators.
    2. Focus mutation testing on critical areas if full coverage is impractical.

## Fuzz Testing
1. Using random, invalid, or unexpected inputs to identify vulnerabilities.
2. It's looking for system crashes or unusual behavior without relying on specific expected results.
3. Methods:
    1. Mutation-Based: Starts with valid test data ("seed") and introduces random mutations (e.g., modifying strings, numbers).
    2. Generation-Based: Generates random data based on input format specifications, requiring syntax knowledge to create abnormal scenarios.
4. Limitations
    1. Non-Exhaustive Testing: Fuzz testing can’t cover all possible inputs.
    2. Coverage Constraints: Achieving thorough coverage is challenging.
    3. It doesn’t guarantee correct system behavior if no crash occurs.


## Metamorphic Testing
1. In complex applications, defining exact expected outcomes is challenging.
2. Metamorphic Properties
    1. Assumes relationships between inputs and outputs.
    2. By modifying inputs in known ways, testers can predict expected changes in outputs.
    3. Example
        1. input x, output f(x)
        2. input P(x), output f(P(x))
3. The review of the paper: Metamorphic Runtime Checking of Applications Without Test Oracles
    1. Traditionally, metamorphic testing applies at the program or system level.
    2. This paper demonstrates applying metamorphic testing at finer levels (e.g., subsystems, components, or functions) yielding more precise results.


## Defect Based Testing
1. https://cwe.mitre.org/data/definitions/699.html
2. Organize defects into categories to guide test case design.
3. Test cases are derived to detect particular defects
4. Process
    1. Choose a defect taxonomy
    2. Develop test cases for targeted defects
    3. Execute tests
    4. Evaluate results


## Exploratory Testing
1. Dynamically create test cases based on system behavior and previous results.
2. It's flexible, adaptive and not pre-defined, but still structured.
3. There is potential to detect errors missed by scripted/planed tests.
4. Session Based Testing 
    1. To conduct a test on a charter/tour over a period of time
    2. Common Types of Tours
        1. Requirements: Focuses on reviewing and validating product documentation.
        2. Complexity or Criticality: Targets complex or critical system features.
        3. Continuous Use: Tests system stability over extended use.
        4. Feature
        5. Inter-operability: Examines interactions with third-party systems.
        6. Scenario: Follows typical user scenarios end-to-end.
        7. Variability: Tests different configurations and customizations.
    3. Generate a report at the end