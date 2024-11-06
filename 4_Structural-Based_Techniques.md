# Unit 4: Structural-Based Techniques
### Learning Objectives
1. Develop test cases to achieve control flow coverage
2. Apply structured testing technique
3. Develop test cases to achieve data flow coverage
4. Identify static analysis techniques
5. Utilize symbolic execution

## Dynamic Analysis
### Control Flow Testing
1. It is a lower-level form of testing.

2. Control Flow Code Coverage
    1. Challenges
        1. Undocumented Requirements
        2. Dead Code: Code that cannot be executed
        3. Incomplete Test Cases
    2. Coverage Levels: vary in strength and effectiveness.
        1. Statement Coverage: Every statement is executed at least once.
        2. Decision Coverage: Also known as branch coverage; tests all possible decision outcomes.
        3. Decision Condition Coverage: Tests each condition in a decision.
        4. Multiple Condition Coverage: Tests all possible combinations of conditions.
    3. Control Flow Graph/diagram (CFG)
        1. The ovals橢圓 represent the statements
        2. The diamonds are referred to as test predicates測試謂詞, like `if x < 10`, `if y > 0`

3. Statement Coverage
    1. Every statement is executed at least once.
    2. Steps:
        1. Draw a CFG to represent the code logic, including statements and decisions.
        2. Analyze the CFG to determine the number of test cases.
        3. Achieve 100% statement coverage.
    3. The most basic level of coverage and is often the initial testing goal.

4. Decision Coverage
    1. Each branch of decision points is traversed at least once but not necessarily all combinations.
    2. Statement and Decision Coverage
        1. Decision coverage implies statement coverage: traversing all branches leads to executing all statements.
        2. Statement coverage does "not" guarantee decision coverage: there could be a branch without a statement.
    3. Decision Coverage is stronger than Statement Coverage.
    4. Decision Condition Coverage
        1. one test predicate may contains multiple conditions
        2. Each condition in a test predicate (Decision) takes on all possible outcomes at least once.
        3. Example:
            1. `if X>1 or Y<1 and Z=0`
            2. test cases should cover all three condition at least once.
        4. Not going through all combinations, only each of them.
    5. Multiple Condition Coverage
        1. All possible combinations of conditions in a decision are executed at least once
        2. Example
            1. `if X>1 or Y<1`
            2. test cases: (T, T), (T, F), (F, T), (F, F)
            3. 2^2 = 4 combinations to test
   
5. Control Flow Testing Summary:
    1. Coverage Level: Multiple Condition Coverage > Decision/Condition Coverage > Decision Coverage > Statement Coverage
    2. Statement Coverage: Every statement is executed at least once.
    3. Decision Coverage: Every decision's branches are executed.
    4. Decision Condition Coverage Every condition within decisions is tested.
    5. Multiple Condition Coverage: All combinations of condition outcomes in decisions are tested.
    6. Most software development standards advocate for at least 100% decision and statement coverage during unit testing.


### Structured Testing
1. Cyclomatic Complexity
    1. a metric for measuring the complexity of a control flow.
    2. `V(G)=E−N+2P`
        1. E: edges
        2. N: nodes
        3. P: connected components, usually 1 in program graphs.
    3. In practice, the program's complexity simplifies to `test predicates + 1`

2. High cyclomatic complexity correlates with
    1. Increased number of defects
    2. Longer time to understand and modify

3. Basis Paths
    1. Structured testing uses cyclomatic complexity to identify a subset of paths called basis paths.
    2. The number of basis paths equals the cyclomatic complexity of the program.
    3. Basis paths are selected so that any other path is a linear combination of these paths.
    4. Selecting Basis Paths
        1. Start with an arbitrary path through the graph (preferably a longer one).
        2. Flip the first condition (from true to false or vice versa) while keeping others constant to create a new basis path
        3. Repeat the process for each condition


### Data Flow Testing
1. Annotate Control Flow Graph
    1. def(i): variables defined at node i
    2. C-use(i): variables used in computations at node i
    3. P-use(i): variables used in predicate at node i

2. Annotate Example
    ```
    #1  Get x, z; 
    #1  y := 0; 
    #I  If x > 10 
    #2    then y := 15; 
    #II If z > 0
    #3    then w := y+1;
    #4    else w := y-1;
    ```
    1. def(i)
        1. def(1) = {x, y, z}
        2. def(2) = {y}
        3. def(3) = {w}
        4. def(4) = {w}
    2. C-use(i)
        1. C-use(1) = {}
        2. C-use(2) = {}
        3. C-use(3) = {y}
        4. C-use(4) = {y}
    3. P-use(i)
        1. P-use(I) = {x}
        2. P-use(II) = {z}

