#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docx import Document
import re
import json

# 3학년 문서 읽기
doc = Document('(3학년) 광고콘텐츠 재작.docx')

all_text = []
for para in doc.paragraphs:
    text = para.text.strip()
    if text:
        all_text.append(text)

# 정답표 찾기 (일반적인 형식: "정답" 또는 "답" 이라는 단어 이후)
print("=== 파일의 모든 텍스트 (마지막 100줄) ===\n")

for i, text in enumerate(all_text[-100:]):
    print(f"[{len(all_text)-100+i}] {text}")

print("\n\n=== 정답 추출 시도 ===\n")

# 정답표 패턴 찾기
answer_pattern = re.compile(r'(\d+)[.)]*\s*([①②③④⑤])', re.UNICODE)

answers_dict = {}

# 모든 텍스트에서 정답 찾기
for text in all_text:
    matches = answer_pattern.findall(text)
    for num, answer in matches:
        q_num = int(num)
        # ①②③④⑤를 0-4로 변환
        answer_idx = ord(answer) - ord('①')
        answers_dict[q_num] = answer_idx
        print(f"문제 {q_num}: {answer} (인덱스: {answer_idx})")

print(f"\n추출된 정답: {len(answers_dict)}개")

# 정답 저장
with open('3rd_grade_answers.json', 'w', encoding='utf-8') as f:
    json.dump(answers_dict, f, ensure_ascii=False, indent=2)

print("3rd_grade_answers.json에 저장됨")
