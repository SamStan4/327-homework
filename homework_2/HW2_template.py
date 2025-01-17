import hashlib

def compute_gcd(a : int, b : int) -> list[tuple[int, int]]:
    """
    Computes the GCD of two numbers a and b using the Euclidean algorithm.

    The function also records all steps in the GCD computation process. Each step
    is stored as a tuple (a, b) representing the dividend and divisor at that stage.

    Parameters:
        a (int): The first number (dividend in the first step).
        b (int): The second number (divisor in the first step).

    Returns:
        tuple: (gcd, steps)
            gcd (int): The greatest common divisor of a and b.
            steps (list of tuple): The list of (a, b) pairs at each step of the computation.
    """
    s = []
    while True:
        s.append((a, b))
        if b == 0:
            break
        elif a < b:
            a, b = b, a
        else:
            a, b = b, a % b
    return (a, s)
        


def get_k_step(steps : list[tuple[int, int]], k : int) -> tuple[int, int]:
    """
    Retrieves the k-th step tuple from the steps of the GCD computation.

    Steps are indexed starting from 1, so the first step corresponds to k=1.
    If k is out of range (greater than the total number of steps), None is returned.

    Parameters:
        steps (list of tuple): The list of (a, b) tuples from the GCD computation.
        k (int): The step number to retrieve (1-indexed).

    Returns:
        tuple or None: The k-th step tuple (a, b), or None if k is out of range.
    """
    if k > len(steps) or k <= 0:
        return None
    return steps[k-1]


def construct_response_string(gcd_value, depth, k_step):
    """
    Constructs the response string in the format "GCD,Depth,k-step-a,k-step-b".

    If the k-th step is out of range, the string will end with "None".

    Parameters:
        gcd_value (int): The computed GCD value.
        depth (int): The total number of steps in the computation.
        k_step (tuple or None): The tuple (a, b) at the k-th step, or None if out of range.

    Returns:
        str: The constructed response string.
    """
    if k_step:
        return f"{gcd_value},{depth},{k_step[0]},{k_step[1]}"
    else:
        return f"{gcd_value},{depth},None"


def compute_sha256(wsuid, sk, response_string):
    """
    Computes the SHA256 hash of the concatenation of WSUID, SK, and the response string.

    Parameters:
        wsuid (str): A unique identifier (e.g., a student ID).
        sk (str): A secret key used for hash generation.
        response_string (str): The response string generated from the GCD computation.

    Returns:
        str: The SHA256 hash of the concatenated string.
    """
    pass


def gcd_with_sha256(a, b, k, wsuid, sk):
    """
    Computes the GCD of two numbers a, b along with additional information.

    The function calculates the GCD, the total depth of recursion, the tuple at the k-th step,
    and a SHA256 hash based on WSUID, SK, and the response string.

    Parameters:
        a (int): The first number.
        b (int): The second number.
        k (int): The step number for which the tuple should be returned.
        wsuid (str): WSUID string (e.g., a student ID).
        sk (str): Secret key string.

    Returns:
        tuple: (gcd, depth, k-th tuple, SHA256 hash)
            gcd (int): The greatest common divisor of a and b.
            depth (int): The total number of steps in the GCD computation.
            k-th tuple (tuple or None): The (a, b) pair at the k-th step, or None if k is out of range.
            SHA256 hash (str): The hash of WSUID, SK, and the response string.
    """
    gcd_value, steps = compute_gcd(a, b)
    depth = len(steps)
    k_step = get_k_step(steps, k)
    response_string = construct_response_string(gcd_value, depth, k_step)
    sha256_hash = compute_sha256(wsuid, sk, response_string)

    return gcd_value, depth, k_step, sha256_hash


def test_gcd_with_sha256():
    """
    Tests the gcd_with_sha256 function using 20 hardcoded test cases.
    Compares the computed response string with the expected values.
    Prints a message if a test case fails.
    """
    test_cases = [
        (48, 18, 3, "6,4,12,6"),
        (56, 98, 2, "14,5,98,56"),
        (101, 103, 1, "1,5,101,103"),
        (123456, 789012, 4, "12,13,48276,26904"),
        (540, 150, 2, "30,5,150,90"),
        (1000000, 500000, 3, "500000,2,None"),
        (987654, 123456, 5, "6,3,None"),
        (42, 56, 1, "14,4,42,56"),
        (144, 89, 2, "1,11,89,55"),
        (999999, 333333, 2, "333333,2,333333,0"),
        (250, 1000, 3, "250,3,250,0"),
        (77, 121, 1, "11,6,77,121"),
        (36, 60, 2, "12,5,60,36"),
        (84, 36, 3, "12,3,12,0"),
        (700, 1050, 4, "350,4,350,0"),
        (27, 81, 2, "27,3,81,27"),
        (600, 750, 2, "150,4,750,600"),
        (48, 180, 3, "12,5,48,36"),
        (1024, 2048, 2, "1024,3,2048,1024"),
        (12345, 54321, 5, "3,7,2463,15"),
    ]


    for i, (a, b, k, expected_response) in enumerate(test_cases, 1):
        gcd_value, steps = compute_gcd(a, b)
        depth = len(steps)
        k_step = get_k_step(steps, k)
        actual_response = construct_response_string(gcd_value, depth, k_step)

        if actual_response != expected_response:
            print(f"Test Case {i} Failed:")
            print(f"Input: a={a}, b={b}, k={k}")
            print(f"Expected Response: {expected_response}")
            print(f"Actual Response: {actual_response}")
            print("----------------------------------")
        else:
            print(f"Test Case {i} Passed.")


def main():
    test_gcd_with_sha256()
    
if __name__ == "__main__":
    main()