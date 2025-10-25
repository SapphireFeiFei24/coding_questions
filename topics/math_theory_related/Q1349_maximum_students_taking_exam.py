"""
Description
Given a m * n matrix seats that represent seats distributions in a classroom.
If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.
Students can see the answers of those sitting next to the left, right, upper left and upper right,
but he cannot see the answers of the student sitting directly in front or behind him.

Return the maximum number of students that can take the exam together without any cheating being possible.
Students must be placed in seats in good condition.

Solution: DP+BitMasking
State(r, m): a student seat masking for row r.
* It's only valid if it's a sub-state derived from the original valid seat maps
Transition Func:
State(r, m) = max(State(r-1, m') + student_counts(State(r,m))
where State(r-1, m') and State(r, m) must not have adjacent students
student_counts can be calculated from the bit count of mask m.

Masking Tricks:
* Get i-th bit in the state x
``(x>>i) & 1``
* Check if x is a subset of y
``(x&y) == x``
* Check if there are no adjacent valid status in x
``(x&(x>>1))== 0``
"""


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        # Precompute number of each valid mask
        # There are 2^M states
        N, M = len(seats), len(seats[0])
        valid_bits = [0]
        for state in range(1, 2 ** M):
            prev = valid_bits[state // 2]
            valid_bits.append(prev + (state % 2 == 1))
        # print("valid_bits", valid_bits)
        # Get validity mask for each row
        potential_seats = []
        for r in range(N):
            mask = 0
            for c in range(M):
                if seats[r][c] == ".":
                    mask |= 1 << c
            potential_seats.append(mask)
        dp = [-1 for i in range(1 << M)]
        dp[0] = 0  # the virtual row zero is a valid state with no students sitting
        for r in range(N):
            ps = potential_seats[r]
            # print("potential seats for row:{r}", bin(ps))
            new_dp = [-1 for i in range(1 << M)]
            for state in range(1 << M):
                # Check the status that's only valid based on the intial potential seat map
                # AND no adjacent student seating together
                if state & ps == state and state & (state >> 1) == 0:
                    # Check valid states from row r-1
                    for prev in range(1 << M):
                        # print("prev", prev, dp)
                        if dp[prev] >= 0:
                            # print("checking valid prev state")
                            if ((prev >> 1) & state == 0) and ((state >> 1) & prev == 0):
                                new_dp[state] = max(new_dp[state], dp[prev] + valid_bits[state])
            dp = new_dp
            # print("row", r, dp)
        return max(dp)


