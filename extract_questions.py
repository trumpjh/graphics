from docx import Document

# .docx 파일 읽기
doc = Document("2학년 광고콘텐츠제작.docx")

# 모든 텍스트 출력
print("=== 모든 텍스트 (정답 포함) ===")
for i, para in enumerate(doc.paragraphs):
    text = para.text.strip()
    if text:
        print(f"{i}: {text}")
