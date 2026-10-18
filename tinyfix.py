
print("=" * 35)
print("             TINYFIX")
print("   Turn a problem into one step")
print("=" * 35)

# Step 1: Ask how much time is available
print("\nHow much time do you have?")
print("1. 5 minutes")
print("2. 10 minutes")
print("3. 15 minutes")

time_choice = input("Choose 1, 2, or 3: ").strip()

times = {"1": 5, "2": 10, "3": 15}

if time_choice not in times:
    print("Invalid time choice. Please try again.")
else:
    minutes = times[time_choice]

    # Step 2: Ask what is stopping the user
    print("\nWhat is stopping you?")
    print("1. I am confused")
    print("2. I don't have materials")
    print("3. There are too many steps")
    print("4. I don't feel motivated")

    problem = input("Choose 1, 2, 3, or 4: ").strip()

    actions = {
        "1": {
            5: "Write down one specific question.",
            10: "Study one example and identify what confuses you.",
            15: "Break the topic into three smaller parts."
        },
        "2": {
            5: "List the resource you are missing.",
            10: "Look for an alternative resource.",
            15: "Gather the materials you already have."
        },
        "3": {
            5: "Write down the first small step.",
            10: "Divide the task into three smaller steps.",
            15: "Complete the first part of your task."
        },
        "4": {
            5: "Choose one tiny task to start.",
            10: "Work on one small part without aiming for perfection.",
            15: "Try one short work session and review your progress."
        }
    }

    if problem not in actions:
        print("Invalid problem choice. Please try again.")

    else:
        action = actions[problem][minutes]

        # Step 3: Display the recommendation
        print("\n" + "=" * 35)
        print("          YOUR TINYFIX")
        print("=" * 35)
        print("Available time:", minutes, "minutes")
        print("Your next step:", action)

        # Step 4: Collect feedback
        feedback = input(
            "\nWas this suggestion helpful? (yes/no): "
        ).strip().lower()

        if feedback not in ["yes", "no"]:
            print("Please enter yes or no. Feedback not saved.")

        else:
            # Step 5: Save feedback
            with open("tinyfix_feedback.txt", "a") as file:
                file.write(
                    f"Time: {minutes} minutes | "
                    f"Problem: {problem} | "
                    f"Helpful: {feedback}\n"
                )

            print("Feedback saved successfully!")

            # Step 6: Analyse all saved feedback
            helpful = 0
            not_helpful = 0

            with open("tinyfix_feedback.txt", "r") as file:
                for line in file:
                    if "Helpful: yes" in line:
                        helpful += 1
                    elif "Helpful: no" in line:
                        not_helpful += 1

            total = helpful + not_helpful

            # Step 7: Display the report
            print("\n" + "=" * 35)
            print("         TINYFIX REPORT")
            print("=" * 35)
            print("Helpful suggestions:", helpful)
            print("Not helpful suggestions:", not_helpful)
            print("Total feedback:", total)

            if total > 0:
                percentage = (helpful / total) * 100
                print("Helpful rate:", round(percentage, 2), "%")

            print("=" * 35)
            print("Thank you for using TinyFix!")
