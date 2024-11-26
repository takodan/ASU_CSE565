
# Unit 7: Test Management - Part 1


### Learning Objectives
1. Identify the major components of a system test plan
2. Create a test schedule
3. Estimate testing effort
4. Follow a process for estimating testing effort
5. Perform risk-based testing
6. Select test exit criteria
7. Identify the different types of test documentation



## Test Planning


### Overview
1. Scope of testing (ascending order)
    1. unit testing
    2. integration testing
    3. system testing
    4. beta testing
    6. acceptance testing
2. Planning becomes more formal as the scope increases.
3. Key elements
    1. Objectives
        1. Identify what to accomplish
        2. Common objectives: functionality, usability, security, performance, etc.
        3. Testing stops when objectives are met.
    2. Dependencies and Assumptions (constraints)
        1. Dependencies: resources, environments, etc.
        2. Assumptions: "software being completed on time"
    3. Strategy
        1. Define how testing object will be met.
        2. Adopt a risk-based testing strategy to prioritize efforts.
        3. Test environment: tools, platforms, etc.
        4. Entry and exit criteria
            1. Defines conditions that must be met before the next testing.
            2. Test readiness assessment
        5. Schedule: effort estimation and resource allocation分配
        6. Risk management
            1. risks such as: delay, not functioning as expected, etc.
            2. Risk prioritization
            3. Mitigation activities
            4. Contingency plans


### Test Schedule
1. steps
    1. identify tasks
    2. analyze dependencies
    3. estimate the effort and resources
    4. assign tasks
    5. map testing tasks to a time line
2. PERT chart
    1. a type of network graph
    2. nodes represent project activities and time units
    3. links represent precedence relations先後關係
3. Critical path analysis
    1. A method for identifying the minimum time required to complete a project.
    2. It also identify critical activities and activities can be parallel.
    3. The path through the PERT chart with no slack time (gap).
    4. Example
        1. activity(start, end)
        2. A(0, 2) -> B(2, 4) and C(2, 8) -> D(8, 10)
        3. critical path: A->C->D
        4. there are slack time (gap) between B and D
4. Tips
    1. Not only should we assign work based on, but also balance efficiency with opportunities for team members to learn new skills.
    2. Allocate buffers (additional time) to account for unforeseen problems.
    3. Include testers in the planning process to ensure understanding and commitment to the schedule.
    4. Use tools like Gantt charts to visualize tasks, timelines, and resource allocations.
    5. Adjust schedules and buffers based on risk assessments.


### Estimating Testing Effort
1. Common factors affecting effort
    1. Size
    2. Complexity
    3. Scope
    4. Technology
    5. Desired Quality
    6. Process
    7. Customer Collaboration
    8. Quality of Code (Code Stability)
        1. Pass of First Attempt (POFA): The pass rate of the initial test.
2. Approach for developing test estimates
    1. historical data 
    2. a cost estimation model
    3. a percentage of the development estimate
3. Common causes of inaccurate estimates
    1. Misunderstanding requirements
    2. Overlooked忽視 tasks: like tool setup or training.
    3. Inadequate time to produce thoughtful estimates.
    4. Lack of guidelines: absence of structured approaches to estimation.
    5. No historical data
    6. External pressure: management or clients pushing to reduce estimates.
4. Generic estimation process (not only for testing)
    1. Assign responsibilities
    2. Clarify objectives, deliverables, milestones and constraints
    3. Identify tasks: account for tasks like test case development, training, and environment setup.
    4. Estimate size
        1. Define size measure
            1. number of requirements
            2. number of use cases / scenarios
            3. lines of code
            4. number of test cases
        2. Select size estimation method
            1. Top-Down
                1. Use analogies from similar projects to estimate size and effort.
                2. Relies on expert judgment and historical comparisons.
            2. Bottom-Up
                1. Break tasks into smaller components and estimate each separately.
        3. Estimate
            1. 80/20 rule
            2. Ensure size estimate are meaningful (have basis of estimate, BOE).
    5. Converting size to effort
        1. Use historical data or industry benchmarks to estimate effort based on size.
        2. Productivity metrics (e.g., lines of code per hour, test cases per day).
    6. Validation and sanity checks
        1. Compare estimates for similar components
        2. historical data
        3. expert reviews


### Risk Based Testing
1. prioritizes testing efforts based on risk exposure.
2. Risk Exposure (RE): RE = probability of an adverse event * consequences of that event
3. Likelihood of failure
    1. Errors are clustered
    2. common factors
        1. complexity
        2. recent modifications
        3. outsourced or untested code
4. Consequences of Failure
    1. Requires interaction with customer and developers.
    2. can be assessed in terms of severity levels嚴重程度
    3. techniques
        1. fault trees
        2. failure mode effect analysis
5. Strategies
    1. Test high-risk areas early
    2. Test high-risk areas thoroughly


