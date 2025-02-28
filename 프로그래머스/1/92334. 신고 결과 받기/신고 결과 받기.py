def solution(id_list, report, k):
    # 신고 결과 정리
    report_dict = {}
    for i in range(len(report)):
        ed, pp = report[i].split()
        if pp in report_dict:
            report_dict[pp].add(ed)
        else:
            report_dict[pp] = {ed}
    # 메일 발송 정리
    mail_dict = {people:0 for people in id_list}
    for pp in report_dict:
        if len(report_dict[pp]) >= k:
            for ed in report_dict[pp]:
                mail_dict[ed] += 1
    # 결과출력
    result = []
    for m in mail_dict:
        result.append(mail_dict[m])
    return result
    