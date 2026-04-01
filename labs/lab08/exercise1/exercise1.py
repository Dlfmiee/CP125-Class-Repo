# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    passing_scores = []
    
    with open(input_file, "r") as f:
        lines = f.readlines()
    
    # Handle both formats: "student_id score" per line OR alternating lines
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        parts = line.split()
        
        # Format: "student_id score" on same line
        if len(parts) == 2:
            student_id = parts[0]
            try:
                score = int(parts[1])
                if score >= 80:
                    passing_scores.append(f"{student_id} {score}")
            except ValueError:
                pass
        # Format: student_id on this line, score on next line (alternating)
        elif len(parts) == 1 and i + 1 < len(lines):
            student_id = line
            try:
                score = int(lines[i + 1].strip())
                if score >= 80:
                    passing_scores.append(f"{student_id} {score}")
                i += 1  # Skip next line since we used it
            except ValueError:
                pass
        
        i += 1
    
    with open(output_file, "w") as f:
        for student in passing_scores:
            f.write(student + "\n")
    
    return len(passing_scores)
