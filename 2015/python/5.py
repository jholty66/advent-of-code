f=open("../5.txt")
I=f.read().split("\n")
ans=[s for s in I if all(b not in s for b in ["ab","cd","pq","xy"]) and sum([s.count(v) for v in ["a","e","i","o","u"]]) >=3 and any(s[c]==s[c-1] for c in range(1,len(s)-1))]
print(len(ans))
