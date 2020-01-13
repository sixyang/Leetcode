class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        if (rec1[0] >= rec2[2] or rec2[0] >= rec1[2] or rec1[3] <= rec2[1] or rec2[3] <= rec1[1]){
            return false;
        }    
        return true;
    }
};
