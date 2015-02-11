public class Solution {
    public int majorityElement(int[] num) {
        //implement moore's voting algorithm
        int mindex = 0;
        int melement = num[0];
        int count = 0;
        //1st phase, find a candidate by scanning the array
        for (int i=0;i<num.length;i++){
            if (num[i] == melement ){
                count+=1;
            }
            else{count= count-1;}
            if (count==0){
                count = 1;
                melement = num[i];
                
            }
        }
        return melement;
        //2nd phase, verify the candidate by scanning again.
        
        
    }
}