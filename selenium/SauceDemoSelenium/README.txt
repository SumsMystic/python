This project is my practice attempt at Selenium Automation for website 'https://www.saucedemo.com/' using Python and PyTest Framework for now.
So far I am trying to use the following concepts:
	- Page Object Model (POM) based Test Automation Design.
	- ASSERT statements for test case validation
	- pytest-html package for HTML reports generation
	- Try-Except blocks so as to catch exceptions like 'Element Not Found' or 'Timeout Exception'.
	- Relative searching of Elements from another element on the page.
	- PyTest Fixtures for Suite as well as Test Case level Setup and Teardown
	- PyTest Markers (Tags) for Logical grouping of Test Cases. This is currently at primitive level. Will enhance this later. 
	
Things planned to be done later: 
	- I will later try to incorporate same Automation test cases using Robot Framework as well as Behave (Python BDD) framework.
	- End to end test case scenarios for each of the specified users
	- WebDriverWait instead of 'sleep' that I am using in few places for now.
	- Parameterization of Test execution so that runs can be configured in CI/CD or Jenkins pipeline jobs. (E.g., log level, browser for test execution, etc.)