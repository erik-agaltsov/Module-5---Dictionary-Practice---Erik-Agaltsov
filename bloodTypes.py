with open('bloodTypes.txt', 'r') as file:
    blood_data = file.readlines()

blood_type_counts = {
    "A-pos": 0, "A-neg": 0, "B-pos": 0, "B-neg": 0,
    "AB-pos": 0, "AB-neg": 0, "O-pos": 0, "O-neg": 0
}

blood_group_counts = {
    "A": 0, "B": 0, "AB": 0, "O": 0
}

rh_factor_counts = {
    "pos": 0,
    "neg": 0
}

for line in blood_data:
    blood_type = line.strip() 

    if blood_type in blood_type_counts:
        blood_type_counts[blood_type] += 1
    
    if blood_type.startswith("A") and not blood_type.startswith("AB"):
        blood_group_counts["A"] += 1
    elif blood_type.startswith("B") and not blood_type.startswith("AB"):
        blood_group_counts["B"] += 1
    elif blood_type.startswith("AB"):
        blood_group_counts["AB"] += 1
    elif blood_type.startswith("O"):
        blood_group_counts["O"] += 1

    if blood_type.endswith("pos"):
        rh_factor_counts["pos"] += 1
    elif blood_type.endswith("neg"):
        rh_factor_counts["neg"] += 1

print("Blood Type Counts:")
for blood_type, count in blood_type_counts.items():
    print(f"{blood_type}: {count}")

print("\nBlood Group Counts:")
for group, count in blood_group_counts.items():
    print(f"{group}: {count}")

print("\nRh Factor Counts:")
for rh, count in rh_factor_counts.items():
    print(f"{rh}: {count}")