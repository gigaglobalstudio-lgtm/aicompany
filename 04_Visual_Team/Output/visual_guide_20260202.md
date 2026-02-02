# 비주얼 에셋 가이드
## 콘텐츠: "1인 기업가의 AI 팀 만들기"

**작성일:** 2026.02.02
**Creative Director:** 방향 설정 완료
**Art Director:** 콘셉트 개발 완료
**Prompt Engineer:** 프롬프트 작성 완료
**QA:** 승인

---

## 1. 비주얼 콘셉트

### 핵심 메시지
> "혼자지만 혼자가 아닌, AI 팀과 함께"

### 무드 키워드
| 카테고리 | 키워드 |
|----------|--------|
| 감정 | 자신감, 희망, 혁신 |
| 스타일 | 모던, 미니멀, 클린 |
| 분위기 | 밝음, 전문적, 미래지향 |

### 컬러 팔레트

| 용도 | 컬러명 | HEX | 사용처 |
|------|--------|-----|--------|
| Primary | 딥 블루 | #1E3A8A | 메인 요소, 제목 |
| Secondary | 스카이 블루 | #3B82F6 | 보조 요소, 아이콘 |
| Accent | 오렌지 | #F97316 | CTA, 강조 |
| Light | 라이트 그레이 | #F3F4F6 | 배경 |
| Dark | 차콜 | #1F2937 | 텍스트 |

### 참고 이미지 스타일
- Apple 제품 마케팅 이미지 (클린, 미니멀)
- Notion 일러스트레이션 (플랫, 친근)
- Linear 앱 비주얼 (모던, 테크)

---

## 2. 유튜브 썸네일 (1280x720px)

### 레이아웃 옵션

**Option A: 인물 중심**
```
┌─────────────────────────────────────────────┐
│                                             │
│   ┌──────┐                                  │
│   │      │     "나 혼자"                   │
│   │ 인물 │      10개 팀                    │
│   │      │      운영하기                   │
│   └──────┘                                  │
│                        ┌───┐ ┌───┐ ┌───┐   │
│                        │🤖│ │🤖│ │🤖│   │
│                        └───┘ └───┘ └───┘   │
└─────────────────────────────────────────────┘
```

**Option B: 아이콘 중심**
```
┌─────────────────────────────────────────────┐
│                                             │
│         👤                                  │
│    "1인 기업가의"                          │
│      ┌─────────────────┐                   │
│      │   AI 팀 만들기   │                   │
│      └─────────────────┘                   │
│    🤖 🤖 🤖 🤖 🤖                          │
│    🤖 🤖 🤖 🤖 🤖                          │
│                                             │
└─────────────────────────────────────────────┘
```

### AI 이미지 프롬프트

#### Midjourney 프롬프트 (Option A)
```
A confident Asian entrepreneur standing in center, surrounded by
10 floating holographic AI robot assistants in a semi-circle,
each robot has a different department icon (marketing, finance,
strategy), modern minimal office background, blue and orange
color scheme, soft studio lighting, professional photography style,
clean composition, 16:9 aspect ratio --ar 16:9 --v 6 --s 200
```

#### Midjourney 프롬프트 (Option B)
```
Minimalist flat illustration of a solo entrepreneur icon in the
center with 10 small AI robot icons arranged below, modern tech
style, blue gradient background (#1E3A8A to #3B82F6), clean
vector art, no text, simple geometric shapes, professional and
friendly mood --ar 16:9 --v 6 --s 150
```

#### DALL-E 프롬프트
```
Create a YouTube thumbnail concept showing a single person
silhouette in the center with 10 friendly AI robot icons
floating around them in a protective circle formation. Use a
modern, clean design with a deep blue to light blue gradient
background. The style should be minimalist and professional,
similar to tech startup branding. The robots should look
helpful and approachable, not intimidating. Aspect ratio 16:9.
```

### 텍스트 오버레이 가이드

| 요소 | 내용 | 폰트 | 크기 | 컬러 |
|------|------|------|------|------|
| 메인 타이틀 | "나 혼자 10개 팀 운영" | Pretendard Bold | 72px | 화이트 |
| 서브 타이틀 | "AI 에이전트 활용법" | Pretendard Medium | 36px | #F97316 |
| 뱃지 (옵션) | "실제 사례 공개" | Pretendard SemiBold | 24px | 화이트 on 오렌지 |

### 주의사항
- [ ] 텍스트는 좌측 또는 우측에 배치 (중앙 X)
- [ ] 모바일에서도 텍스트 가독성 확인
- [ ] 얼굴/인물은 우측에 배치 (클릭 유도)

---

## 3. 블로그 히어로 이미지 (1200x630px)

### 레이아웃
```
┌──────────────────────────────────────────────────┐
│                                                  │
│      ┌────────────────────────────────────┐     │
│      │                                    │     │
│      │  [중앙에 개념적 일러스트레이션]    │     │
│      │                                    │     │
│      │   1인 → AI팀 10개 변환 비주얼     │     │
│      │                                    │     │
│      └────────────────────────────────────┘     │
│                                                  │
└──────────────────────────────────────────────────┘
```

