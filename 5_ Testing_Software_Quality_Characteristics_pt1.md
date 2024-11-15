# Unit 5: Testing Software Quality Characteristics - Part 1


### Learning Objectives
1. Utilize strategies for performance testing
2. Utilize strategies for stress testing
3. Utilize strategies for volume testing
4. Utilize strategies for configuring testing
5. Generate regression tests
6. Identify approaches for mobile system testing



## Performance Testing
1. The goal is to ensure the system meets performance requirements under defined conditions.
2. Criteria:
    1. Performance requirements must be quantifiable and measurable
    2. The system must be stable enough for performance testing
    3. Testing should represent real user conditions.
    4. Realistic data sets are crucial for accurate performance testing
    5. Ensure scenarios reflect operational realities.
3. Example: Airline Reservation System
    1. Requirement:
        1. "The system should have excellent response time.": not quantified
        2. "The system should have a response time of less than one second."
    2. Further specification is necessary.
        1. Defining the response time from when a form is completed and the transmit button is pressed.
    3. Normal conditions must be defined.
        1. 100 users on the system.
        2. They are browsing or simultaneously submitting requests.
4. Load
    1. Represent different activity volumes and user behavior combinations.
    2. Testing should involve increasing the load and observing:
        1. response time
        2. resource utilization


### Stress Testing
1. Testing system's behavior when its resources are saturated and pushed beyond their limits.
2. Aim to find stress points
3. Steps:
    1. Identify Stress Points: To find potential bottlenecks in the system, such as CPU or memory.
    2. Develop a Stress Strategy
        1. Plan how to stress the system.
        2. Involve tools to simulate high loads.
    3. Verify Stress Creation: Ensure that the system is genuinely under stress by measuring resource usage
    4. Observe Behavior Under Stress: Analyzing extensive data even if the system does not crash


### Volume Testing
1. Testing with large volume of activity over an extended period of time, without turning off.
2. Potential problems:
    1. memory leaks
    2. counters overflow
    3. resource depletion



## Configuration Testing
1. Testing aims to verify functional and performance requirements across different system configurations.
2. Steps:
    1. Defining Parameters
        1. Identify parameters that could impact the system's requirements.
        2. such as different CPUs, operating systems, and memory.
    2. Sampling and Partitioning
        1. Group similar parameters to reduce the number of tests.
        2. Understand equivalent configurations.
    3. Identify configuration combination to test
        1. Boundary testing: focus on extreme configurations.
        2. Risk-based testing: test configurations used by the majority.
        3. Design of experiments: pairwise testing, etc.



## Regression Testing
1. Ensures that after code modifications, existing functional continue to work.
2. Modifying software is a high-risk activity, more error-prone than creating new code.
    1. ripple effects
    2. unintended interactions between features
3. All development levels should include regression testing.
4. Testing strategies
    1. Full regression testing
        1. Re-run all existing tests after any modification.
        2. This is ideal but often impractical.
    2. Selective regression testing
        1. Focus on tests related to the modified parts of the code.
        2. Confidence tests: Run a subset of high-level tests that cover essential functionalities.
        3. Code delta testing
            1. Track code changes (delta) using source code management tools, etc.
            2. Run tests that cover modified or affected areas.
        4. Ripple effect analysis
            1. Identify which parts of the system might be impacted by changes
            2. Focus regression testing on those areas.
5. Maintain and validate regression tests when adding new features to ensure tests remain relevant and accurate.


### The review of the paper
1. Model Based Regression Test Selection Technique
    1. Model-based software development involves representing system behavior in an executable model.
    2. Technique:
        1. Creating a model-based control flow diagram for the original and updated models.
        2. Focusing on differences to select appropriate tests.

2. Testing in O&M: Software Does Not Wear Out, It Degrades
    1. Operations and Maintenance (O&M)
    2. Verification and Validation (V&V)
    3. Traditional regression testing often focuses on identifying subsets of tests for re-execution
    4. However, testing strategies may need to adapt beyond merely rerunning existing tests.
    5. Area to be consider:
        1. Security and Privacy
        3. Hazards Introduced by System Changes
        4. Performance Needs Growth
        5. Environment and Hardware Changes

3. Developing, Verifying, and Maintaining High Quality Automated Test Scripts
    1. Software Test Code Engineering (STCE)
    2. Conceptual Steps of Testing:
        1. Setup: Prepare test cases and their environment.
        2. Execution: Run the test cases.
        3. Verification: Compare expected results with actual outcomes.
        4. Teardown: Reset the environment for the next test.
    3. Quality Assessment for Test Code:
        1. Correctness: Ensures test cases are accurate and free from defects.
        2. Effectiveness: Ensures test cases provide adequate coverage of requirements and code.
        3. Maintainability: Test code should be easy to understand and modify.

4. Mobile Applications Testing
    1. Distinctive Characteristics and Testing Implications
        1. Connectivity: Mobile apps require network access
            1. Impacting performance testing, security testing, and reliability testing.
        2. Convenience: 
            1. Relates to usability testing and the user interface.
        3. Device Diversity: The variety of hardware, operating systems, and sensors.
            1. Necessitates using emulators and simulators.
        4. Resource Constraints: Mobile devices' limited resources
            1. Require stress testing and volume testing.
        5. Context Awareness:
            1. Applications must be tested in different environments and conditions to ensure functionality.
