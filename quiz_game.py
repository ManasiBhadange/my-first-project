print("===================================")
print("        PYTHON QUIZ GAME 🎯")
print("===================================")

score = 0

# Question 1
print("\nQ1. Who is the founder of Python?")
print("a) Dennis Ritchie")
print("b) James Gosling")
print("c) Guido van Rossum")

ans1 = input("Enter your answer (a/b/c): ").lower()

if ans1 == "c":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is Guido van Rossum")


# Question 2
print("\nQ2. Which of the following is an immutable data type?")
print("a) List")
print("b) Dictionary")
print("c) Tuple")

ans2 = input("Enter your answer (a/b/c): ").lower()

if ans2 == "c":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is Tuple")


# Question 3
print("\nQ3. What will be the output of: print(type(5.0)) ?")
print("a) int")
print("b) float")
print("c) double")

ans3 = input("Enter your answer (a/b/c): ").lower()

if ans3 == "b":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is float")


# Question 4
print("\nQ4. What is the output of: print(10 // 3) ?")
print("a) 3.33")
print("b) 3")
print("c) 4")

ans4 = input("Enter your answer (a/b/c): ").lower()

if ans4 == "b":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is 3")


# Question 5
print("\nQ5. What will be the output of: print(type(\"123\")) ?")
print("a) int")
print("b) str")
print("c) float")

ans5 = input("Enter your answer (a/b/c): ").lower()

if ans5 == "b":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is str")


# Final Result
percentage = (score / 5) * 100

print("\n===================================")
print("           RESULT 📊")
print("===================================")
print("Your Final Score:", score, "/ 5")
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Grade: A 🏆 Excellent!")
elif percentage >= 60:
    print("Grade: B 👍 Good Job!")
elif percentage >= 40:
    print("Grade: C 🙂 You Passed")
else:
    print("Grade: F ❌ Better Luck Next Time")

print("\nThank you for playing! 👋")
