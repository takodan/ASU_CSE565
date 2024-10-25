# Unit 1: Software Testing Overview
### Learning Objectives
1. Define common testing terminology
2. Describe how testing is integrated into software development phases
3. Define the objectives of the different levels of testing
4. Explain best practices for software testing

## Testing Background
1. History and Background
    1. With the increasing reliability of computer hardware and the growing complexity of software, the root cause of system failures has shifted towards software-related issues.
    2. Even with the evolution of technology and development practices, software development is still plagued by similar issues.
2. Reliability and Testers
    1. Poor Reliability
        1. Software defect rates are around 1 per thousand lines of code.
        2. However, applications can contain millions of lines of code.
    2. Testers (similar to scientific pollster)
        1. paid to made prediction
        2. lots of constraints (money, time,...)
        3. impossible to do an exhaustive testing (only representative samples)
3. Classic Testing Mistakes
    1. Thinking that the purpose of testing is to find bugs. (not focusing on the important problems)
    2. Starting testing too late. 
    3. A testing effort biased toward functional testing. (also need to test performance, security etc.)
    4. An overreliance on beta testing.
    5. Sticking stubbornly to the test plan.
    6. Using testing as a transitional job for new programmers.
    7. A physical separation between developers and testers.
    8. Believing that programmers can't test their own code.
    9. Programmers are neither trained nor motivated to test.
    10. Attempting to automate all tests.
    11. Embracing code coverage as the end-all.
    12. Using coverage as a performance goal for testers.
4. Definitions
    1. (roughly pull from IEEE)
    2. Reliability: the probability that a software program operates for some given time period without software error.
    3. Validation:
        1. Are we building the right product?
        2. The product meets the customer’s needs and adds value to the customer.
    4. Verification:
        1. Are we building the product right?
        2. if the product meets the predefined requirements and specifications, assuming those requirements are correct.
    5. Testing: The examination of the behavior of the program by executing it on "representative" sample data sets.
    6. Error: A mistake made by humans.
    7. Defect/Fault: The result of an error manifested in the code.
    8. Failure: the software does not do what it's supposed to do or does something wrong
5. "State of Testing Report 2018"
    1. Roles of Testers: Respondents held various roles such as test engineers, automation testers, and test architects, highlighting the diversity in testing roles.
    2. Testing as a Career: Many testers are staying in the field long-term, indicating that software testing is seen as a viable career path.
    3. Tester Responsibilities: Testers engage in tasks like test automation, data management, documentation, and test-driven development, reflecting the broad scope of the role.
    4. Testing Techniques: Exploratory and pair testing are increasingly common, especially in Agile environments.
    5. Essential Skills: Communication skills, automation knowledge, and familiarity with Agile are critical for testers.
    6. Development Models: Agile is the dominant methodology, but a significant portion of testers still work with Waterfall.
    7. Automation's Role: Automation is growing in importance, not just for functional testing, but across continuous integration and delivery.
    8. Hiring Needs: Testers need a proactive mindset, problem-solving skills, creativity, and strong communication, along with technical expertise.

## Testing Throughout Software Life Cycle
1. Waterfall and Incremental Models:
    1. Testing typically occurs at the end of development, but testers are involved early in refining requirements and preparing test cases.
    2. A key issue with waterfall is the "throwing over the wall" mentality: The next phase can only begin after the previous one is completed.
2. Agile Methodologies:
    1. Agile involves continuous testing throughout the process, with testers working closely with developers and customers  in iterative sprints.
    2. Test-Driven Development (TDD) is a key approach in Agile.
3. Test-Driven Development (TDD)
    1. In TDD, developers write minimal tests to define desired behaviors before writing the code.
    2. Developers write just enough code to pass the tests, ensuring quality from the start.
4. Test Development Process
    1. Similar phases exist between software and test development
        1. Requirements: Defining test objectives.
        2. Design: Test design and strategy, similar to software architecture.
        3. Coding: Writing test cases and scripts.
        4. Testing: Executing tests is similar to executing the software.
        5. Maintenance: Updating tests as new software requirements emerge.
    2. Test development requires just like in software development
        1. estimation
        2. planning
        3. tracking
        4.  configuration management
5. Levels of Testing
    1. Unit/Component Testing: Done by developers at their workstations, often automated, to validate and verify individual components.
    2. Integration Testing: Combines units and components, focusing on their interaction and higher-level functions.
    3. System Testing: Tests the entire system, also including non-functional aspects like security, performance, and usability.
    4. Acceptance Testing: Performed by customers to verify if the system meets contractual requirements.
    5. Beta Testing: External customers test the system before full release, with potential risks.
