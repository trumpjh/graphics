#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docx import Document
import json
import re

# 정답 테이블 추출
doc = Document('(3학년) 광고콘텐츠 재작.docx')
table = doc.tables[0]

answers_dict = {}

# 테이블에서 정답 추출 (행 1부터 시작, 0은 헤더)
for row_idx in range(1, len(table.rows)):
    row = table.rows[row_idx]
    
    # 각 행에는 4개의 (문항, 정답) 쌍이 있음
    for col_idx in range(0, 8, 2):
        question_num_text = row.cells[col_idx].text.strip()
        answer_text = row.cells[col_idx + 1].text.strip()
        
        if question_num_text.isdigit():
            q_num = int(question_num_text)
            
            # ①②③④⑤를 0-4 인덱스로 변환
            # 여러 정답이 있으면 첫 번째를 사용 (예: "①,⑤" -> "①")
            first_answer = answer_text.split(',')[0].strip()
            
            if first_answer and first_answer[0] in '①②③④⑤':
                answer_idx = ord(first_answer[0]) - ord('①')
                answers_dict[q_num] = answer_idx

print(f"추출된 정답: {len(answers_dict)}개")
for q_num in sorted(answers_dict.keys()):
    ans_idx = answers_dict[q_num]
    ans_char = chr(ord('①') + ans_idx)
    print(f"  문제 {q_num}: {ans_char} (인덱스: {ans_idx})")

# 기존 질문 JSON 로드
with open('3rd_grade_full.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"\n기존 질문: {len(questions)}개")

# 질문에 정답 병합
for i, question in enumerate(questions):
    q_num = i + 1
    if q_num in answers_dict:
        question['correct'] = answers_dict[q_num]
    else:
        print(f"경고: 문제 {q_num}의 정답을 찾을 수 없음")

# 저장
with open('3rd_grade_complete.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"\n3rd_grade_complete.json에 저장 완료")

# 미리보기 (처음 5개)
print("\n처음 5개 문제 미리보기:")
for i in range(min(5, len(questions))):
    q = questions[i]
    ans_char = chr(ord('①') + q['correct']) if q['correct'] >= 0 else '?'
    print(f"\n{i+1}. {q['question'][:60]}...")
    print(f"   정답: {ans_char} ({q['options'][q['correct']]})")
