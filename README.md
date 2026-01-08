# LFM2.5 Function Calling Example

Ollama와 LFM2.5 모델을 사용한 Function Calling(도구 호출) 예제 프로젝트입니다.

## 프로젝트 개요

이 프로젝트는 Ollama 클라이언트를 사용하여 AI 모델이 외부 함수/도구를 호출할 수 있도록 구현하는 방법을 보여줍니다.

## 기능

- OpenAI Function Calling 형식의 도구 정의
- LFM2.5 모델을 통한 도구 호출 요청
- 도구 실행 결과를 모델에 다시 전달하여 최종 답변 생성
- 온도 조회 함수 예시 (`get_current_temperature`)

## 전제 조건

1. **Ollama 설치**
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. **LFM2.5 모델 다운로드**
   ```bash
   ollama pull lfm2.5
   ```

3. **Ollama 서버 실행**
   ```bash
   ollama serve
   ```

## 설치

```bash
# 가상환경 생성 (선택사항)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate  # Windows

# 필요한 패키지 설치
pip install ollama
```

## 사용 방법

```bash
python app.py
```

## 코드 설명

### 도구 정의

`get_current_temperature` 함수는 지정된 위치의 현재 온도를 반환합니다. 실제 날씨 API 대신 더미 데이터를 사용합니다.

### Function Calling 흐름

1. 사용자 메시지와 도구 정의를 Ollama에 전송
2. 모델이 필요한 도구를 식별하고 호출 요청 (`tool_calls`)
3. 도구를 실행하고 결과 획득
4. 실행 결과를 모델에 다시 전달하여 최종 답변 생성

## 파일 구조

```
LFM2.5/
├── app.py              # 메인 예제 코드
├── README.md           # 이 파일
├── Modelfile           # Ollama 모델 설정
└── blog.html           # 블로그 페이지
```

## 라이선스

MIT License
