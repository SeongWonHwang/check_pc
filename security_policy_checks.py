import subprocess
import chardet


# 로컬정책 체크
class SecurityPolicyChecker:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.encoding = self._detect_encoding()

    # 파일 인코딩
    def _detect_encoding(self) -> str:
        with open(self.file_path, 'rb') as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            return result['encoding']

    # 로컬 정책 가져오기
    def _get_policy_value(self, policy_name: str) -> int or None:
        try:
            with open(self.file_path, 'r', encoding=self.encoding) as file:
                lines = file.readlines()
                for line in lines:
                    if policy_name in line:
                        key, value = line.strip().split('=')
                        if key.strip() == policy_name:
                            return int(value.strip())
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None

    # 로컬 정책 체크
    def _check_policy(self, policy_name: str, policy_value: int, comparison_operator: callable) -> int or str:
        value = self._get_policy_value(policy_name)
        if value is None:
            return f"Policy value for {policy_name} could not be retrieved."
        if comparison_operator(value, policy_value):
            return 1
        else:
            return 0
