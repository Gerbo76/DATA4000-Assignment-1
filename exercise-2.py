score = int(input("Input Credit Score "))
if score < 300 or score > 850:
    print("Invalid Score")
elif 750 <= score <= 850:
    print("Excellent - Loan Approved")
elif 700 <= score <= 750:
    print("Good - Loan Approved with Review")
elif 600 <= score <= 700:
    print("Fair - Loan Conditional")
else:
    print("Poor - Loan Denied")

if score >= 700:
    print("Interest rate: Low")
if 300 <= score < 700:
    print("Seek credit improvement.")

