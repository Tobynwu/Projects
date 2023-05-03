"""
Tobenna Nwufo
CIS 2348
2054054
"""
def fat_burning_heart_rate(age):
    return (220 - age) * 0.7

def get_age():
    age = int(input())
    if 18 <= age <= 75:
        return age
    raise ValueError("Invalid age.")

if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate} bpm")
    except ValueError as error:
        print(error)
        print("Could not calculate heart rate info.\n")