### AI 이미지 프롬프트

#### Midjourney 프롬프트
```
Isometric illustration of a modern home office desk with a
laptop, from the laptop screen emerging 10 small friendly AI
robot assistants floating upward, each holding different business
tools (chart, document, megaphone, calculator, lightbulb),
soft pastel blue background, minimal clean style, no text,
professional and optimistic mood, slight 3D depth --ar 1.91:1
--v 6 --s 200
```

#### DALL-E 프롬프트
```
Create a blog hero image showing a conceptual illustration of
digital transformation. A single laptop on a clean desk with
10 small, cute AI robot characters emerging from the screen,
each representing a different business function (one holds a
megaphone for marketing, one holds charts for finance, etc.).
The style should be modern, minimal, with soft blue and white
colors. The mood should feel empowering and optimistic.
No text in the image. Aspect ratio approximately 1.9:1.
```

### 대체 콘셉트: 추상적 표현
```
Abstract visualization of AI collaboration: a single glowing
human silhouette node in the center connected by elegant flowing
lines to 10 smaller AI nodes arranged in a network pattern,
deep blue to purple gradient background, modern data visualization
style, subtle particle effects, professional and futuristic,
clean minimal design --ar 1.91:1 --v 6 --s 250
```

---

## 4. 인스타그램 피드 (1080x1080px)

### 시리즈 콘셉트
10장 카드뉴스의 첫 이미지 (후킹용)

### 레이아웃
```
┌────────────────────────────┐
│                            │
│     "혼자인데              │
│      10명이 일한다?"       │
│                            │
│         👤                 │
│      ╱  │  ╲              │
│    🤖  🤖  🤖              │
│   🤖  🤖  🤖  🤖           │
│    🤖  🤖  🤖              │
│                            │
│   ───────────────          │
│   저장 필수 👆             │
│                            │
└────────────────────────────┘
```

### AI 이미지 프롬프트

#### Midjourney 프롬프트
```
Square format Instagram post design, single person icon at top
center with 10 small AI robot icons arranged below in a pyramid
formation, connected by subtle dotted lines, solid deep blue
background (#1E3A8A), flat minimal illustration style, plenty
of negative space for text overlay, clean and modern, no text
in image --ar 1:1 --v 6 --s 150
```

#### 배경 전용 프롬프트
```
Abstract geometric background for Instagram post, subtle blue
gradient from #1E3A8A to #3B82F6, minimal circuit-like pattern
faintly visible, clean modern tech aesthetic, perfect for text
overlay, corporate professional style --ar 1:1 --v 6 --s 100
```

### 텍스트 오버레이

| 요소 | 내용 | 스타일 |
|------|------|--------|
| 후킹 카피 | "혼자인데 10명이 일한다?" | Bold, 화이트, 48px |
| 하단 CTA | "저장 필수 👆" | Medium, 화이트, 24px |

---

## 5. 디자인 시스템 요약

### 공통 적용 규칙

| 항목 | 규칙 |
|------|------|
| 여백 | 최소 10% 마진 유지 |
| 텍스트 | 배경 대비 명확하게 |
| 아이콘 | 일관된 스타일 (Flat/Outlined) |
| 그라데이션 | 부드러운 전환, 최대 2컬러 |

### 금지 사항
- ❌ 과도한 그림자/효과
- ❌ 3개 이상 폰트 혼용
- ❌ 채도 높은 네온 컬러
- ❌ 복잡한 배경 패턴
- ❌ 저작권 불명확한 이미지

### 파일 명명 규칙
```
[플랫폼]_[콘텐츠명]_[버전]_[날짜].[확장자]

예시:
youtube_ai팀만들기_v1_20260202.png
blog_ai팀만들기_hero_20260202.png
instagram_ai팀만들기_01_20260202.png
```

---

## 6. 최종 체크리스트

### 썸네일 (YouTube)
- [ ] 1280x720px
- [ ] 모바일 가독성 확인
- [ ] 텍스트 30% 이하
- [ ] 고대비 컬러

### 히어로 (Blog)
- [ ] 1200x630px
- [ ] OG 이미지로 활용 가능
- [ ] 텍스트 없는 버전도 준비

### 피드 (Instagram)
- [ ] 1080x1080px
- [ ] 시리즈 일관성
- [ ] 프로필 그리드 고려

---

## QA 검증 결과

### 브랜드 일관성
- [x] 컬러 팔레트 준수
- [x] 톤앤매너 통일
- [x] 크로스 플랫폼 일관성

### 기술 요건
- [x] 해상도 충족
- [x] 파일 형식 명시
- [x] 프롬프트 테스트 가능

### 승인
**QA 승인 완료** ✅

---
*Visual Team | My_AI_Company*
