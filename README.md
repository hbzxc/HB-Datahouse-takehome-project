



# Compatibility Predictor
Take home project for Datahouse to determined new applicant compatibility scores.
Input and output in JSON
Compatibility scores fall in a range from 0 to 1

## Setup
 - Project running on Python 3.10.11
 - Every module used is built into python
	- JSON
	- OS
	- Sys
	- Unittest
	
 - JSON file with the sample data labled "sample_data.json" should be in the same directory as the script
 - Output will be to the folder "Results" and called "scoredApplicants_Results.json"

## How compatibility is determined
-Find the lowest attribute(s) of the current team members and select candidates to fill in those gaps

 1. Sum up all the attribute scores for each attribute category
    
	 Eddie: (intelligence, 4) (strength, 1)

	 Will: (intelligence, 5) (strength, 7)

	 would combine into (intelligence, 9) (strength, 8)
	 
3. Find the lowest total attribute score(s)
   
	In the example above the lowest score is strength.
	In case of multiple attributes being the lowest both are taken into account

5. Evaluate applicants on needed attributes
   
	In the example a candidate who has a high strength attribute will score better. A 10 in strength would be a 		perfect score.
	
    **formula for single attribute: desired_attribute / 10**
	
	For multiple attributes an applicants attributes are summed up and divided by the number of attributes * 10

	**formula for multiple attributes: sum_desired_attributes /(number_of_attributes x 10)**
		

## How I arrived at this criteria
I looked at the combined averages of the sample data given 
Perfect score would be 1

| Current Team Members |Combined Attributes /40 |
|--|--|
| Eddie | 0.25 |
| Will | 0.5 |
| Mike | 0.475 |

| New Applicants |Combined Attributes /40 |
|--|--|
| John | 0.3 |
| Jane | 0.4 |
| Joe | 0.325 |

There did not seem to be a threshold for an average score but team members did seem to excel in certain areas.

Eddie is the strongest

Will has the highest intelligence

Mike has the most endurance

It looks like team was made to be rounded out so a perspective applicant should preserve that balance.
To accomplish this find what the team is currently lacking and rate the applicants based on that attribute(s).

## Testing
I wrote 3 tests to check the 3 functions I included

1. Test is_valid_data function. If invalid sample data is submitted it should get rejected
2. Check the get_lowest_avg function should return the lowest attribute(s)

| Attribute|score |
|--|--|
| intelligence | 5 |
| strength | 4 |
| endurance | 5 |
| spicyFoodTolerance | 1 |

expected return: spicyFoodTolerance

| Attribute|score |
|--|--|
| intelligence | 1 |
| strength | 4 |
| endurance | 5 |
| spicyFoodTolerance | 1 |

expected return: intelligence, spicyFoodTolerance

3. Check get_results function. Should return the lowest attribute(s) over 10

| Applicant Attributes|score |
|--|--|
| intelligence | 9 |
| strength | 9 |
| endurance | 9 |
| spicyFoodTolerance | 1 |

expected return when given [strength] as the desired criteria: 0.9 (9/10)

expected return when given [strength] and [spicyFoodTolerance] as the desired criteria: 0.5 (9+1)/(2*10)
