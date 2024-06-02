# A cafe has N computers. Several customers come to the cafe to use these computers.
# A customer will be serviced only if there is any unoccupied computer at the moment
# the customer visits the cafe. If there is no unoccupied computer, the customer
# leaves the cafe.
# You are given an integer N representing the number of computers in the cafe and
# a sequence of uppercase letters S. Every letter in S occurs exactly two times.
# The first occurrence denotes the arrival of a customer and the second occurrence
# denotes the departure of the same customer if he gets allocated the computer.
# You have to find the number of customers that walked away without using a computer.
# Example 1:
#     Input:
#     N = 3
#     S = GACCBDDBAGEE
#     Output: 1
#     Explanation: Only D will not be able to get any computer. So the answer is 1.
# Example 2:
#     Input:
#     N = 1
#     S = ABCBAC
#     Output: 2
#     Explanation: B and C will not be able to get any computers. So the answer is 2.

def count_customers_without_computers(N, S):
    in_use = {}
    available_computers = N
    walked_away = 0

    for event in S:
        if event not in in_use:
            if available_computers > 0:
                in_use[event] = True
                available_computers -= 1
            else:
                walked_away += 1
        else:
            if in_use[event]:
                available_computers += 1
                del in_use[event]

    return walked_away

N = int(input("Enter the number of computers: "))
S = input("Enter the sequence of customer coming in and going out using alphabets: ")
result = count_customers_without_computers(N, S)
print(f"Number of customers that walked away: {result}")
