# My AI Company 조직도

## 10개 팀 구조 (Mermaid Diagram)

```mermaid
flowchart TB
    subgraph CEO["CEO / 1인 대표"]
        direction TB
        FOUNDER["창업자<br/>전략 총괄"]
    end

    subgraph STRATEGY["01 전략기획실"]
        direction LR
        S1["Strategy Director"]
        S2["Optimist / Pessimist<br/>Realist / Innovator"]
    end

    subgraph MARKETING["02 마케팅팀"]
        direction LR
        M1["Marketing Director"]
        M2["Channel Specialist<br/>Copywriter"]
    end

    subgraph CONTENT["03 콘텐츠팀"]
        direction LR
        C1["Content Director"]
        C2["Writer / Researcher<br/>Editor"]
    end

    subgraph VISUAL["04 비주얼팀"]
        direction LR
        V1["Art Director"]
        V2["Prompt Engineer<br/>Image Curator"]
    end

    subgraph ECOMMERCE["05 이커머스팀"]
        direction LR
        E1["Ecommerce Manager"]
        E2["Product Designer<br/>Copywriter"]
    end

    subgraph FINANCE["06 재무팀"]
        direction LR
        F1["CFO Agent"]
        F2["Analyst<br/>Accountant"]
    end

    subgraph BIZDEV["07 사업개발팀"]
        direction LR
        B1["BD Director"]
        B2["RFP Analyst<br/>Proposal Writer"]
    end

    subgraph EDUCATION["08 교육콘텐츠팀"]
        direction LR
        ED1["Education Director"]
        ED2["Curriculum Designer<br/>Quiz Master"]
    end

    subgraph BRAINSTORM["09 브레인스토밍팀"]
        direction LR
        BR1["Facilitator"]
        BR2["Ideator / Critic<br/>Connector"]
    end

    subgraph SUPPORT["10 경영지원팀"]
        direction LR
        SP1["Admin Manager"]
        SP2["Scheduler<br/>Document Handler"]
    end

    FOUNDER --> STRATEGY
    FOUNDER --> MARKETING
    FOUNDER --> CONTENT
    FOUNDER --> VISUAL
    FOUNDER --> ECOMMERCE
    FOUNDER --> FINANCE
    FOUNDER --> BIZDEV
    FOUNDER --> EDUCATION
    FOUNDER --> BRAINSTORM
    FOUNDER --> SUPPORT

    %% 팀 간 협업 관계
    STRATEGY -.->|전략 방향| MARKETING
    STRATEGY -.->|사업 계획| BIZDEV
    CONTENT -.->|콘텐츠 제작| MARKETING
    VISUAL -.->|디자인 지원| CONTENT
    VISUAL -.->|상세페이지| ECOMMERCE
    FINANCE -.->|예산 관리| BIZDEV
    BRAINSTORM -.->|아이디어| STRATEGY
    SUPPORT -.->|행정 지원| ALL

    style CEO fill:#1a1a2e,color:#fff
    style FOUNDER fill:#16213e,color:#fff
    style STRATEGY fill:#0f3460,color:#fff
    style MARKETING fill:#e94560,color:#fff
    style CONTENT fill:#533483,color:#fff
    style VISUAL fill:#0f3460,color:#fff
    style ECOMMERCE fill:#e94560,color:#fff
    style FINANCE fill:#533483,color:#fff
    style BIZDEV fill:#0f3460,color:#fff
    style EDUCATION fill:#e94560,color:#fff
    style BRAINSTORM fill:#533483,color:#fff
    style SUPPORT fill:#0f3460,color:#fff
```

---

## 팀별 역할 요약

| # | 팀명 | 핵심 역할 | 주요 산출물 |
|---|------|----------|------------|
| 01 | 전략기획실 | 사업 전략 수립, 의사결정 지원 | 전략 보고서, 실행 로드맵 |
| 02 | 마케팅팀 | 채널별 마케팅 전략, OSMU | 마케팅 콘텐츠, 캠페인 |
| 03 | 콘텐츠팀 | 블로그, 아티클 작성 | 롱폼 콘텐츠, SEO 글 |
| 04 | 비주얼팀 | AI 이미지 생성, 디자인 | 썸네일, 배너, 프롬프트 |
| 05 | 이커머스팀 | 상품 기획, 상세페이지 | 상세페이지, 상품 카피 |
| 06 | 재무팀 | 재무 분석, 예산 관리 | 재무 보고서, 손익 분석 |
| 07 | 사업개발팀 | 제안서 작성, 입찰 | 제안서, 윈닝 전략 |
| 08 | 교육콘텐츠팀 | 강의 기획, 교안 작성 | 커리큘럼, 퀴즈, 슬라이드 |
| 09 | 브레인스토밍팀 | 아이디어 발굴, 기획 | 아이디어 보고서 |
| 10 | 경영지원팀 | 행정, 일정 관리 | 미팅 자료, 체크리스트 |

---

## 워크플로우 다이어그램

```mermaid
flowchart LR
    subgraph INPUT["INPUT"]
        I1["요청/브리프"]
        I2["데이터/자료"]
    end

    subgraph PROCESS["PROCESS"]
        P1["Orchestrator<br/>작업 분배"]
        P2["Workers<br/>실행"]
        P3["Validator<br/>검증"]
    end

    subgraph OUTPUT["OUTPUT"]
        O1["최종 산출물"]
        O2["피드백/개선"]
    end

    I1 --> P1
    I2 --> P1
    P1 --> P2
    P2 --> P3
    P3 -->|승인| O1
    P3 -->|수정| P2
    O1 --> O2
    O2 -.->|반영| I1

    style INPUT fill:#2d3436,color:#fff
    style PROCESS fill:#0984e3,color:#fff
    style OUTPUT fill:#00b894,color:#fff
```

---

## 에이전트 계층 구조

```mermaid
graph TD
    A["CEO / 사용자"] --> B["Orchestrator<br/>(팀 디렉터)"]
    B --> C["Worker 1"]
    B --> D["Worker 2"]
    B --> E["Worker 3"]
    C --> F["Validator"]
    D --> F
    E --> F
    F --> G["Output"]

    style A fill:#e17055,color:#fff
    style B fill:#0984e3,color:#fff
    style C fill:#00cec9,color:#fff
    style D fill:#00cec9,color:#fff
    style E fill:#00cec9,color:#fff
    style F fill:#6c5ce7,color:#fff
    style G fill:#00b894,color:#fff
```
