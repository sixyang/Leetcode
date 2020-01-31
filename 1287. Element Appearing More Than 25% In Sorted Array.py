class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        thods = len(arr)//4
        for index in range(len(arr)):
            if arr[index] == arr[index+thods]:
                return arr[index]
                
'''
class Solution {
    public int findSpecialInteger(int[] arr) {
        int threshold = arr.length / 4;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i + threshold] == arr[i]) {
                return arr[i];
            }
        }
        return 0;
    }
}
'''                
