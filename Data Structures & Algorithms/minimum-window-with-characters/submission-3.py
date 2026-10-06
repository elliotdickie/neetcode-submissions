class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_map = {}
        pos_map = {}
        s_queue = deque()
        res_l = 0
        res_r = -1
        c_check = 0
        for c in t:
            if c in freq_map:
                freq_map[c]+=1
            else:
                c_check += 1
                freq_map[c] = 1
                pos_map[c] = deque()
        l = 0
        for r in range(len(s)):
            if s[r] not in pos_map: continue
            pos_map[s[r]].append(r)
            if len(pos_map[s[r]]) == freq_map[s[r]]:
                c_check -= 1
            s_queue.append(s[r])
            while len(pos_map[s_queue[0]]) > freq_map[s_queue[0]]:
                pos_map[s_queue[0]].popleft()
                s_queue.popleft()
                l=pos_map[s_queue[0]][0]
            while (s[l] not in pos_map):
                l+=1
            if c_check == 0 and ((res_r-res_l > r-l) or res_r == -1):
                res_l = l
                res_r = r
        if res_r == -1: return ""
        return s[res_l:res_r+1]