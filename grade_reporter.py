# grade_reporter.py

scores = [72, 45, 90, 61, 38]

passed_count = 0
failed_count = 0
total_score = 0

for score in scores:
    # Determine the grade using if / elif / else
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(f"Score: {score}, Grade: {grade}")

    # Track passes and fails (passing is 50 or more)
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1

    # Accumulate total score
    total_score += score

# Calculate average rounded to one decimal place
average_score = round(total_score / len(scores), 1)

print("\n--- Summary ---")
print(f"Number of learners who passed: {passed_count}")
print(f"Number of learners who failed: {failed_count}")
print(f"Average score: {average_score}")