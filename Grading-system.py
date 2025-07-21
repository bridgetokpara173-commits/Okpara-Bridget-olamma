+ # Grading System Program by Okpara Bridget Olamma 
+ # Reg.No:2024704005
+
+ try:
+ score = Int("Enter your' score (0-100)"))
+
+ # check if the score is within the acceptable range
+ If 0 <= score <= 100:
+      If to <= score <= 100:
+          grade = 'A'
+ elif 60 <= score <= 69:
+          grade = 'B'
+ elif 50 <= score <= 59:
+          grade = 'C'
+ elif 45 <= score <= 49:
+         grade = 'D'
+ elif 40 <= score <= 44:
+         grade = 'E'
+ else:
+        grade = 'F'
+
+ print ( f"YES! Your grade is:{grade}")
+ else
+ print ("Invalid score. Score must be between 0 and 100.")
+
+ except ValueError:
+ print ("Invalid input. please enter a whole number.)
