class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        retval = [];
        retmap = {}
        for i in range(len(nums)):
            if nums[i] > 0:
                break;
            #find two elements in a sorted array who has some -nums[i]
            trgt = -nums[i]
            fp = i+1
            bp = len(nums)-1
            while bp > fp and fp < len(nums):
                currsum = nums[fp]+nums[bp]
                if currsum < trgt:
                    fp +=1 
                elif currsum > trgt: 
                    bp -= 1
                else:
                    sol = [nums[i], nums[fp], nums[bp]]
                    if tuple(sol) not in retmap:
                        retval.append(sol)
                        retmap[tuple(sol)]=True
                    fp += 1
                    bp -= 1
        return retval
                    
                
            
            