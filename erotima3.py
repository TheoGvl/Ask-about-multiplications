import time
from erotima1 import generate_random_text, inject_multiplications, compute

def main():
    start_time = time.time()
    
    text = generate_random_text(1_000_000)
    step1_time = time.time()
    print(f"Time for generate_random_text: {step1_time - start_time:.2f} sec")
    
    modified_text = inject_multiplications(text, 100_000)
    step2_time = time.time()
    print(f"Time for inject_multiplications: {step2_time - step1_time:.2f} sec")
    

    result = compute(modified_text)
    step3_time = time.time()
    print(f"Time for compute: {step3_time - step2_time:.2f} sec")
    

    print(f"Result: {result}")
    print(f"Total time: {step3_time - start_time:.2f} sec")

if __name__ == "__main__":
    main()
