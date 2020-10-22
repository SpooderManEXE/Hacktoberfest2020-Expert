package src;

import java.util.HashSet;
import java.util.Set;

public class largest_consecutive_sum {

    public int longestConsecutive(int[] nums) {

        int ans  = Integer.MIN_VALUE;

        if (nums.length == 0)
            return 0;


        Set<Integer> set = new HashSet<>();

        for(int i : nums)
            set.add(i);

        for(int i : nums)
        {
            if (!set.contains(i-1))
            {
                int streak = 1;
                int k = i;
                while(set.contains(k+1))
                {
                    streak++;
                    k++;
                }
                ans = Math.max(ans, streak);
            }
        }
        return ans;
    }

    public static void main(String[] args)
    {
        //main function
    }
}