3. Definition Clear Path
    1. for a variable `x`
    2. a path from node `i` (where `x` is defined) to node `j` (where `x` is used)
    3. no redefinition of `x` along the path
    4. variables maintain their defined values until they are used

4. Definition Use Coverage
    1. test cases that cover all definition use paths
    2. definition use paths: same as definition clear paths


### The review of the paper: Test Automation Not Just for Test Execution
1. Key Elements of the Testing Process
    1. Test Case Design
        1. Defines test strategies such as black-box testing, equivalence partitioning, boundary values, cause-effect testing, etc.
        2. Involves finite state machine testing strategies that cover testing every state and transition.
        3. Can be performed manually or automated.
    2. Test Scripting
        1. Includes detailed steps and actions like clicking and data entry.
        2. Can be manually scripted or generated with tools.
    3. Test Execution and Result Evaluation:
        1. After running the test scripts, outputs must be examined to determine if the tests passed or failed.
        2. Involves the test oracle issue, which relates to determining the correctness of test results.



## Static Analysis
1. Analyzing the program without execution
2. Focuses on where variables or are defined and used (Data Flow Testing).
3. Data Flow Anomalies Examples
    1. Variable redefinition without reference (being used)
    2. Referencing undefined variables
    3. Variables defined but never used
4. Challenges
    1. Dynamic Data Structures
    2. Loops and Iterations
5. Huang's Theorem
    1. For sets A, B, C of character sequences (with minimal length of one character), and a two-character string T
    2. If T is a substring of A b^n C, then T will appear in A B^2 C
    3. It's sufficient to consider up to two iterations of a loop when searching for anomalies


### Symbolic Execution
1. Analyze programs by tracking symbolic values rather than concrete data inputs.
2. Example: one path
    ```
    #0 input A, B
    #1 A := A + B
    #2 C = A + B
    ```
    1. #0
        1. A0 = defined
        2. B0 = defined
        3. C0 = undefined
    2. #1
        1. A1 = A0+B0
        2. B1 = B0
        3. C1 = C0 = undefined
    3. #2
        1. A2 = A1 = A0+B0
        2. B2 = B1 = B0
        3. C2 = A2+B2 = A1+B1 = A0+B0+B0
3. The goal of symbolic execution is to identify the inputs needed to execute specific paths.
4. These inputs are represented as symbolic path conditions.
5. Example: multiple paths
    ```
    #0 if (x<0) or (y<0)
    #1    then x = x^2, y = y^2
    #2 if (x<1) or (y<)
    #3    then x = x+1, y = y+1
    ```
    1. True True Path
        1. #0 (X0<0) or (Y0<0)
        2. #1 X1 = X0^2, Y1 = Y0^2
        3. #2 (X1<1) or (Y1<1)
        4. [(X0<0) or (Y0<0)] and [(X0^2<1) or (Y0^2<1)]
6. Applications
    1. Analyze the final state of program variables, which helps in program verification.
    2. Generate test data or determine if a path is feasible.
7. Challenges
    1. Combinatorial Explosion
    2. Loop Handling
    3. Complex Structures

### The review of the paper: DevOps Advantages for Testing
1. Development ops (DevOps) emphasizes collaboration and integration among everyone involved in the software lifecycle.
2. Continuous Delivery and Continuous Integration
    1. Continuous Delivery (CD)
        1. Involves the release of software multiple times a day
        2. Requiring a well-structured pipeline
    2. Continuous Integration (CI)
        1. New code is continuously integrated into builds.
        2. Triggering automated tests for immediate feedback.
3. Automated testing
    1. Crucial to detect issues early and minimize rework
    2. start with less costly and progress to more complex tests
4. Critical Testing Techniques
    1. Unit Testing and Code Coverage
    2. Mutation Testing
    3. Static Analysis: Low-cost and early detection
    4. Sunny Day and Rainy Day Testing: Normal conditions and edge cases
5. Optimizing the Pipeline
    1. Long-running tests, such as performance tests, should run in parallel.
    2. Early exploratory tests can determine if more in-depth testing is warranted.