import sys

# https://practice.geeksforgeeks.org/problems/coin-piles/0


# There are N piles of coins each containing  Ai (1<=i<=N)  coins.  Now, you have to
# adjust the number of coins in each pile such that for any two piles, if a is the
# number of coins in first pile and b is the number of coins in second pile
# then |a-b|<=K. In order to do that you can remove coins from different piles to
# decrease the number of coins in those piles but you cannot increase the number of
# coins in a pile by adding more coins. Now, given a value of N and K, along with the
# sizes of the N different piles you have to tell the minimum number of coins to be
# removed in order to satisfy the given condition.
#
# Note: You can also remove a pile by removing all the coins of that pile.

###############################################################################

def get_diffs(arr, n, k):
    rv = [-1]
    for i in range(len(arr)-1):
        rv.append(abs(arr[i]-arr[i+1]))
    return rv

def is_valid(diffs):
    for x in diffs[1:]:
        if x > k: return False
    return True

# TODO: handle empty columns (columns with zero coins)
def coin_piles(arr, n, k):
    changes = 0
    diffs = get_diffs(arr, n, k)
    #print(diffs, is_valid(diffs))
    while not is_valid(diffs):
        max_diff = max(diffs)
        i = diffs.index(max_diff)
        if arr[i-1] < arr[i]:
            arr[i] -= 1
            changes += 1
        else:
            arr[i-1] -=1
            changes += 1
        diffs = get_diffs(arr, n, k)
        #print(diffs, is_valid(diffs))
    return changes


###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (4, 0, "2 2 2 2", 0) )
    test_inputs.append( (6, 3, "1 2 5 1 1 1", 1) )
    test_inputs.append( (6, 3, "1 5 1 2 5 1", 2) )

    """ Run process on sample inputs 
    """
    for n, k, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{n} {k} {arr}')
        rv = coin_piles(arr, n, k)
        print(f"{rv} expected: {results}")

"""Explanation  
1. In the first test case, for any two piles the difference in the number of coins
   is <=0. So no need to remove any coins.
2. In the second test case if we remove one coin from pile containing 5 coins then
   for any two piles the absolute difference in the number of coins is <=3.
3. In the third test case if we remove one coin each from both the piles containing
   5 coins , then for any two piles the absolute difference in the number of coins
   is <=3."""




"""#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main()
 {
	int t, n, k;
	cin >> t;
	while(t--) {
	    cin >> n >> k;
	    vector <int> piles(n);
	    for(int i = 0; i < n;  i++)
	        cin >> piles[i];
	    sort(piles.begin(), piles.end());
	    int ans = INT_MAX;
	    int prevSum = 0, curSum = 0;
	    for(int i = 0; i < n; i++) {
	        prevSum += i < 1 ? 0 : piles[i-1];
	        curSum = 0;
	        for(int j = n-1; j > i; j--) {
	            if(piles[j] - piles[i] <= k)
	                break;
	            curSum += piles[j] - piles[i] - k;
	        }
	        ans = min(ans, curSum + prevSum);
	    }
	    cout << ans << endl;
	}
	return 0;
}"""
