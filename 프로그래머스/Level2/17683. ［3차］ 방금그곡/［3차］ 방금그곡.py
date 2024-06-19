def solution(m, musicinfos):
    music = []
    m = m.replace('C#', 'c')
    m = m.replace('D#', 'd')
    m = m.replace('F#', 'f')
    m = m.replace('G#', 'g')
    m = m.replace('A#', 'a')

    for mm in musicinfos :
        mu = mm.split(',')
        mu[3] = mu[3].replace('C#', 'c')
        mu[3] = mu[3].replace('D#', 'd')
        mu[3] = mu[3].replace('F#', 'f')
        mu[3] = mu[3].replace('G#', 'g')
        mu[3] = mu[3].replace('A#', 'a')
        l = t(mu[0],mu[1])
        
        if mel(m, mu[3], l) == True :
            new = []
            new.append(l)
            new.append(mu[0])
            new.append(mu[2])
            music.append(new)
            
    if len(music) == 0 :
        return "(None)"
    else :
        music.sort(key = lambda x:x[1])
        music.sort(key = lambda x:x[0], reverse=True)
        return music[0][2]

def t(m0, m1) :
    if int(m1[3:]) - int(m0[3:]) >= 0 :
        h = int(m1[0:2]) - int(m0[0:2])
        m = int(m1[3:]) - int(m0[3:])
    else :
        h = int(m1[0:2]) - int(m0[0:2]) - 1
        m = 60 + int(m1[3:]) - int(m0[3:])
    mm = m + (h*60)
    return mm
    
def mel(m, mu, l) :
    a = l//len(mu)
    b = l%len(mu)
    c = mu*a + mu[:b]
    if m in c :
        return True
    else :
        return False