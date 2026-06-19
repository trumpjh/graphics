#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docx import Document
import re

# 3학년 문서 읽기
doc = Document('(3학년) 광고콘텐츠 재작.docx')

all_text = []
for para in doc.paragraphs:
    text = para.text.strip()
    if text:
        all_text.append(text)

print("=== 정답 섹션 찾기 ===\n")

# 정답 섹션 찾기
in_answer_section = False
for i, text in enumerate(all_text):
    if '정답' in text or '답안' in text or '답' in text:
        print(f"[{i}] {text}")
        in_answer_section = True
    elif in_answer_section and ('1.' in text or '①' in text or '②' in text):
        print(f"[{i}] {text}")
    elif in_answer_section and (text.isdigit() or text[0].isdigit()):
        print(f"[{i}] {text}")
        if i > 100:  # 너무 많으면 중단
            break

print("\n\n=== 14번과 46번 정답 찾기 ===\n")

# 정답 부분 추출 (보통 맨 뒤에 있음)
answer_section = []
for i in range(len(all_text)-1, max(0, len(all_text)-150), -1):
    answer_section.insert(0, all_text[i])

print("마지막 150줄:")
for line in answer_section:
    if '14' in line or '46' in line or line[0].isdigit() if len(line) > 0 else False:
        print(line)
