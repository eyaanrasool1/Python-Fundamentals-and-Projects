numbers = []

num_questions = int(input("How many numbers in your sequence? "))
if num_questions <= 1:
    print("Please enter a number greater than 1")
else:
    for i in range(1, num_questions + 1):
        num = int(input(f"Number {i}: "))
        numbers.append(num)

Differences = numbers [1] - numbers[0]

for i in range(1, len(numbers) - 1):
        if numbers[i + 1] - numbers[i] != Differences:
            print("The sequence is not an arithmetic sequence. No common difference.")
            break

else:
    print("The sequence is an arithmetic sequence. Common difference is ", Differences)