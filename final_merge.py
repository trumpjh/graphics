#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docx import Document
import json

# 정답 테이블 추출
doc = Document('(3학년) 광고콘텐츠 재작.docx')
table = doc.tables[0]

answers_dict = {}

# 테이블에서 정답 추출
for row_idx in range(1, len(table.rows)):
    row = table.rows[row_idx]
    
    for col_idx in range(0, 8, 2):
        question_num_text = row.cells[col_idx].text.strip()
        answer_text = row.cells[col_idx + 1].text.strip()
        
        if question_num_text.isdigit():
            q_num = int(question_num_text)
            
            # ①②③④⑤를 0-4 인덱스로 변환
            first_answer = answer_text.split(',')[0].strip()
            
            if first_answer and first_answer[0] in '①②③④⑤':
                answer_idx = ord(first_answer[0]) - ord('①')
                answers_dict[q_num] = answer_idx

# 추출한 질문 로드
with open('3rd_grade_all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"질문: {len(questions)}개, 정답: {len(answers_dict)}개")

# 질문에 정답 병합
for i, question in enumerate(questions):
    q_num = i + 1
    if q_num in answers_dict:
        question['correct'] = answers_dict[q_num]

# 저장
with open('3rd_grade_complete.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"3rd_grade_complete.json에 저장 완료")

# 미리보기
print("\n처음 3개 문제 미리보기:")
for i in range(min(3, len(questions))):
    q = questions[i]
    if q['correct'] >= 0:
        ans_char = chr(ord('①') + q['correct'])
        print(f"\n{i+1}. {q['question'][:60]}...")
        print(f"   정답: {ans_char} ({q['options'][q['correct']]})")
    else:
        print(f"\n{i+1}. 정답 없음")

print(f"\n35번, 36번 이미지 문제 확인:")
for i in [34, 35]:  # 35번, 36번 (0-indexed)
    if i < len(questions):
        q = questions[i]
        print(f"{i+1}. {q['question']}")
