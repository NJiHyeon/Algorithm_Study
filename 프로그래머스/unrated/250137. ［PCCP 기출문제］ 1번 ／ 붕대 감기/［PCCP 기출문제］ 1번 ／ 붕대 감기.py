def solution(bandage, health, attacks):
    success = 0
    healthing = health
    attack_time = [attacks[i][0] for i in range(len(attacks))]
    attack_score = [attacks[i][1] for i in range(len(attacks))]
    
    for i in range(1, attacks[-1][0]+1) :
        if i in attack_time :
            # 공격받으면
            success = 0
            healthing -= attack_score[attack_time.index(i)]
            if healthing <= 0 :
                return -1
        else :
            # 공격 안받으면
            success += 1
            if success == bandage[0] :
                new = healthing + (bandage[2]+bandage[1])
                success = 0
                if new <= health :
                    healthing = new
                else :
                    healthing = health
            else :
                new = healthing + bandage[1]
                if new <= health :
                    healthing = new
                else :
                    healthing = health
    
    return healthing