6. Types of Testing
    1. Functional Testing: Verifies that the software does what it's supposed to, applicable at all levels.
    2. Non-Functional Testing: Focuses on "ilities" (security, usability, performance) at higher levels.
    3. Structural (White Box) Testing: Ensures logic and code execution quality, mostly at the unit level.
    4. Regression Testing: Ensures changes haven’t broken existing functionality, applicable at all levels.

## Testing Best Practices and Standards
1. Testing Principles
    1. Testing only shows the presence of defects: Testing doesn’t prove the absence of defects, only their presence.
    2. Exhaustive testing is impossible: It's unrealistic to test all inputs, especially with complex systems.
    3. Start testing early: Early involvement, such as in test-driven development (TDD), is crucial.
    4. Defects cluster: Defects tend to appear in specific areas, often due to complexity or human error.
    5. Testing is context-dependent: Tests depend on the system's state and external factors, especially for mobile apps.
    6. Absence of errors fallacy: Even defect-free software may not meet customer needs.

2. Testing Attitudes:
    1. Independence: Testing should ideally be done independently to avoid bias, though it's difficult at the unit level.
    2. Customer Perspective: Testers should adopt the customer’s viewpoint to ensure software meets real-world needs.
    3. Test for intended and unintended functionality: Verify the system works as expected and deliberately try to "break" it (e.g., test edge cases).
    4. Professionalism in Testing: Testing requires specialized skills, education, and knowledge of best practices.

3. Classic Testing Mistakes:
    1. Focusing only on finding bugs: Testing should focus on identifying important problems and predicting system quality, not just finding bugs.
    2. Ignoring usability: Usability is critical to product success and should not be overlooked.
    3. Starting testing too late: Delayed testing increases costs and risk. Early involvement helps prevent issues.
    4. Waiting until the end for performance/stress testing: Delaying these tests may leave insufficient time to resolve issues.
    5. Not testing documentation: Testing should ensure the product aligns with customer expectations.
    6. Not using domain experts: Domain knowledge is crucial for effective testing, especially from the customer's perspective.
    7. Failing to review test designs: Test strategies and cases must be carefully reviewed to avoid errors in testing.
    8. Inflexible test plans: Test plans need to adapt to changes in the software.
    9. Not learning from previous tests: Test teams should review past test activities and apply lessons learned.

4. Best Testing Practices:
    1. Use statistical testing for reliability: Techniques like operational profile testing.
    2. Agile test design: Testing should adapt to changing software.
    3. Model-based testing: Develop models for software behavior that can generate test cases automatically.
    4. Integrate development and test teams: Collaboration between teams is essential.
    5. Automate testing where possible: Automation reduces costs and increases efficiency.
    6. Emphasize usability testing: It’s a crucial part of the process for user-centered design and product success.
    7. When to Stop Testing: All requirements are met, code coverage is achieved, reliability objectives are reached, and customer satisfaction is ensured.

5. Literature reading: Software Testing Best Practices
    1. https://www.chillarege.com/authwork/TestingBestPractice.pdf
    2. Reviews and Inspections: Regularly review both code and test cases to ensure accuracy.
    3. Entry and Exit Criteria: Define clear guidelines for when to start and stop testing.
    4. Multi-Platform Testing: Test across various platforms, especially for mobile and IoT.
    5. Automated Testing: Automate test execution to support continuous deployment.
    6. ODC Feedback Loops: Analyze defects and use feedback to prevent repeated issues.
    7. Requirements Management: Effective test planning relies on well-managed requirements.
    8. Usability Testing: Essential for ensuring user-friendly products.
    9. Collaborating Testers and Developers: Close teamwork in Agile environments improves testing efficiency.
    10. Code Coverage: Use tools to ensure thorough testing, but don’t over-focus on it.
    11. Automated Test Environment: Rapid test generation is crucial in DevOps.
    12. Model-Based Testing: Use models to generate test cases efficiently.
    13. Statistical Testing: Test how customers use the system.
    14. Bug Bounties/Crowd Testing: Incentivize testers to find bugs externally.

5. Literature reading: Automation's Role in the Fall of Software Testing
    1. Over-Reliance on Automation: Automation is helpful for repetitive tasks but struggles with deeper, complex testing scenarios, which still require human involvement.
    2. Shallow Testing: Automated tests often cover surface-level issues but fail to handle complex, real-world user cases effectively.
    3. Testing vs. Checking: Automation is good at checking routine tasks but doesn’t replace thorough testing, which requires deeper exploration.
