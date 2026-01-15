Βήματα:
Βήμα 1: Δημιουργία τυχαίου κειμένου (1.000.000 χαρακτήρες)
    text = generate_random_text(1_000_000)
    step1_time = time.time()
    print(f"Time for generate_random_text: {step1_time - start_time:.2f} sec")
Βήμα 2: Εισαγωγή 100.000 εντολών πολλαπλασιασμού
    modified_text = inject_multiplications(text, 100_000)
    step2_time = time.time()
    print(f"Time for inject_multiplications: {step2_time - step1_time:.2f} sec")
Βήμα 3: Υπολογισμός αθροίσματος των γινομένων
    result = compute(modified_text)
    step3_time = time.time()
    print(f"Time for compute: {step3_time - step2_time:.2f} sec")
Βήμα 4 εμφάνιση αποτελέσματος:
    print(f"Result: {result}")
    print(f"Total time: {step3_time - start_time:.2f} sec")
Ο κώδικας τρέχει και βγάζει πολλά αποτελέσματα για την κάθε τυχαία εντολή και στο τέλος βγάζει τα εξής:
Χρόνος για inject_multiplications: 124.12 sec
Χρόνος για compute: 0.07 sec
Τελικό αποτέλεσμα: 153494671
Συνολικός χρόνος εκτέλεσης: 124.37 sec