### The review of the paper
1. Dealing with the Time Crunch in Software Testing
    1. The impacts of inadequate testing time
        1. Lack of test coverage
        2. Lack of quality
        3. Poor morale
        4. Missed expectations
    2. Strategies
        1. Prioritization approaches
            1. Mission need
            2. Stakeholder needs
            3. Risk
            4. Management directive
            5. Experience
            6. Sampling
        2. Efficiency
            1. Optimize testing
                1. Sampling methods
                2. Pareto principle: 80/20 rule
                3. Design of experiments
            2. Leverage tools
            3. Agile methods
            4. Avoid over-testing: Focus on delivering the desired quality rather than achieving perfection.
    3. Clearly communicate trade-offs to management, helping them understand the implications of reduced testing time.

2. Improving Test Efficiency through System Test Prioritization
    1. Prioritization of Requirements for Test (PORT): Four factors
        1. T1: Customer-Assigned Priority
        2. T2: Developer-Perceived Implementation Complexity
        3. T3: Fault-Proneness: Based on historical data.
        4. T4: Requirements Volatility: How often requirements have changed.
    2. Total Severity of Failures Detected (TSFD)
        1. Measures the cumulative severity of detected defects, calculated by summing the weighted severities of individual defects.
        2. severity levels: Highly 16, Medium 8, Less 4, Least 2
    3. Results show that PORT improves the detection of high-severity defects early in the process.

3. Risk-Driven Model-Based Testing of Washing Machine Software
    1. Risk-Driven Testing: Prioritizing tests based on the likelihood of defects and the severity of their potential consequences.
    2. Operational Profiles: Testing based on real-world usage patterns to better mimic actual user behavior.

### Test Exit Criteria (when to stop testing)
1. Ideal criteria is when test objectives are met.
2. Defect density
    1. Depends on historical data
    2. e.g., "3 defect per 1,000 lines of code"
3. Defect pooling
    1. Use two independent testing teams to identify defects
    2. Calculate
        1. Estimated_Total_Defects = Defects_Team_A * Defects_Team_B / Common_Defect_C
        2. Unique_Defects = Defects_Team_A + Defects_Team_B - Common_Defect
        3. Estimated_Remaining_Defect = Estimated_Total_Defects - Unique_Defects
        4. Example
            1. A = 30, B = 40, C = 20
            2. Unique_Defects = 50
            3. Estimated_Total_Defects = 60
            4. Estimated_Remaining_Defect = 10
    3. It is typically used with operational profiles.
4. Defect seeding
    1. Intentionally insert a known number of defects.
    2. Assess the detection rate and use it to estimate total defects.
    3. Example
        1. 20 seeded defects; 10 were detected; detection rate is 50%.
        2. Testers found 50 unseeded defects.
        3. Estimated total defects are 50 / 0.5 = 100
5. Trend Analysis
    1. Data collection over time provides insight into when to stop testing
    2. Common metrics
        1. Mean Time to Failure (MTTF)
            1. MTTF should increase as testing progresses and stable over time
        2. Cumulative Number of Defects
            1. Defect discovery starts rapidly and slows over time
        3. Failure Rate: Number of defects found per unit of time (CPU hours).
            1. Failure rate should decrease as testing progresses and defects are fixed.
    3. Anomalies
        1. Temporary increases in failure rate might indicate
            1. new testing phases
            2. new defect types
            3. poorly integrated changes.
        2. Persistent upward trends in failure rates could signal new defects introduced during fixes.
        3. Cumulative defects leveling out may indicate testers are running repetitive or non-creative tests.
6. No single indicator can determine when to stop testing.
7. Combine multiple data points, such as:
    1. Defect density
    2. Requirements coverage
    3. Functional coverage
    4. Trend metrics


## Test Documentation
1. Documentation is essential for Communication and Archival
2. Types of Test Documentation
    1. Test Plans
    2. Test Cases, include:
        1. Inputs and expected outputs
        2. Unique identifiers: Ensure traceability and coverage.
        3. Test Environment
        4. Inter-case dependencies: Sequence of test cases to achieve specific conditions.
        5. Special procedures: Custom setups or handling instructions.
        6. Reference
         
    2. Test Incident Reports
        1. A test failure report
        2. Focusing on repeatability: Essential to help developers replicate and fix defects.
        3. Must provide detailed and clear information for each viewer.
            1. Developers often specialize in specific modules or services.
            2. Testers must provide contextual defect reports that developers can interpret and act upon.
        4. include
            1. Identifiers
            2. Summery
            3. Incident description
            4. Impact
        5. Severity vs Priority
            1. Severity: Measures customer impact; Typically rated on a scale.
            2. Priority: Reflects project impact.
                1. A high-severity defect affecting few users might have low priority.
                2. A low-severity defect blocking testing might have high priority.
        6. some organizations have reports reviewed by another tester
            1. Completeness
            2. Repeatability
            3. Clarity
            4. Severity evaluation (not Priority)

    3. Test Summary Reports, include:
        1. Summary of what was tested
        2. Variances from the initial plan
        3. Comprehensive assessments: coverage, traceability to requirements.
        4. Summary of result
        5. Evaluation: Predict outcomes if the product is released as is.
3. In projects with regulatory compliance監管合規 or outsourcing外包, test documentation may be a formal deliverable.
4. key information about documentation
    1. Planning: Helps organize testing activities.
    2. Tracking: Monitors progress and identifies issues.
    3. Supporting Decisions: Guides release or further testing actions.
