# Unit 2: Specification-Based Techniques - Part 1


### Learning Objectives
1. Contrast requirement-based versus scenario-based testing
2. Apply the equivalence partitioning testing technique
3. Apply cause-effect testing technique
4. Test asynchronous events
5. Apply state-based testing technique
6. Describe model-based testing strategies




## Input Sampling Techniques
1. Black-box Testing
    1. Tests the system's functionality without looking at internal code logic.
    2. Suitable for all testing levels (integration, component, service, etc.).
    3. The key idea is test the system as if you were the end-user.
2. Requirements-based Testing (Static)
    1. Develops test cases directly from requirements (e.g., specs, user manuals).
    2. Focuses on traceability: every requirement must map to at least one test case.
    3. Each test cases often cover multiple requirements.
    4. Example: In an ATM system:
        1. Card insertion, PIN validation, cash withdrawal are all requirements.
        2. Number the requirements as 1.0, 1.1, 1.2, etc., and design tests to cover each one.
        3. Test cases verify that these requirements are executed properly.
        4. One test can validate multiple requirements, and several tests may address the same requirement.
3. Scenario-based Testing (Behavioral)
    1. Focuses on system behavior and responses to inputs.
    2. Test cases are based on use-cases that describe normal and alternative scenarios.
    3. Addresses both verification and validation
    4. Example compare to Requirements-based Testing: packing bags for a trip
        1. Requirements-based
            1. You make a list of items to pack and verify they are all packed.
            2. You might forget to add something to the checklist.
        2. Scenario-based
            1. You think about the activities on your trip and pack based on those scenarios.
            2. Ensures you don't miss anything by considering real-world use cases.
    5. Use-cases construction
        1. Identify the actors (people or sub-systems)
        2. Identify how each actor uses the system (use-case)
        3. Detail each use-case


### The review of the paper: An introduction to Scenario Testing
1. Key characteristics of a good scenario test
    1. Story-driven: Focuses on a customer's goals and behaviors.
    2. Motivating: Adds value and demonstrates usefulness to the customer.
    3. Credible: Based on realistic situations.
    4. Reasonably complex: Involves both simple and complex scenarios.
    5. Easy to evaluate: Clear pass/fail criteria. 
2. Differences between testers and requirements analysts
    1. Requirements analysts work with customers to ensuring that all parties agree on the system’s functionality.
    2. Testers focus on finding gaps or missing requirements.
        1. exploit potential disagreements
        2. don’t make decisions about how the system should work
        3. highlight potential issues or unintended consequences
3. Twelve Ways to Create Good Scenarios
    1. Write life histories for objects: Track an object’s lifecycle (e.g., insurance policy) through different events.
    2. List possible users: Identify users and analyze their goals (e.g., minimizing losses).
    3. Consider disfavored users: Think about how malicious users might exploit the system.
    4. List system events: Identify how the system handles key events.
    5. List special events: Focus on rare events that need special handling (e.g., year-end processes).
    6. List benefits and create tasks: Ensure the system delivers its intended benefits with end-to-end testing.
    7. Interview users about past challenges: Learn from users’ experiences with older systems.
    8. Work alongside users: Observe users to understand real-world use.
    9. Research similar systems: Study documentation about similar systems for insights.
    10. Study complaints: Analyze user complaints from previous systems to find potential issues.
    11. Create a mock business: Simulate real-world use by creating a mock business scenario.
    12. Convert real-life data: Test the system using actual data from previous or competing products.


### Equivalence Partitioning Testing
1. Definition
    1. A technique to divide the input domain of a program into a finite有限 number of partitions (both valid and invalid).
    2. Allows you to test a representative value from each partition, assuming the program will behave the same for all values in that partition.
2. Steps in Equivalence Partitioning
    1. Identify equivalence partitions for each input (valid and invalid).
    2. Write test cases covering as many valid partitions as possible.
    3. For invalid partitions, create test cases that cover only one invalid condition at a time.
        1. Isolate errors: It avoids uncertainty about which invalid condition caused the failure
        2. Clear feedback: Testing one invalid condition provides clearer error messages
3. Example: A program accepting two inputs (X: 1-10, Y: 50-100)
    1. Identify equivalence partitions
        1. Valid partitions: X (1-10), Y (50-100).
        2. Invalid partitions: X (<1, >10), Y (<50, >100).
    2. Write test cases
        1. Select values like (5, 55) for valid
        2. handle invalid inputs one at a time, like (-3, 60).
    3. create test cases that cover only one invalid condition at a time
        1. don't write a test case like (-3, 45)
4. Assumptions
    1. This method assumes inputs are independent of each other. 
    2. It does not handle combinations of dependent inputs.


### Boundary Value Testing
1. Definition
    1. Selecting test cases on, above, and below the edges of input and output equivalence partitions.
