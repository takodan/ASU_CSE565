# Unit 8: Test Management - Part 2


### Learning Objectives
1. Utilize various measures to track testing progress
2. Identify how to analyze and improve the testing process
3. Develop a plan for outsourcing testing
4. Apply best practices for maximizing test team performance
5. Plan and participate in various work product inspections
6. Apply causal analysis to improve test effectiveness
7. Assess the maturity level of a testing organization



## Test Tracking
1. Two aspects
    1. Progress Tracking
    2. Quality Tracking: reaching exit criteria
2. Progress measures
    1. percentage of tests developed
    2. percentage of tests executed
    3. percentage of requirements tested
3. Earned Values
    1. Tracks progress by assigning relative values (e.g., time) to tasks based on estimated effort.
    2. Key metrics
        1. Budgeted Cost of Work Scheduled (BCWS) 預期會花費的成本
        2. Budgeted Cost of Work Performed (BCWP) 依據實際完成的工作所計算的預期成本
        3. Actual Cost of Work Performed (ACWP) 實際花費的成本



## Test Process Improvement
1. Understand the Current Process: "If you don't know where you are, a map won't help"
    1. Perceived Process: What people think they do.
    2. Official Process: What is documented.
    3. Actual Process: What is really done, observed through practice.
2. Analyze the Current Process (Actual Process): "You cannot control what you cannot measure"
    1. Identify what works, what doesn’t, and sources of variability.
    2. Use data and metrics for objective analysis.
3. Characterize the Target Process
    1. GQM (goal, question, metric) Paradigm
        1. Define the goals of the measurement process.
        2. Derive questions that must be answered to meet the goals.
        3. Develop metrics to answer the questions.
    2. Example
        1. Goals: Reduce testing time by 50%.
        2. Questions: Where is most testing time spent?
        3. Metrics: Time spent on scripting.
4. Redesign the Process
    1. Post-Mortems / Lessons Learned / Retrospectives
        1. Identify what worked
        2. Identify problems and areas for improvement.
    2. Causal Analysis
5. Implement and Iterate


### The review of the paper
1. Enhancing Defect Tracking Systems to Facilitate Software Quality Improvement
    1. Questions for test process improvement
        1. What are the main defect types?
        2. What can the company do to prevent defects in a project’s early stages?
        3. What are the reasons for the actual defect-fixing effort?
        4. What can the company do to detect defects before the new software release reaches customers?
        5. Which testing activities discovered or reproduced the most defects?
2. Evaluating a Corpus of Root Causes and Measures to guide RCA Processes in Critical Software
    1. Orthogonal Defect Classification (ODC)
        1. A structured approach to defect analytics.
        2. Classify defects by type, timing, severity, and testing phase.
    2. Analytics Process
        1. Data Collection
        2. Defect Classification
        3. Root Cause Identification, e.g.
            1. Lack of traceability.
            2. Inadequate tools or test environments.
            3. Incomplete tests or plans.
        4. Improvement Recommendations
    3. Recommended V&V (Verification & Validation) Measures
        1. Develop detailed test plans and strategies (focus on unit and integration testing).
        2. Ensure automated traceability analysis to prevent gaps in requirements tracking.
        3. Improve test completeness, coverage, and review rigor.
        4. Implement non-functional tests for fault detection, injection, and recovery.
        5. Apply tools for design and implementation compliance.


### Causal Analysis
1. Identifying the root causes of defects and preventing future occurrences to enhance test effectiveness.
2. Steps
    1. Collect Defect Data
    2. Analyze Defects
        1. Identify probable causes.
        2. Look for patterns or clusters among defects.
        3. "Five Whys" Method: Repeatedly ask "Why?" to drill down to the root cause
    3. Categorize Root Causes
        1. Use tools like the Ishikawa (Fishbone) Diagram.
    4. Identify Solutions
3. Common root cause categories and strategies for elimination
    1. Communication Issues
        1. Improve tracking systems and notification tools.
    2. Oversight
        1. Implement checklists, peer reviews, and automation.
    3. Education gaps
        1. Provide training and mentoring.
    4. Transcription errors
        1. Automate comparisons to reduce human errors.



