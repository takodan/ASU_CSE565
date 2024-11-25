# Unit 6: Testing Software Quality Characteristics - Part 2


### Learning Objectives
1. Develop error detection, recovery and serviceability tests
2. Generate usability tests
3. Identify how software reliability models work
4. Apply operational profile testing to assess software reliability
5. Identify basic security testing approaches



## Error Detection, Recovery and Serviceability Testing
1. Ability to detect and recover from defects, include
    1. user errors
    2. hardware 
    3. software
    4. other system
2. Testing by inject failures and confirm the system's detection and recovery capabilities.
3. Approach
    1. Develop a list of anticipated errors
    2. Create testing scenarios
4. Serviceability Testing: Ensure that serviceability requirements are met, include
    1. problem reporting  
    2. problem isolation
    3. problem correction
    4. problem verification
    5. fix release
5. Challenges
    1. The complexity of designing tests to inject failures.
    2. Observing system performance under failure conditions.



## Usability Testing
1. Usability
    1. The ability to perform tasks the product is meant to support in intended environment.
    2. Satisfied by the procedures.
    3. Protected from consequences of their action (e.g. delete a file).
2. Usability requirement aspect
    1. learnability: time and effort
    2. memorability: retain skills
    3. efficiency: speed
    4. errors: the number of incorrect actions
    5. satisfaction: overall feeling
3. Address reliability and validity in usability tests.
4. Evaluation
    1. Formative evaluation: Conducted early in the project to refine designs.
    2. Summative evaluation: Conducted at the end to validate usability goals.
5. Strategies
    1. Pilot Test: Test early prototypes.
    2. Identify representative users.
    3. To differentiate between various user groups (e.g. novice初學者 and expert).
6. Ethical aspects with human subjects
    1. Ensure comfort and privacy for participants.
    2. Testers should emphasize that it’s the system, not the user, being evaluated.
7. Think aloud protocol
    1. Ask test subject continuously thinking out loud.
    2. Testers may need periodically prompt test subject.



## Reliability Testing
1. Reliability: Probability that a system functions without failure for a specified time or number of natural units (e.g. 1 failed per 100 call) in a specific environment.
2. Availability:
    1. Probability that a system functions satisfactorily at any given time in a specific environment.
    2. Mean time to failure / (mean time to failure plus mean time to repair)
    3. Systems achieving five nines availability (99.999%) translate to about five minutes of allowable downtime per year.
3. Fault prevention and Fault tolerance
4. Redundancy for Fault tolerance Example
    1. Hardware redundancy: Multiple hardware
    2. Software redundancy: varied versions of a software
    3. Voting algorithms: compare multiple results
5. Operational Profile Testing
    1. Predict the reliability of software by simulates real-world operation.
    2. occurrence rate
    3. obtaining profile data come from
        1. historical data
        2. marketing
        3. competing systems


### Reliability Models
1. Early models were influenced by hardware, which accounted for "burn-in" and "wear-out" failures.
2. Software does not wear out; its failures are primarily design problems.
3. Reliability growth models
    1. Assuming that testing, debugging, and defect removal will improve software reliability.
    2. Models should ideally help determine when to stop testing.
4. Key concepts
    1. Garbage in, garbage out: Model outputs are only as good as the input data.
    2. Failure intensity: failures per natural or time unit
5. Common assumption
    1. No new errors introduced by fixes (typically untrue).
    2. Mathematical distributions to represent reliability growth (not linear).
    3. Operational profile must be used for collecting failure data to match real-world use.
6. Challenges
    1. Developing an good operational profile can be difficult.
    2. Operational profile testing requires time and significant data collection.
    3. Statistical uncertainty
        1. High-reliability systems must also test rare cases.
        2. Testing these low-probability events increases costs and may yield limited failure data.
7. Experiment with different models to find the optimal one for your needs.


### The review of the paper
1. IEEE Recommended Practice on Software Reliability - section 4
    1.  IEEE Standard 610 defines reliability as: The ability of a system or component to perform its required functions under stated conditions for a specified period of time.
    2. Strategy
        1. Planning: Early-stage planning and scope identification.
        2. Analysis: Risk and failure mode analysis.
        3. Prediction: Using operational profiles to predict reliability.
        4. Testing: Generating data to support predictions and decisions.
        5. Release: Assessing readiness based on reliability objectives.
        6. Operation: monitoring and failure rate tracking.
    3. Key objectives
        1. Achieve desired mean time between failures (MTBF)
        2. Use reliability growth models to refine predictions.
        3. Support decisions for readiness based on forecasting defects.
    4. Proposes a dedicated reliability sprint for final reliability data collection

2. When to Stop Testing: a study from the perspective of software reliability models
    1. Key factors
        1. Time to market
        2. Risk of failures
        3. Cost of continued testing
    2. Reliability models provide guidance on whether the software meets the reliability requirements.
    3. Challenges
        1. Collecting operational profile data
        2. Selecting appropriate reliability models
        3. Calibrating models
        4. Measuring failure intensity in terms of execution time rather than calendar time.
    4. Categories of models
        1. Prediction models
            1. Use historical data to estimate potential defects
            2. Used after code completion but before actual testing.
        2. Estimation Models
            1. Use current testing data to assess reliability.
            2. Used after actual testing, later in the life cycle.

3. UML-Based Statistical Test Case Generation
    1. Once all functions have been verified through plan-based testing, statistical testing will be employed to estimate reliability.
    2. Generate test input data using an operational profile.


## Security Testing
1. Software correctness and security are not the same.
2. Key concepts
    1. Confidentiality: Protecting data and application capabilities from unauthorized access.
    2. Integrity: Ensuring that only authorized modifications to data are allowed.
    3. Denial of Service (DoS) and Distributed Denial of Service (DDoS) attack.
3. Challenges
    1. Side effects and unknown functionality can complicate security testing.
    2. Testing must involve interactions.
4. Basic strategies
    1. Access Control Verification (訪問控制驗證)
    2. Password Protection Testing (密碼保護測試)
    3. Malicious Activity Testing (惡意活動測試)
    4. Encryption Checks (加密檢查)
    5. Memory Storage Security Verification (內存儲存安全驗證)
    6. Stress Testing (壓力測試)
    7. Fault Injection (故障注入)
    8. Recovery Mode Testing (恢復模式測試)
    9. Buffer Overflow Testing (緩衝區溢出測試)
    10. Special Character Input Testing (特殊字符輸入測試)
    11. Default and Common Username Testing (默認及常見用戶名測試)
    12. Validation Level Verification Across Scenarios (不同場景的驗證級別檢查)
    13. Error Message and Recovery Process Testing (錯誤消息與恢復過程測試)
    14. Simulating Trojan Horse Attacks (模擬特洛伊木馬攻擊)
    15. Testing for Exploiting Timeouts (測試超時漏洞)
    16. Testing Multiple Task Methods (測試多種任務方法)
    17. Ensuring Proper Validation Pathways (確保正確的驗證路徑)
5. The CERT Division provides resources for cybersecurity and tracks recent vulnerabilities.