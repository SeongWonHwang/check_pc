import subprocess
import chardet


class NetShareChecks:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.encoding = self._detect_encoding()

    # 파일 인코딩
    def _detect_encoding(self) -> str:
        with open(self.file_path, 'rb') as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            return result['encoding']

    def _get_netshare_value(self) -> int:
        try:
            with open(self.file_path, 'r', encoding=self.encoding) as file:
                lines = file.readlines()
                for line in lines:
                    if "IPC$" in line:
                        continue
                    # 공유 폴더 이름이 존재하는 라인인지 확인
                    if line.strip() and not line.startswith('-----') and not line.startswith("명령을 잘 실행했습니다.") and not line.startswith("공유 이름"):
                        return 0  # 불만족
            return 1  # 만족

        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"공유 폴더 내보내기 중 오류 발생: {e.stderr}")
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return 0  # 파일이 없으면 불만족으로 간주
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0  # 기타 오류 발생 시 불만족으로 간주
