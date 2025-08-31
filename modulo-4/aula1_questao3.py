def calculate_student_status(grade1, grade2, grade3):
    """
    Calculates the average of three grades and determines the student's status.
    
    Args:
        grade1 (float): The first grade.
        grade2 (float): The second grade.
        grade3 (float): The third grade.
        
    Returns:
        str: The student's status ("Aprovado", "Recuperacao", or "Reprovado").
    """
    average = (grade1 + grade2 + grade3) / 3
    
    if average >= 60:
        return "Aprovado"
    elif average >= 40:
        return "Recuperacao"
    else:
        return "Reprovado"
    
if __name__ == "__main__":
    try:
        # User input is handled within a try-except block
        n1 = float(input("Enter the first grade: "))
        n2 = float(input("Enter the second grade: "))
        n3 = float(input("Enter the third grade: "))

        status = calculate_student_status(n1, n2, n3)
        print(status)
        
    except ValueError:
        print("Error: Please enter numbers only.")
        
    finally:
        print("Fim")