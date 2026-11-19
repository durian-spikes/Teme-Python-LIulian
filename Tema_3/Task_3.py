words = input("Words: ").split()

anagram_groups = {}

# Group words using their sorted letters
for word in words:
    key = "".join(sorted(word.lower()))

    if key not in anagram_groups:
        anagram_groups[key] = []

    anagram_groups[key].append(word)


# Print groups in the order they first appeared
for group in anagram_groups.values():
    sorted_group = sorted(group, key=str.lower)

    print(", ".join(sorted_group))


# Stretch: Find the largest group
largest_group = max(
    anagram_groups.values(),
    key=len
)

print("\nLargest group:", ", ".join(sorted(largest_group, key=str.lower)))
print("Group size:", len(largest_group))