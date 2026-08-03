class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        m = len(tasks)
        pref = [0] * (m+1)
        for i in range(m):
            pref[i+1] = pref[i] + tasks[i]

        ans = []
        l = 0
        curr_rem = tasks[0] if m > 0 else 0
        for shift in shifts:
            if l ==m:
                l = 0
                curr_rem = tasks[0]

            if shift < curr_rem:
                curr_rem -= shift
                ans.append(m-l)
                continue
            shift -= curr_rem
            l+=1

            if l == m:
                ans.append(0)
                continue
            target = shift+pref[l]
            idx = bisect.bisect_right(pref,target) - 1

            shift -= (pref[idx]-pref[l])
            l = idx
            if l == m:
                ans.append(0)
            else:
                curr_rem = tasks[l] - shift
                ans.append(m-l)
        return ans