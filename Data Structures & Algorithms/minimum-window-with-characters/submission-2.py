class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_map = {}
        pos_map = {}
        s_queue = deque()
        res = ""
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
            if len(pos_map[s[r]]) == freq_map[s[r]]: c_check -= 1
            s_queue.append(s[r])
            while len(pos_map[s_queue[0]]) > freq_map[s_queue[0]]:
                if pos_map[s_queue[0]] == freq_map[s[r]]:
                    c_check+=1
                pos_map[s_queue[0]].popleft()
                s_queue.popleft()
                l=pos_map[s_queue[0]][0]
            while (s[l] not in pos_map):
                l+=1
            if c_check == 0 and (len(res)>len(s[l:r+1]) or res == ""): res = s[l:r+1]
        return res