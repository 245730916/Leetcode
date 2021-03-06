class Solution:
    def twoSum(self, nums, target):
        for x in nums: 
            n=nums.index(x)
            nums.remove(x)
            if (target-x) in nums: 
                return [n, nums.index(target-x)+1] 
            else:
                nums.insert(n,x)
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            line = next(lines)
            target = int(line);
            
            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()