## Test Outsourcing
1. Decision Factors
    1. Cost
    2. Speed
    3. Expertise
    4. Strategic Value
    5. Maintenance
2. Define the objects/plan
    1. Determine which testing activities to outsource.
    2. Minimize dependencies.
    3. Ensuring knowledge transfer for maintenance.
    4. Statement of work
        1. Specify tasks, technical requirements, processes and responsibility.
        2. Identify
    5. Risk management
    6. Estimate resources
3. Select Contractors base on plan
    1. Specifying legal terms of contract
    2. Negotiating
4. Monitor Progress
    1. Regularly review metrics, such as test case execution and defect tracking.
    2. Maintain visibility into testing activities.
    3. Ensure clear communication channels.
    4. Validate milestones
5. Acceptance驗收
    1. Deliverables
        1. Test results, including passed and failed cases.
        2. Defect reports.
    2. Accept the work only if convinced that it meets requirements and quality standards.



## People Management
1. Key Factors for Teams
    1. People: ability, experience and motivation
    2. Processes
    3. Technology
2. Team Leader
    1. Responsibilities
        1. Negotiating for resources and schedules.
        2. Establishing team priorities.
        3. Managing and motivating the team.
    2. Skills
        1. Leadership
        2. Communication
        3. Delegation分工能力
        4. Problem solving
        5. Negotiation
    3. Goals:
        1. Build cohesive teams.
        2. Foster trust and collaboration.
        3. Motivate individuals to work toward shared objectives.
        4. achieving project success.
3. Motivators
    1. Fair rewards including recognition and technical growth.
    2. Pride in accomplishments.
    3. Early successes to build confidence.
4. De-motivators
    1. Lack of resources.
    2. Unclear goals or expectations.
    3. Perceived unfairness.
5. Characteristics of effective teams
    1. Members help each other.
    2. Comfortable interactions.
    3. Quick conflict resolution.
    4. Shared commitment and pride in work.
    5. Use of "we" rather than "I" in discussions.
    6. Leadership viewed as coaching.
    7. Members understand their roles and Responsibilities.
    8. Teams believes thar it will be success.



## Test Inspections/Review
1. Formal method with preparation, checklists, and statistical data collection.
2. Inspections including
    1. Test plans
    2. Test cases
    3. Incident reports
3. Checklists
    1. Ensure consistency and thoroughness.
    2. Examples: Requirements
        1. testability
        2. completeness
        3. correct
        4. consistency
        5. clarity
    3. Examples: Test plans
        1. objectives
        2. strategies
        3. schedules
        4. environments
    4. Examples: Test cases
        1. repeatable
        2. inputs, expected results
        3. environments


## Test Maturity Model
1. Test Maturity Model Integration (TMMI)
    1. TMMI builds on the Capability Maturity Model Integration (CMMI)
    2. CMMI assesses the maturity of software development organizations.
    3. CMMI is originally used by federal agencies to assess software organizations bidding for contracts.
2. Maturity Levels in CMMI and TMMI
    1. Level 1: Initial
        1. Process unpredictable, poorly controlled and reactive.
        2. No defined methodology or tools.
        3. TMMI: Testing is not a priority and begins after code code is written.
    2. Level 2: Managed (TMMI: Phase Definition)
        1. Expertise lies on individuals.
        2. TMMI: Introduction of testing phases and basic testing methods.
        3. TMMI: Goals are defined.
    3. Level 3: Defined (TMMI: Integration)
        1. Processes are documented and standardized
        2. TMMI: Testing integrated into the development process.
        3. TMMI: Testing progress is tracked, and risk management is introduced.
    4. Level 4: Quantitatively Managed (TMMI: Managed and Measured)
        1. Uses metrics to guide process and decision-making
        2. TMMI metrics examples: Defect containment rate, defect leakage rate.
    5. Level 5: Optimizing
        1. Focus on continuous improvement.
        2. TMMI: Uses advanced techniques like root cause analysis and statistical monitoring.