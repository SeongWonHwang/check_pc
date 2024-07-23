import subprocess


#정책 내보냄
def export_securitypolicy():
    command = ['secedit', '/export', '/cfg', 'C:\\securitypolicy_export.inf', '/areas', 'SECURITYPOLICY']

    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"정책 내보내기 중 오류 발생: {e.stderr}")
    except FileNotFoundError:
        raise FileNotFoundError("secedit 명령을 찾을 수 없음")
    except Exception as e:
        raise RuntimeError(f"예상치 못한 오류: {e}")


def export_netshare():
    command = ['net', 'share']

    try:
        # net share 명령어 실행 및 출력 저장
        result = subprocess.run(command, check=True, capture_output=True, text=True)

        # 출력 결과를 C 드라이브의 netshare_export.txt 파일로 저장
        with open('C:\\netshare_export.inf', 'w') as file:
            file.write(result.stdout)

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"공유 폴더 내보내기 중 오류 발생: {e.stderr}")
    except FileNotFoundError:
        raise FileNotFoundError("net 명령을 찾을 수 없음")
    except Exception as e:
        raise RuntimeError(f"예상치 못한 오류: {e}")
