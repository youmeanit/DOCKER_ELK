import json

# 입력 JSON 파일 경로
input_file_path = 'C:/Users/yumin/docker-elk/data.json'  # 여기서 'input_data.json'은 입력 파일명

# 출력 JSON 파일 경로
output_file_path = 'bulk_data.json'

# JSON 파일 읽기
with open(input_file_path, 'r') as f:
    data = [json.loads(line.strip()) for line in f.readlines()]

# bulk 형식으로 변환
bulk_data = []
for item in data:
    action = {
        "index": {
            "_index": "potato",  # 원하는 인덱스 이름
            "_id": item["id"]
        }
    }
    bulk_data.append(action)
    bulk_data.append(item)  # 실제 데이터 추가

# 파일로 저장
with open(output_file_path, 'w') as f:
    for line in bulk_data:
        f.write(json.dumps(line) + "\n")

print(f"{output_file_path} 파일이 생성되었습니다.")
