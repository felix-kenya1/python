# Check if all scores are within the valid range.
def calculate_grade(score):
    if score >= 70 and score <= 100:
        return 'A'
    elif score >= 60 and score <= 69:
        return 'B'
    elif score >= 50 and score <= 59:
        return 'C'
    elif score >= 40 and score <= 49:
        return 'D'
    elif score >= 0 and score <= 39:
        return 'FAIL'
    else:
        return 'Invalid Score'

def main():
    subjects = ['first', 'second', 'third']
    total_score = 0

    for subject in subjects:
        while True:
            score = int(input(f"Enter marks for {subject} subject (0-100): "))
            if score >= 0 and score <= 100:
                break
            else:
                print("INVALID SCORE!!! please enter again.")

        total_score += score

    average_score = total_score / len(subjects)
    print(f"Average score: {average_score:.2f}")
    print(f"Grade: {calculate_grade(average_score)}")

if __name__ == "__main__":
    main()
