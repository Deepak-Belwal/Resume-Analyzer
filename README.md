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