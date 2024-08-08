def solution(new_id):
    import re
    # "...!@BaT#*..y.abcdefghijklm"
    step1 = new_id.lower()
    step2 = re.sub('[^a-z0-9-_.]', '', step1)
    while '..' in step2:
        step2 = step2.replace('..', '.')
    step3 = step2[:]
    step4 = step3.strip('.')
    if step4 == '':
        step4 += 'a'
    step5 = step4[:]
    if len(step5) >= 16:
        step5 = step5[:15]
    step6 = step5.rstrip('.')
    while len(step6) <= 2:
        step6 += step6[-1]
    step7 = step6[:]
    return step7
        