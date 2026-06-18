#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docx import Document
import re

# 3학년 문서 읽기
doc = Document('(3학년) 광고콘텐츠 재작.docx')

print("=== 마지막 30개 문단 (정답 찾기) ===\n")

# 뒤에서부터 30개 문단 출력
all_paras = [p.text.strip() for p in doc.paragraphs if p.text.strip()]

for text in all_paras[-50:]:
    print(text[:120])
