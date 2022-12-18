objets = [(60, 8), (100, 20), (100, 60), (40, 20)]
m_max = 60
ratio = []
m_sac = 0
for i, item in enumerate(objets):
    ratio.append((item[0]/item[1], i))
ratio.sort(reverse=True)
solution = []
i = 0
n = 0
while i<len(ratio) and m_sac<m_max:
    if m_sac + objets[ratio[i][1]][1]<=m_max:
        m_sac = m_sac + objets[ratio[i][1]][1]
        n=n+1
    else:
        solution.append((ratio[i][1], n))
        i=i+1
print(solution)
