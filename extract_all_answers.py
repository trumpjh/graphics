#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docx import Document
import json

def extract_all_answers_from_table(filename, grade):
    """테이블에서 모든 정답 추출 (8칼럼 구조)"""
    doc = Document(filename)
    
    answers = {}
    
    for table in doc.tables:
        if len(table.rows) < 2:
            continue
        
        # 헤더 확인
        header = [cell.text.strip() for cell in table.rows[0].cells]
        if '문항' not in header or '정답' not in header:
            continue
        
        # 데이터 행 처리
        for row_idx in range(1, len(table.rows)):
            row = table.rows[row_idx]
            cells = [cell.text.strip() for cell in row.cells]
            
            # 8칼럼 구조: [문항1, 정답1, 문항2, 정답2, 문항3, 정답3, 문항4, 정답4]
            for col_offset in range(0, len(cells), 2):
                if col_offset + 1 < len(cells):
                    q_num_str = cells[col_offset].strip()
                    answer = cells[col_offset + 1].strip()
                    
                    # 문제 번호가 숫자인지 확인
                    if q_num_str.isdigit():
                        q_num = int(q_num_str)
                        answers[q_num] = answer
    
    return answers

# 3학년 정답 추출
print("="*60)
print("3학년 정답 추출 (전체 테이블)")
print("="*60)
answers_3rd = extract_all_answers_from_table('(3학년) 광고콘텐츠 재작.docx', 3)
print(f"추출된 3학년 정답: {len(answers_3rd)}개")
for k in sorted(answers_3rd.keys()):
    print(f"  {k}: {answers_3rd[k]}")

# 2학년 정답 추출
print("\n" + "="*60)
print("2학년 정답 추출 (전체 테이블)")
print("="*60)
answers_2nd = extract_all_answers_from_table('2학년 광고콘텐츠제작.docx', 2)
print(f"추출된 2학년 정답: {len(answers_2nd)}개")
for k in sorted(answers_2nd.keys()):
    print(f"  {k}: {answers_2nd[k]}")

# 저장
with open('all_extracted_answers.json', 'w', encoding='utf-8') as f:
    json.dump({
        '3rd_grade': answers_3rd,
        '2nd_grade': answers_2nd
    }, f, ensure_ascii=False, indent=2)

print("\nall_extracted_answers.json 파일 생성 완료")
