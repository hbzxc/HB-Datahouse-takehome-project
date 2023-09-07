import json
import os
import sys

# Check if the input data has the expected structure and contains valid values
def is_valid_data(data):
    if not isinstance(data, dict):
        return False
    if "team" not in data or "applicants" not in data:
        return False
    for member in data.get("team", []):
        if not isinstance(member, dict) or "attributes" not in member:
            return False
        attributes = member.get("attributes", {})
        if not all(isinstance(attributes.get(attr), (int, float)) or attributes.get(attr) is None for attr in attributes):
            return False
    for applicant in data.get("applicants", []):
        if not isinstance(applicant, dict) or "attributes" not in applicant:
            return False
        attributes = applicant.get("attributes", {})
        if not all(isinstance(attributes.get(attr), (int, float)) or attributes.get(attr) is None for attr in attributes):
            return False

    return True

# Find the lowest agrigate attribute for team members
def get_lowest_avg(inputDic):
    lowest_score = min(score for score in inputDic.values() if score is not None)
    lowest_attributes = [attribute for attribute, score in inputDic.items() if score == lowest_score and score is not None]
    return lowest_attributes

#calculate the compatibility result for an applicant
def get_result (applicant, wanted_attributes):
    app_attributes = applicant.get('attributes', {})
    total_qualities = len(wanted_attributes)
    #if more than one attribute needs to be checked sum them
    score_total = sum(app_attributes.get(quality, 0) for quality in wanted_attributes)
    # formula to calculate result
    result = score_total / (total_qualities * 10)
    return result

# Read in the sample data and verify that it is valid if not exit
try:
    with open('sample_data.json', 'r') as json_file:
        sample_data = json.load(json_file)
except (FileNotFoundError, json.JSONDecodeError):
    print("Error: Invalid or missing sample data file.")
    sys.exit(1)

if not is_valid_data(sample_data):
    print("Error: Invalid input data format.")
    sys.exit(1)

# Sum the attribute scores from each team member into 
team_member_average = {}
for member in sample_data.get('team', []):
    attributes = member.get('attributes', {})
    for attribute, score in attributes.items():
        team_member_average[attribute] = team_member_average.get(attribute, 0) + score

#get the name(s) of the attributes the team is currently lacking the most
low_attributes = get_lowest_avg(team_member_average)

# Calculate scores for applicants based on what attributes the team could use
empty_dic = []
for applicant in sample_data.get('applicants', []):
    app_name = applicant.get('name', '')
    empty_dic.append({"name": app_name, "score": get_result(applicant, low_attributes)})

#setup the final python dictionary before converting to JSON
results = {"scoredApplicants": empty_dic}

#output the results to a results folder and call it scoredApplicants_Results.json
output_file_path = os.path.join("Results", "scoredApplicants_Results.json")

# Save the JSON data to the specified relative path
with open(output_file_path, 'w') as output_file:
    json.dump(results, output_file)