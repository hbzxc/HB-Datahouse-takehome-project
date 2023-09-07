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

# Calculate the average attribute scores for team members
team_member_average = {}
for member in sample_data.get('team', []):
    attributes = member.get('attributes', {})
    for attribute, score in attributes.items():
        team_member_average[attribute] = team_member_average.get(attribute, 0) + score

low_attributes = get_lowest_avg(team_member_average)

# Calculate scores for applicants based on what attributes the team could use
empty_dic = []
for applicant in sample_data.get('applicants', []):
    app_name = applicant.get('name', '')
    app_attributes = applicant.get('attributes', {})
    total_qualities = len(low_attributes)
    score_total = sum(app_attributes.get(quality, 0) for quality in low_attributes)
    # formula to calculate result
    result = score_total / (total_qualities * 10)
    empty_dic.append({"name": app_name, "score": result})

#create the final python dictionary before converting to JSON
results = {"scoredApplicants": empty_dic}

#output the results to a results folder and call it output_file.json
output_file_path = os.path.join("Results", "output_file.json")

# Save the JSON data to the specified relative path
with open(output_file_path, 'w') as output_file:
    json.dump(results, output_file)