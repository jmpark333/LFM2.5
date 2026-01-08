from ollama import Client

# Ollama 클라이언트 초기화 (로컬에서 실행 중인 Ollama 서버에 연결)
client = Client(host='http://localhost:11434')

# 도구(Tool) 정의 - 실제로 실행할 함수
def get_current_temperature(location: str, unit: str = "celsius"):
    """지정된 위치의 현재 온도를 반환합니다."""
    # 실제로는 날씨 API를 호출하겠지만, 예시를 위해 더미 데이터 반환
    weather_data = {
        "Seoul, South Korea": 18,
        "New York, USA": 22,
        "Tokyo, Japan": 20,
    }
    temp = weather_data.get(location, 25)  # 기본값 25도
    if unit == "fahrenheit":
        temp = temp * 9/5 + 32
    return {"location": location, "temperature": temp, "unit": unit}

# 사용자 질문
user_message = "What's the temperature in Seoul, South Korea in celsius?"

# 도구 정의 (OpenAI Function Calling 형식)
tools = [{
    "type": "function",
    "function": {
        "name": "get_current_temperature",
        "description": "Get the current temperature at a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The location to get the temperature for"
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "The unit to return the temperature in"
                }
            },
            "required": ["location"]
        }
    }
}]

# Ollama 모델에 메시지 전송 (도구 호출 포함)
response = client.chat(
    model='lfm2.5',
    messages=[{"role": "user", "content": user_message}],
    tools=tools
)

# 도구 호출 응답 처리
print("AI Response:", response['message'])

# 함수 실행 및 최종 답변 생성
if response['message'].get('tool_calls'):
    for tool_call in response['message']['tool_calls']:
        function_name = tool_call['function']['name']
        function_args = tool_call['function']['arguments']

        # 함수 실행
        if function_name == "get_current_temperature":
            result = get_current_temperature(**function_args)
            print(f"Function Result: {result}")

            # 함수 실행 결과를 다시 모델에 전달하여 최종 답변 생성
            final_response = client.chat(
                model='lfm2.5',
                messages=[
                    {"role": "user", "content": user_message},
                    {"role": "assistant", "content": str(response['message'])},
                    {"role": "tool", "content": str(result)}
                ]
            )
            print("Final Answer:", final_response['message']['content'])