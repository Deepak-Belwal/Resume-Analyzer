# Resume-Analyzer
A simple resume analyzer that uses pre-defined keywords to extract skills and match them with suitable job roles.

## Problem Statement
It is inconvenient to extract skills from every resume by visually going over it and then noting the data, later checking it with each job role.

## Working
This analyzer will extract skills from a resume that's provided to it and find the suitable job role for that skill set.
### Input
- Resume text
### Process
- Extract skills using keywords.
- Compare with predefined job skill sets.
### Output
- List of the skills detected.
- Suggested job roles with match score.

## Development Progress
- DAY 1:
    - Created the project skeleton.
    - Noted approach and tech-stack for the project.
    - Finalized data structures to be used in the main code.
- DAY 2:
    - The project can now select a suitable job role based on percentage match between the candidate's skills and predefined job role-skill set dictionary.
    - Skill names were normalized to remove case sensitivity during comparisons and computations.
    - Percentages are calculated with basic formulas to avoid confusion and formatted to show up to 2 decimal places for clarity.
    - Best job is simply chosen by comparing the percentage match of an individual's skills to the pre-defined job roles and displaying the one with highest suitability.
- DAY 3:
    - Enabled user to enter resume data as text.
    - Created a function to extract tokens from the input text and process it further to filter out the required skills. This involved :
        - Punctuation removal
        - Whitespace tokenization
        - Handling duplicates
        - Text matching
    - Handled various edge cases that occurred like division by zero during percentage calculation and skills not found in user input.
    - Enhanced overall readability of the code by adding comments and dividing the complete code into different sections based on their functioning.
- DAY 4:
    - Made the code more flask friendly by updating the functions to return values instead of simply executing the logic and printing.
    - Did final testing of the main logic and added docstrings and other comments to enhance readability even further.
    - Added another important variable to store a list of unmatched values.
- DAY 5:
    - Built a Flask app within the main code to host the backend server.
    - Added a POST /analyze endpoint to invoke core functions when requested and handled edge cases.
    - Tested the code using curl commands and verified the results for multiple edge cases.
- DAY 6(Final day for core building of the project):
    - Added a frontend to the project using HTML and JavaScript to interact with the backend.
    - Enabled flask's render_template module inside the root ("/") endpoint (HomePage), rendering frontend on the same port as the backend server and avoiding CORS-related issues.
    - Updated requirements.txt showing the project's current dependencies.
    - Made minor adjustments to the POST /analyze endpoint:
        - Improved input handling for better interpretation and reliablility.
        - Fixed HTTP error codes for I/O related edge cases.