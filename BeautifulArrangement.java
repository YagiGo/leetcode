// https://leetcode.com/problems/beautiful-arrangement/
/*
We make use of a visited array of size NN. Here, visited[i]visited[i] refers to the i^{th}ith number being already placed/not placed in the array being formed till now(True indicates that the number has already been placed).

We make use of a calculate function, which puts all the numbers pending numbers from 1 to N(i.e. not placed till now in the array), indicated by a FalseFalse at the corresponding visited[i]visited[i] position, and tries to create all the permutations with those numbers starting from the pospos index onwards in the current array. While putting the pos^{th}pos 
th
  number, we check whether the i^{th}i 
th
  number satisfies the divisibility criteria on the go i.e. we continue forward with creating the permutations with the number ii at the pos^{th}pos 
th
  position only if the number ii and pospos satisfy the given criteria. Otherwise, we continue with putting the next numbers at the same position and keep on generating the permutations.
*/
class Solution {
    int count = 0;
    public int countArrangement(int N) {
        boolean[] visited = new boolean[N+1];
        calculate(N, visited, 1);
        return count;
    }
    
    public void calculate(int N, boolean[] visited, int pos) {
        if (pos > N) {
            count ++;
        }
        for(int i = 1; i <= N; i++) {
            if(!visited[i] && (pos % i == 0 || i % pos == 0)) {
                visited[i] = true;
                calculate(N, visited, pos+1);
                visited[i] = false;
            }
        }
    }
}
