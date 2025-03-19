def generate_permutations(words):
    def permute(current, remaining):
        if not remaining:
            permutations.append(current)
        else:
            for i in range(len(remaining)):
                permute(current + [remaining[i]], remaining[:i] + remaining[i+1:])
    
    permutations = []
    permute([], words)
    return permutations

def is_permutation_present(permutations, long_string):
    for perm in permutations:
        perm_str = ' '.join(perm)
        if perm_str in long_string:
            return True
    return False

def main():
    words = ["apple", "banana", "cherry"]
    long_string = "I have an apple and a banana and a cherry in my basket"

    perms = generate_permutations(words)
    found = is_permutation_present(perms, long_string)

    print("Is any permutation present in the long string?", found)

if __name__ == "__main__":
    main()