2. Example: Password Length
    1. the valid password length is 6 to 10
    2. Equivalence Partitioning: Test values within and outside this range (<6, 6-10, >10).
    3. Boundary Value Testing:
        1. Test values on the boundary (6, 10), and just below/above (5, 7, 9, 11).
        2. In practice, values within the valid range (7, 9) are usually skipped.
3. It’s also important to test output boundaries
    1. Exact boundary testing can be difficult (e.g., tweaking inputs to hit exactly output)
    2. In some cases, inspecting the code may be a more effective way to confirm boundary behavior.


### The review of the paper: Equivalence Class Partitioning and Boundary Value Analysis - A Review
1. The main limitation is that black-box testing does not provide code coverage (white-box do cover).
2. types of Equivalence Partitioning
    1. Uni-dimensional(單維度的) Equivalence Partitioning: testing a single, independent variable
    2. Multi-dimensional Equivalence Partitioning: testing combinations of dependent variables (e.g., (X, Y, Z))
    3. Weak Robust Equivalence Class Testing: Tests one invalid input at a time
    4. Strong Robust Equivalence Class Testing: Tests combinations of invalid inputs to find additional errors
3. Boundary Value Analysis
    1. internal boundaries: such as word size or data structure limits
    2. Variations of Boundary Value Testing
        1. Robust Testing: Tests individual boundary values separately.
        2. Worst-Case Testing: Tests combinations of boundary values across multiple variables.


### Cause Effect Analysis
1. Example: Customers and an Order Program
    1. Equivalence Partitioning alone is insufficient because customer type and order amount are dependent on each other.
    2. The combinations of customer type and order amount must be tested together.
2. Cause Effect Testing
    1. Test the combinations of inputs
    1. Techniques
        1. Decision Tables: Lists all possible combinations of inputs and their corresponding outputs.
        2. Decision Trees: A graphical representation showing how decisions flow based on different inputs.
3. Combinatorial Explosion
    1. In more complex cases with many input variables, the number of combinations can grow exponentially.
    2. Strategies
        1. Simplifying partitions: Reduce the number of equivalence classes for each input by look inside the box.
        2. Reducing dependencies: Test only necessary combinations of inputs.
4. Invalid Inputs
    1. Introducing invalid inputs increases the number of test cases.
    2. The goal is to find a balance between complete coverage and reducing test cases by making reasonable assumptions about error handling.
    3. For example, assuming that the validation of customer type and order amount are independent.


### Testing Asynchronous Events
1. External events that can occur at any point during the system's operation.
2. e.g., power failures, messages, errors.
3. The timeline helps visualize when events occur, and testers can use it to identify test cases for each event point.
4. Example: ATM System
    1. The timeline lays out key steps of this transaction
    2. insert card, enter PIN, request withdrawal, etc.
    3. asynchronous events (like a power failure) can be tested at different points
    4. "What if the power fails while dispensing cash?".
    5. If a power failure happens before the ATM dispenses cash, the system should return the customer’s card and not debit the account.
5. Timelines also help with validation of the system.


### State-Based Testing
1. State machines represent different system states and events that cause transitions between these states.
2. States and events are represented in either tabular or UML diagrams.
3. Example: ATM System
    1. states like idle, card insertion, and pin entry
    2. events like entering a stolen card, a valid card, or a bad pin
    3. trying a pin three times are different states
4. Testing State Machines
    1. Ensure that every state and event combination is accounted for, especially when things get complicated.
        1. contradictions矛盾
        2. unreachable states
        3. dead states (states with no transitions)
    2. Ensure that testing covers each state and transition (a minimal state machine cover).
5. Testing steps
    1. Develop a state testing tree
        1. The tree starts at the root (initial state).
        2. Expanding by testing each transition to reach new states.
    2. Identify test sequences
        1. Test sequences are paths through the tree.
        2. Ensuring all states and transitions are covered.
    3. Develop Tests
        1. Test every state and each transition from those states (test sequences).


### Model-Based Testing
1. Model-Based Software Development
    1. UML (Unified Modeling Language) and various state-based models are commonly used to create models.
    2. The goal is generating code directly from the model.
2. Model-Based Testing leverages the same model to automatically generate and execute tests
3. Steps
    1. Create a system model: most challenging and expertise-driven step.
    2. Select test generation criteria: define the type of tests needed based on the model (e.g., EP or BV).
    3. Generate tests
    4. Execute tests
4. Advantages
    1. Precision and reduced ambiguity歧義
    2. Automated test generation
    3. Ease of handling changes


### The review of the paper: Model-Based Testing
1. Definition
    1. Test cases are automatically generated from models of the system or its environment.
    2. The goal is to create a executable model of the system.
2. Generations of Model-Based Testing
    1. First Generation
        1. The model is created by the requirements analysts or developers similar to software model.
        2. Tests are generated based on specific criteria (e.g., covering all states and transitions in a state machine).
    2. Second Generation
        1. Testers create an independent test model.
        2. It allows independent validation by testers, enhancing testing accuracy.
3. Challenges
    1. Tool costs
    2. Adaptation and rollout costs
    3. Model maintenance