# We are making n stone piles! The first pile has n stones. If n is
# even, then all piles have an even number of stones. If n is odd, all
# piles have an odd number of stones. Each pile must have more
# stones than the previous pile but as few as possible. Write a
# Python program to find the number of stones in each pile.
# Sample Input: n = 7
# Sample Output: Stones in a single pile = [2, 4, 6]

def create_stone_piles(n):
    if n % 2 == 0:
        first_pile = n if n % 2 == 0 else n + 1
    else:
        first_pile = n if n % 2 == 1 else n + 1
    piles = []
    for i in range(first_pile, first_pile + n * 2, 2):
        piles.append(i)
    return piles

n = int(input("Enter the number of piles (n): "))
stone_piles = create_stone_piles(n)
print(f"Stones in each pile: {stone_piles}")
